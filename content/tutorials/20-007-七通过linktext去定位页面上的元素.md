---
weight: 7
title: （七）通过linkText去定位页面上的元素
date: '2017-08-07T02:59:32+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1509515837298-2c67a3933321?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### 链接的定位

链接可以使用By.linkText和By.partialLinkText的方式去定位。

链接的html标签是```<a></a>```。

看这个html代码```<a href="http://www.itet.info">这就是linkText<a>```，这里**[这就是linkText]** 便是这个链接的linkText，partialLinkText指的是部分的链接文本，如果链接的文本过长的时候，使用partialLinkText会起到简化代码的作用。


### 目的

* 熟悉selenium webdriver 定位方式
* 学会通过linkText和partialLinkText属性去定位元素
* 学会使用```getAttribute()```方法获取html元素的属性
* 学会使用```then()```方法传入回调函数来搞定Thenable的Promise

### 练习对象

我们使用[html5-test-page](https://github.com/cbracco/html5-test-page/blob/master/index.html)作为我们的练习对象。

将html代码拷贝一份并保存到本地，文件名为```index.html```。

### 场景

定位下面html代码所示的a元素，并打印这些元素的href属性

```html
<ul>
  <li><a href="#text__headings">Headings</a></li>
  <li><a href="#text__paragraphs">Paragraphs</a></li>
  <li><a href="#text__blockquotes">Blockquotes</a></li>
  <li><a href="#text__lists">Lists</a></li>
  <li><a href="#text__hr">Horizontal rules</a></li>
  <li><a href="#text__tables">Tabular data</a></li>
  <li><a href="#text__code">Code</a></li>
  <li><a href="#text__inline">Inline elements</a></li>
</ul>
```

### 代码

```javascript
var path = require('path');
var webdriver = require('selenium-webdriver'),
  By = webdriver.By;

var testFile = "file://" + path.join(__dirname,  "index.html");

var dr = new webdriver.Builder().forBrowser('chrome').build();
dr.get(testFile);

dr.findElement(By.linkText('Headings')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.linkText('Paragraphs')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.linkText('Blockquotes')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.linkText('Lists')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.linkText('Horizontal rules')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.linkText('Tabular data')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.linkText('Code')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.findElement(By.partialLinkText('Inline')).getAttribute('href').then(function(href) {
  console.log(href);
});

dr.quit();

```


### 运行结果

xxxx代表你的本机index.html的路径

```

file://xxxx/index.html#text__headings
file://xxxx/index.html#text__paragraphs
file://xxxx/index.html#text__blockquotes
file://xxxx/index.html#text__lists
file://xxxx/index.html#text__hr
file://xxxx/index.html#text__tables
file://xxxx/index.html#text__code
file://xxxx/index.html#text__inline

```

### 总结

如果你不熟悉[Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)，那么上面的代码是有点难以理解的。

```getAttribute``` 方法返回了[Thenable](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/promise_exports_Thenable.html)的实例，Thenable跟Promise很像，我们可以使用```then()```方法来传入回调，表示当异步过程成功结束的时候进行调用。




原始封面

![课程图片](https://images.unsplash.com/photo-1509515837298-2c67a3933321?w=300)

