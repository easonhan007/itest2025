---
weight: 1
title: （一）TestNG介绍与安装
date: '2017-11-25T12:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1498758536662-35b82cd15e29?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---





#### 介绍
---
TestNG 官方网址：http://testng.org/doc/

TestNG是一个测试框架的灵感来自JUnit和NUnit,但引入一些新的功能，使它更强大和更容易使用，如：

* 注释。
* 在任意大线程池中运行测试，并提供各种策略（所有方法都在自己的线程中，每个测试类有一个线程，等等）。
* 测试你的代码多线程是安全的。
* 灵活的测试配置。
* 数据驱动的测试支持（@dataProvider）。
* 参数支持。
* 强大的执行模型(不再有TestSuite)。
* 通过各种工具和插件支持（Eclipse, IDEA, Maven 等..）。
* 通过进一步的灵活性Beanshell。
* 运行时和日志的默认JDK功能(无依赖性)。
* 应用服务器测试的相关方法。

TestNG 表示下一代(Next Generation的首字母)。它的设计覆盖所有类别的测试：单元、功能、端到端、集成等。

#### 安装
---
本教程基于 [IntelliJ IDEA](/idea/) 和 [Maven](/maven/) ，所以，这里只介绍 Maven 的安装方式。

```
<!-- https://mvnrepository.com/artifact/org.testng/testng -->
<dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>6.13</version>
    <scope>test</scope>
</dependency>

```




原始封面

![课程图片](https://images.unsplash.com/photo-1498758536662-35b82cd15e29?w=300)

