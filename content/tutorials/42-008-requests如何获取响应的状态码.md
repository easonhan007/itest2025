---
weight: 8
title: requests如何获取响应的状态码?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507919909716-c8262e491cde?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



使用```status_code``` 就可以了。

```
>>> r = requests.get('http://httpbin.org/get')
>>> r.status_code
200
```

为方便引用，Requests还附带了一个内置的状态码查询对象：

```
>>> r.status_code == requests.codes.ok
True
```

如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：

```
>>> bad_r = requests.get('http://httpbin.org/status/404')
>>> bad_r.status_code
404

>>> bad_r.raise_for_status()
Traceback (most recent call last):
  File "requests/models.py", line 832, in raise_for_status
    raise http_error
requests.exceptions.HTTPError: 404 Client Error
```

如果在测试用例中直接使用```raise_for_status()```方法，如果有异常抛出的话，用例会自动失败。




原始封面

![课程图片](https://images.unsplash.com/photo-1507919909716-c8262e491cde?w=300)

