---
weight: 1
title: （一）mock 与 Mockito 介绍
date: '2017-11-25T12:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1508830524289-0adcbe822b40?w=300
tags: []
categories:
- mockito简明教程
lightgallery: true
toc:
  auto: false
---




#### 什么是mock ？
---

mock在翻译过来是模拟的意思。这里要介绍的mock是辅助单元测试的一个模块。它允许你用模拟对象来替换你的系统的部分，并对它们已使用的方式进行断言。

什么意思呢？说的直白些，我们要测试一个模块（类、方法或接口），但是这个模块还没有实现，或者它属于第三方模块，真的去调用会比较麻烦，这个时候就可以借助 mock 技术，给该模块设置预期结果。

可能你和我一样会有疑问，把要测试的模块都mock掉了，这不是自己骗自己嘛，那我们还测什么？

但是，在实际生产中的项目是非常复杂的，对其进行单元测试的时候，会遇到以下问题：

* 接口的依赖
 
* 外部接口调用

* 测试环境非常复杂

单元测试应该只针对当前单元进行测试, 所有的内部或外部的依赖应该是稳定的, 已经在别处进行测试过的.使用mock 就可以对外部依赖组件实现进行模拟并且替换掉，从而使得单元测试将焦点只放在当前的单元功能。

__mock技术的目的和作用就是模拟一些在应用中不容易构造或者比较复杂的对象，从而把测试与测试边界以外的对象隔离开。__

#### 什么是 Mockito ?
---

官方网站：http://site.mockito.org/

Tasty mocking framework for unit tests in Java

优雅的mock框架用于Java的单元测试。

GitHub 地址：https://github.com/mockito/mockito


#### 安装 Mockito
---
以 [Maven](/maven/) 方式安装为例。

```
 <dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-all</artifactId>
    <version>2.0.2-beta</version>
    <scope>test</scope>
</dependency>
```

因为 Mockito是其于单元测试的框架，所以，接下来的练习最好在单元框架框架下运行，通过 Maven 配置 JUnit 单元测试框架。

```
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>
```









原始封面

![课程图片](https://images.unsplash.com/photo-1508830524289-0adcbe822b40?w=300)

