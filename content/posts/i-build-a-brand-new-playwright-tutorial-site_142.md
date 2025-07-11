---
weight: 1
title: "我肝了一个playwright的教程及资讯站"
date: 2024-07-12T01:26:34+08:00
lastmod: 2024-07-12T01:26:34+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "我创建了一个playwright的教程及资讯站:playwright.itest.info"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1720983590448-28b749bd403d?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

我花了一周的时间肝了个 playwright 的教程站，域名是 playwright.itest.info，事情的起因还要从 1 个油管视频说起。

我从那个视频上了解到，1 个做 AI 硬件的公司把 playwright 的自动化操作功能跟 AI 硬件结合了起来，融了 2000 万美金。

**这让我大受震撼。**

首先我没想到这么高大上的产品竟然用的是如此朴实无华的技术，更让我感到惊讶的是这家公司选择的工具是 playwright，而不是自动化届的老大哥 selenium。毕竟如果从纯技术的角度上考虑，selenium 是在原生浏览器上跑的，它的兼容性其实更好。

看来 playwright 确实是有它独到之处的。

这也让我陷入了思考，可能大部分人学习 ui 自动化工具的初衷不是测试，而是赚钱。

毫无疑问，在 2024 年的今天，playwright 是最有钱景的自动化测试工具，当然了，是金钱的钱。

不过我发现 playwright 的中文资料非常有限，所以我和虫师创建了这个站点，希望可以一直维护下去吧。

## 关于目前的进度

目前上线的版本有大概 24 篇左右的原创加翻译的资料。

我写了个爬虫去关注 playwright 的最新进展，也爬了 120 多篇非常优秀的英文教程。后面我会持续更新，这样一来资料会更加丰富一些。

除了翻译，我目前主要的精力是放在了原创教程上。在 playwright 可以找到的资料里，大部分的内容都是和自动化测试相关的，这些内容很好，不过我想如果我的教程把关注的重点放在爬虫和自动操作上，那么是不是受众会更广泛一些。

爬虫可以获取数据，在 AI 大行其道的今天，数据是各种大语言模型的基础。

自动化操作可以提升工作效率，在提效这个赛道上，永远是有商机可以挖掘的。

所以我开始肝一套 playwright 的中文教程，可以写的素材相当的丰富，既然要写很多，那么不如就写一本书吧。

目前书籍的进度大概是这样的，typescript 版本应该完成了有 50%了，等肝完 ts 的版本，再花点时间把 python 版本结束掉。

关于网站内容的质量，翻译的文章，我尽量翻译的通俗易通，然而水平毕竟有限，一些翻译的资料中会出现比较神奇的表达，希望大家可以多多指正。

原创的文章我会尽量做到深入浅出，让大家容易理解。

另外 playwright 的 api 变化很快，之前已经过期的内容我这边会人肉过滤掉，尽量保证呈现出的内容是最新的，一些翻译文章里我会加入自己的看法，明目张胆的夹带私货了。

结束掉文本资料的部分后，我会根据教程的内容录制一套 playwright 的视频教程，也会把重点放在爬虫和自动化操作上。

## 最后汇报一下这里用到建站技术

教程网站我是用[zola](https://www.getzola.org/documentation/getting-started/overview/)和[tailwindcss](https://tailwindcss.com)去搭建的。zola 是 rust 语言编写的静态站点生成引擎，跟 go 语言里的 Hugo 非常相似。tailwindcss 我比较熟悉，所以前端界面就交给它了。大家把玩一下就可以看出，因为是静态站点，所以网站的响应速度还是比较快的。

教程书籍我是用 rust 社区的 mdbook 去写的，这也是个静态站点的生成引擎，不过这个工具是专业写文档的，上手容易，用起来也很舒服。

最后大家如果对现在对 playwright 感兴趣的话，目前 b 站上虫师的那套 playwright 入门教程是非常不错的选择，强烈推荐。
