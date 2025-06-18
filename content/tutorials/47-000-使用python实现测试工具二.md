---
weight: 0
title: 使用python实现测试工具(二)
date: '2018-07-11T06:55:32+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1473800447596-01729482b8eb?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



本系列教程使用的python版本是**3.6.3**。

### 背景

这一节我们实现一个简单的ui测试工具。

该工具的作用是访问某个页面，然后根据css选择器去定位页面上的元素，最后判断页面上元素的个数与我们的预期是否相符。

举一个具体的例子，比如我们去访问[www.itest.info](www.itest.info)这个页面，我们需要判断页面上```class = thumbnail-img```的元素存在，并且有4个。因为每一个元素代表一门课程，所以这个断言的意思是重定向科技主页上应该有4门主要课程。

视频讲解在[这里](https://ke.qq.com/webcourse/index.html#course_id=246722&term_id=100291046&taid=1567401070281666&vid=x1419ozo3qn)。

### 工具设计

我们设计一个命令行工具，给工具传3个参数。

* 被访问页面的url
* 页面上元素的css选择器
* 预期的元素数量，页面上可以存在n个元素，如果传入0，则表示元素不存在，做反向断言

所以工具大概是这样用的: ```python script_name.py url css_selector length```

### 代码实现

简单起见，我们会用到requests-html库。安装文档在[这里](http://html.python-requests.org/)。

```python

from requests_html import HTMLSession
from sys import argv
DEBUG = True

USAGE = '''
USAGE:
python html_assertion.py www.itest.info .thumbnail-img 4
'''

if len(argv) != 4:
  print(USAGE)
  exit(1)

script_name, url, css_selector, length = argv

if url[:4] != 'http':
  url = 'http://' + url

session = HTMLSession()
r = session.get(url)

elements = r.html.find(css_selector)


def debug():
  if DEBUG:
    print('*' * 100)
    print(f"css选择器: {css_selector}, 共找到{len(elements)}个元素\n")
    for element in elements:
      print(element.html)
      print(element.attrs)
      print()


if len(elements) != int(length):
  print(f"失败! 预期{length}个元素，实际存在{len(elements)}个元素\n")
  debug()
  exit(1)
else:
  print(f"成功!\n")
  debug()


```

### 精讲

* 用例失败之后使用```exit(1)```表示异常退出，这样在使用jenkins运行的时候，用例失败jenkins的job结果也会相应失败
* requests-html库的基本使用参考[这里](http://html.python-requests.org/#tutorial-usage)

### 运行示例

```
# 失败情况
python html_assertion.py www.itest.info .thumbnail-img 1
失败! 预期1个元素，实际存在4个元素

****************************************************************************************************
css选择器: .thumbnail-img, 共找到4个元素

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/7/mission_impossible_cut.jpg"/></div><a class="btn-more hover-effect" href="/courses/7">更多</a></div>
{'class': ('thumbnail-img',)}

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/6/120606ineam4nspdc6qdaw.jpg"/></div><a class="btn-more hover-effect" href="/courses/6">更多</a></div>
{'class': ('thumbnail-img',)}

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/3/12.jpg"/></div><a class="btn-more hover-effect" href="/courses/3">更多</a></div>
{'class': ('thumbnail-img',)}

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/2/13.jpg"/></div><a class="btn-more hover-effect" href="/courses/2">更多</a></div>
{'class': ('thumbnail-img',)}

# 成功情况
python html_assertion.py www.itest.info .thumbnail-img 4
成功!

****************************************************************************************************
css选择器: .thumbnail-img, 共找到4个元素

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/7/mission_impossible_cut.jpg"/></div><a class="btn-more hover-effect" href="/courses/7">更多</a></div>
{'class': ('thumbnail-img',)}

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/6/120606ineam4nspdc6qdaw.jpg"/></div><a class="btn-more hover-effect" href="/courses/6">更多</a></div>
{'class': ('thumbnail-img',)}

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/3/12.jpg"/></div><a class="btn-more hover-effect" href="/courses/3">更多</a></div>
{'class': ('thumbnail-img',)}

<div class="thumbnail-img"><div class="overflow-hidden"><img class="img-responsive" src="/uploads/course/image/2/13.jpg"/></div><a class="btn-more hover-effect" href="/courses/2">更多</a></div>
{'class': ('thumbnail-img',)}
```

### 动手时间

* 抄一遍代码，看自己能不能运行起来
* 给这段代码每一行都加上注释，理解代码做了些什么

### 扩展阅读

* [最新的爬虫工具REQUESTS-HTML](http://www.testclass.net/2018/04/25/requests-html/)
* [css选择器](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)

### 源码地址

[github地址](https://github.com/easonhan007/simple_test_tools)




原始封面

![课程图片](https://images.unsplash.com/photo-1473800447596-01729482b8eb?w=300)

