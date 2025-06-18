---
weight: 6
title: 6.unittest框架
date: '2017-08-25T04:41:43+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1527192491265-7e15c55b1ed2?w=300
tags: []
categories:
- python接口测试实践教程
lightgallery: true
toc:
  auto: false
---



在我们真正的编写测试用例之前，我们需要了解一下测试框架。

unittest是python自带的单元测试框架，尽管其主要是为单元测试服务的，但我们也可以用它来做接口的自动化测试。

unittest框架为我们编写用例提供了如下的能力

* 定义用例的能力。unittest框架有一套固有套路，可以让我们定义测试用例时更加简单和统一

* 断言的能力。unittest框架提供了一系列的断言

* 各种执行策略。通过test suit或者扩展的方式，我们可以自定义用例执行的策略

### 简单的例子

```python
import unittest

class StringTestCase(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.test_string = "This is a string"

    def testUpper(self):
        # Act and Assert
        self.assertEqual("THIS IS A STRING", self.test_string.upper())

if __name__ == '__main__':
    unittest.main()

```

### 剖析

```python
import unittest
```

导入unittest库，不导入就没办法使用，好比手机如果要使用某个app就必须先安装该app一样，是套路，记住就好。

------------

```python
class StringTestCase(unittest.TestCase):
```

定义测试类，初学者看到这一行就害怕，其实大可不必。这还是套路，测试类的名字你可以随意取，当然了首字母最好大写，这样更符合规范一些。所有的测试类都必须直接或间接的继承自```unittest.TestCase```类。总之，这还是套路，记住就好。

------------

```python
def setUp(self):
    # Arrange
    self.test_string = "This is a string"
```

继续套路。```setUp(self)```方法是一个钩子方法，在每个测试用例执行之前都会执行一次，是做数据初始化的好地方。

在上面的例子里，我们为每一个测试方法都定义了被测对象，```self.test_string```

------------

```python
def testUpper(self):
    # Act and Assert
    self.assertEqual("THIS IS A STRING", self.test_string.upper())
```

套路继续。这里定义了一个名为```testUpper```的测试方法，这个方法就是一个测试用例。

**注意，只有方法名以test开头的方法才是测试用例**

```self.assertEqual```是一个断言方法，作用是如果第一个参数跟第二个参数相等，那么用例通过，否则用例失败，并在测试报告中打印出错误原因。上面的例子里，我们判断```self.test_string.upper()```方法会将```"This is a string"```字符串转换成```"THIS IS A STRING"```

------------


```python
if __name__ == '__main__':
    unittest.main()
```

最后依然是套路，上面的代码表示，如果直接执行该python文件的话，就运行所有的测试类里的测试用例，也就是运行所有的以**test**开头的方法。

### 总结

使用unittest的话需要记住下面的几点

* 导入unittest
* 定义继承自```unittest.TestCase```的测试类
* 定义以**test**开头的测试方法，这个方法就是测试用例，你可以在一个类里定义n个测试用例
* 断言
* ```unittest.main()```是执行测试用例最简单的方式




原始封面

![课程图片](https://images.unsplash.com/photo-1527192491265-7e15c55b1ed2?w=300)

