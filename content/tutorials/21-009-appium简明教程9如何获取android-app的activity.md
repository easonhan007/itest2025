---
weight: 9
title: appium简明教程（9）——如何获取android app的Activity
date: '2017-08-12T08:11:31+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1566352207769-3a591a2c9567?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---


有时候在appium的Desired Capabilities中需要指定被测app的appActivity，下面的方法可能会对你有所帮助。

**方法一**

如有你有待测项目的源码，那么直接查看源码就好。如果没有，那么请联系有源码的同学，这是推荐方法。

**方法二**

如果你没有代码，那么可以反编译该app。

这里将用到2个工具，分别是dex2jar和jd-gui。你可以在这里下载目前为止的最新版本以及示例apk。

我们以工具包里的ContactManager.apk为例，简单介绍一下反编译的流程。

* 1，重命名ContactManager.apk为ContactManager.zip并解压得到文件classes.dex；
* 2，解压dex2jar-0.0.9.15.zip，并从命令行进入该文件夹；
* 3，运行命令

```
d2j-dex2jar.bat path_to\classes.dex
在当前文件夹下得到classes-dex2jar.jar；
```

* 4，解压jd-gui-0.3.6.windows.zip得到文件jd-gui.exe；
* 5，使用jd-gui.exe打开classes-dex2jar.jar；


嗯，好了，可以尽情欣赏了。上图。

![](http://oriphg3yh.bkt.clouddn.com/get_activity.png)

上图所示的ContactManager就是待测app的main activity。

**方法三**

参考testerhome的[这个帖子](http://testerhome.com/topics/1030)

使用log查看大法(嗯，windows上没grep不幸福，好在有powershell的Select-String，可以拿来勉强一用)，直接搬砖。

* a、启动待测apk
* b、开启日志输出：adb logcat>D:/log.txt
* c、关闭日志输出：ctrl+c
* d、查看日志

找寻：

```
Displayed com.mm.android.hsy/.ui.LoginActivity: +3s859ms
appPackage = com.mm.android.hsy
appActivity = .ui.LoginActivity
```

好了，准备活动做的差不多了。下一节乙醇带大家进行控件定位之旅。




原始封面

![课程图片](https://images.unsplash.com/photo-1566352207769-3a591a2c9567?w=300)

