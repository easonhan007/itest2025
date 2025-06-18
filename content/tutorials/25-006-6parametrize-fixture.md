---
weight: 6
title: 6.Parametrize Fixture
date: '2017-10-29T07:22:42+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1490682143684-14369e18dce8?w=300
tags: []
categories:
- pytest从入门到精通
lightgallery: true
toc:
  auto: false
---



### 背景

```@pytest.mark.parametrize```  装饰器可以让我们每次参数化fixture的时候传入多个项目。回忆上一节，我们参数化的时候只能传入传入1个字符串或者是其他的数据对象，parametrize每次多个参数，更加灵活。

### 例子

```python
import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

test_eval方法中传入了2个参数，就如同```@pytest.mark.parametrize```装饰器中定义的那样，因此简单理解，我们可以把parametrize装饰器想象成是数据表格，有表头(test_input,expected)以及具体的数据。

###  运行结果

```
$ pytest
======= test session starts ========
platform linux -- Python 3.x.y, pytest-3.x.y, py-1.x.y, pluggy-0.x.y
rootdir: $REGENDOC_TMPDIR, inifile:
collected 3 items

test_expectation.py ..F

======= FAILURES ========
_______ test_eval[6*9-42] ________

test_input = '6*9', expected = 42

    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 42),
    ])
    def test_eval(test_input, expected):
>       assert eval(test_input) == expected
E       AssertionError: assert 54 == 42
E        +  where 54 = eval('6*9')

test_expectation.py:8: AssertionError
======= 1 failed, 2 passed in 0.12 seconds ========
```




原始封面

![课程图片](https://images.unsplash.com/photo-1490682143684-14369e18dce8?w=300)

