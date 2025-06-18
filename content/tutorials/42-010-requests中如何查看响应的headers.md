---
weight: 10
title: requests中如何查看响应的headers?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1501959181532-7d2a3c064642?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



```r.headers``` 可以拿到Python 字典形式展示的服务器响应头：

```
>>> r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}
```

但是这个字典比较特殊：它是仅为 HTTP 头部而生的。根据[RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)， HTTP 头部是大小写不敏感的。

因此，我们可以使用任意大写形式来访问这些响应头字段：

```
>>> r.headers['Content-Type']
'application/json'

>>> r.headers.get('content-type')
'application/json'
```




原始封面

![课程图片](https://images.unsplash.com/photo-1501959181532-7d2a3c064642?w=300)

