---
weight: 7
title: （七）soapUI设置Auth
date: '2017-09-20T20:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1524219726159-3cbf91ce4b70?w=300
tags: []
categories:
- SoupUI实用教程
lightgallery: true
toc:
  auto: false
---



<br>
#### 设置用户认证（Auth）
----
当我们请求一个接口时，一般需要认证，认证是判断用户是否有请求权限的常用手段。

参考前面学习的添加 SOAP 和 REST 请求。

点击 __“Request 1”__ 窗口左下角 __“Auth”__ 按钮，Authoriaztion 选项中选择 __“add New Authoriaztion”__ ，在弹出的窗口中 Type 选择 __“Basic”__ 选项，点击 __“OK”__ 按钮，如下图。

![](http://img.testclass.net/sopaui_add_auth.png)

添加认证用户,如下图。

![](http://img.testclass.net/sopaui_setting_auth.png)

填写用户认证 Username 和 Password ，勾选 __“Authenticate pre-emptvely”__ 选项。

Username：用于填写基本认证的用户名。

Password：用于填写基本认证的密码。

Domain：域名是基本认证的可选项，设置为空。

Pre-emptive auth：设置定义认证的行为。

 *  Use global preference ：用于定义HTTP设置为全局首选项。
 *  Authenticate pre-emptively：仅适用于此请求，不需要等待身份验证质询时发送凭据。




原始封面

![课程图片](https://images.unsplash.com/photo-1524219726159-3cbf91ce4b70?w=300)

