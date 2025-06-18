---
weight: 4
title: requests如何发送其他请求
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1559523182-a284c3fb7cff?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)

delete,options,put等类型的请求在requests中均有对应的方法

```
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')
```

也可以使用requests统一的request方法来发送各种请求

```
r = requests.request('get', 'https://api.github.com/events')
>>> r = requests.request('post', 'http://httpbin.org/post', data = {'key':'value'})
>>> r = requests.request('put', 'http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.request('delete', 'http://httpbin.org/delete')
>>> r = requests.request('head', 'http://httpbin.org/get')
>>> r = requests.request('options', 'http://httpbin.org/get')
```




原始封面

![课程图片](https://images.unsplash.com/photo-1559523182-a284c3fb7cff?w=300)

