---
weight: 0
title: 安利一下pytest的mark用法
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1519120944692-1a8d8cfc107f?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



昨天有同事分享了pytest的相关内容，忽然想起pytest在运行用例时有非常大的灵活性，很适合跟jenkins任务结合起来实现一些动态用例运行的效果。

我们以下面这个非常简单的测试用例为例，说明一下如何使用pytest实现一些动态的测试策略


```python
# runner_example.py
import pytest

@pytest.mark.p1
def test_1():
    assert 1 == 1

@pytest.mark.p2
def test_2():
    assert 1 in [1, 2, 3]

@pytest.mark.p3
def test_3():
    assert 3 / 2 == 1

@pytest.mark.p0
def test_4():
    assert 'abc'[::-1] == 'cba'

```

上面例子里，我们使用```@pytest.mark```装饰器定义了4种类型的用例，分别是p0/p1/p2/p3。按惯例，p0的用例是优先级最高的用例，p3优先级最低。

### 场景1: 只运行p0的测试用例

这个非常简单，在命令行中输入

```
pytest runner_example.py -m p0
```

这里runner_example.py是包含测试用例的名字，默认情况下pytest会认为所有名称以```test_```开头的函数都是测试用例。

运行结果

```
================================================================ test session starts =================================================================
platform darwin -- Python 2.7.15, pytest-4.6.3, py-1.8.0, pluggy-0.12.0
rootdir: /Users/yichun.han/code/testclass.net/src/pytest
collected 4 items / 3 deselected / 1 selected

runner_example.py .                                                                                                                            [100%]
```

符合预期。

### 场景2: 只运行p0和p1的用例

可以用or来实现。

```
pytest runner_example.py -m "p0 or p1"

```

-m参数后面可以接python的表达式，所以用or关键字就可以实现多选的效果了。

运行结果

```
================================================================ test session starts =================================================================
platform darwin -- Python 2.7.15, pytest-4.6.3, py-1.8.0, pluggy-0.12.0
rootdir: /Users/yichun.han/code/testclass.net/src/pytest
collected 4 items / 2 deselected / 2 selected

runner_example.py ..                                                                                                                           [100%]

================================================================== warnings summary ==================================================================
```

可以看到运行了2个用例。

###  场景3:运行除p0之外的所有用例

还是用表达式，不过这次用的是not。

```
pytest runner_example.py -m "not p0"
```

运行结果

```
================================================================ test session starts =================================================================
platform darwin -- Python 2.7.15, pytest-4.6.3, py-1.8.0, pluggy-0.12.0
rootdir: /Users/yichun.han/code/testclass.net/src/pytest
collected 4 items / 1 deselected / 3 selected

runner_example.py ...                                                                                                                          [100%]

================================================================== warnings summary ==================================================================
```

### 总结

* 我们可以使用@pytest.mark装饰器来给用例分类
* 运行的时候使用-m，m是mark的意思，来运行某个或某些分类
* -m参数支持python表达式
* 用or实现多选的效果
* 用not实现反选的效果




原始封面

![课程图片](https://images.unsplash.com/photo-1519120944692-1a8d8cfc107f?w=300)

