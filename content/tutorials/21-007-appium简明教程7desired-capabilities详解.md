---
weight: 7
title: appium简明教程（7）——Desired Capabilities详解
date: '2017-08-14T08:01:35+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1447433553548-2fc162393482?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



Desired Capabilities在启动session的时候是必须提供的。

Desired Capabilities本质上是key value的对象，它告诉appium server这样一些事情：

* 本次测试是启动浏览器还是启动移动设备？
* 是启动andorid还是启动ios？
* 启动android时，app的package是什么？
* 启动android时，app的activity是什么？

**Appium的Desired Capabilities是扩展了webdriver的Desired Capabilities的，下面的一些通用配置是需要指定的：**

* automationName：使用哪种自动化引擎。appium（默认）还是Selendroid？
* platformName：使用哪种移动平台。iOS, Android, orFirefoxOS？
* deviceName：启动哪种设备，是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator, Galaxy S4, etc...
* app：应用的绝对路径，注意一定是绝对路径。如果指定了appPackage和appActivity的话，这个属性是可以不设置的。另外这个属性和browserName属性是冲突的。
* browserName：移动浏览器的名称。比如Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android；与app属性互斥。
* udid：物理机的id。比如1ae203187fc012g。

**下面这些属性是android平台特定的：**

* appActivity：待测试的app的Activity名字。比如MainActivity, .Settings。注意，原生app的话要在activity前加个"."。
* appPackage：待测试的app的java package。比如com.example.android.myApp, com.android.settings。

本文主要讨论android平台的appium测试方法和技巧，因此在这里就不列出ios设备特定的属性了。

更多信息请参考[官方文档](https://github.com/appium/appium/blob/master/docs/en/caps.md)

在这里我们发现，我们经常要获取app的package和activity名字，那么有什么工具可以让我们方便的获取到这些信息呢？下一节讲回答这个问题。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1447433553548-2fc162393482?w=300)

