---
weight: 1
title: （一）Locust 介绍
date: '2017-10-16T14:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1512981566925-4937ba1d2b2c?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



Locust 官方网站：https://www.locust.io/

#### Locust 介绍
----
An open source load testing tool.

一个开源性能测试工具。

define user behaviour with python code, and swarm your system with millions of simultaneous users.

使用 Python 代码来定义用户行为。用它可以模拟百万计的并发用户访问你的系统。

![](http://img.testclass.net/locust_UI.png)

<br>
#### 性能工具对比
----
__LoadRunner__ 是非常有名的商业性能测试工具，功能非常强大。使用也比较复杂，目前大多介绍性能测试的书籍都以该工具为基础，甚至有些书整本都在介绍 LoadRunner 的使用。

__Jmeter__ 同样是非常有名的开源性能测试工具，功能也很完善，在本书中介绍了它作为接口测试工具的使用。但实际上，它是一个标准的性能测试工具。关于Jmeter相关的资料也非常丰富，它的官方文档也很完善。

__Locust__ 同样是性能测试工具，虽然官方这样来描述它 “An open source load testing tool.” 。但其它和前面两个工具有着较大的不同。相比前面两个工具，功能上要差上不少，但它也并非优点全无。

* Locust 完全基本 Python 编程语言，采用 Pure Python 描述测试脚本，并且 HTTP 请求完全基于 Requests 库。除了 HTTP/HTTPS 协议，Locust 也可以测试其它协议的系统，只需要采用Python调用对应的库进行请求描述即可。

* LoadRunner 和 Jmeter 这类采用进程和线程的测试工具，都很难在单机上模拟出较高的并发压力。Locust 的并发机制摒弃了进程和线程，采用协程（gevent）的机制。协程避免了系统级资源调度，由此可以大幅提高单机的并发能力。

正是基于这样的特点，使我选择使用Locust工具来做性能测试，另外一个原因是它可以让我们换一种方式认识性能测试，可能更容易看清性能测试的本质。

我想已经成功的引起了你的兴趣，那么接下来就跟着来学习Locust的使用吧。




原始封面

![课程图片](https://images.unsplash.com/photo-1512981566925-4937ba1d2b2c?w=300)

