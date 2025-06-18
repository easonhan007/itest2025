---
weight: 5
title: （五）WebDriver常用方法
date: '2017-06-26T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1465056836041-7f43ac27dcb5?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---



<br>
### 点击和输入
前面我们已经学习了定位元素， 定位只是第一步， 定位之后需要对这个元素进行操作， 或单击（按钮）
或输入（输入框） ， 下面就来认识 WebDriver 中最常用的几个方法：

 * clear()： 清除文本。

 * send_keys (value)： 模拟按键输入。

 * click()： 单击元素。

```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.quit()
```



<br>
### 提交

 * submit()

submit()方法用于提交表单。 例如， 在搜索框输入关键字之后的“回车” 操作， 就可以通过该方法模拟。

```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()

driver.quit()
```
有时候 submit()可以与 click()方法互换来使用， submit()同样可以提交一个按钮， 但 submit()的应用范围远不及 click()广泛。

<br>
### 其他常用方法

 * size： 返回元素的尺寸。

 * text： 获取元素的文本。

 * get_attribute(name)： 获得属性值。

 * is_displayed()： 设置该元素是否用户可见。

```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()

```
输出结果：
```
{'width': 500, 'height': 22}
©2015 Baidu 使用百度前必读 意见反馈 京 ICP 证 030173 号
text
True
```
执行上面的程序并查看结果： size 方法用于获取百度输入框的宽、 高， text 方法用于获得百度底部的备案信息， get_attribute()用于获得百度输入的 type 属性的值， is_displayed()用于返回一个元素是否可见， 如果可见则返回 True， 否则返回 False。




原始封面

![课程图片](https://images.unsplash.com/photo-1465056836041-7f43ac27dcb5?w=300)

