---
weight: 14
title: （十四）处理下拉列表 select
date: '2017-08-01T01:49:18+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1450631835004-9b95ff5cd66f?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### 什么是下拉列表

```html
<select id="select">
  <optgroup label="Option Group">
    <option>Option One</option>
    <option>Option Two</option>
    <option>Option Three</option>
  </optgroup>
</select>

```

下拉列表的标签是select，如上所示，其中

* select表示下拉列表
* option表示列表里的子项

上面的html里，这个下拉列表中一共有3项，分别是Option One, Option Two和Option Three。


### 目的

* 学会选择下拉列表里的特定项目
* 学会使用层级定位

### 场景

选择上面html代码所示的下拉列表的最后一项，也就是Option Three。

### 代码

```javascript

var path = require('path');
var webdriver = require('selenium-webdriver'),
  By = webdriver.By;

var testFile = "file://" + path.join(__dirname,  "index.html")

var dr = new webdriver.Builder().forBrowser('chrome').build();
dr.get(testFile)

dr.findElement(By.id('select')).then(function(select) {
  dr.findElements(By.css('option')).then(function(options) {
    options[options.length - 1].click();
  });
});

```

### 运行结果

![](http://wx4.sinaimg.cn/mw1024/726a2979gy1fhp1kxp8qdj20f606kaa6.jpg)




原始封面

![课程图片](https://images.unsplash.com/photo-1450631835004-9b95ff5cd66f?w=300)

