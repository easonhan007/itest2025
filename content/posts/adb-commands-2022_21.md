---
weight: 1
title: "常用的adb命令"
date: 2024-03-08T09:02:04+08:00
lastmod: 2024-03-08T09:02:04+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "值得收藏"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1581093804475-577d72e38aa0?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

Android Debug Bridge 是我们比较常用的命令行工具，该工具可以在 Android 设备上执行不同的操作，例如安装或卸载应用程序、输入文本、捕获屏幕截图等，下面是一些常用的 adb 命令及使用场景。

### \***\*列出连接的设备\*\***

```bash
adb devices
```

上面的命令可以列出设备的序列号和状态，如果连接了许多设备并且我们想将它们区分开来，我们可以运行带有`-l`选项的命令以列出有关设备的更多详细信息。

```bash
adb devices -l
```

此命令向我们显示设备、型号等。

### \***\*安装应用程序\*\***

通过提供`.apk`文件的路径，可以在设备上安装应用程序

```bash
adb install <path_to_apk>.apk
```

如果连接了多个设备，直接运行上面的命令是会报错的，这时应使用`-s`选项指定目标设备的序列号。

```bash
adb -s <serial_number> install <path_to_apk>.apk
```

这里的`-s`是一个常用选项，用于指定具体的设备，会在 adb 命令中大量使用到。

### \***\*列出 package\*\***

`adb shell` 中的包管理器(package manager)工具可用于列出设备上安装的所有包

```bash
adb shell pm list packages
```

后面接`grep`命令可以实现更为精确的过滤

```bash
adb shell pm list package | grep what_you_want
```

### 启动\***\*Activity\*\***

可以用下面的命令来找到指定的 package 中的某个 activity

```bash
adb shell dumpsys package | grep <package_name> | grep Activity
```

然后下面的命令可以启动 activity

```bash
adb shell am start <package_name>/<activity_name>
```

比如下面的命令可以启动 google map

```bash
adb shell am start com.google.android.apps.maps/com.google.android.maps.MapsActivity
```

### \***\*在浏览器中打开 URL\*\***

这里要用到工具是活动管理器 am，activity manager

```bash
adb shell am start -a android.intent.action.VIEW -d "<some_url>"
```

比如下面的例子

```bash
adb shell am start -a android.intent.action.VIEW -d "https://developer.android.com/docs"
```

### 输入文字

在文本框中输入并 focus 文本

```bash
adb shell input text "<some_input>"
```

一些特殊字符`!`, `&`, `(`,是需要用反斜杠(`\`)转义的

```bash
adb shell input text "\!\&\(\)\<\>\*\|"
```

### 点击 Home 按钮

`KEYCODE_HOME`事件可以用来模拟点击 Home 按钮的效果

```bash
adb shell input keyevent KEYCODE_HOME
```

### 干掉应用

可以通过模拟按钮的方式来终止应用

```bash
adb shell input keyevent KEYCODE_APP_SWITCH
adb shell input keyevent KEYCODE_DPAD_DOWN
adb shell input keyevent DEL
```

### 清除应用数据

```bash
adb shell pm clear <package_name>
```

在这个例子里 Google Chrome 浏览器打开了 4 个 tab。当应用数据被清除并再次启动 Activity 时，显示`Terms of Service`页面（首次启动时显示的页面）并表明应用缓存和数据被清除。

### 屏幕截图

截图并拉回本地

```bash
adb shell screencap /sdcard/<screenshot_name>.png
adb pull /sdcard/<screenshot_name>.png
```

### 录屏

```bash
adb shell screenrecord /sdcard/<some_video_name>.mp4
```

注意: 命令执行之后，需要按下`ctrl+c`来停止录屏

最后把视频拉回到本地

```bash
adb pull /sdcard/<some_video_name>.mp4
```

### 查看应用程序日志

```bash
adb logcat
```

### 访问应用程序的 data 目录

这时候需要用到`adb shell`

```bash
adb shell
run-as <package_name>
```

### 卸载应用

```bash
adb uninstall <package_name>
```

[https://lavanyamohan.hashnode.dev/common-adb-commands-i-use-while-testing?utm_campaign=Software%2BTesting%2BWeekly&utm_medium=email&utm_source=Software_Testing_Weekly_114](https://lavanyamohan.hashnode.dev/common-adb-commands-i-use-while-testing?utm_campaign=Software%2BTesting%2BWeekly&utm_medium=email&utm_source=Software_Testing_Weekly_114)
