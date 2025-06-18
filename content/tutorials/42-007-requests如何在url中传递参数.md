---
weight: 7
title: requests如何在url中传递参数?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1416339442236-8ceb164046f8?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)

我们经常需要在请求中加参数，比如一些分页信息，每页返回的资源数量等。

如果我们手工去构造这些参数的话，我们会在url后面接```?```，然后传入key/value对，比如```httpbin.org/get?key=val```。多个key/value对以```&```分隔。

在Requests里，我们一般使用```params```关键字参数的方式，传入dict来传递url参数。比如，假设我们想传递```key1=value1```和```key2=value2```这2个参数，我们可以用下面的代码

``` python
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('http://httpbin.org/get', params=payload)
```

可以通过url方法来查看requests帮我们构造的编码后的url

```
>>> print(r.url)
http://httpbin.org/get?key2=value2&key1=value1
```

我们还可以为同一个key传递一组数据，比如

```
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```




原始封面

![课程图片](https://images.unsplash.com/photo-1416339442236-8ceb164046f8?w=300)

