---
weight: 1
title: appium新手入门（1）—— appium介绍
date: '2017-09-08T12:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1505860125062-3ce932953cf5?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---




### appium介绍
----
[官方网站](http://appium.io/)

#### 1、特点
----
appium 是一个自动化测试开源工具，支持 iOS 平台和 Android 平台上的原生应用，web应用和混合应用。

* “移动原生应用”是指那些用iOS或者 Android SDK 写的应用（Application简称app）。

* “移动web应用”是指使用移动浏览器访问的应用（appium支持iOS上的Safari和Android上的 Chrome）。

* “混合应用”是指原生代码封装网页视图——原生代码和 web 内容交互。比如，像 Phonegap，可以帮助开发者使用网页技术开发应用，然后用原生代码封装，这些就是混合应用。

重要的是，appium是一个跨平台的工具：它允许测试人员在不同的平台（iOS，Android）使用同一套API来写自动化测试脚本，这样大大增加了iOS和Android测试套件间代码的复用性。

#### 2、appium与Selenium
----
appium类库封装了标准Selenium客户端类库，为用户提供所有常见的JSON格式selenium命令以及额外的移动设备控制相关的命令，如多点触控手势和屏幕朝向。

appium客户端类库实现了Mobile JSON Wire Protocol（一个标准协议的官方扩展草稿）和W3C WebDriver spec（一个传输不可预知的自动化协议，该协议定义了MultiAction 接口）的元素。

appium服务端定义了官方协议的扩展，为appium 用户提供了方便的接口来执行各种设备动作，例如在测试过程中安装/卸载App。这就是为什么我们需要appium特定的客户端，而不是通用的Selenium 客户端。当然，appium 客户端类库只是增加了一些功能，而实际上这些功能就是简单的扩展了Selenium 客户端，所以他们仍然可以用来运行通用的Selenium会话。

#### 3、支持多平台、多语言
----
appium是跨平台的，可以用在OSX，Windows以及Linux桌面系统上运行。

appium选择了Client/Server的设计模式。只要client能够发送http请求给server，那么的话client用什么语言来实现都是可以的，这就是appium及Selenium(WebDriver)如何做到支持多语言的原因；

appium扩展了WebDriver的协议，没有自己重新去实现一套。这样的好处是以前的WebDriver API能够直接被继承过来，以前的Selenium（WebDriver）各种语言的binding都可以拿来就用，省去了为每种语言开发一个client的工作量；

|  语言/框架  |    Github地址    |
|:-----------|:-----------|
|Ruby |	https://github.com/appium/ruby_lib |
|Python|	https://github.com/appium/python-client  |
|Java	|  https://github.com/appium/java-client  |
|JavaScript (Node.js)|	https://github.com/admc/wd  |
|Objective C|	https://github.com/appium/selenium-objective-c  |
|PHP	|https://github.com/appium/php-client  |
|C# (.NET)|	https://github.com/appium/appium-dotnet-driver  |
|RobotFramework|	https://github.com/jollychang/robotframework-appiumlibrary  |


#### 4、appium工作原理
----
在安装和介绍appium之前，非常有必要介绍一下appium是如何工作的。

![](http://img.testclass.net/appium_principle.png)

通过上面一张图简单展示了appium的工具原理。

首先，appium支持多语言，因为它针对流的几种语言分别开发的相应的appium库。好处就是我们可以选择自己熟悉的语言编写appium脚本。

其次，appium支持多平台，包括MAC和Windows。它针对这两大平台开发了appium-Server。

最后，appium又同时支持Android 和 iOS两个操作系统。

这就使得appium变得非常灵活。

当我在MAC平台上，通过Python（__python-client__ ）编写了一个appium自动化脚本并执行，请求会首先到 appium.dum （MAC下的appium-Server），appium-Server通过解析，驱动iOS设备来执行appium自动化脚本。

或者，我在Windows平台上，通过Java（ __java-client__ ）编写了一个appium自动化脚本并执行，请求会首先到 appiumForWindow.zip（Window下的appium-Server），appium-Server通过解析，驱动Android虚拟机或真机来执行appium脚本。

所以，你会看到appium的强大之处就在于此。

#### 5、你都需要安装什么？
-----

这才是你最关心的问题，使用appium都需要安装些什么？其实，从appium工作原理你就应该知道需要装什么了。

* __编程语言__

想用 Python 的同学，点[这里](/selenium_python/install-selenium/)

想用 Java 的同学，点[这里](/selenium_java/install-java/)

* __appium client__

参考 <font color=#DC143C>3、支持多平台、多语言</font> 的列表，根据你选择的语言来选择对应的 appium-client。

* __appium Server__

参考 <font color=#DC143C>4、appium工作原理</font> 的介绍，根据你的系统平台选择 对应的 appium-server。

* __测试运行环境__

你需要一个Android模拟器，或 一个 Android 手机，或 一台 iPhone 手机。




原始封面

![课程图片](https://images.unsplash.com/photo-1505860125062-3ce932953cf5?w=300)

