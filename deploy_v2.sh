#!/usr/bin/env bash
# Upload and validate a version before atomically switching the live directory.
# Usage: ./deploy_v2.sh
# Override defaults: HOST=example.com SSH_USER=ubuntu SSH_KEY=... ./deploy_v2.sh
# Roll back: ./deploy_v2.sh --rollback /home/ubuntu/itest2025.releases/RELEASE
set -Eeuo pipefail

HOST=${HOST:-itest.info}
SSH_USER=${SSH_USER:-ubuntu}
SSH_PORT=${SSH_PORT:-22}
SSH_KEY=${SSH_KEY:-$HOME/.ssh/id_rsa}
DEPLOY_PATH=${DEPLOY_PATH:-/home/ubuntu/itest2025}
SITE_URL=${SITE_URL:-https://itest.info}
SITE_URL=${SITE_URL%/}
RELEASES_DIR="${DEPLOY_PATH}.releases"
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

usage() {
  echo "Usage: $0 [--rollback ABSOLUTE_RELEASE_PATH]"
  echo 'Settings: HOST SSH_USER SSH_PORT SSH_KEY DEPLOY_PATH SITE_URL'
}
ROLLBACK=''
case "${1:-}" in
  '') [[ $# == 0 ]] || { usage; exit 2; } ;;
  --rollback) [[ $# == 2 ]] || { usage; exit 2; }; ROLLBACK=$2 ;;
  -h|--help) usage; exit 0 ;;
  *) usage; exit 2 ;;
esac
# Remote paths are shell arguments; constrain them before constructing commands.
[[ "$DEPLOY_PATH" =~ ^/[a-zA-Z0-9_./-]+$ && "$DEPLOY_PATH" != / && "$DEPLOY_PATH" != */ && "$DEPLOY_PATH" != *..* ]] || { echo 'Invalid DEPLOY_PATH' >&2; exit 2; }
[[ "$HOST" =~ ^[a-zA-Z0-9][a-zA-Z0-9.-]*$ && "$SSH_USER" =~ ^[a-zA-Z_][a-zA-Z0-9_-]*$ && "$SSH_PORT" =~ ^[0-9]+$ ]] || { echo 'Invalid SSH settings' >&2; exit 2; }
[[ -f "$SSH_KEY" ]] || { echo "SSH key not found: $SSH_KEY" >&2; exit 1; }
SSH=(ssh -p "$SSH_PORT" -i "$SSH_KEY" -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20)
SCP=(scp -P "$SSH_PORT" -i "$SSH_KEY" -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20)
REMOTE="$SSH_USER@$HOST"
WORK_DIR=$(mktemp -d)
trap 'rm -rf -- "$WORK_DIR"' EXIT

activate() {
  "${SSH[@]}" "$REMOTE" "bash -s -- '$DEPLOY_PATH' '$RELEASES_DIR' '$1'" <<'REMOTE_SCRIPT'
set -Eeuo pipefail
live=$1
releases=$2
candidate=$3
# Serialize activation between v2 deployments; legacy deployers must not run concurrently.
exec 9>"${live}.deploy.lock"
flock -x 9
python3 - "$live" "$releases" "$candidate" <<'PY'
import ctypes
import datetime
import os
from pathlib import Path
import sys
import uuid

live, releases, candidate = map(Path, sys.argv[1:])
if candidate.is_symlink() or candidate.parent != releases or not candidate.is_dir():
    raise SystemExit('Refusing release outside the releases directory or a symlink')
if not (candidate / 'index.html').is_file() or (candidate / 'index.html').stat().st_size == 0:
    raise SystemExit('Release has no valid index.html; live site unchanged')
if live.is_symlink() and live.resolve() == candidate.resolve():
    print('Already serving this release:', candidate)
    raise SystemExit(0)
previous = str(live.resolve()) if live.is_symlink() else None
# This path becomes the preserved old directory during first-time migration.
backup = releases / ('legacy-' + datetime.datetime.now().strftime('%Y%m%dT%H%M%S') + '-' + uuid.uuid4().hex[:8])
os.symlink(str(candidate), str(backup))
try:
    if live.is_dir() and not live.is_symlink():
        # Linux renameat2(RENAME_EXCHANGE) swaps directory and symlink atomically.
        # Unsupported systems fail without moving/deleting the existing live site.
        libc = ctypes.CDLL(None, use_errno=True)
        exchange = getattr(libc, 'renameat2', None)
        if exchange is None:
            raise RuntimeError('Atomic first migration requires Linux renameat2')
        exchange.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
        exchange.restype = ctypes.c_int
        if exchange(-100, os.fsencode(backup), -100, os.fsencode(live), 2) != 0:
            error = ctypes.get_errno()
            raise OSError(error, os.strerror(error))
        previous = str(backup)
    elif live.is_symlink() or not live.exists():
        os.replace(backup, live)
    else:
        raise RuntimeError('Live path is neither directory nor symlink')
finally:
    if backup.is_symlink():
        backup.unlink()
print('ACTIVE_RELEASE=' + str(candidate))
if previous:
    print('PREVIOUS_RELEASE=' + previous)
    print('Rollback with: ./deploy_v2.sh --rollback ' + previous)
PY
REMOTE_SCRIPT
}

if [[ -n "$ROLLBACK" ]]; then
  [[ "$ROLLBACK" == "$RELEASES_DIR/"* && "$ROLLBACK" =~ ^/[a-zA-Z0-9_./-]+$ && "$ROLLBACK" != *..* ]] || { echo 'Invalid rollback path' >&2; exit 2; }
  activate "$ROLLBACK"
else
  command -v hugo >/dev/null || { echo 'Hugo is required' >&2; exit 1; }
  RELEASE="$(date -u +%Y%m%dT%H%M%SZ)-$(basename "$WORK_DIR")"
  TARGET="$RELEASES_DIR/$RELEASE"
  echo 'Building an isolated production release...'
  HUGO_ENVIRONMENT=production hugo --source "$SCRIPT_DIR" --destination "$WORK_DIR/public" --baseURL "$SITE_URL/" --minify
  [[ -s "$WORK_DIR/public/index.html" ]] || { echo 'Build has no index.html; deployment aborted' >&2; exit 1; }
  COPYFILE_DISABLE=1 tar -czf "$WORK_DIR/site.tar.gz" -C "$WORK_DIR/public" .
  "${SSH[@]}" "$REMOTE" "mkdir -p '$RELEASES_DIR' && chmod 755 '$RELEASES_DIR' && mkdir '$TARGET'"
  echo "Uploading $RELEASE (current site stays online)..."
  "${SCP[@]}" "$WORK_DIR/site.tar.gz" "$REMOTE:$TARGET/site.tar.gz"
  "${SSH[@]}" "$REMOTE" "bash -s -- '$TARGET'" <<'REMOTE_SCRIPT'
set -Eeuo pipefail
target=$1
tar --no-same-owner -xzf "$target/site.tar.gz" -C "$target"
rm -- "$target/site.tar.gz"
test -s "$target/index.html"
find "$target" -type d -exec chmod 755 {} +
find "$target" -type f -exec chmod 644 {} +
REMOTE_SCRIPT
  activate "$TARGET"
fi

echo 'Checking the public homepage...'
if curl --fail --silent --show-error --location --max-time 30 --output /dev/null "${SITE_URL%/}/"; then
  echo 'Done. Homepage HTTP check passed. Nginx configuration and reload are not required.'
else
  echo 'Activation completed, but HTTP verification failed. Use the printed rollback command if needed.' >&2
  exit 1
fi
