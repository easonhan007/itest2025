---
weight: 10
title: appium新手入门（10）—— appium API 之上下文操作
date: '2017-09-07T10:22:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1505312926838-645f295a20e1?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



其实上下文的操作主要针对于混合应用。啥是混合应用，简单来说就是APP用里面嵌入网页。Android上的浏览器就属于混合应用。

#### 1、获取当前上下文
---
方法：

* getContext()

获取当前所有的可用的上下文。该方法不需要入参。
```java
String ct = driver.getContext();
System.out.println(ct);

-----------计算器应用的打印结果-----------------------
NATIVE_APP
```

#### 2、当前所有上下文句柄
---
方法：

* getContextHandles()

获取当前所有可用的上下文。该方法不需要入参。


#### 3、切换上下文
---
* context()

切换到特定的上下文中。需要指定上下文的名称。
```java
driver.context('NATIVE_APP')
driver.context('WEBVIEW_1')
```




原始封面

![课程图片](https://images.unsplash.com/photo-1505312926838-645f295a20e1?w=300)

