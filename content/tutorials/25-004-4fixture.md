---
weight: 4
title: 4.Fixture
date: '2017-10-31T07:22:42+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1529688124-e6c364d3285c?w=300
tags: []
categories:
- pytest从入门到精通
lightgallery: true
toc:
  auto: false
---



我们可以简单的把Fixture理解为准备测试数据和初始化测试对象的阶段。

一般我们对测试数据和测试对象的管理有这样的一些场景

* 所有用例开始之前初始化测试数据或对象
* 所有用例结束之后销毁测试数据或对象
* 每个用例开始之前初始化测试数据或对象
* 每个用例结束之后销毁测试数据或对象
* 在每个／所有module的用例开始之前初始化数据或对象
* 在每个／所有module的用例开始之后销毁数据或对象
* ......
* ......

pytest的fixture特性可以满足上面的需求。

### 简单的例子

考虑这种场景，我们需要判断用户的密码中包含简单密码，规则是这样的，密码必须至少6位，满足6位的话判断用户的密码不是password123或者password之类的弱密码。

我们将用户的信息导出成名为users.dev.json的文件，该文件如下所示

```json
[
  {"name":"jack","password":"Iloverose"},
  {"name":"rose","password":"Ilovejack"},
  {"name":"tom","password":"password123"}
]

```

新建名为test_user_password.py的文件，键入以下内容，一定要**保证users.dev.json文件与该文件在同一路径下**

```python
import pytest
import json

class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read()) # 读取当前路径下的users.dev.json文件，返回的结果是dict

    def test_user_password(self, users):
        # 遍历每条user数据
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a weak password" %(user['name'])
            assert passwd != 'password', msg
            assert passwd != 'password123', msg
```

### 运行

pytest可以通过指定文件名的方式运行单个用例文件，这里我们只运行test_user_password.py文件

```
pytest test_user_password.py
```

### 运行结果

```
$ pytest test_user_password.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 2.7.12, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
rootdir: /Users/easonhan/code/testclass.net/src/pytest, inifile:
collected 1 item

test_user_password.py F

============================================================================== FAILURES ===============================================================================
_________________________________________________________________ TestUserPassword.test_user_password _________________________________________________________________

self = <test_user_password.TestUserPassword object at 0x1046e3290>
users = [{'name': 'jack', 'password': 'Iloverose'}, {'name': 'rose', 'password': 'Ilovejack'}, {'name': 'tom', 'password': 'password123'}]

    def test_user_password(self, users):
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a weak password" %(user['name'])
            assert passwd != 'password', msg
>           assert passwd != 'password123', msg
E           AssertionError: user tom has a weak password
E           assert 'password123' != 'password123'

test_user_password.py:14: AssertionError
====================================================================== 1 failed in 0.03 seconds =======================================================================
```

### 分析

* 使用@pytest.fixture装饰器可以定义feature
* 在用例的参数中传递fixture的名称以便直接调用fixture，拿到fixture的返回值
* 3个assert是递进关系，前1个assert断言失败后，后面的assert是不会运行的，因此重要的assert放到前面
* ``` E           AssertionError: user tom has a weak password```可以很容易的判断出是哪条数据出了问题，所以定制可读性好的错误信息是很必要的
* 任何1个断言失败以后，for循环就会退出，所以上面的用例1次只能发现1条错误数据，换句话说任何1个assert失败后，用例就终止运行了

### 执行顺序

pytest是这样运行上面的用例的

1. pytest找到以test_开头的方法，也就是```test_user_password```方法，执行该方法时发现传入的参数里有跟fixture users名称相同的参数
2. pytest认定users是fixture，执行该fixture，读取json文件解析成dict实例
3. test_user_password方法真正被执行，users fixture被传入到该方法

**注意** 我们可以使用下面的命令来查看用例中可用的fixtures

```python
pytest --fixtures test_user_password.py
```

### 数据清理

有时候我们需要在用例结束的时候去清理一些测试数据，或清除测试过程中创建的对象，我们可以使用下面的方式

```python
import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp():
    smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp  # provide the fixture value
    print("teardown smtp")
    smtp.close()
```

* yield 关键字返回了fixture中实例化的对象smtp
* module中的用例执行完成后```smtp.close()```方法会执行，无论用例的运行状态是怎么样的,都会执行

### 更多的数据清理方式

```addfinalizer``` 也可以完成数据清理的工作，具体见(这里)[https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code]




原始封面

![课程图片](https://images.unsplash.com/photo-1529688124-e6c364d3285c?w=300)

