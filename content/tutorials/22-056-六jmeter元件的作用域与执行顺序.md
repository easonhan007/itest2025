---
weight: 56
title: （六）JMeter元件的作用域与执行顺序
date: '2017-07-23T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1548588681-adf41d474533?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
### 元件的作用域
----
先来讨论一下元件有作用域。《[JMeter基础元件介绍](/jmeter/base-element/)》一节中，我们介绍了8类可被执行的元件（测试计划与线程组不属于元件），这些元件中，__取样器__ 是典型的不与其它元件发生交互作用的元件，__逻辑控制器__ 只对其子节点的取样器有效，而其它元件（config elements 、timers 、post-processors、assertions、listeners）需要与取样器（sampler）等元件交互。

* __配置元件（config elements）__

元件会影响其作用范围内的所有元件。

* __前置处理程序（Per-processors）__

元件在其作用范围内的每一个sampler元件之前执行。

* __定时器（timers ）__

元件对其作用范围内的每一个sampler有效。

* __后置处理程序（Post-processors）__

元件在其作用范围内的每一个sampler元件之后执行。

* __断言（Assertions）__

元件对其作用范围内的每一个sampler元件执行后的结果执行校验。

* __监听器（Listeners）__

元件收集其作用范围的每一个sampler元件的信息并呈现。

<br>
在JMeter中，元件的作用域是靠测试计划的的树型结构中元件的父子关系来确定的，作用域的原则是：

* 取样器（sampler）元件不和其它元件相互作用，因此不存在作用域的问题。

* 逻辑控制器（Logic Controller）元件只对其子节点中的取样器 和 逻辑控制器作用。

* 除取样器和逻辑控制器元件外，其他6类元件，如果是某个sampler的子节点，则该元件会对其父子节点起作用。

* 除取样器和逻辑控制器元件外，其他6类元件，如果其父节点不是sampler ，则其作用域是该元件父节点下的其他所有后代节点（包括子节点，子节点的子节点等）。

讲了这些，你可能迷糊了，到底是肿么个情况呀！？通过两个栗子（例子）来理解一下他们的作用域。

__例一__

<font color=#FF6347 >注：下图只是为了说明作用域，无法正常运行。</font>

![](http://img.testclass.net/element_scope_demo1.png)

__取样器：__ HTTP请求 、FTP请求 、TCP取样器；__逻辑控制器：__ 循环控制器；__监听器：__ 图形结果、聚合报告。

*  HTTP请求、FTP请求、TCP取样器 元件没有作用域的概念。

*  循环控制器 元件作用域是其子节点FTP请求 、TCP取样器 。

*  图形结果 元件的作用域是FTP请求 、TCP取样器。

*  聚合报告 元作的作用域是HTTP请求 、FTP请求 、TCP取样器。

__例二__

<font color=#FF6347 >注：下图只是为了说明作用域，无法正常运行。</font>

![](http://img.testclass.net/element_scope_demo2.png)


这个例子稍微复杂一些，包含的元件较多。先来分分类。

__取样器：__ HTTP请求 、FTP请求 、TCP取样器、 JDBC Request ；__逻辑控制器：__ 循环控制器、随机控制器；__定时器：__ 定时器、Uniform Random Timer ；__断言：__ 响应断言、XML断言；__监听器：__ 图形结果、聚合报告。

根据作用域原则，这些元件的作用域分别为：

*  HTTP请求 、FTP请求 、TCP取样器、 JDBC Request 元件没有作用域名概念。

*  循环控制器 的作用域为 FTP请求 、TCP取样器和 随机控制器。

*  固定定时器 作用于 HTTP请求 、 Uniform Random Timer 作用于所有取样器。

*  响应断言 作用于JDBC Request  、 XML断言作用于FTP请求 、TCP取样和JDBC Request。

*  图形结果 作用于FTP请求 、TCP取样和JDBC Request 、聚合报告作用于所有取样器。


__其实，通过上面的分析，并没有你想象的那么复杂，我们从各个元件的层次结构就可以判断每个元件的作用域。__

Jmeter中的逻辑控制器（Config Elements）在其作用范围内的行为与其他元件相比稍有不同。逻辑控制器元件分两大类：
默认配置（HTTP默认请求、FTP默认请求等）和 管理（HTTP 头管理、HTTP cookie 管理等）。

其中默认配置（Configuration Defaults）元件中设置的值可以在作用域内叠加，例如，在一个测试计划中添加两个HTTP
默认请求，其中第一个默认设置 Server name or IP 为www.google.com ，第二个默认设置Path 为/page-not-exist，
则在这两个元件作用域内的所有HTTP 默认请求，其默认的Server name or IP 和Path 均为Server name or IP 和
/page-not-exist 。（你有一个故事，我有一个笑话，我们一交换，两个人都分别拥有了一个故事加一个笑话。）

管理（Manager）类逻辑控制器元件的效果则不能进行叠加。如果两个或两个以上相同的管理类元件作用域有重叠。则在重叠
作用域内的取样器元件只会随机受到其中一个的作用，这样会导致取样器行为的不确定性。因此，在使用管理类逻辑控制器时，
一定要注意保证相同的管理类元件的作用域不发生重叠。

<br>
### 元件的执行顺序
----
了解了元件有作用域之后，来看看元件的执行顺序，元件执行顺序的规则很简单，在同一作用域名范围内，测试计划中的元件按照如下顺序执行。

（1）配置元件（config elements ）

（2）前置处理程序（Per-processors）

（3）定时器（timers ）

（4）取样器（Sampler）

（5）后置处理程序（Post-processors）（除非Sampler 得到的返回结果为空）。

（6）断言（Assertions）（除非Sampler 得到的返回结果为空）。

（7）监听器（Listeners）（除非Sampler 得到的返回结果为空）。

关于执行顺序，有两点需要注意：

*  前置处理器、后置处理器和断言等元件只能对 取样器起作用，因此，如果在它们的作用域内没有任何取样器，则不会被执行。

*  如果在同一作用域范围内有多个同一类型的元件，则这些元件按照它们在测试计划中的上下顺序一次执行。

----
注：本文件中提到的取样器（Sampler）在有些资料中翻译为“采样器”。




原始封面

![课程图片](https://images.unsplash.com/photo-1548588681-adf41d474533?w=300)

