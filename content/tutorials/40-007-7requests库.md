---
weight: 7
title: 7.requests库
date: '2017-08-24T04:41:43+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1501555790667-ba7ea28b4cea?w=300
tags: []
categories:
- python接口测试实践教程
lightgallery: true
toc:
  auto: false
---



[requests](http://docs.python-requests.org/en/master/)库可以极大的简化我们发送http请求及获取响应的代码，简洁而优雅。

### 简单示例

```
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}

```

上面的例子相信大家很容易看明白，在我们做接口自动化测试的时候，我们往往使用requests的提供的接口发送请求和获取响应，并根据响应类型将响应转换成python自建的数据结构。比如上面的例子里，我们将响应的json字符串转换成了python的dict。


### 安装

[官方文档](http://docs.python-requests.org/en/master/user/install/)
[中文文档](http://docs.python-requests.org/zh_CN/latest/user/install.html)

### 快速开始

[官方文档](http://docs.python-requests.org/en/master/user/quickstart/)
[中文文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

### 划重点

* [发请求](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)
* [传参](http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
* [获取响应](http://docs.python-requests.org/en/master/user/quickstart/#response-content)
* [解析json](http://docs.python-requests.org/en/master/user/quickstart/#json-response-content)
* [自定义header](http://docs.python-requests.org/en/master/user/quickstart/#custom-headers)
* [响应状态码](http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes)
* [响应headers](http://docs.python-requests.org/en/master/user/quickstart/#response-headers)
* [post](http://docs.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests)

英文不好的同学可以参考[中文文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)的相关章节。




原始封面

![课程图片](https://images.unsplash.com/photo-1501555790667-ba7ea28b4cea?w=300)

