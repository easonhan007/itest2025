---
weight: 1
title: （一）持续集成与 Jenkins 介绍
date: '2017-10-16T14:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1627757691655-7afffb88d7b2?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



<br>
#### 持续集成
----
持续集成（Continuous integration，简称 CI），随着近几年的发展，持续集成在项目中得到了广泛的推广和应用。本章将带领读者一起了解持续集成工具 Jenkins 的安装与使用。

__1．什么是持续集成？__

软件集成就是用一种较好的方式，使多种软件的功能集成到一个软件里，或是把软件的各部分组合在一起。如果项目开发的规模较小，且对外部系统的依赖很小，那么软件集成不是问题，例如一个人的项目。但是随着软件项目复杂度的增加，会对集成和确保软件组件能够在一起工作提出了更多的要求-->要早集成、常集成。早集成、频繁的集成能够帮助项目开发者在早期发现项目风险和质量问题，越到后期发现的问题，解决的成本越高，从而有可能导致项目延期或者项目失败。

__2．定义__

大师 Martin Fowler 对持续集成是这样定义的：持续集成是一种软件开发实践，即团队开发成员经常集成他们的工作，通常每个成员每天至少集成一次，也就意味着每天可能会发生多次集成。每次集成都通过自动化的构建（包括编译、发布、自动化测试）来验证，从而尽快地发现集成错误。许多团队发现这个过程可以大大减少集成的问题，让团队能够更快地开发内聚的软件。

<br>
#### Jenkins
----

Jenkins 官方网站：https://jenkins.io/

提到 Jenkins 就不得不提另一个持续集成工具——Hudson ， Hudson 由 Sun 公司开发，2010 年 Sun 公司被 Oracle 公司收购， oracle 公司声称对 hudson 拥有商标所有权。 Jenkins是从 Hudson 中分离出来的一个版本，并将继续走 Open Source 的道路。二者现在由不同的团队在维护。

Jenkins 主要用于监视执行重复工作，如建立一个软件项目或工作运行的计划任务。当前 Jenkins 关注以下两个工作。

__不断地进行项目的构建/测试软件：__ 就像 CruiseControl 或 DamageControl。概括地说，Jenkins 提供了一个易于使用的所谓的持续集成系统，使开发人员更容易修改整合到项目中，并使它更容易为用户获得一个新的版本。自动连续生成提高了生产效率。

__监控外部运行的作业：__ 如计划任务作业和 Qrocmail 的工作，即使是那些在远程机器上运行的计划任务。 Jenkins 生成这些日志并且很容易让你注意到错误的出现。




原始封面

![课程图片](https://images.unsplash.com/photo-1627757691655-7afffb88d7b2?w=300)

