---
weight: 5
title: Fiddler（五）设置显式IP地址
date: '2017-12-19T13:45:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1497601089782-06319e8be3a0?w=300
tags: []
categories:
- 抓包工具Fiddler使用教程
lightgallery: true
toc:
  auto: false
---



在测试过程中，我们经常需要通过host在不同的环境之间切换，如果知道自己的环境是否切换成功，那么通过IP地址就很容易判断。

#### Fiddler设置显示IP地址
---
打开Fiddler, 菜单栏：__Rules->Customize Rules…__ 或快捷键 __Ctrl+R__ 。

![](http://img.testclass.net/fiddler_07_1.png)

通过快捷键 __Ctrl+F__  ,搜索：__static function Main()__ 函数。 在函数中添加一行代码，如下：

```JavaScript
   // The Main() function runs everytime your FiddlerScript compiles
    static function Main() {
        var today: Date = new Date();
        FiddlerObject.StatusText = " CustomRules.js was loaded at: " + today;
        // 显示IP 地址
        FiddlerObject.UI.lvSessions.AddBoundColumn("ServerIP", 120, "X-HostIP");

        // Uncomment to add a "Server" column containing the response "Server" header, if present
        // UI.lvSessions.AddBoundColumn("Server", 50, "@response.server");

        // Uncomment to add a global hotkey (Win+G) that invokes the ExecAction method below...
        // UI.RegisterCustomHotkey(HotkeyModifiers.Windows, Keys.G, "screenshot");
    }

```

然后，点击菜单栏：__File --> Save__ 或快捷键 __Ctrl+S__，关闭窗口。

再次查看Fiddler请求，将多出 “__ServerIP__” 一列显示IP请求的IP地址。

![](http://img.testclass.net/fiddler_07_2.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1497601089782-06319e8be3a0?w=300)

