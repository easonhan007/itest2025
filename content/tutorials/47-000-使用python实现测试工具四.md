---
weight: 0
title: 使用python实现测试工具(四)
date: '2018-08-21T06:55:32+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1466854076813-4aa9ac0fc347?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



本系列教程使用的python版本是**3.6.3**。

### 背景

这一节我们对unittest模块做一丁点的扩展，我们将实现动态运行用例的功能。

测试用例如下，基本上是从python官方文档上摘取的。

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split_important(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
```

### 运行TestCase下全部的用例

这个需求是最常见的。根据官网的文档，代码实现如下

```python
# load all test methods from a TestCase class
common_suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(common_suite)
```
使用```TestLoader```类中自带的```loadTestsFromTestCase```方法创建```TestSuite```运行既可。


### 运行TestCase下的某些用例

我们可以手动添加TestCase下的部分用例，然后一次执行。核心方法是使用```addTest()```方法

```python
# add only 1 test method
one_case_suite = unittest.TestSuite()
one_case_suite.addTest(TestStringMethods('test_upper'))
unittest.TextTestRunner(verbosity=2).run(one_case_suite)
```

### 给用例打标签，只运行某些具有标签的用例

很多的测试框架都有类似的功能，我们可以用最简单的方式在unittest中实现类似功能。这里有一个小小的trick，就是我们通过命名测试用例的方式来实现打标签的功能。比如我们可以在测试方法名称后加上```_important```表示这是重要的测试方法，需要在每天进行回归。

```python
# only run test methods the name of which ends with important
only_run_important_suite = unittest.TestSuite()
for case in [method for method in dir(TestStringMethods) if method.endswith('important')]:
    only_run_important_suite.addTest(TestStringMethods(case))
unittest.TextTestRunner(verbosity=2).run(only_run_important_suite)
```

这里的关键点是

* 在测试方法名后加上标签的名字
* 使用```dir(ClassName)```的方式获取该类下所有定义的方法名
* 使用```addTest()```动态添加用例


### 自定义用例的运行顺序

下面的代码演示了如何按照用例名称的长度，由长到短运行用例方法。也就是名称长的先执行，名称短的后执行。

```python
# run test methods in custom order
custom_order_suite = unittest.TestSuite()
for case in sorted([method for method in dir(TestStringMethods) if method.startswith('test_')], key=len, reverse=True):
    custom_order_suite.addTest(TestStringMethods(case))
unittest.TextTestRunner(verbosity=2).run(custom_order_suite)
```

### 源码地址

[github地址](https://github.com/easonhan007/simple_test_tools)




原始封面

![课程图片](https://images.unsplash.com/photo-1466854076813-4aa9ac0fc347?w=300)

