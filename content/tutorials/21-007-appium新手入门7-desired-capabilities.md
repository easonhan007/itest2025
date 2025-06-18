---
weight: 7
title: appium新手入门（7）—— Desired Capabilities
date: '2017-09-07T10:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1429734956993-8a9b0555e122?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



<font color="blue">从后台统计来看，appium 系列的教程很受欢迎！于是，我继续更新，也希望你把这个教程推荐给更多学习 appium 的小伙伴！</font>

#### Desired Capabilities
---

Desired Capabilities 在启动 session 的时候是必须提供的。

Desired Capabilities 本质上是以 key value 字典的方式存放，客户端将这些键值对发给服务端，告诉服务端我们想要怎么测试。它告诉 appium Server这样一些事情：

* 本次测试是启动浏览器还是启动移动设备。

* 是启动Andorid还是启动iOS。

* 启动Android时，app的package是什么。

* 启动Android时，app的activity是什么。

* ...

#### Desired Capabilities 配置
---
Appium 的 Desired Capabilities 基本配置如下：

```Java

DesiredCapabilities capabilities = new DesiredCapabilities();
capabilities.setCapability("deviceName", "Android Emulator");
capabilities.setCapability("automationName", "Appium");
capabilities.setCapability("platformName", "Android");
capabilities.setCapability("platformVersion", "5.1");
capabilities.setCapability("appPackage", "com.android.calculator2");
capabilities.setCapability("appActivity", ".Calculator");

WebDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);

```
* deviceName：启动哪种设备，是真机还是模拟器？iPhone Simulator，iPad Simulator，iPhone Retina 4-inch，Android Emulator，Galaxy S4...

* automationName：使用哪种自动化引擎。appium（默认）还是Selendroid。

* platformName：使用哪种移动平台。iOS, Android, orFirefoxOS。

* platformVersion：指定平台的系统版本。例如指的Android平台，版本为5.1。

* appActivity：待测试的app的Activity名字。比如MainActivity、.Settings。注意，原生app的话要在activity前加个"."。

* appPackage：待测试的app的Java package。比如com.example.android.myApp, com.android.settings。


更多的参数配置 ，参考 [这里](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)




原始封面

![课程图片](https://images.unsplash.com/photo-1429734956993-8a9b0555e122?w=300)

