---
weight: 12
title: appium新手入门（12）—— appium API 之 TouchAction 操作
date: '2017-09-07T10:10:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507917570388-d661984ea008?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



Appium的辅助类，主要针对手势操作，比如滑动、长按、拖动等。

#### 1、按压控件
---
方法：

* press()

开始按压一个元素或坐标点（x,y）。通过手指按压手机屏幕的某个位置。

__press(WebElement el, int x, int y)__

press也可以接收屏幕的坐标（x,y）。

例：

```java
TouchAction(driver).press(x=0,y=308).release().perform()
```
除了press()方法之外，本例中还用到了别外两个新方法。

* release()
结束的行动取消屏幕上的指针。

* Perform()
执行的操作发送到服务器的命令操作。


#### 2、长按控件
---
方法：

* longPress()

开始按压一个元素或坐标点（x,y）。
相比press()方法，longPress()多了一个入参，既然长按，得有按的时间吧。duration以毫秒为单位。1000表示按一秒钟。其用法与press()方法相同。

__longPress(WebElement el, int x, int y, Duration duration)__

例：
```java
TouchAction action = new TouchAction(driver);
action.longPress(names.get(1),1000).perform().release();
action.longPress(1 ,302,1000).perform().release();
```

####  3、点击控件
---
方法：

* tap()

对一个元素或控件执行点击操作。用法参考press()。

__tap(WebElement el, int x, int y)__

例：
```java
TouchAction action = new TouchAction(driver);
action.tap(names.get(1)).perform().release();
action.tap(1 ,302).perform().release();
```

#### 4、移动
---
方法：

* moveTo()

将指针（光标）从过去指向指定的元素或点。

__movTo(WebElement el, int x, int y)__

其用法参考press()方法。

例：
```Java
TouchAction action = new TouchAction(driver);
action.moveTo(names.get(1)).perform().release();
action.moveTo(1 ,302).perform().release();
```

#### 5、暂停
---

方法：

* wait()

暂停脚本的执行，单位为毫秒。
```Java
action.wait(1000);
```




原始封面

![课程图片](https://images.unsplash.com/photo-1507917570388-d661984ea008?w=300)

