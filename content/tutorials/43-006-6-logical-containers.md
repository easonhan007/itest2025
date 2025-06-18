---
weight: 6
title: 6. Logical Containers
date: '2017-10-24T06:55:26+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1495465798138-718f86d1a4bc?w=300
tags: []
categories:
- webium简明教程
lightgallery: true
toc:
  auto: false
---



逻辑容器适用于这样的场景：页面上有一些元素确实存在于容器中，但这些元素都有可以唯一能够定位的属性，比如id等，而我们为了代码的可读性，往往希望将这些元素放在某个容器中。

比如页面上的菜单元素，每个子菜单都有id属性，不过为了代码能够更好的被他人理解，我们希望将子菜单放到菜单容器里。

逻辑容器和普通容器的区别：

* 普通容器需要继承自```WebElement```，而逻辑容器不需要
* 定义逻辑容器时Find方法不需要by和value参数

```python
from selenium.webdriver.common.by import By
from webium import Find, BasePage


class Nav(object):
    class_info = Find(by=By.CSS_SELECTOR, value='a[href*="/newclass"]')
    faq = Find(by=By.CSS_SELECTOR, value='a[href*="/faq"]')


class ItestPage(BasePage):
    # here we are just grouping Header elements together without any influence on actual search
    nav = Find(Nav)

    def __init__(self):
        super(StructuredPage, self).__init__(url='http://itest.info')


if __name__ == '__main__':
    page = ItestPage()
    page.open()
    print(page.menu.class_info.text)
    print(page.menu.faq.text)

```



原始封面

![课程图片](https://images.unsplash.com/photo-1495465798138-718f86d1a4bc?w=300)

