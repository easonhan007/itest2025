---
weight: 3
title: Android测试（三）：Android 单元测试
date: '2017-12-20T14:45:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1516251193007-45ef944ab0c6?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---



原文：https://developer.android.com/training/testing/unit-testing/index.html


单元测试是你的应用程序测试策略的基本测试。 通过针对您的代码创建和运行单元测试，你可以轻松验证各个单元的逻辑是否正确。 在每次构建之后运行单元测试可帮助你快速捕获并修复由代码更改引入到应用程序的软件回归。

单元测试通常以可重复的方式实现尽可能小的代码单元（可以是方法，类或组件）的功能。 当你需要验证应用程序中特定代码的逻辑时，你应该构建单元测试。 例如，你创建了一个类，单元测试可以帮助检查该类是否处于正确的状态。 通常，单元测试是相对独立的，你的测试只会影响和检查被测试单元的变更，mock框架可以用来隔离你要测试单元的依赖。

注意：单元测试不适合测试复杂的UI交互事件。 相反，您应该使用UI测试框架，如[UI自动化测试](https://developer.android.com/training/testing/ui-testing/index.html)中所述。

为了测试Android应用程序，你通常需要创建这些类型的单元测试：

* __本地测试：__ 仅在本地机器上运行的单元测试。这些测试被编译为在Java虚拟机（JVM）本地运行，以最小化执行时间。使用这种方法来运行没有依赖于Android框架的单元测试，或者可以使用mock对象来填充依赖关系。

* __Instrumented测试：__ 在Android设备或模拟器上运行的单元测试。 这些测试可以访问工具信息，例如被测试的应用程序的上下文。 使用此方法运行具有Android依赖关系的单元测试，这些测试不能使用mock对象轻松填充。

接下来将告诉你如何构建这两种类型单元测试。

本课的教训将告诉您如何构建这些类型的自动化单元测试。

#### Lessons
----

[Building Local Unit Tests（创建本地单元测试）](https://developer.android.com/training/testing/unit-testing/local-unit-tests.html)

学习如何构建在本地机器上运行的单元测试。

[Building Instrumented Unit Tests（创建Instrumented单元测试）](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html)

了解如何构建在Android设备或模拟器上运行的单元测试。




原始封面

![课程图片](https://images.unsplash.com/photo-1516251193007-45ef944ab0c6?w=300)

