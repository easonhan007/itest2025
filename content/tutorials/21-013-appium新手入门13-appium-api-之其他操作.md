---
weight: 13
title: appium新手入门（13）—— appium API 之其他操作
date: '2017-09-07T10:01:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1500877015165-e1fb7f2db007?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



其它操作针对移动设备上特有的一些操作。

#### 1、熄屏
---
方法：
* lockDevice()

点击电源键熄灭屏幕。

在iOS设备可以设置熄屏一段时间。Android上面不带参数，所以熄屏之后就不会再点亮屏幕了。
```java
driver.lockDevice(1000);  // iOS
driver.lockDriice();   //Android  
```

#### 2、当前Activity（Android only）
---
方法：

* currentActivity()

得到当前应用的activity。只适用于Android。
例（通讯录）：
```Java
String ca = driver.currentActivity();
System.out.print(ca);
-------------输出结果为-------------
.activities.PeopleActivity
```

### 3、收起键盘
---
方法：

* hideKeyboard()

收起键盘，这个方法很有用，当我们对一个输入框输入完成后，需要将键盘收起，再切换到一下输入框进行输入。
```Java
driver.hideKeyboard();  //收起键盘
```

#### 4、滑动
---
方法：

* swipe()

模拟用户滑动。将控件或元素从一个位置（x,y）拖动到另一个位置（x,y）。

__swipe(int startx, int starty, int endx, int endy, int duration)__
* start_x：开始滑动的x坐标。
* start_y：开始滑动的y坐标。
* end_x：结束滑动的x坐标。
* end_y：结束滑动的y坐标。
* duration：持续时间。

例：
```Java
driver.swipe(75, 500, 75, 0, 800);
```

#### 5、拉出文件
---
方法：

* pullFile()

从设备中拉出文件。

例：
```Java
driver.pullFile('Library/AddressBook/AddressBook.sqlitedb')
```

#### 6、推送文件
---
方法：

* pushFile()

推送文件到设备中去。

__pushFile(String remotePath, byte[] base64Data)__

例：
```Java
String content = "some data for the file";
byte[] data = Base64.encodeBase64(content.getBytes());
driver.pushFile("sdcard/test.txt", data);
```




原始封面

![课程图片](https://images.unsplash.com/photo-1500877015165-e1fb7f2db007?w=300)

