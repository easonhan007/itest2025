---
weight: 0
title: 一起读测试论文(2)--基于selenium+testNG的测试框架
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1445768593937-05a3f7832b68?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



今天给大家带来的论文发表于2015年，全文的主旨是在描述如何使用selenium + testNG来实现一个稳定高效的web自动化测试框架。

文章开篇还是祖传的测试论文三件套

* 为什么要做测试
* 什么是web自动化测试
* 用什么工具做web自动化测试

这里就不展开了。

后面直接上了一张模块图，并对每个模块进行了详细的说明。

### Object Repository

对象库。好吧，你说你没有对象...

selenium支持多种定位业务元素的方式，不过如果页面频繁变化的话，用selenium原生的地方方式就会带来一个维护成本偏高的问题。

于是有人就提出了对象库的概念，把所有的元素定位都集中在一个地方管理，我最早是在08年左右在一个叫做QPT的自动化测试工具中了解到这个概念的，如今12年过去了，这种方式依然行之有效。

### Input file

在web系统中，用户经常需要输入一些信息，比如登录时候的用户名和密码。这些输入就可以放在input file里维护，这样每次输入相同内容的时候就可以直接从文件里读取了。不过要注意的是，这里仅维护一些必填项，一些可选项我们可以用随机值的方式去代替。

### Utility Section

工具库，可以分成下面几种。

* User Actions File：selenium提供了一些基本的元素操作方式，比如点击，但是另外一些操作，比如选择select box等的复杂操作其实并没有提供(原文大概是这个意思，不过selenium后面的版本确实提供了多种多样的操作行为工具，比如action chains以及select的操作等，可能当年文章写作时selenium是缺乏该能力的)，可以将这些操作封装起来，后面调用的时候就可以多次复用了。

* Utility file： 这个文件封装了一些常用功能，比如登录登出。

* Screenshot Generation：实现了用例错误时自动截图的功能。

具体截图过程如下

* 创建文件夹
* 从testNG拿执行结果
* 判断执行结果
* 如果执行失败则自动截图
* 截图用执行时间来命名
* 保存截图

### Test suite

testNG提供。

### Customization of test report

自定义测试报告。基本上就是用的testNG提供的html report。

### Email customized report to respective person

发邮件通知相关人员。使用 Mail.jar来实现。


### 结果对比

文中最后给出了该框架prowork Framework对比传统方式的优势，基本上是全面碾压。

### 总结

可以看出框架整体的结构是非常简单的，核心思想就是尽量复用TestNG的功能，然后封装一些工具函数，增加框架的可维护性。

如果大家遇到一些技术瓶颈或是想了解最新的一些测试思潮，偶然读一些论文还是很有帮助的。




原始封面

![课程图片](https://images.unsplash.com/photo-1445768593937-05a3f7832b68?w=300)

