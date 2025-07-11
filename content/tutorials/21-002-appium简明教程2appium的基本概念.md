---
weight: 2
title: appium简明教程（2）——appium的基本概念
date: '2017-08-19T06:14:09+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1513112300738-bbb13af7028e?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



### Client/Server Architecture

appium的核心其实是一个暴露了一系列REST API的server。

这个server的功能其实很简单：监听一个端口，然后接收由client发送来的command。翻译这些command，把这些command转成移动设备可以理解的形式发送给移动设备，然后移动设备执行完这些command后把执行结果返回给appium server，appium server再把执行结果返回给client。

在这里client其实就是发起command的设备，一般来说就是我们代码执行的机器，执行appium测试代码的机器。狭义点理解，可以把client理解成是代码，这些代码可以是java/ruby/python/js的，只要它实现了webdriver标准协议就可以。

这样的设计思想带来了一些好处：

* 1，可以带来多语言的支持；
* 2，可以把server放在任意机器上，哪怕是云服务器都可以；（是的，appium和webdriver天生适合云测试）

### Session

session就是一个会话，在webdriver/appium，你的所有工作永远都是在session start后才可以进行的。一般来说，通过POST /session这个URL，然后传入**Desired Capabilities**就可以开启session了。

开启session后，会返回一个全局唯一的session id，以后几乎所有的请求都必须带上这个session id，因为这个seesion id代表了你所打开的浏览器或者是移动设备的模拟器。

进一步思考一下，由于session id是全局唯一，那么在同一台机器上启动多个session就变成了可能，这也就是selenium gird所依赖的具体理论根据。

### Desired Capabilities

Desired Capabilities携带了一些配置信息。从本质上讲，这个东东是key-value形式的对象。你可以理解成是java里的map，python里的字典，ruby里的hash以及js里的json对象。实际上Desired Capabilities在传输时就是json对象。

Desired Capabilities最重要的作用是告诉server本次测试的上下文。这次是要进行浏览器测试还是移动端测试？如果是移动端测试的话是测试android还是ios，如果测试android的话那么我们要测试哪个app？ server的这些疑问Desired Capabilities都必须给予解答，否则server不买账，自然就无法完成移动app或者是浏览器的启动。

具体例子如下：

> For example, we might set the platformName capability to iOS to tell Appium that we want an iOS session, rather than an Android one. Or we might set the safariAllowPopupscapability to true in order to ensure that, during a Safari automation session, we’re allowed to use JavaScript to open up new windows. See the capabilities doc for the complete list of capabilities available for Appium

### Appium Server

这就是每次我们在命令行用appium命令打开的东西。

### Appium Clients

由于原生的webdriver api是为web端设计的，因此在移动端用起来会有点不伦不类。appium官方提供了一套appium client，涵盖多种语言ruby/java/python，在我看来ruby client是实现最好的。在测试的时候，一般要使用这些client库去替换原生的webdriver库。这实际上不是替换，算是client对原生webdriver进行了一些移动端的扩展，加入了一些方便的方法，比如swipe之类，appium client让我们可以更方便的写出可读性更好的测试用例。

### Appium.app, Appium.exe

appium server的GUI版本，前者用在osx上，后者是windows上。可视化、不需要装node，可以看app的UI结构是这个东东的卖点。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1513112300738-bbb13af7028e?w=300)

