---
weight: 1
title: "2024年最值得学习的自动化测试工具"
date: 2024-06-30T13:31:24+08:00
lastmod: 2024-06-30T13:31:24+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "2024年最值得学习的自动化测试工具"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

![](https://img.ethanhan.cc/file/e8bea6744d9a0e2895ad1.png)

这是一张 主流的 3 大自动化测试工具每周 npm 下载量的统计对比。

npm 是 nodejs 的依赖管理工具，所以这张图可以看出在 javascript 这门语言领域，每种工具使用人数的变化情况。

看图说话，从趋势图上看，3 大工具在 2024 年的命运大相径庭。

- cypress 增速明显放缓，考虑到 cypress 只有 javascript(typescript)版本，所以可以比较确定的是，cypress 的用户数已经停滞不前了;
- selenium 的用户数开始退坡，考虑到 selenium 有 java 和 python 的版本，我们只能说，在前端领域用 selenium 的人变少了；
- playwright 的用户数急剧增加，特别是在 2023 年的下半年，曲线陡然上升，可能新用户和从 selenium 转投过来的用户带来了这次爆发式的增长；

结合上次我做的一个关于如何使用 playwright 狂赚美刀的视频，结论很明显了。

2024 年最值得学习的自动化测试框架就是 playwright 了。

### 为什么是 playwright

- 首先 playwright 有个好爹，微软出品，如果项目不被砍的话，更新和维护的力度是可以得到保证的；
- 其次 playwright 的入门比 selenium 其实是要简单不少的，适合初学者；
- 另外 playwright 的多种特性保证了初学者可以用相对简单的代码写出可以稳定运行的测试用例，做过自动化测试的同学肯定知道，对于用例来说，稳定运行意味着什么；
- 最后，也就是最为重要的一点就是，大部分的在其他测试层面，比如单元测试或者接口测试，搞不定的用例或者操作，都可以用 ui 自动化工具来实现。也就是重剑无锋，大巧不工。这就意味着，除了测试，ui 自动化工具的应用范围其实非常广，学的好真的可以赚钱。还是我上次视频里提到的 ai 设备之耻——rabbit R1 的例子，既然 ai 现阶段没办法实现自动打车或者定外卖的功能，那就让 playwright 去实现吧；

### 如何学习

- 首先建议初学者使用 typescript 的版本，原因很简单，ts 版本配合编辑器会带来完备的代码提示，对初学者来说很可能带来极大的帮助；
- 建议使用默认的带 testsuit 也就是测试套件的版本进行学习，因为这个版本自带断言，测试的目的就是为了各种断言；
- 官方文档是最好的学习资料，因为官方文档更新非常及时，毕竟 playwright 还在密集开发中，经常隔一段时间就会带来一些新特性；

### 开坑

一转眼就下半年了，准备开个 playwright 教程的坑，其实之前一直想做的，但无奈 playwright 更新太快，所以就这么搁置起来了。

目前 playwright 的 api 相对稳定了不少，是时候可以开个坑了。
