#!/usr/bin/env python3
"""Cache the first Bilibili video's cover for each video article (stdlib only)."""
import argparse
import gzip
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SHORTCODE = re.compile(r'\{\{[<%]\s*bilibili\b.*?[>%]\}\}', re.S)
BVID = re.compile(r'BV[0-9A-Za-z]{10}')


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cover = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('property') == 'og:image':
            self.cover = attrs.get('content')


def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request, timeout=20) as response:
        body = response.read(12 * 1024 * 1024 + 1)
    if len(body) > 12 * 1024 * 1024:
        raise ValueError('response exceeds 12 MB')
    return gzip.decompress(body) if body.startswith(b'\x1f\x8b') else body


def image_extension(body):
    if body.startswith(b'\xff\xd8\xff'):
        return '.jpg'
    if body.startswith(b'\x89PNG\r\n\x1a\n'):
        return '.png'
    if body.startswith(b'RIFF') and body[8:12] == b'WEBP':
        return '.webp'
    raise ValueError('cover response is not a supported image')


def first_bvid(text):
    shortcode = SHORTCODE.search(text)
    match = BVID.search(shortcode.group()) if shortcode else None
    return match.group() if match else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--force', action='store_true', help='refresh cached covers')
    args = parser.parse_args()
    output = ROOT / 'assets' / 'bilibili'
    failures = []
    seen = set()
    for article in sorted((ROOT / 'content' / 'video').rglob('*.md')):
        bvid = first_bvid(article.read_text(encoding='utf-8'))
        if not bvid or bvid in seen:
            continue
        seen.add(bvid)
        existing = list(output.glob(bvid + '.*'))
        if existing and not args.force:
            print(f'CACHED {bvid}')
            continue
        try:
            metadata = Metadata()
            metadata.feed(fetch(f'https://www.bilibili.com/video/{bvid}/').decode('utf-8'))
            url = metadata.cover
            if not url:
                raise ValueError('public page has no og:image metadata')
            if url.startswith('//'):
                url = 'https:' + url
            parsed = urlparse(url)
            if parsed.scheme not in ('http', 'https') or not (parsed.hostname or '').endswith('.hdslb.com'):
                raise ValueError('unexpected cover host')
            body = fetch(url)
            extension = image_extension(body)
            output.mkdir(parents=True, exist_ok=True)
            destination = output / (bvid + extension)
            temporary = destination.with_suffix(extension + '.tmp')
            temporary.write_bytes(body)
            temporary.replace(destination)
            for old in existing:
                if old != destination:
                    old.unlink()
            print(f'SAVED {bvid}: {destination.relative_to(ROOT)} ({len(body)} bytes)')
        except Exception as error:
            failures.append(bvid)
            print(f'FAILED {bvid} ({article.name}): {error}; keeping any cached cover', file=sys.stderr)
    if failures:
        print('Unavailable: ' + ', '.join(failures), file=sys.stderr)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
