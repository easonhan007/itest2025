---
weight: 1
title: appium简明教程（1）——appium和它的哲学世界
date: '2017-08-20T06:05:07+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1496450681664-3df85efbd29f?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



### 什么是appium？

下面这段介绍来自于appium的官网。

> Appium is an open-source tool you can use to automate mobile native, mobile web, and mobile hybrid applications on iOS and Android platforms. “Mobile native apps” are those written using the iOS or Android SDKs. “Mobile web apps” are web apps accessed using a mobile browser (Appium supports Safari on iOS and Chrome on Android). “Mobile hybrid apps” have a native wrapper around a “webview” – a native control that enables interaction with web content. Projects like Phonegap, for example, make it easy to build apps using web technologies that are then bundled into a native wrapper – these are hybrid apps.

> Importantly, Appium is “cross-platform”: it allows you to write tests against multiple platforms (iOS, Android), using the same API. This enables a large or total amount of code reuse between iOS and Android testsuites.



我们可以从上面的介绍里获得这样的一些信息：

* 1，appium是开源的移动端自动化测试框架；
* 2，appium可以测试原生的、混合的、以及移动端的web项目；
* 3，appium可以测试ios，android应用（当然了，还有firefox os）；
* 4，appium是跨平台的，可以用在osx，windows以及linux桌面系统上；


### appium的哲学

> Appium was designed to meet mobile automation needs according to a certain philosophy. The key points of this philosophy can be stated as 4 requirements:

> You shouldn’t have to recompile your app or modify it in any way in order to automate it.
You shouldn’t be locked into a specific language or framework to write and run your tests.
A mobile automation framework shouldn’t reinvent the wheel when it comes to automation APIs.
A mobile automation framework should be open source, in spirit and practice as well as in name!


appium的设计哲学是这样的：

* 1，不需要为了自动化而且重新编译或修改测试app；
* 2，不应该让移动端自动化测试限定在某种语言和某个具体的框架；也就是说任何人都可以使用自己最熟悉最顺手的语言以及框架来做移动端自动化测试；
* 3，不要为了移动端的自动化测试而重新发明轮子，重新写一套惊天动地的api；也就是说webdriver协议里的api已经够好了，拿来改进一下就可以了；
* 4，移动端自动化测试应该是开源的；

### appium的技术架构

* iOS: Apple’s UIAutomation
* Android 4.2+: Google’s UiAutomator
* Android 2.3+: Google’s Instrumentation. (Instrumentation support is provided by bundling a separate project, Selendroid)

### appium的设计思想

> We meet requirement #2 by wrapping the vendor-provided frameworks in one API, theWebDriver API. WebDriver (aka “Selenium WebDriver”) specifies a client-server protocol (known as the JSON Wire Protocol). Given this client-server architecture, a client written in any language can be used to send the appropriate HTTP requests to the server. There are already clients written in every popular programming language. This also means that you’re free to use whatever test runner and test framework you want; the client libraries are simply HTTP clients and can be mixed into your code any way you please. In other words, Appium & WebDriver clients are not technically “test frameworks” – they are “automation libraries”. You can manage your test environment any way you like!

> We meet requirement #3 in the same way: WebDriver has become the de facto standard for automating web browsers, and is a W3C Working Draft. Why do something totally different for mobile? Instead we have extended the protocol with extra API methods useful for mobile automation.

> It should be obvious that requirement #4 is a given – you’re reading this because Appium is open source.



首先，为了能够实现哲学里描述的第2条，也就是不应该让移动端自动化测试限定在某种语言和某个具体的框架；也就是说任何人都可以使用自己最熟悉最顺手的语言以及框架来做移动端自动化测试；appium选择了client-server的设计模式。只要client能够发送http请求给server，那么的话client用什么语言来实现都是可以的，这就是appium及webdriver如何做到支持多语言的；

其次，为了能够实现不要为了移动端的自动化测试而重新发明轮子，重新写一套惊天动地的api；也就是说webdriver协议里的api已经够好了，拿来改进一下就可以了；这个思想，appium扩展了webdriver的协议，没有自己重新去实现一套。这样的好处是以前的webdriver api能够直接被继承过来，以前的webdriver各种语言的binding都可以拿来就用，省去了为每种语言开发一个client的工作量；

最后appium当然是开源的，这也实现了哲学思想里的最后一点。

下一节讲介绍appium的一些基本概念。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1496450681664-3df85efbd29f?w=300)

