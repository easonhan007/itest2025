# 版本

## hugo

```
hugo version
hugo v0.147.8-10da2bd765d227761641f94d713d094e88b920ae+extended+withdeploy darwin/arm64 BuildDate=2025-06-07T12:59:52Z VendorInfo=gohugoio
```

## LoveIt

v0.3.0

# 文档

最有用的文档应该是[这个](https://hugoloveit.com/categories/documentation/)

# 安装

hugo new site 之后下载最新的 release 版本解压到 themes 里面就可以完成安装了。

# 遇到的问

https://github.com/easonhan007/itest2025/issues/1

# 资源

- [简体中文说明](https://github.com/dillonzq/LoveIt/blob/master/README.zh-cn.md)
- [项目主页](https://github.com/dillonzq/LoveIt/)

# 项目路径

内容都在 content 下面

- [posts](https://github.com/easonhan007/itest2025/tree/main/content/posts): 所有的文章都放在这里
- [tutorials](https://github.com/easonhan007/itest2025/tree/main/content/tutorials): 教程放这里

# 首页展示

front matter 里设置`weight: 1`

# 分类

front matter 里设置`categories:[]`，可以设置多个

# tags

front matter 里设置`tags:[]`，可以设置多个

# 视频列表封面

运行 `python3 scripts/sync_bilibili_covers.py`，读取 `content/video` 中每篇文章的第一个 B 站短代码，从公开页面获取封面并缓存到 `assets/bilibili/`。需要联网，仅使用 Python 标准库。

默认跳过已有封面；使用 `--force` 更新。将图片一并提交即可，正常 Hugo 构建和访客浏览不访问 B 站接口。抓取失败会报告 BV 号并返回非零状态，保留已有缓存。

视频列表优先使用文章的 `featured-image` 资源，其次按 BV 号读取缓存；缺失或图片加载失败时显示占位。文章中的播放器与链接不变。
