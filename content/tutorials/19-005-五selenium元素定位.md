---
weight: 5
title: （五）selenium元素定位
date: '2017-07-04T07:37:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=300
tags: []
categories:
- slenium java 语言教程
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

* findElement(By.id())
* findElement(By.name())
* findElement(By.className())
* findElement(By.tagName())
* findElement(By.linkText())
* findElement(By.partialLinkText())
* findElement(By.xpath())
* findElement(By.cssSelector())

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
driver.findElement(By.id("kw"))
```

* 通过name定位:
```
driver.findElement(By.name("wd"))
```

* 通过class name定位:
```
driver.findElement(By.className("s_ipt"))
```

* 通过tag name定位:
```
driver.findElement(By.tagName("input"))
```

* 通过xpath定位，xpath定位有N种写法，这里列几个常用写法:
```java
driver.findElement(By.xpath("//*[@id='kw']"))
driver.findElement(By.xpath("//*[@name='wd']"))
driver.findElement(By.xpath("//input[@class='s_ipt']"))
driver.findElement(By.xpath("/html/body/form/span/input"))
driver.findElement(By.xpath("//span[@class='soutu-btn']/input"))
driver.findElement(By.xpath("//form[@id='form']/span/input"))
driver.findElement(By.xpath("//input[@id='kw' and @name='wd']"))
```

* 通过css定位，css定位有N种写法，这里列几个常用写法:
```java
driver.findElement(By.cssSelector("#kw")
driver.findElement(By.cssSelector("[name=wd]")
driver.findElement(By.cssSelector(".s_ipt")
driver.findElement(By.cssSelector("html > body > form > span > input")
driver.findElement(By.cssSelector("span.soutu-btn> input#kw")
driver.findElement(By.cssSelector("form#form > span > input")
```

接下来，我们的页面上有一组文本链接。
```
<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
<a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>
```

* 通过link text定位:
```
driver.findElement(By.linkText("新闻")
driver.findElement(By.linkText("hao123")
```

* 通过link text定位:
```
driver.findElement(By.partialLinkText("新")
driver.findElement(By.partialLinkText("hao")
driver.findElement(By.partialLinkText("123")
```

<br>
关于xpaht和css的定位比较复杂，请参考：
[xpath语法](http://www.w3school.com.cn/xpath/xpath_syntax.asp)、
[css选择器](http://www.w3school.com.cn/cssref/css_selectors.asp)




原始封面

![课程图片](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=300)

