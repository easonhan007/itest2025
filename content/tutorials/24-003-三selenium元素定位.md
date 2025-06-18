---
weight: 3
title: （三）selenium元素定位
date: '2017-06-28T07:37:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1512847179643-f1794c3e0ac8?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---



<br>
### selenium定位方法

Selenium提供了8种定位方式。

* id
* name
* class name
* tag name
* link text
* partial link text
* xpath
* css selector

这8种定位方式在Python selenium中所对应的方法为：

 * find_element_by_id()
 * find_element_by_name()
 * find_element_by_class_name()
 * find_element_by_tag_name()
 * find_element_by_link_text()
 * find_element_by_partial_link_text()
 * find_element_by_xpath()
 * find_element_by_css_selector()

<br>
### 定位方法的用法

假如我们有一个Web页面，通过前端工具（如，Firebug）查看到一个元素的属性是这样的。
```
<html>
  <head>
  <body link="#0000cc">
    <a id="result_logo" href="/" onmousedown="return c({'fm':'tab','tab':'logo'})">
    <form id="form" class="fm" name="f" action="/s">
      <span class="soutu-btn"></span>
        <input id="kw" class="s_ipt" name="wd" value="" maxlength="255" autocomplete="off">
```
我们的目的是要定位input标签的输入框。

* 通过id定位:
```
dr.find_element_by_id("kw")
```

* 通过name定位:
```
dr.find_element_by_name("wd")
```

* 通过class name定位:
```
dr.find_element_by_class_name("s_ipt")
```

* 通过tag name定位:
```
dr.find_element_by_tag_name("input")
```

* 通过xpath定位，xpath定位有N种写法，这里列几个常用写法:
```
dr.find_element_by_xpath("//*[@id='kw']")
dr.find_element_by_xpath("//*[@name='wd']")
dr.find_element_by_xpath("//input[@class='s_ipt']")
dr.find_element_by_xpath("/html/body/form/span/input")
dr.find_element_by_xpath("//span[@class='soutu-btn']/input")
dr.find_element_by_xpath("//form[@id='form']/span/input")
dr.find_element_by_xpath("//input[@id='kw' and @name='wd']")
```

* 通过css定位，css定位有N种写法，这里列几个常用写法:
```python
dr.find_element_by_css_selector("#kw")
dr.find_element_by_css_selector("[name=wd]")
dr.find_element_by_css_selector(".s_ipt")
dr.find_element_by_css_selector("html > body > form > span > input")
dr.find_element_by_css_selector("span.soutu-btn> input#kw")
dr.find_element_by_css_selector("form#form > span > input")
```

接下来，我们的页面上有一组文本链接。
```
<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
<a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>
```

* 通过link text定位:
```
dr.find_element_by_link_text("新闻")
dr.find_element_by_link_text("hao123")
```

* 通过link text定位:
```
dr.find_element_by_partial_link_text("新")
dr.find_element_by_partial_link_text("hao")
dr.find_element_by_partial_link_text("123")
```

<br>
关于xpaht和css的定位比较复杂，请参考：
[xpath语法](http://www.w3school.com.cn/xpath/xpath_syntax.asp)、
[css选择器](http://www.w3school.com.cn/cssref/css_selectors.asp)




原始封面

![课程图片](https://images.unsplash.com/photo-1512847179643-f1794c3e0ac8?w=300)

