---
weight: 17
title: （十七）调用JavaScript代码
date: '2017-06-14T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1464039397811-476f652a343b?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---


<br>
虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了execute_script()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：
```html
<!-- window.scrollTo(左边距,上边距); -->
window.scrollTo(0,450);
```
window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。其代码如下：

```python
from selenium import webdriver
from time import sleep

# 访问百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小
driver.set_window_size(500, 500)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()
```
通过浏览器打开百度进行搜索，并且提前通过set_window_size()方法将浏览器窗口设置为固定宽高显示，目的是让窗口出现水平和垂直滚动条。然后通过execute_script()方法执行JavaScripts代码来移动滚动条的位置。




原始封面

![课程图片](https://images.unsplash.com/photo-1464039397811-476f652a343b?w=300)

