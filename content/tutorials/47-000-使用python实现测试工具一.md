---
weight: 0
title: 使用python实现测试工具(一)
date: '2018-07-10T06:55:32+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



本系列教程我们将使用python实现一些简单的测试工具，为了尽可能的简单，我们的工具以**命令行**工具为主。

本系列教程使用的python版本是**3.6.3**。

### 背景

这一节我们实现简单的命令行发送get请求的工具，使用方式如下：

```
python get.py www.v2ex.com/api/nodes/show.json\?name\=python
接口地址: http://www.v2ex.com/api/nodes/show.json?name=python

状态码: 200

Headers:
Date : Tue, 10 Jul 2018 07:06:12 GMT
Content-Type : application/json;charset=UTF-8
Transfer-Encoding : chunked
Connection : keep-alive
Vary : Accept-Encoding
X-Rate-Limit-Remaining : 119
Expires : Tue, 10 Jul 2018 08:03:49 GMT
Server : Galaxy/3.9.8.1
Etag : W/"76a33d25372411dc6fa4190a5cf9679caa0edc2a"
X-Rate-Limit-Reset : 1531209600
Cache-Control : max-age=3600
X-Rate-Limit-Limit : 120
Google : XY
Content-Encoding : gzip
Strict-Transport-Security : max-age=31536000
{
    "id" : 90,
    "name" : "python",
    "url" : "https://www.v2ex.com/go/python",
    "title" : "Python",
    "title_alternative" : "Python",
    "topics" : 9530,
    "stars" : 6601,

        "header" : "这里讨论各种 Python 语言编程话题，也包括 Django，Tornado 等框架的讨论。这里是一个能够帮助你解决实际问题的地方。",


        "footer" : null,

    "created" : 1278683336,
    "avatar_mini" : "//cdn.v2ex.com/navatar/8613/985e/90_mini.png?m=1531131631",
    "avatar_normal" : "//cdn.v2ex.com/navatar/8613/985e/90_normal.png?m=1531131631",
    "avatar_large" : "//cdn.v2ex.com/navatar/8613/985e/90_large.png?m=1531131631"
}
```

主要使用场景是快速访问http的api接口，查看状态码，响应头以及响应内容。


### 代码实现

简单起见，我们会用到requests库。安装文档在[这里](http://docs.python-requests.org/en/master/user/install/)。

```python
import requests
from sys import argv

USAGE = '''
USAGE:
python get.py https://api.github.com
'''

if len(argv) != 2:
  print(USAGE)
  exit()

script_name, url = argv

if url[:4] != 'http':
  url = 'http://' + url

r = requests.get(url)

print(f"接口地址: {url}\n")
print(f"状态码: {r.status_code}\n")
print(f"Headers:")
for key, value in r.headers.items():
  print(f"{key} : {value}")

print(r.text)

```

### 动手时间

* 抄一遍代码，看自己能不能运行起来
* 给这段代码每一行都加上注释，理解代码做了些什么
* 如果需要在发送get请求的时候默认加上```Content-Type: application/json```的headers，这段代码该如何修改


### 扩展阅读

* [requests](http://docs.python-requests.org/en/master/)
* [基于http协议的接口测试](http://www.testclass.net/interface/)

### 源码地址

[github地址](https://github.com/easonhan007/simple_test_tools)



原始封面

![课程图片](https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=300)

