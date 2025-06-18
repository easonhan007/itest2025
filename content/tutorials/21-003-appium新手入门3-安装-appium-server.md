---
weight: 3
title: appium新手入门（3）—— 安装 appium Server
date: '2017-09-07T11:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



我们可以在Appium官方网站上下载操作系统相应的Appium版本。

https://bitbucket.org/appium/appium.app/downloads/

当前最新版本为 __AppiumForWindows_1_4_16_1.zip__ ，注意这是一个 Windows 版本，如果你的电脑为MAC请下载 __appium-1.5.3.dmg__ 。虽然你已经看到了这些下载包，但我不保证你能下载的下来。

所以，再来提供一个百度网盘的下载链接：https://pan.baidu.com/s/1pKMwdfX

我们以 Windows 为例，将下载的 AppiumForWindows.zip 进行解压，点击 __appium-installer.exe__ 进行安装。

![](http://img.testclass.net/appium_server_install.png)

根据提示，一步一步进行安装，这里不再啰嗦。最终在会桌面上生成 __Appium图标__ , 双击启动，appium server 界面如下。

![](http://img.testclass.net/appium_server_view.png)

Appium-Server已经可以打开了。至于Appium的使用我们放到后面的章节进行介绍。

最后，打开Windows命令提示符，输入“appium-doctor”命令，如果出现以下提示，说明你Appium所需要的各项环境都已准备完成。

![](http://img.testclass.net/appium_server_environment.png)

注：如果提示：__“appium-doctor”不是内部或外部命令__，找到Appium的安装目录，例如：

__C:\Program Files\Appium\node_modules\\.bin__

添加到环境变量path下面（参考Java环境的设置）。




原始封面

![课程图片](https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=300)

