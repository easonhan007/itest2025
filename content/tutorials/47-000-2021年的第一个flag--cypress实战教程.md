---
weight: 0
title: 2021年的第一个flag--cypress实战教程
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



cypress的目的是为前端开发同学降低日常工作中重复的end to end测试工作量，提高测试效率，尽管是面向开发，但测试同学花时间去学习还是非常值得的。

会测试的开发其实是受欢迎的，会开发的测试竞争力也是有目共睹的。

前几天听到一个理论，要想达到高收入，那么你可能需要在某一个领域技能达到90或100分，显然这是很难的。

但是你也可以跨界，为自己多开辟一个赛道，你可以在某个领域做到50分，然后另一个领域也是50分，这样合起来也是竞争力比某个领域精通的90分其实也不差，测试学习开发技能的底层逻辑也就这里。

既然对于大多数人来说，炒房资金不足，又不想去股市币圈当韭菜，那么把有限的时间和金钱花在投资自己身上，其实是明智的决定。

随手在搜索引擎上找了一下，发现结构良好的cypress教程还是屈指可数的。

新的一年到来了，不如先立个flag，写一套cypress的实用教程吧。

那我为什么要写教程呢？

* 写教程也是学习的过程，我需要持续学习来提升自己的竞争力
* 写教程让人痛苦，不过有痛苦才会有进步，撸铁的同学肯定有类似的体验
* 我乐于分享，而且坚持了好久，成了习惯
* 有了文字教程就可以尝试视频教程，剪辑制作高质量的视频教程也是我2021年想提高的点

既然是实用教程，那么一定要从实际项目开始，好在cypress非常贴心的提供了cypress realworld项目，尽管这个项目没啥现实生活中的实际实用意义，不过有前端，有后台，有单元测试用例，接口测试用例以及ui测试用例，五脏俱全，工整优雅，来源于学习的目的，但实际上对我们的测试思路还是有很好的指导效果的。所以cypress教程不如换个思路来做，直接看别人的项目是怎么做自动化测试的，用例怎么选取的，断言如何写的，项目目录结构是怎么样的，从实战中去补充基础知识，这样效果也许会更好一点，或者是更功利一点。


### 整体思路

分析cypress realworld项目，地址：https://github.com/cypress-io/cypress-realworld-app，从项目中学会

* typescript的简单语法，因为项目是typescript写的，会一点简单的语法方便我们进行源码阅读
* 体验cypress realworld项目，梳理出主要功能，这是熟悉需求
* 梳理后端接口和数据结构，这一步是了解后台逻辑实现
* 了解express,lowdb的简单使用，这一步的目的是为了让我们能看懂项目的后台代码
* 了解react,xstate的简单使用，为了看懂前端代码，这两个框架的时间投入还是值得的
* 了解cypress功能
* 了解前后端分离app的工作模式
* 单元测试怎么写?看一下实际项目中的单元测试实现
* 接口用例怎么写？看一下高水平的开发者的接口测试思路
* ui测试用例怎么写？这里很难一言以蔽之
* database seeding是什么？为什么会降低ui测试的难度？
* cypress怎么做ci/cd的？了解ci/cd的工作原理与工作流程

### 大纲草稿

* ts语法简介，主要参考微软官方文档:https://www.typescriptlang.org/docs/handbook/intro.html
* cypress realdworld项目部署(也可以不用部署)
* cypress realworld项目初体验，输出主要功能文档
* cypress的主要功能，参考https://docs.cypress.io/guides/core-concepts/introduction-to-cypress.html#Cypress-Can-Be-Simple-Sometimes
    * 重试机制
    * 元素的交互
    * 分支测试
* cypress relaworld的后台接口分析
* 如何使用express+lowdb实现后台接口
    * 数据库设计
    * 鉴权
    * 路由及持久化实现
* 分析cypress relaworld的单元测试实现
* 分析cypress relaworld的接口测试实现
* 如何使用react+xstate实现前端功能
    * react简介以及页面的渲染
    * 路由实现
    * 状态机实现
    * 与后台的交互
* 分析ui测试用例
    * 如何选取用例
    * 断言怎么写
    * 什么是db seeding，有什么好处
    * 怎么调试
    * 怎么截图和录视频
    * 怎么设置环境变量
    * 如何使用test runner去命令行跑指定用例
    * 怎么做多浏览器兼容性测试
    * 怎么做ci/cd

随便列了一下，发现内容还是相当丰富的，如果一周出一篇的话，基本上半年大半年就过去了。

### 时间计划

所以先立个flag，争取在今年年中，大概7月份之前完成吧。

在如今定量宽松的时代，投资稍有不慎贬值的机率是比较大的，不过投资自己却是少有的低成本高收益的投资方式。

新的一年，不如我们一起花点时间，让自己增值吧，也许你会发现，你自身才是自己最优质的资产。







原始封面

![课程图片](https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?w=300)

