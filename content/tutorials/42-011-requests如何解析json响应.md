---
weight: 11
title: requests如何解析json响应?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1497215641119-bbe6d71ebaae?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



[官方文档](http://docs.python-requests.org/en/master/user/quickstart/#json-response-content)

如果服务器返回json格式的数据，那么我们一般希望可以把json字符串转成python的dict数据类型。

```
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

如果JSON解析失败，r.json()会抛异常。比如假设响应的返回状态码是204(No Content)，又或者响应的返回json字符串格式有错误，那么r.json()回抛出```ValueError: No JSON object could be decoded.```异常。

需要引起注意的是r.json()解析成功了并不代表请求是成功的。很多服务器在响应失败的时候也会返回json字符串，如果要判断响应的状态的话，建议使用```r.raise_for_status()``` 或者使用``` check r.status_code ```来判断返回值是否符合预期。




原始封面

![课程图片](https://images.unsplash.com/photo-1497215641119-bbe6d71ebaae?w=300)

