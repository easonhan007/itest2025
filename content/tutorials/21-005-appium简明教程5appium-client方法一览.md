---
weight: 5
title: appium简明教程（5）——appium client方法一览
date: '2017-08-16T07:30:01+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1504387103978-e4ee71416c38?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



appium client扩展了原生的webdriver client方法

下面以java代码为例，简单过一下appium client提供的适合移动端使用的新方法

```
resetApp()
getAppString()
sendKeyEvent()
currentActivity()
pullFile()
pushFile()
pullFolder()
hideKeyboard()
runAppInBackground()
performTouchAction()
performMultiTouchAction()
tap()
swipe()
pinch()
zoom()
getNamedTextField()
isAppInstalled()
installApp()
removeApp()
launchApp()
closeApp()
endTestCoverage()
lockScreen()
shake()
complexFind()
scrollTo()
scrollToExact()
openNotifications()
Context Switching: .context(), .getContextHandles(), getContext())
```

新增的locator

```
findElementByAccessibilityId()
findElementsByAccessibilityId()
findElementByIosUIAutomation()
findElementsByIosUIAutomation()
findElementByAndroidUIAutomator()
findElementsByAndroidUIAutomator()
```

这些方法主要覆盖了3大类：

* driver扩展：比如增加了resetApp等操作app的方法
* action扩展：增加一些移动端的特有的action（怎么描述呢，相当于是移动端 特有的操作），比如swipe，shake(嗯，有了这个方法就可以让代码帮你摇一摇了)等；
* locator扩展：增加了一些移动端专属的定位策略

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1504387103978-e4ee71416c38?w=300)

