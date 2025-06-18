---
weight: 6
title: appium新手入门（6）—— appium-desktop
date: '2017-09-07T10:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1533972441521-98c9365b64f3?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



#### 什么是 Appium-desktop？
-----

项目地址：https://github.com/appium/appium-desktop


项目描述：

>Appium Server and Inspector in Desktop GUIs for Mac, Windows, and Linux。

Appium 移动测试中有个很重新的组件 [Appium-Server](/appium/appium-base-server/)，它主要用来监听我们的移动设备（真机或模拟器），然将不同编程语言编写的 appium 测试脚本进行解析，然后，驱动移动设备来运行测试。

但Appium-Server有一两年没有更新了。Windows版在 2015 年底止步于的 __AppiumForWindows_1_4_16_1.zip__

于是，新的工具 Appium-desktop 来了！ 它来继续 Appium-Server的使命，当然， Appium-Server当前仍然是可用的。

#### 下载与安装
----

appium-desktop 下载地址：[这里](https://github.com/appium/appium-desktop/releases)

根据自己的平台选择相关的包进行下载。本文以 Windows 为例，所以选择 __appium-desktop-Setup-1.2.4.exe__ 文件进行下载。

安装过程太简单了，双击 exe 文件，然后，等待安装完就好了，中间都不需要你设置任何选项。所以，这里就不贴图了。


#### 启动运行
----
安装完成桌面会生成一个紫色的 appium 图标，双击打开。

![](http://img.testclass.net/appium_desktop_01.png)

默认显示监控的 host 和 port ，这和 Appium-Server中是一致的。点击 __“Start Server V 1.7.1”__ 按钮启动服务。

![](http://img.testclass.net/appium_desktop_02.png)

现在启动 启动你的移动设备（真机或模拟器），编写 Appium 自动化测试脚本，可以通过 Appium-desktop 来运行测试了。

至于 Appium-Server , 你可以把它卸载了！




原始封面

![课程图片](https://images.unsplash.com/photo-1533972441521-98c9365b64f3?w=300)

