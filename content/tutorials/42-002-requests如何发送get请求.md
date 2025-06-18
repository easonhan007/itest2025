---
weight: 2
title: requests如何发送get请求?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1513470270416-d3ff6f16b22f?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)

使用requests发送请求其实非常简单。

首先导入Requests模块

```
>>> import requests
```

下面试着去发送具体的请求，比如获取github的timeline信息

```
r = requests.get('https://api.github.com/events')
```

r是requests的[响应(Response)](http://docs.python-requests.org/en/master/api/#requests.Response)对象，我们可以从r里面获取各种信息，比如获取响应的内容```print(r.text)```




原始封面

![课程图片](https://images.unsplash.com/photo-1513470270416-d3ff6f16b22f?w=300)

