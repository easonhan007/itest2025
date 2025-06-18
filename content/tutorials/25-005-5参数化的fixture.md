---
weight: 5
title: 5.参数化的Fixture
date: '2017-10-30T07:22:42+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1464254786740-b97e5420c299?w=300
tags: []
categories:
- pytest从入门到精通
lightgallery: true
toc:
  auto: false
---



### 背景

继续上一节的测试需求，在上一节里，任何1条测试数据导致断言不通过后测试用例就会停止运行，这样每次只能检查出1条不符合规范的数据，有没有什么办法可以一次性把所有的不符合结果都测出来呢？

这时候我们就需要用到参数化的fixture特性了

### 更新数据文件

新建```users.test.json```文件，内容如下

```json
[
  {"name":"jack","password":"Iloverose"},
  {"name":"rose","password":"Ilovejack"}
  {"name":"tom","password":"password123"},
  {"name":"mike","password":"password"},
  {"name":"james","password":"AGoodPasswordWordShouldBeLongEnough"}
]
```

我们增加了2条用户信息，其中mike的密码是弱密码。

### 参数化fixture

参数化fixture允许我们向fixture提供参数，参数可以是list，该list中有几条数据，fixture就会运行几次，相应的测试用例也会运行几次。

参数化fixture的语法是

```python
@pytest.fixture(params=["smtp.gmail.com", "mail.python.org"])
```

其中```len(params)```的值就是用例执行的次数

在fixture的定义中，可以使用```request.param```来获取每次传入的参数，如下:

```python
@pytest.fixture(scope="module",
                params=["smtp.gmail.com", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp
    print ("finalizing %s" % smtp)
    smtp.close()
```

* 上面的代码smtp fixture会执行2次
* 第1次```request.param == 'smtp.gmail.com'```
* 第2次```request.param == 'mail.python.org'```

### 实现用例

我们现在使用参数化fixtures来实现一次性检查出弱密码的用例。

新建文件```test_user_password_with_params.py```，内容如下:

```python

import pytest
import json
users = json.loads(open('./users.test.json', 'r').read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" %(user['name'])
        assert passwd != 'password', msg
        assert passwd != 'password123', msg
```

上面的例子里，我们先把所有用户信息读到users变量里，注意users这时候是list类型，可以直接传入到fixture的params


### 运行及结果

运行

```
pytest test_user_password_with_params.py
```

结果

```
$ pytest test_user_password_with_params.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 2.7.12, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
rootdir: /Users/easonhan/code/testclass.net/src/pytest, inifile:
collected 5 items

test_user_password_with_params.py ..FF.

============================================================================== FAILURES ===============================================================================
_________________________________________________________ TestUserPasswordWithParam.test_user_password[user2] _________________________________________________________

self = <test_user_password_with_params.TestUserPasswordWithParam object at 0x10de1d790>, user = {'name': 'tom', 'password': 'password123'}

    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" %(user['name'])
        assert passwd != 'password', msg
>       assert passwd != 'password123', msg
E       AssertionError: user tom has a weak password
E       assert 'password123' != 'password123'

test_user_password_with_params.py:15: AssertionError
_________________________________________________________ TestUserPasswordWithParam.test_user_password[user3] _________________________________________________________

self = <test_user_password_with_params.TestUserPasswordWithParam object at 0x10de1df50>, user = {'name': 'mike', 'password': 'password'}

    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" %(user['name'])
>       assert passwd != 'password', msg
E       AssertionError: user mike has a weak password
E       assert 'password' != 'password'

test_user_password_with_params.py:14: AssertionError
================================================================= 2 failed, 3 passed in 0.05 seconds ==================================================================
```

稍微留意一下, 可以看出tom和mike使用了弱密码。总共运行了5个用例,3个成功,2个失败。

### fixture的更多特性

fixture还有很多更加灵活和深入的用法，具体见[这里](https://docs.pytest.org/en/latest/fixture.html#pytest-fixtures-explicit-modular-scalable)




原始封面

![课程图片](https://images.unsplash.com/photo-1464254786740-b97e5420c299?w=300)

