---
weight: 15
title: requests中如何设置请求的超时时间?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1498758536662-35b82cd15e29?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



使用timeout 参数可以设定等待连接的秒数，如果等待超时，Requests会抛出异常

```
>>> requests.get('http://github.com', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```

timeout 仅对连接过程有效，与响应体的下载无关。 timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时)。




原始封面

![课程图片](https://images.unsplash.com/photo-1498758536662-35b82cd15e29?w=300)

