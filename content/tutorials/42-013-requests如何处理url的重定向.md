---
weight: 13
title: requests如何处理url的重定向?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1542744095-fcf48d80b0fd?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



默认情况下，除了HEAD请求, Requests 会自动处理所有重定向。

如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理：

```
>>> r = requests.get('http://github.com', allow_redirects=False)
>>> r.status_code
301
>>> r.history
[]
```

可以使用```history```方法来追踪重定向

```
>>> r = requests.get('http://github.com')

>>> r.url
'https://github.com/'

>>> r.status_code
200

>>> r.history
[<Response [301]>]
```

如果你使用了 HEAD 方法，你也可以启用重定向：

```
>>> r = requests.head('http://github.com', allow_redirects=True)
>>> r.url
'https://github.com/'
>>> r.history
[<Response [301]>]
```




原始封面

![课程图片](https://images.unsplash.com/photo-1542744095-fcf48d80b0fd?w=300)

