---
weight: 4
title: Fiddler（四）设置代理 HTTPS 请求
date: '2017-12-19T13:50:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1459504346581-19d0b0a889dc?w=300
tags: []
categories:
- 抓包工具Fiddler使用教程
lightgallery: true
toc:
  auto: false
---




#### HTTPS 介绍
---
HTTPS（全称：Hyper Text Transfer Protocol over Secure Socket Layer），是以安全为目标的HTTP通道，简单讲是HTTP的安全版。

HTTPS在HTTP的基础上加入了SSL协议，SSL依靠证书来验证服务器的身份，并为浏览器和服务器之间的通信加密。

HTTPS和HTTP的区别主要为以下四点：

一、https协议需要到ca申请证书，一般免费证书很少，需要交费。

二、http是超文本传输协议，信息是明文传输，https 则是具有安全性的ssl加密传输协议。

三、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

四、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。


#### Fiddler设置HTTPS代理
---

1、打开Fiddler，菜单栏：__Tools –> Fiddler Options__ 打开fiddler配置。

![](http://img.testclass.net/fiddler_06_1.png)

2、打开 HTTPS 配置项，勾选“__Capture HTTPS CONNECTs__”和“__Decrypt HTTPS traffic__”，然后点击“OK”。

![](http://img.testclass.net/fiddler_06_2.png)

重启Fiddler，就可以实现HTTPS请求的代理了。




原始封面

![课程图片](https://images.unsplash.com/photo-1459504346581-19d0b0a889dc?w=300)

