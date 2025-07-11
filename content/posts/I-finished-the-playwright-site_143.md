---
weight: 1
title: "我终于肝完了playwright的中文站"
date: 2024-07-18T12:48:10+08:00
lastmod: 2024-07-18T12:48:10+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "高强度肝了两周，第1个playwright中文教程站终于诞生了"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

经过两个星期的努力，我终于肝完了 playwright 中文站的主要内容。

站点地址 [playwright.itest.info](playwright.itest.info)

后面我会把精力放到 playwright 的原创教程上去，预计也会在这两周发布吧。

这次技术选型的时候遇到了一些问题，肝到快结束才发现 zola 并不支持中文索引的能力，也就是说搜索功能就没办法实现了。

所以我搞了个全部教程的 archive 页面，大家需要搜索的话可以可以在全部教程页面进行搜索。

目前全站应该更新了 90 篇左右的资料，涉及到 playwright 的基础，框架设计，api 测试以及各种最佳实践，技术含量还是不错的。

在整理和翻译教程的过程中，我自己对 playwright 也有了比较深入的了解，对目前正在写的 playwright 教程的帮助很大，一些实现和配置目前基本上手到擒来，所以建站的过程也是一个非常好的学习的过程，付出和收获是对等的。

另外一些文章翻译的质量不是很高，比如有一篇关于 playwright 视觉测试的教程，英文内容本来是很好的，不过翻译过来之后就显得牛头不对马嘴，我自己理解起来都觉得费劲，所以下周我决定抽时间把这篇教程本地化一下，做一个高质量的视频教程。

因为写了很多爬虫的关系，站点的内容应该会持续更新下去的，后面有机会的话看能不能把之前 selenium 的内容也整理出来，做一个 selenium 的中文教程站，毕竟现在对静态网站的制作也是非常得心应手了。

## 推荐内容

我精选了一些我认为比较好的内容，我把教程的名字放在这里，感兴趣的内容大家自行去所有教程的存档页面搜索就可以了。

- 如何让 playwright 运行的更快: 非常实用，特别是你的自动化代码足够多的话
- 如何使用 Playwright 监控 JavaScript 控制台日志和异常: 监听页面的`pageerror`事件，对实时前端页面监控很有意义
- 挖掘 playwright 的隐藏宝藏: 各种最佳实践，量大管饱
- 全面的基于 Playwright 的 ui 自动化测试，使用页面对象模型的模块化框架: 用 playwright+po 实现测试框架
- Playwright: 如何正确使用 fixture 构建页面对象: 使用 fixture 来组织 po，这个实践的工程化水平很高，推荐
- 使用 playwrigth api 测试: 用 playwright 做 api 测试，这一系列教程确实写的很好
- 如何使用组件来重构 playwright 的代码: 在元素之上，page 之下还可以抽象 1 个组件层，代码思想很好

## 最后

创作内容和维护内容不易，希望这个站点对大家会有所帮助。
