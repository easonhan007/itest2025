---
weight: 9
title: appium新手入门（9）—— appium API 之应用操作
date: '2017-09-07T10:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1495490311930-678c8ecdd120?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



本小节的所罗列的方法主要针对应用的操作，如应用的安装、卸载、关闭、启动等。

#### 1、安装应用
---
方法：

* installApp()

安装应用到设备中去。需要apk包的路径。

```java
driver.installApp("path/to/my.apk");
driver.installApp("D:\\android\\apk\\ContactManager.apk");
```
#### 2、卸载应用
方法：

* removeApp()

从设备中删除一个应用。
```java
driver.removeApp("com.example.android.apis");
```

#### 3、关闭应用
---
方法：

* closeApp()

关闭打开的应用，默认关闭当前打开的应用，所以不需要入参。这个方法并非真正的关闭应用，相当于按home键将应用置于后台，可以通过launchApp()再次启动。

#### 4、启动应用
---
方法：

* launchApp()

启动应用。你一定很迷惑，不是在初始化的配置信息已经指定了应用，脚本运行的时候就需要启动应用，为什么还要有这个方法去启动应用呢？重新启动应用也是一个测试点，该方法需要配合closeApp()使用的。
```java
driver.closeApp();
driver.launchApp();
```

#### 5、检查应用是否安装
---
方法：

* isAppInstalled()

检查应用是否已经安装。需要传参应用包的名字。返回结果为Ture或False。
```java
driver.isAppInstalled('com.example.android.apis');
```

#### 6、将应用置于后台
---
方法：

* runAppInBackground()

将当前活跃的应用程序发送到后台。这个方法需要入参，需要指定应用置于后台的时长。

```java
driver.runAppInBackground(2);
```

#### 7、应用重置
---
方法：

* resetApp()

重置当前被测程序到出始化状态。该方法不需要入参。
```java
driver.resetApp();
```




原始封面

![课程图片](https://images.unsplash.com/photo-1495490311930-678c8ecdd120?w=300)

