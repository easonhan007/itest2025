---
weight: 5
title: JMeter官方文档：5. 构建一个高级web测试计划
date: '2017-08-24T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1672206790227-99ae2b0bf4f3?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---


[《JMeter官方文档--翻译计划》](/2017/08/24/jmeter-translation-plans/) [原文地址](http://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)

## 5. 构建一个高级web测试计划
----
在本章，你将学习如何创建高级[测试计划](http://jmeter.apache.org/usermanual/build-test-plan.html)，来测试一个web网站。

有关基础测试计划的示例，请参考[构建Web测试计划](http://jmeter.apache.org/usermanual/build-web-test-plan.html)


### 5.1 使用URL重写用户session
----
如果你的 Web 应用程序，是使用URL重写而不是使用cookie保存session信息，那么你将需要做一点额外的设置来测试你的网站。

为了争取响应URL重写，JMeter 需要解析从服务器接受的 HTML，并检索唯一的 sessionID。

使用恰当的 [HTTP URL 重写修改器](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_URL_Re-writing_Modifier)来完成这项工作。只需要将sessionID参数名输入到修改器，jmeter会找到它并将它添加到每个请求中。如果请求已经有这个参数值，则会替换它。如果勾选Cache Session id?复选框，那么最后找到的sessionID将被保存，如果先前的http示例不包含sessionID，则会使用它。


#### URL重写修改器示例
----
下载这个示例。__图1__ 显示一个使用URL重写的测试计划。注意，URL重写修改器被添加到事务控制器中，因此它只会影响该事务控制器下的请求。

![](http://img.testclass.net/05_http_URL_Re_writ.png)

图1  测试树

在 __图2__ 中，我们看到URL重写修改器的GUI界面，它有一个字段是供用户修改指定sessionID的。还有一个复选框，用于标记sessionID是地址的一部分（由“；”分隔），而不是作为请求参数。

![](http://img.testclass.net/05_http_URL_Re_writ2.png)

图2 请求参数


### 5.2 使用头文件管理器
----
Jmeter的 [HTTP头文件管理器](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager)，允许您自定义HTTP请求头文件，这个头文件包括“User-Agent"，"Pragma", "Referer"等属性。

HTTP 头文件管理器，和 [HTTP cookie 管理器](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager)类似，应该在线程组级别添加，除非出于特殊原因，您希望在测试中给某几个 [HTTP 请求](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request) 设置不一样的头文件。




原始封面

![课程图片](https://images.unsplash.com/photo-1672206790227-99ae2b0bf4f3?w=300)

