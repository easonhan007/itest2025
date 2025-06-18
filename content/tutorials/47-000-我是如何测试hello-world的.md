---
weight: 0
title: 我是如何测试hello world的
date: '2018-01-08T10:10:24+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



回顾一下问题，对于下面这种简单的hello world代码，我们应该怎么测试呢？

```python

print('hello world')

```

下面是我的一些思路，抛砖引玉。

**注意:下面的代码均在python2.7中运行通过，python3可能无法运行**


### 重构代码，测试输出

第一种方式很容易想到，上面的代码没有办法很好的进行测试是因为我们不太好去自动判断输出。

如果能够拿到具体的输出，然后判断输出是否符合预期，这样测试就相对容易了。

这里我们需要先假设```print```方法是python的内置方法，是可以信任，不需要进行测试的，那么我们的测试点就变成了测试```print```方法的入参是不是我们所期望的```hello world```字符串。

重构代码，达到我们的目的，并进行测试

```python
# test_hello_world.py
import unittest

def return_hello_world():
    return 'hello world'

print(return_hello_world())


class HelloWorldTest(unittest.TestCase):

    def test_return_hello_world(self):
        self.assertEqual('hello world', return_hello_world())


if __name__ == '__main__':
    unittest.main()
```

### 拿到标准输出里的内容做断言

其实```print```是将参数中的内容打印到标准输出设备，我们只要知道标准输出设备究竟输出了什么内容就可以比较容易的对简单的hello world进行测试了。

参考[这个回答](https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call)，我们将实现调用```print('hello world')```，然后拿到标准输出中的内容，再去判断标准输出中的内容是否是```hello world```，代码如下

```python
# test_hello_world_1.py

import unittest
import sys
from cStringIO import StringIO
# for python 3
# from io import StringIO

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class TestHelloWorld1(unittest.TestCase):

    def test_hello_world(self):
        with Capturing() as output:
            print("hello world")
            print("hello python")
            print("hello python 2.7")

        self.assertEqual("hello world", output[0])
        self.assertEqual("hello python", output[1])
        self.assertEqual("hello python 2.7", output[-1])

if __name__ == '__main__':
    unittest.main()
```

### 使用pytest框架进行测试

pytest框架自带了捕获标准输出内容的特性，可以参考[官方文档](https://docs.pytest.org/en/latest/capture.html)

这里贴一下官方文档的示例代码,启发一下思路。


```python
def test_myoutput(capsys): # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"
```




原始封面

![课程图片](https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=300)

