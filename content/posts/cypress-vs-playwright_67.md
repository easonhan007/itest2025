---
weight: 1
title: "playwright 大战cypress"
date: 2024-03-08T09:03:12+08:00
lastmod: 2024-03-08T09:03:12+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "仅供参考"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1683107983270-38225df18859?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

之前看到一篇文章比较系统的比较了 playwright 和 cypress，这里简单翻译了一下，希望可以给大家在技术选型时提供一些参考。原文地址在这里：[https://applitools.com/blog/cypress-vs-playwright/](https://applitools.com/blog/cypress-vs-playwright/?utm_campaign=Software%2BTesting%2BWeekly&utm_medium=email&utm_source=Software_Testing_Weekly_133)。文本中的演示代码可以在 github 仓库找到：[https://github.com/applitools/webinar-cypress-vs-playwright](https://github.com/applitools/webinar-cypress-vs-playwright)

### 第一轮：元素操作

首先从最常见的场景进行比较，看看最简单的流程。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled.png)

这是一个简单的登录场景，初相见感觉是差别不大，不过 cypress 显得更加简洁一些。在用户投票中，cypress 以 61%的得票胜出。

### 第二轮：如何对 iframe 进行测试

尽管 iframe 的测试在日常的工作中并不是特别常见，不过 iframe 的处理对 qa 来说确实是一件非常有挑战的事情。实际上 cypress 需要引入插件才能进行处理，所以可能在这一轮 playwright 会稍微占据一些优势。playwright 原生支持对 iframe 进行操作，省去了额外安装插件的工序。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%201.png)

### 第三轮：等待与重试

因为现代 web 页面的特性，等待与重试成为了自动化测试工具非常重要的一种能力。参赛双方都有自动等待和重试的机制，直接看代码吧，在用户投票中这一轮 cypress 以 53%的选票获胜。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%202.png)

### 第四轮：处理浏览器的原生 alert

鉴于每个工具的不同设计，看看它们各自如何处理本地浏览器事件是很有趣的事情。Playwright 使用 websocket 服务器与浏览器进行通信，而 Cypress 则被注入到浏览器中，并从那里实现应用程序的自动化。处理本地浏览器的事件可能会更复杂，在这一轮比赛中也证明了这一点。虽然 Playwright 对警报和提示显示了一致的解决方案，不过 Cypress 对所有三种情况都有自己的解决方案，最后 Playwright 在本轮比赛中取得了 91%的横扫胜利。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%203.png)

### 第五轮：打开新窗口

在下一个例子中，我们试图将一个打开新窗口的页面实现自动化。每个工具的设计再次被证明是一个决定性因素。Playwright 有一个 API 来处理一个新打开的标签，而 Cypress 则采用了一个 hack 的解决方案，从一个链接中移除目标属性，并完全防止打开一个新窗口。虽然我认为这实际上是一个足够好的解决方案，但观众中的测试同学们并不买账，并以 80:20 的票数支持 Playwright。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%204.png)

### 第六轮:处理 API 请求

能够处理 API 请求是一种自动化的超能力。你可以用它们来配置你的应用程序，创建测试数据，甚至是登录，甚至可以直接用这两种工具来进行纯的 API 测试! Cypress 和 Playwright 都能很好地处理 API 请求。在 Playwright 中，你创建一个新的上下文，并从该上下文发射 API 请求。Cypress 使用其现有的命令链语法来发送请求并测试返回值。三分之二的听众更喜欢 Cypress 的解决方案，并为其投票。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%205.png)

### 第七轮：page object 模式

尽管页面对象通常不被认为是 Cypress 的最佳选择，但它仍然是一种流行的模式。它们提供了必要的抽象性，并有助于使代码更加可读。这里的观众投票真的很接近。在现场活动中，实际上似乎是 Playwright 赢得了这一场，在节目结束后的交流中，我们发现这一轮应该以平局告终。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%206.png)

### 第八轮：支持的语言

如今，测试人员使用的编程语言种类相当多。这就是为什么 Playwright 对语言的更广泛支持在这一轮中似乎是一个明显的赢家。然而，Cypress 试图迎合开发人员的工作流程，对 JavaScript 和 TypeScript 的支持已经足够好。然而，对于来自不同语言背景、不习惯用这些语言编写代码的测试人员来说，这可能是一个痛点。似乎观众们同意更广泛的语言支持是更好的，并投票支持 Playwright，投票率为 77%。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%207.png)

### 第九轮: 支持的浏览器

尽管 Chrome 是最流行的浏览器，并在大多数国家成为主导，但在测试 web 应用时，浏览器支持仍然很重要。两种工具都对各种浏览器有良好的支持，不过 Cypress 目前缺乏对 Safari 或 WebKit 的支持。这一轮 playwright 自然更胜一筹。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%208.png)

### 第十轮：运行速度与性能

最后一轮的比拼是关于速度的。每个人都希望他们的测试能够快速运行，这样他们就能尽快得到关于他们应用程序状态的反馈。Playwright 是这次的明显赢家，因为它的执行时间比 Cypress 快 4 倍。Cypress 方面的一些最新改进肯定有帮助，但就速度而言，Playwright 仍然是王者。

![Untitled](playwright%20%E5%A4%A7%E6%88%98cypress%2011b717732e2e4ceebd0b58c3fd83cc16/Untitled%209.png)

## 所以最后的胜利者是？

整个代码之争最终 Playwright 以 70%的支持率获胜。活动结束后，我们举行了一个小型的余兴节目，更深入地讨论了这些例子并回答了一些问题。这是一个很好的方式，可以为例子提供更多的背景，并讨论一些没有说过的东西。

我非常喜欢 Twitter 上有人说的一句话，他说真正的赢家是测试人员和 QA 工程师，他们可以在这些很棒的工具中挑选。我个人希望有更多的 Cypress 用户在活动后试用 Playwright，反之亦然。

这个活动绝对是有趣的，虽然比较代码片段和工具的不同能力很有趣，但我们很清楚，这些并不能说明问题的全部。测试人员的日常生活充满了调试、维护、复杂的测试设计决策、考虑风险和自动化的有效性......仅仅看一小段代码并不能告诉我们这些工具在现实工作中的表现如何。

所以你觉得谁应该是最后的赢家呢？
