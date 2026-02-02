# CR Tool

一个用于创建 Hugo 周刊文章目录的命令行工具。

## 功能

该工具可以自动在 `content/posts/` 目录下创建新的周刊目录，并从最新的 Markdown 文件中提取日期信息生成 `index.md`。

### 主要功能

1. 在 `content/posts/` 下创建指定的目录
2. 自动查找 `content/posts/` 目录下最新修改的 `.md` 文件
3. 从最新文件的 front matter 中提取 `date` 字段
4. 在新建目录下创建 `index.md`，只保留 `date` 字段，清空其他 front matter 字段和正文内容

## 安装与构建

### 前置要求

- Go 1.16 或更高版本
- Hugo 站点结构（包含 `content/posts/` 目录）

### 构建方法

**使用 Makefile：**

```bash
cd tools
make build      # 构建二进制文件
make clean      # 清理构建产物
make install    # 安装到 /usr/local/bin
make test       # 构建并测试
make help       # 显示帮助
```

**使用 build.sh：**

```bash
cd tools
./build.sh build    # 构建（默认）
./build.sh clean    # 清理
./build.sh install  # 安装到 /usr/local/bin
./build.sh test     # 构建并测试
./build.sh help     # 显示帮助
```

**直接使用 go：**

```bash
cd tools
go build -o cr main.go
```

## 使用方法

### 基本用法

```bash
./cr <directory-name>
```

### 示例

```bash
# 创建 weekly_02 目录
./cr weekly_02

# 输出示例
Created content/posts/weekly_02/index.md with date: 2024-03-08T09:02:25+08:00
```

生成的 `content/posts/weekly_02/index.md` 内容：

```yaml
---
date: 2024-03-08T09:02:25+08:00
---
```

### 查看帮助

```bash
./cr -h
./cr --help
```

## 注意事项

- 工具会从 `content/posts/` 目录及其子目录下的所有 `.md` 文件中选择**最新修改**的文件
- 如果找不到 `date` 字段，会使用当前时间作为默认值
- 如果目录已存在，不会被覆盖（但 `index.md` 会被更新）
- 该工具需要在 Hugo 项目的根目录下运行（或确保 `content/posts/` 路径存在）

## 文件说明

- `main.go` - 主程序源代码
- `Makefile` - 构建自动化（支持 build/clean/install/test）
- `build.sh` - 替代构建脚本（带颜色输出）
- `go.mod` - Go 模块定义

## 许可证

与主项目保持一致
