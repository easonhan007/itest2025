---
weight: 0
title: 命令行里的postman? wuzz初体验
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1523978591478-c753949ff840?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



postman是我用的非常顺手的调试以及测试工具，界面简洁优雅，扩展性相对较强，平时使用频率还是很高的。

不过postman有的一个比较大的问题就是没办法在服务器端使用，而使用go实现的wuzz则弥补了这一遗憾。

![](https://github.com/asciimoo/wuzz/blob/master/docs/images/screencast.gif)

wuzz是命令行里的http请求交互工具，我们可以很清晰的看到，wuzz可以进行

* 类似于postman的请求调试工作
* 可以修改请求参数以及headers
* 保存请求
* 兼容curl
* 支持搜索

该工具整体的操作逻辑也很简单

* 使用tab键切换区域
* 用上下键翻页
* 类似于bash的一些操作，比如ctrl+w修改word之类的

### 安装

首先安装go，版本是1.10以上，建议直接上1.15以上。

```
$ go get github.com/asciimoo/wuzz
$ "$GOPATH/bin/wuzz" --help
```

###  使用体验

稍微体验了一下，优势和不足如下

优点

* 可视化的操作
* 相对清晰的操作逻辑
* 确实有一些postman的意思了
* 可以保存请求
* 可以查看历史
* 响应里的中文可以正常显示

不足

* 在我的乞丐版云服务器上整体的操作还是有点卡的
* 不支持自动补全
* 安装其实有点点难度


### 总结

* 命令行调试操作确实是可用的
* 但对于简单的请求，我可能还是会选择httpie




原始封面

![课程图片](https://images.unsplash.com/photo-1523978591478-c753949ff840?w=300)

