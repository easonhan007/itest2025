---
weight: 8
title: （八）soapUI创建性能测试
date: '2017-09-20T20:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1546471180-335a013cb87b?w=300
tags: []
categories:
- SoupUI实用教程
lightgallery: true
toc:
  auto: false
---



<br>

这一节我们来介绍性能测试，以前面添加的 SOAP 项目为例。

[（五）soapUI创建SOAP项目](/soapui/create-soap-project/)

#### 创建测试用例
----

右键点击 __“requests 1”__ 请求，选择 __“Add to TestCase”__ ...，如下图。

![](http://img.testclass.net/soapui_add_to_TestCase.png)

第一步，默认设置测试套件名为：TestSuite 1。

第二步，默认设置测试用例名为：TestCase 1。

第三步，添加 Requests 到 测试用例，如下图。

![](http://img.testclass.net/soapui_add_requests_to_TestCase.png)

点击 __“OK”__ 完整测试用例的创建，如下图。

![](http://img.testclass.net/soapui_add_LoadTest.png)

<br>
#### 创建性能测试用例 & 运行
----

接下来，创建性能测试用例，右键点击 __“Load Tests (1)” --> “New LoadTest”__ , 创建完成，参考上图，多出来一个 __“LoadTest 1”__ 的选项。

最后，运行性能测试。在 __“LoadTest 1”__ 窗口，点解右上角的绿色按钮，运行性能测试。

![](http://img.testclass.net/soapui_run_LoadTest.png)

__Limit__：表示要持续执行时间，秒为单位，默认是60。

__Threads__：负载测试所用的线程数，性能测试中所说的并发数。默认是5。

__TestDelay__：设置测试时线程的休眠时间，即在完成一次完整的测试用例后，开始下一次执行时，线程的休眠时间，以毫秒为单位，（1000毫秒等于1秒），默认是1000毫秒。

__Random__：该值得设置，于testDelay的设置结合在一起，它表示休眠的时间会在TestDelay*(1-0.5)=100毫秒，和testdelay*(1+0.5)=300毫秒之捡波动。此处如果设置为0，则表示test delay的值不会随意变化，直接是初始设置的毫秒数。




原始封面

![课程图片](https://images.unsplash.com/photo-1546471180-335a013cb87b?w=300)

