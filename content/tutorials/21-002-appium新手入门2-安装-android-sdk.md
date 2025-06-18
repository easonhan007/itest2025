---
weight: 2
title: appium新手入门（2）—— 安装 Android SDK
date: '2017-09-07T12:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1419833173245-f59e1b93f9ee?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



<font color=#DC143C>__注明：__ 理论上这一章不是必须的，如果你不想使用 Android 模拟器运行测试的话可以跳过，不过，建议安装；原生 Android 好折腾！关键是它自带的一些工具是你做 appium 测试必须要用的！</font>

### 安装Android SDK
----
Android SDK（Software Development Kit，软件开发工具包）提供了 Android API 库和开发工具构建，测试和调试应用程序。简单来讲，Android SDK 可以看做用于开发和运行 Android 应用的一个软件。

#### 1、下载Android SDK
----
我在官网上没有找到单独 Android SDK 的下载链接，官方推荐下载包含 Android SDK 的 Android Studio。

Android Studio & Android SDK 下载地址：https://developer.android.com/studio/index.html?hl=zh-cn

拖到页面底部，你将找到下载链接，根据自己的平台选择对应的链接下载。

一方面是包含 Android SDK 的 Android Studio 的安装包很大。另一方面它们二者也不是强关联的。因为 Appium也会用到 Android SDK，而 Android Studio 也可以调用真机来运行 Android程序。

所以，Android SDK 下载地址（才是我们想要的）：

http://tools.android-studio.org/index.php/sdk

你可以通过别的网站进行下载，身为IT从业人员，如何利用搜索工具和科学上网工具是你的必备技能。

将下载的 Android SDK 解压，将得到如下目录。

![](http://img.testclass.net/appium_sdk_path.png)

图 Android SDK目录


#### 2、设置Android环境变量
----
下面设置 Android 环境变量，方法与Java环境变量类似。我本机的目录结果为：

__D:\android\android-sdk-windows__

下面设置环境变量：

“我的电脑” 右键菜单 ---> 属性 ---> 高级 ---> 环境变量 ---> 系统变量 ---> 新建...

|  变量名  |   变量值    |
|:-----------|:-----------|
|ANDROID_HOME |	D:\android\Android\sdk |

找到 __path__ 变量名—> “编辑” 添加：

|  变量名  |   变量值    |
|:-----------|:-----------|
|PATH |	;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools; |


#### 3、安装Android 版本
----
双击 __SDK Manage.exe__ 启动SDK管理器。

![](http://img.testclass.net/appium_sdk_manage.png)

你需要科学上网，或者查找到国内的 Android 镜像，安装一个版本的Android虚拟机。你可以根据自己的喜好选择安装 Android 5.0 /5.1 /6.0 /7.0 版本。

这里推荐一个网站：http://www.androiddevtools.cn/



#### 3、安装Android 版本
----

双击 __AVD Manage.exe__ 启动AVD管理器。

![](http://img.testclass.net/appium_avd_manage.png)

点击 __“Create...”__ 按钮，创建Android虚拟机。

![](http://img.testclass.net/appium_create_new_avd.png)

不要选择超过电脑屏幕分辨率的Device，其它选项参考上图。点击 __“OK”__ 创建完成。在 AVD Manage 工具中选中创建的Android虚拟机，点击 __“Start...”__ 按钮启动。

![](http://img.testclass.net/appium_android_system.png)

Android模拟器已经启动。




原始封面

![课程图片](https://images.unsplash.com/photo-1419833173245-f59e1b93f9ee?w=300)

