---
weight: 2
title: Fiddler（二）主界面介绍
date: '2017-12-19T13:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1574169208099-7257315d2993?w=300
tags: []
categories:
- 抓包工具Fiddler使用教程
lightgallery: true
toc:
  auto: false
---



在开始Fiddler工具之前，请先学习 [HTTP基础](/proxy_tools/http-base/)

### Fiddler主界面
---

![](http://img.testclass.net/fiddler_04.png)

Fiddler 工具界面如上图。

#### 请求列表（左侧窗口）
---
显示Fiddler 工具拦截的 HTTP/HTTPS 请求。

* `#` 显示资源类型与编号。

![](http://img.testclass.net/fiddler_04_1.png)

* `Result` 表示HTTP返回的状态码。如 200、302、500等。

* `Protocol` 表示请求的协议：HTTP/HTTPS

* `Host` 请求的IP或网址。

* `URL` 请求的路径。

* `Body`  请求资源的大小。

* `Caching` 请求的缓存过期时间或者缓存控制值。

* `Content-Type`  请求响应的类型。

* `Process` 发送此请求的进程：进程ID。

* `Comments` 允许用户为此回话添加备注。

* `Custom` 允许用户设置自定义值。


#### Statistics（右则窗Statistics标签）
---

 Statistics 显示关于HTTP请求的性能以及数据分析。

![](http://img.testclass.net/fiddler_04_2.png)

#### Inspectors （右则窗Inspectors标签）
---
Inspectors 是用于查看会话的内容，上半部分是请求的内容，下半部分是响应的内容。

![](http://img.testclass.net/fiddler_04_3.png)

对于每一部分，提供了多种不同格式查看每个请求和响应的内容。

* `Header` 标签用于显示HTTP请求和响应的头信息。

* `TextView` 标签用于查看 HTML/JS/CSS 等格式的数据。

* `ImageView` 标签用于显示图片格式的数据。

* `WebForms` 标签用于显示请求的表单数据。如登录请求，就可以通过它查查看登录用户名密码信息。它以表格形式显示。

* `Raw` 标签可以查看原始的符合HTTP标准的请求和响应头。

* `Auth` 标签可以查看授权Proxy-Authorization 和 Authorization的相关信息。

* `Cookies` 标签可以看到请求的cookie和响应的set-cookie头信息。

* `XML` 和 `JSON`  标签用于显示 XML和JSON格式的数据。

* 其它标签，暂时先介绍这么多吧！




原始封面

![课程图片](https://images.unsplash.com/photo-1574169208099-7257315d2993?w=300)

