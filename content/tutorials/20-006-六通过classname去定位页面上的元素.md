---
weight: 6
title: （六）通过className去定位页面上的元素
date: '2017-08-08T02:28:40+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1492446190781-58ac4285911d?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### 为什么是className

用className定位实际上是通过元素的html属性class定位，由于最早的webdriver client版本是使用java实现的，java中class是一个保留字，class不给用，所以就使用了className来替代。

### 复合的class属性

selenium**不支持**复合的class属性。比如```class="col-md-1 col-sm-2"```，我们只能通过```col-md-1```或者是```col-sm-2```来定位，不能同时使用这2个class进行定位。

### 目的

* 熟悉selenium webdriver 定位方式
* 学会通过class属性去定位元素

### 练习对象

我们使用[html5-test-page](https://github.com/cbracco/html5-test-page/blob/master/index.html)作为我们的练习对象。

将html代码拷贝一份并保存到本地，文件名为```index.html```。

### 场景

我们将使用className定位下面html代码所示的输入框，并输入一些内容

```html
<p>
  <label for="input__text3" class="error">Error</label>
  <input id="input__text3" class="is-error" type="text" placeholder="Text Input">
</p>
<p>
  <label for="input__text4" class="valid">Valid</label>
  <input id="input__text4" class="is-valid" type="text" placeholder="Text Input">
</p>
```

### 代码

```javascript
var path = require('path');
var webdriver = require('selenium-webdriver'),
  By = webdriver.By;

var testFile = "file://" + path.join(__dirname,  "index.html")

var dr = new webdriver.Builder().forBrowser('chrome').build();
dr.get(testFile)

dr.findElement(By.className('is-error')).sendKeys('should be error');
dr.findElement(By.className('is-valid')).sendKeys('should be valid');

```


### 运行结果

如下图所示

![](http://wx3.sinaimg.cn/mw690/726a2979gy1fhb4ojpahqj20ea04ydfw.jpg)




原始封面

![课程图片](https://images.unsplash.com/photo-1492446190781-58ac4285911d?w=300)

