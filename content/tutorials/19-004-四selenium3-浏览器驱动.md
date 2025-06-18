---
weight: 4
title: （四）selenium3 浏览器驱动
date: '2017-07-04T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1525135501285-621c7433f0f0?w=300
tags: []
categories:
- slenium java 语言教程
lightgallery: true
toc:
  auto: false
---



<br>
### 下载浏览器驱动

当selenium升级到3.0之后，对不同的浏览器驱动进行了规范。如果想使用selenium驱动不同的浏览器，必须单独下载并设置不同的浏览器驱动。

各浏览器下载地址：

Firefox浏览器驱动：[geckodriver](https://github.com/mozilla/geckodriver/releases)

Chrome浏览器驱动：[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home)  [taobao备用地址](https://npm.taobao.org/mirrors/chromedriver)

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

```java
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.opera.OperaDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriver;

……

WebDriver driver = new ChromeDriver();    //Chrome浏览器

WebDriver driver = new FirefoxDriver();   //Firefox浏览器

WebDriver driver = new EdgeDriver();      //Edge浏览器

WebDriver driver = new InternetExplorerDriver();  // Internet Explorer浏览器

WebDriver driver = new OperaDriver();     //Opera浏览器

WebDriver driver = new PhantomJSDriver();   //PhantomJS

……
```




原始封面

![课程图片](https://images.unsplash.com/photo-1525135501285-621c7433f0f0?w=300)

