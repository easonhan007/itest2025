---
weight: 3
title: Fiddler（三）代理 HTTP 请求
date: '2017-12-19T13:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1581922820051-88380611f5b8?w=300
tags: []
categories:
- 抓包工具Fiddler使用教程
lightgallery: true
toc:
  auto: false
---



上一小节对Fiddler的界面了简单的认识。接下来介绍如何通过Fiddler拦截HTTP请求。

#### 代理 HTTP 请求
---

启动 Fiddler:

![](http://img.testclass.net/fiddler_05.png)

1、 __启动代理__  ：点击窗口左下角，显示 “__Capuring__” 侧说明当前处于代理状态。

2、通过浏览器访问相关网页或执行页面操作（如，登录、搜索）。

3、通过Fiddler查看代理的HTTP请求进行分析。

#### 清除请求
---
当Fiddler拦截的请求比较多时，不方便查看，我们可以清除已经代理的请求，重新代理。如上图，Fiddler提供了几种清理选项。

* Remove all ：  清空整个请求列表

* Images ： 清除图片请求

* COMMECTs ： 清除HTTP的CONNECT请求

* Non-200s ： 清除HTTP状态不是 200 的请求

* ……




原始封面

![课程图片](https://images.unsplash.com/photo-1581922820051-88380611f5b8?w=300)

