---
weight: 52
title: （二）JMeter插件管理
date: '2017-07-29T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1482406611936-43ea538e39d4?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
#### Jmeter插件管理
----
JMeter 插件管理器的使用方法很简单：不要手动安装各种插件，它提供了友好的用户界面来完成：安装、升级、卸载。

它管理插件包括 [jmeter-plugins.org](https://www.jmeter-plugins.org/) 上面常用的插件，和各种第三方插件甚至核心JMeter插件。

<br>
#### 安装插件管理：
----
1、下载 [plugins-manager.jar](http://www.jmeter-plugins.org/get/)

2、将 __plugins-manager.jar__ 放到 __...\apache-jmeter-3.2\lib\ext\__ 目录下。

3、双击 __ApacheJMeter.jar__ 启动Jmeter。

4、菜单栏“选项”会多出一个“Plugins Manager”的选项。
![](http://img.testclass.net/plugins_manager_01.png)

点击 “Plugins Manager” 选项打开 Jmeter 插件管理
![](http://img.testclass.net/plugins_manager_02.png)

插件管理窗口分三个标签页：

* ```Installed Plugins```：显示已安装的插件。

* ```Available Plugins```: 显示可安装的插件。

* ```Upgrades```: 显示可以升级的插件。

通过__勾选/取消勾选__插件，并点击右下角 "Apply Changes and Restart JMeter" 按钮来__卸载、安装、升级__插件。




原始封面

![课程图片](https://images.unsplash.com/photo-1482406611936-43ea538e39d4?w=300)

