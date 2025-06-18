---
weight: 9
title: 9.使用fixture参数化接口入参
date: '2017-10-26T07:22:42+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1470164971321-eb5ac2c35f2e?w=300
tags: []
categories:
- pytest从入门到精通
lightgallery: true
toc:
  auto: false
---



### 背景

接上一节[v2ex](http://www.v2ex.com)网站的查看论坛节点信息的api。具体如下:

```
节点信息

获得指定节点的名字，简介，URL 及头像图片的地址。

https://www.v2ex.com/api/nodes/show.json

Method: GET
Authentication: None
接受参数：

name: 节点名（V2EX 的节点名全是半角英文或者数字）
例如：

https://www.v2ex.com/api/nodes/show.json?name=python
```

我们试一下，通过传入不同的name，我们可以获取不同的节点信息。上面例子里我们获取了python讨论区的信息。现在我们把name改成java，该接口会返回java讨论区节点的信息，如下所示

```
https://www.v2ex.com/api/nodes/show.json?name=python

{
    "id" : 63,
    "name" : "java",
    "url" : "http://www.v2ex.com/go/java",
    "title" : "Java",
    "title_alternative" : "Java",
    "topics" : 1219,
    "stars" : 1547,

        "header" : "The most popular programming language.",


        "footer" : null,

    "created" : 1272669207,
    "avatar_mini" : "//v2ex.assets.uxengine.net/navatar/03af/dbd6/63_mini.png?m=1509589840",
    "avatar_normal" : "//v2ex.assets.uxengine.net/navatar/03af/dbd6/63_normal.png?m=1509589840",
    "avatar_large" : "//v2ex.assets.uxengine.net/navatar/03af/dbd6/63_large.png?m=1509589840"
}
```

那么新的需求来了，现在我们要测试给定的几个节点名称(python/java/go/nodejs)，v2ex的节点api可以正确返回节点的名字

### 需求分析

根据[3A原则](/interface/3a/)，我们可以设计如下的用例

* 测试数据: 节点的名称:python/java/go/nodejs
* 接口地址: https://www.v2ex.com/api/nodes/show.json
* 断言: 返回的结果里，name字段的值必须等于传入的节点名称

### 代码

在```v2ex_api_test.py```的文件中添加如下内容

```python
import requests
import pytest

class TestV2exApiWithParams(object):
    domain = 'https://www.v2ex.com/'

    @pytest.fixture(params=['python', 'java', 'go', 'nodejs'])
    def lang(self, request):
        return request.param

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' %(lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
        assert 0

```

需要注意的点

* 每次都可以用```request.param```来访问本次传入fixture中的参数
* 在测试方法中传入同名的fixture方法名可以直接访问fixture
* 使用```assert(0)```强制用例失败，这样可以看到每次fixture的参数值


### 运行

```
$ pytest v2ex_api_test.py
======================================================================== test session starts ========================================================================
platform darwin -- Python 2.7.12, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
rootdir: /Users/easonhan/code/testclass.net/src/pytest, inifile:
collected 5 items

v2ex_api_test.py .FFFF

============================================================================= FAILURES ==============================================================================
______________________________________________________________ TestV2exApiWithParams.test_node[python] ______________________________________________________________

self = <v2ex_api_test.TestV2exApiWithParams object at 0x105e0edd0>, lang = 'python'

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' %(lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
>       assert 0
E       assert 0

v2ex_api_test.py:27: AssertionError
_______________________________________________________________ TestV2exApiWithParams.test_node[java] _______________________________________________________________

self = <v2ex_api_test.TestV2exApiWithParams object at 0x1075e2750>, lang = 'java'

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' %(lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
>       assert 0
E       assert 0

v2ex_api_test.py:27: AssertionError
________________________________________________________________ TestV2exApiWithParams.test_node[go] ________________________________________________________________

self = <v2ex_api_test.TestV2exApiWithParams object at 0x107636190>, lang = 'go'

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' %(lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
>       assert 0
E       assert 0

v2ex_api_test.py:27: AssertionError
______________________________________________________________ TestV2exApiWithParams.test_node[nodejs] ______________________________________________________________

self = <v2ex_api_test.TestV2exApiWithParams object at 0x1075e2790>, lang = 'nodejs'

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' %(lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
>       assert 0
E       assert 0

v2ex_api_test.py:27: AssertionError
================================================================ 4 failed, 1 passed in 1.91 seconds =================================================================
```

用例执行失败，但是每次运行时```lang```的值我们可以看的很明白。




原始封面

![课程图片](https://images.unsplash.com/photo-1470164971321-eb5ac2c35f2e?w=300)

