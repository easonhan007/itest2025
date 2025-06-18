---
weight: 9
title: requests如何查看响应内容?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1488998527040-85054a85150e?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



```text``` 方法会拿到请求的响应内容，比如以再github的timeline接口为例

```
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

Requests会自动去解码server端返回的内容，大部分的unicode字符集都会被无缝解码。

当你发送请求的时候，Requests会根据HTTP headers来推断编码，并在```r.text```调用的时候使用。我们可以查看和修改Requests的编码，比如

```
>>> r.encoding
'utf-8'
>>> r.encoding = 'ISO-8859-1'
```




原始封面

![课程图片](https://images.unsplash.com/photo-1488998527040-85054a85150e?w=300)

