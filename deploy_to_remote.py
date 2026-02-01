#!/usr/bin/env python3
"""
Deploy Hugo site to remote server via SSH/SCP
替代 GitHub Actions 的 deploy_to_remote.yml
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
import paramiko
from scp import SCPClient


class HugoDeployer:
    def __init__(self, host, username, private_key_path, port=22, deploy_path=None, site_url=None):
        self.host = host
        self.username = username
        self.private_key_path = private_key_path
        self.port = port
        self.deploy_path = deploy_path or '/var/www/html'
        self.site_url = site_url
        self.ssh_client = None

    def connect(self):
        """建立 SSH 连接"""
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 尝试不同的密钥类型
        private_key = None
        key_types = [
            ('Ed25519Key', paramiko.Ed25519Key),
            ('RSAKey', paramiko.RSAKey),
            ('ECDSAKey', paramiko.ECDSAKey),
        ]

        for name, key_class in key_types:
            try:
                private_key = key_class(filename=self.private_key_path)
                print(f"✓ 使用 {name} 密钥")
                break
            except Exception:
                continue

        if private_key is None:
            raise Exception(f"无法识别私钥格式: {self.private_key_path}")

        self.ssh_client.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            pkey=private_key,
            timeout=30
        )
        print(f"✓ 已连接到 {self.host}:{self.port}")

    def disconnect(self):
        """断开 SSH 连接"""
        if self.ssh_client:
            self.ssh_client.close()
            print("✓ 已断开连接")

    def execute_command(self, command):
        """执行远程命令并返回结果"""
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        exit_status = stdout.channel.recv_exit_status()

        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        if exit_status != 0:
            raise Exception(f"命令执行失败: {command}\n错误: {error}")

        return output

    def build_hugo(self, public_dir='public', site_url=None):
        """构建 Hugo 站点"""
        import subprocess

        base_url_args = ['--baseURL', site_url] if site_url else []

        print(f"开始构建 Hugo 站点...")
        result = subprocess.run(
            ['hugo', '--gc', '--minify'] + base_url_args,
            cwd=os.getcwd(),
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"stderr: {result.stderr}")
            raise Exception(f"Hugo 构建失败: {result.stderr}")

        print(f"✓ Hugo 构建完成，输出目录: {public_dir}")

        # 检查 public 目录是否存在且有内容
        if not os.path.exists(public_dir):
            raise Exception(f"构建输出目录 {public_dir} 不存在")

        file_count = len(list(Path(public_dir).rglob('*')))
        print(f"✓ 共 {file_count} 个文件/目录")

    def backup_remote(self):
        """备份远程服务器上的现有部署"""
        backup_cmd = f"""
        if [ -d "{self.deploy_path}" ]; then
            backup_dir="{self.deploy_path}.backup.$(date +%Y%m%d_%H%M%S)"
            cp -r {self.deploy_path} $backup_dir
            echo "BACKUP_CREATED:$backup_dir"
        else
            echo "NO_BACKUP_NEEDED"
        fi
        """

        output = self.execute_command(backup_cmd)

        if "BACKUP_CREATED:" in output:
            backup_dir = output.strip().split("BACKUP_CREATED:")[1]
            print(f"✓ 已备份到: {backup_dir}")
        elif "NO_BACKUP_NEEDED" in output:
            print(f"⚠ 目标目录不存在，无需备份")

    def prepare_remote_directory(self):
        """准备远程目标目录"""
        print("准备远程目录...")

        # 清空目标目录
        self.execute_command(f'rm -rf {self.deploy_path}/*')
        print(f"✓ 已清空 {self.deploy_path}")

        # 创建目标目录（如果不存在）
        self.execute_command(f'mkdir -p {self.deploy_path}')
        print(f"✓ 确保目录存在: {self.deploy_path}")

    def create_archive(self, source_dir='public'):
        """创建本地压缩包"""
        import tarfile

        archive_name = 'hugo_site.tar.gz'

        print(f"正在打包 {source_dir} -> {archive_name}...")

        # 如果旧压缩包存在，先删除
        if os.path.exists(archive_name):
            os.remove(archive_name)

        # 创建 tar.gz 压缩包
        with tarfile.open(archive_name, 'w:gz') as tar:
            tar.add(source_dir, arcname='.')

        archive_size = os.path.getsize(archive_name)
        archive_mb = archive_size / (1024 * 1024)
        print(f"✓ 打包完成: {archive_mb:.2f} MB")

        return archive_name

    def upload_files(self, source_dir='public'):
        """通过 SCP 上传文件到远程服务器"""
        # 1. 创建本地压缩包
        archive_name = self.create_archive(source_dir)

        # 2. 上传压缩包
        remote_archive = f'/tmp/{archive_name}'
        print(f"开始上传 {archive_name} -> {remote_archive}...")

        with SCPClient(self.ssh_client.get_transport()) as scp:
            scp.put(archive_name, remote_archive)

        print("✓ 压缩包上传完成")

        # 3. 在远程服务器上解压
        print(f"正在解压到 {self.deploy_path}...")
        extract_cmd = f'tar -xzf {remote_archive} -C {self.deploy_path}'
        self.execute_command(extract_cmd)
        print("✓ 解压完成")

        # 4. 删除远程和本地的压缩包
        print("清理压缩包...")
        self.execute_command(f'rm -f {remote_archive}')
        os.remove(archive_name)
        print("✓ 清理完成")

    def set_permissions(self):
        """设置文件权限"""
        print("设置文件权限...")

        # 设置目录权限为 755
        self.execute_command(f'chmod -R 755 {self.deploy_path}')
        print(f"✓ 已设置权限 755: {self.deploy_path}")

    def restart_nginx(self):
        """重启 Nginx"""
        print("重启 Nginx...")

        # 尝试直接执行，如果失败则尝试使用 sudo
        try:
            self.execute_command('systemctl reload nginx')
            print("✓ Nginx 已重新加载")
        except Exception as e:
            # 如果失败，尝试使用 sudo
            try:
                self.execute_command('sudo systemctl reload nginx')
                print("✓ Nginx 已重新加载 (使用 sudo)")
            except Exception:
                print("⚠ 无法重新加载 Nginx，可能需要手动执行或配置免密码 sudo")
                print("  提示: 可以使用 --no-restart 参数跳过此步骤")

    def deploy(self, build=True, restart_service=True):
        """执行完整的部署流程"""
        try:
            # 1. 构建 Hugo
            if build:
                self.build_hugo(site_url=self.site_url)

            # 2. 连接远程服务器
            self.connect()

            # 3. 备份现有部署
            self.backup_remote()

            # 4. 准备远程目录
            self.prepare_remote_directory()

            # 5. 上传文件
            self.upload_files()

            # 6. 设置权限
            self.set_permissions()

            # 7. 重启服务
            if restart_service:
                self.restart_nginx()

            print("\n✓ 部署完成！")

        except Exception as e:
            print(f"\n✗ 部署失败: {e}", file=sys.stderr)
            raise
        finally:
            self.disconnect()


def main():
    parser = argparse.ArgumentParser(description='部署 Hugo 站点到远程服务器')
    parser.add_argument('--host', required=True, help='SSH 主机地址')
    parser.add_argument('--username', required=True, help='SSH 用户名')
    parser.add_argument('--key', required=True, help='SSH 私钥文件路径')
    parser.add_argument('--port', type=int, default=22, help='SSH 端口 (默认: 22)')
    parser.add_argument('--deploy-path', default='/var/www/html', help='远程部署路径 (默认: /var/www/html)')
    parser.add_argument('--site-url', help='站点 URL (用于 Hugo --baseURL)')
    parser.add_argument('--no-build', action='store_true', help='跳过 Hugo 构建，只部署已有的 public 目录')
    parser.add_argument('--no-restart', action='store_true', help='不重启 Nginx')

    args = parser.parse_args()

    # 验证私钥文件存在
    if not os.path.exists(args.key):
        print(f"错误: 私钥文件不存在: {args.key}", file=sys.stderr)
        sys.exit(1)

    # 如果要构建，检查 hugo 是否已安装
    if not args.no_build:
        try:
            import subprocess
            subprocess.run(['hugo', 'version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("错误: Hugo 未安装或不在 PATH 中", file=sys.stderr)
            sys.exit(1)

    # 创建部署器并执行部署
    deployer = HugoDeployer(
        host=args.host,
        username=args.username,
        private_key_path=args.key,
        port=args.port,
        deploy_path=args.deploy_path,
        site_url=args.site_url
    )

    deployer.deploy(
        build=not args.no_build,
        restart_service=not args.no_restart
    )


if __name__ == '__main__':
    main()
