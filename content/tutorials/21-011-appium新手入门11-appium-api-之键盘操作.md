---
weight: 11
title: appium新手入门（11）—— appium API 之键盘操作
date: '2017-09-07T10:20:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
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



模拟键盘输入也是非常重要的操作。这一小节来介绍那些关于键盘的操作。

#### 1、sendKeys()方法
---
方法：

* sendKeys()

用法：

```java
driver.findElements(By.name("Name")).sendKeys("jack");
```

### 2、pressKeyCode()方法
---
除此之外，appium扩展提供了pressKeyCode()方法。该方法Android特有。

方法：

* pressKeyCode()

发送一个键码的操作。需要一个入参。

```Java
driver.pressKeyCode(29); // 字母“a”
```

如果想点击Android的HOME键应该怎么实现的呢？如下
```java
driver.pressKeyCode(AndroidKeyCode.HOME);
```

<font color="blue">__下面提供Android keycode参考表：__</font>

__电话键__

KEYCODE_CALL 拨号键 5

KEYCODE_ENDCALL 挂机键 6

KEYCODE_HOME 按键Home 3

KEYCODE_MENU 菜单键 82

KEYCODE_BACK 返回键 4

KEYCODE_SEARCH 搜索键 84

KEYCODE_CAMERA 拍照键 27

KEYCODE_FOCUS 拍照对焦键 80

KEYCODE_POWER 电源键 26

KEYCODE_NOTIFICATION 通知键 83

KEYCODE_MUTE 话筒静音键 91

KEYCODE_VOLUME_MUTE 扬声器静音键 164

KEYCODE_VOLUME_UP 音量增加键 24

KEYCODE_VOLUME_DOWN 音量减小键 25

__控制键__

KEYCODE_ENTER 回车键 66

KEYCODE_ESCAPE ESC键 111

KEYCODE_DPAD_CENTER 导航键 确定键 23

KEYCODE_DPAD_UP 导航键 向上 19

KEYCODE_DPAD_DOWN 导航键 向下 20

KEYCODE_DPAD_LEFT 导航键 向左 21

KEYCODE_DPAD_RIGHT 导航键 向右 22

KEYCODE_MOVE_HOME 光标移动到开始键 122

KEYCODE_MOVE_END 光标移动到末尾键 123

KEYCODE_PAGE_UP 向上翻页键 92

KEYCODE_PAGE_DOWN 向下翻页键 93

KEYCODE_DEL 退格键 67

KEYCODE_FORWARD_DEL 删除键 112

KEYCODE_INSERT 插入键 124

KEYCODE_TAB Tab键 61

KEYCODE_NUM_LOCK 小键盘锁 143

KEYCODE_CAPS_LOCK 大写锁定键 115

KEYCODE_BREAK Break/Pause键 121

KEYCODE_SCROLL_LOCK 滚动锁定键 116

KEYCODE_ZOOM_IN 放大键 168

KEYCODE_ZOOM_OUT 缩小键 169

__组合键__

KEYCODE_ALT_LEFT Alt+Left

KEYCODE_ALT_RIGHT Alt+Right

KEYCODE_CTRL_LEFT Control+Left

KEYCODE_CTRL_RIGHT Control+Right

KEYCODE_SHIFT_LEFT Shift+Left

KEYCODE_SHIFT_RIGHT Shift+Right

__基本__

KEYCODE_0 按键'0' 7

KEYCODE_1 按键'1' 8

KEYCODE_2 按键'2' 9

KEYCODE_3 按键'3' 10

KEYCODE_4 按键'4' 11

KEYCODE_5 按键'5' 12

KEYCODE_6 按键'6' 13

KEYCODE_7 按键'7' 14

KEYCODE_8 按键'8' 15

KEYCODE_9 按键'9' 16

KEYCODE_A 按键'A' 29

KEYCODE_B 按键'B' 30

KEYCODE_C 按键'C' 31

KEYCODE_D 按键'D' 32

KEYCODE_E 按键'E' 33

KEYCODE_F 按键'F' 34

KEYCODE_G 按键'G' 35

KEYCODE_H 按键'H' 36

KEYCODE_I 按键'I' 37

KEYCODE_J 按键'J' 38

KEYCODE_K 按键'K' 39

KEYCODE_L 按键'L' 40

KEYCODE_M 按键'M' 41

KEYCODE_N 按键'N' 42

KEYCODE_O 按键'O' 43

KEYCODE_P 按键'P' 44

KEYCODE_Q 按键'Q' 45

KEYCODE_R 按键'R' 46

KEYCODE_S 按键'S' 47

KEYCODE_T 按键'T' 48

KEYCODE_U 按键'U' 49

KEYCODE_V 按键'V' 50

KEYCODE_W 按键'W' 51

KEYCODE_X 按键'X' 52

KEYCODE_Y 按键'Y' 53

KEYCODE_Z 按键'Z' 54




原始封面

![课程图片](https://images.unsplash.com/photo-1525490829609-d166ddb58678?w=300)

