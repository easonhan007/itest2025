---
weight: 0
title: curl太难用？试试httpie吧
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



curl是功能非常强大的命令行http客户端，也许是正是因为强大吧，所以很多同学记不太住curl的一些常用参数，再加上curl的命令行参数形式又比较老派，所以日常用起来还是有一点点略显啰嗦的。

既然curl太难用？那我们就试试httpie吧。

项目地址：https://github.com/jakubroztocil/httpie。

一句话介绍，我就不翻译了。

> As easy as HTTPie /aitch-tee-tee-pie/ 🥧 Modern command line HTTP client – user-friendly curl alternative with intuitive UI, JSON support, syntax highlighting, wget-like downloads, extensions, etc.

httpie的特点

* 用户友好
* 非反直觉的ui
* 支持JSON
* 支持语法高亮
* 支持文件下载
* 支持插件

一图以蔽之

![](https://raw.githubusercontent.com/jakubroztocil/httpie/master/httpie.gif)

### 安装

**Mac**

```
$ brew install httpie
# or
$ port install httpie
```

**Linux**

```
# Debian, Ubuntu, etc.
$ apt-get install httpie

# Fedora
$ dnf install httpie

# CentOS, RHEL, ...
$ yum install httpie

# Arch Linux
$ pacman -S httpie
```

**Windows***

```
# Make sure we have an up-to-date version of pip and setuptools:
$ pip install --upgrade pip setuptools
$ pip install --upgrade httpie
```

### 例子

**Hello World:**

```
$ http httpie.org
```

**自定义HTTP Method以及使用JSON**

```
$ http PUT example.org X-API-Token:123 name=John
```

**提交表单**

```
$ http -f POST example.org hello=World
```

**查看请求详情**

```
$ http -v example.org
```

**使用github API去评论某个issue，包含了鉴权**

```
$ http -a USERNAME POST https://api.github.com/repos/jakubroztocil/httpie/issues/83/comments body='HTTPie is awesome! :heart:'
```

**使用重定向的方式上传文件**

```
$ http example.org < file.json
```

**使用重定向的方式下载文件**

```
$ http example.org/file > file
```

**wget style方式的下载**

```
$ http --download example.org/file
```

**使用named session来保持请求之间的上下文**

```
$ http --session=logged-in -a username:password httpbin.org/get API-Key:123

$ http --session=logged-in httpbin.org/headers
```

**自定义Host Header 来绕开DNS**

```
$ http localhost:8000 Host:example.com
```

### 总结

httpie在调试和测试接口的时候还是比较管用的，有兴趣的同学可以深入研究。

遇到问题的话，求人不如求己。

```
$ http --help
```




原始封面

![课程图片](https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?w=300)

