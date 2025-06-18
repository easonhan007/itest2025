---
weight: 3
title: requests如何发送post请求?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/21/mac-glasses.JPG?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)

发送post请求跟发送get请求类似，使用```requests.post```方法就可以了，如果需要传post data的话，直接将data以dict的格式传递就好。

```
>>> import requests
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
```




![课程图片](https://images.unsplash.com/21/mac-glasses.JPG?w=300)

