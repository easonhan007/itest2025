---
weight: 16
title: （十六）执行javascript
date: '2017-07-31T02:49:18+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1520034475321-cbe63696469a?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### 执行javascript

使用driver.executeScript(js)方法会在当前的定位上下文里执行相应的js脚本。


### 传参

executeScript方法支持向脚本中传入参数，所有参数的参数都可以在脚本中通过```arguments```对象来引用。我们可以传入下列类型的参数:

* boolean
* number
* string
* WebElement:也就是我们定位到的页面对象
* Array或者是Object: 只要里面的每一项都是上面的类型就好了


### 返回值

同样的，我们可以接收js脚本的返回值，返回值有下面一些情况

* 如果js返回HTML元素，那么该元素会自动被封装成WebElement
* null 或者 undefined会被转成null
* boolean, number, string 不做转换
* function会被转成相应的字符串表示
* Array和Object中的每一项都按照上面的规则转换

### 目的

* 学会使用executeScript(js)方法
* 学会向js脚本中传参
* 学会从js脚本中接收返回值

### 场景

打开[百度首页](http://www.baidu.com/)

* 先隐藏掉**百度一下**按钮
* 然后返回页面上所有导航链接的文本
* 最后把页面背景变成黑色

### 代码

```javascript
var path = require('path');
var webdriver = require('selenium-webdriver'),
  By = webdriver.By;

var url = "http://www.baidu.com/";

var dr = new webdriver.Builder().forBrowser('chrome').build();
dr.get(url)

// 先隐藏掉百度一下按钮
// 通过arguments[0]传入百度一下按钮
var hideBtn = "arguments[0].style.display='none';"

dr.executeScript(hideBtn, dr.findElement(By.id('su')));


// 然后返回页面上所有导航链接的文本
// 通过return返回需要的结果
var linkTexts = "return $('.mnav').text()"
dr.executeScript(linkTexts).then(function(texts) {
  console.log(texts);
});

// 最后把页面背景变成黑色

dr.executeScript("document.body.style.backgroundColor='black'");
```

### 运行结果

浏览器

![](http://wx4.sinaimg.cn/mw1024/726a2979gy1fhp354hg8ij21ku0xegop.jpg)

命令行输出

```
新闻hao123地图视频贴吧学术
```




原始封面

![课程图片](https://images.unsplash.com/photo-1520034475321-cbe63696469a?w=300)

