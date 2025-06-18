---
weight: 2
title: （二）selenium3 浏览器驱动
date: '2017-06-29T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/34/BA1yLjNnQCI1yisIZGEi_2013-07-16_1922_IMG_9873.jpg?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---



<br>
### 下载浏览器驱动

当selenium升级到3.0之后，对不同的浏览器驱动进行了规范。如果想使用selenium驱动不同的浏览器，必须单独下载并设置不同的浏览器驱动。

各浏览器下载地址：

Firefox浏览器驱动：[geckodriver](https://github.com/mozilla/geckodriver/releases)

Chrome浏览器驱动：[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home) , [taobao备用地址](https://npm.taobao.org/mirrors/chromedriver)

IE浏览器驱动：[IEDriverServer](http://selenium-release.storage.googleapis.com/index.html)

Edge浏览器驱动：[MicrosoftWebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver)

Opera浏览器驱动：[operadriver](https://github.com/operasoftware/operachromiumdriver/releases)

PhantomJS浏览器驱动：[phantomjs](http://phantomjs.org)

注：部分浏览器驱动地址需要科学上网。

<br>
### 设置浏览器驱动

设置浏览器的地址非常简单。
我们可以手动创建一个存放浏览器驱动的目录，如： C:\driver , 将下载的浏览器驱动文件（例如：chromedriver、geckodriver）丢到该目录下。

我的电脑-->属性-->系统设置-->高级-->环境变量-->系统变量-->Path，将“C:\driver”目录添加到Path的值中。

* Path
* ;C:\driver

<br>
### 设置浏览器驱动

验证不同的浏览器驱动是否正常使用。

```
from selenium import webdriver


driver = webdriver.Firefox()   # Firefox浏览器

driver = webdriver.Chrome()    # Chrome浏览器

driver = webdriver.Ie()        # Internet Explorer浏览器

driver = webdriver.Edge()      # Edge浏览器

driver = webdriver.Opera()     # Opera浏览器

driver = webdriver.PhantomJS()   # PhantomJS

……

```




![课程图片](https://images.unsplash.com/34/BA1yLjNnQCI1yisIZGEi_2013-07-16_1922_IMG_9873.jpg?w=300)

