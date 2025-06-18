---
weight: 14
title: requests如何处理二进制的响应内容？
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1501556466850-7c9fa1fccb4c?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#binary-response-content)

有时候服务器返回的数据不是文本的，而是二进制的，这时候我们就需要处理二进制的内容。

Requests中可以使用content方法来返回二进制的响应内容，比如

```
>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

如果响应是gzip压缩过的，Requests会自动解压。

下面这个例子演示了如何从服务器返回的二进制内容创建图片。

```
>>> from PIL import Image
>>> from io import BytesIO

>>> i = Image.open(BytesIO(r.content))
```




原始封面

![课程图片](https://images.unsplash.com/photo-1501556466850-7c9fa1fccb4c?w=300)

