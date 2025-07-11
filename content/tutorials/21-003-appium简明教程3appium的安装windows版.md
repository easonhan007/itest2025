---
weight: 3
title: appium简明教程（3）——appium的安装windows版
date: '2017-08-18T07:14:54+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1525490829609-d166ddb58678?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



appium的哲学里有一条就是不重新发明轮子。同样，官方已经有明确的安装步骤了，因此在这里纯属搬砖。

[原文地址](https://github.com/appium/appium/blob/master/docs/cn/appium-setup/running-on-windows.md)

感谢testerhome的辛勤翻译。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途

### 限制

如果你在windows上安装appium，你没法使用预编译专用于OS X的.app文件，你也将不能测试IOS apps，因为appium依赖OS X专用的库来支持IOS测试。这意味着你只能通过在mac上来运行IOS的app测试。这点限制挺大。

### 开始安装

* 安装nodejs 通过官方的安装程序来安装。

* 安装android的sdk包，(http://developer.android.com/sdk/index.html), 运行依赖sdk中的'android'工具。并确保你安装了Level17或以上的版本api。设置ANDROID_HOME系统变量为你的Android SDK路径，并把tools platform-tools两个目录加入到系统的Path路径里。因为这里面包含有一些执行命令

* 安装java的JDK，并设置JAVA_HOME 变量为你的JDK目录。

* 安装Apache Ant 或者直接使用Android Windows SDK自带的ant，地址在eclipse\plugins目录，你需要把这个目录加到你的系统PATH变量中

* 安装[Apache Maven](http://maven.apache.org/download.cgi). 并且设置M2HOME和M2环境变量，把M2环境变量添加到你的系统PATH变量中。

* 安装[Git](https://git-scm.com/download/win). 确保你安装了windows下的Git，以便可以运行常用的command命令

现在，你已经下载安装了所有的依赖，开始运行 reset.bat

### 运行Appium

要在windows上运行测试用例，你需要先启动Android模拟器或者连接上一个API Level17以上的android真机。 然后在命令行运行appium node .

### 备注

* 你必须带上--no-reset和--full-reset标记，以用于windows上的android
* 有一个硬件加速模拟器用于android，但是它有自己的一些限制，如果你想了解更多，请参考页面
* 确保在你的AVD的config.ini中有一个配置项为hw.battery=yes

### 最简略的安装方式

出于对官方文档的尊重，我按照原文翻译，如下介绍我的安装心得。官方提到的一些工具，其实并不需要安装。 下面介绍我已经测试过的安装和使用过程

### 安装appium

1. 安装nodejs

2. 使用npm安装appium: ```npm install -g appium```

注意：在某些情况下，appium安装的时候并不会把appium的路径放进系统的PATH里，这时候需要手工去加一下。

### 运行appium

启动appium，直接运行appium 即可。

### 更新appium

通过```npm install -g appium``` 来更新appium即可



下一节，appium client的安装

 本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1525490829609-d166ddb58678?w=300)

