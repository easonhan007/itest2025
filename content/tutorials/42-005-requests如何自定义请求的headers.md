---
weight: 5
title: requests如何自定义请求的headers?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1432821596592-e2c18b78144f?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#custom-headers)

有时候我们需要自定义一些请求的headers，比如我们可能需要将jwt的token放到headers里以完成鉴权。

```
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)

```




原始封面

![课程图片](https://images.unsplash.com/photo-1432821596592-e2c18b78144f?w=300)

