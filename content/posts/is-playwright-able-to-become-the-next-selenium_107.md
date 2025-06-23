---
weight: 1
title: "playwright会成为下一个selenium吗？"
date: 2024-03-08T09:04:15+08:00
lastmod: 2024-03-08T09:04:15+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "我觉得selenium不会成为替身的"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1651403984845-03c9c2d1ecb9?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

playwright 是微软推出的一款 e2e（端到端）测试工具，支持多种语言及浏览器，那么它会成为下一个 selenium 吗？前几天看到外国的一篇文章发表了其观点，这里翻译了一下**并夹杂了一点点的私货**，希望可以对大家所有帮助。

selenium 作为浏览器自动化项目来说是非常成功的存在。Selenium 现在已经被下载了几百万次，并继续在全球范围内被广泛接受和使用。

### Selenium 的成功的原因

1. Selenium 是开源的，支持多种（如 Java、C#、Js、Python、Ruby、Perl 等），支持所有的浏览器（chrome、firefox、edge、ie、safari、opera 等），可以在多种操作系统（Windows、MAC、Linux）上运行。
2. Selenium 功能强大--它可以做 web 测试，也能做跨浏览器兼容性测试。另外 selenium 设计的初衷是浏览器的自动化，所以除了用作测试之外，selenium 还在 web 自动化操作领域有所建树。
3. Selenium 有一个庞大的用户社区，可以帮助你快速入门。
4. 与其他开源工具相比，Selenium 非常稳定，它的实现甚至成了标准的 w3c 协议。
5. 最后，Selenium 社区是充满活力的，定期举行许多活动和研讨会，你可以与志同道合的人讨论最新的工具和技术。

### playwright 会成为下一个 selenium 吗？

考虑到现代 Web 应用自动化，Selenium WebDriver 似乎是最受欢迎的工具之一，然而，像 Playwright、Puppeteer、Cypress 这样的替代工具正在出现，并争取在一段长时间之后能对其进行超越。

Playwright 是一个 JavaScript 框架，支持在前端实现 Web 应用程序的自动化。它在后端使用 Node.js，就像 Puppeteer 那样。它扩展了该框架，为用户提供了编写端到端测试或隔离测试应用程序特定部分所需的所有工具。

支持使用包括 Java、Js、C#、Python 在内的语言编写测试用例，并像 Selenium WebDriver 一样在任何浏览器和任何操作系统上运行。它是开源的，很容易使用，支持单兵作战和团队协同。

在 UI 自动化领域，Playwright 能够成为下一个 Selenium 的主要原因有以下七个方面。

- Playwright 得到了微软的支持，其作者来自 Puppeteer（谷歌）团队，因此 playwright 可以吸收 Puppeteer 积极的方面。另外，它已经了一些版本来支持多种编程语言，社区的反馈也非常积极。简而言之微软的钞能力和干爹属性使其相对其他开源项目来说可能会有更多的持续性。

- Playwright 的架构更简化，它摆脱了 selenium 复杂的设置和维护本地 driver 的繁琐过程，基本上开箱即用，工程化方面的实践也更加深入。初学 selenium 的同学应该记得 selenium 安装之后没有下载 driver 的话就是不能用的，特定版本的浏览器需要特定版本的 driver 配合，对于一些长期项目的维护来说确实有时候会带来额外的工作量。

- Playwright 的测试执行速度非常高（平均比 selenium 快 40%），因为它使用 JavaScript 引擎如 Node.js 来运行测试，而不是 Selenium 的 driver 程序。因此，与 Selenium WebDriver 相比，使用 Playright 可以大大降低测试执行时间。

- 与 Selenium WebDriver 不同，Playwright 除了支持测试页面的全屏截图外，还支持边测试边录屏，感觉现代化了不少。

- 与 Selenium WebDriver 相比，Playright 的维护成本更低，因为它使用内部等待，而不像 Selenium WebDriver 需要管理显式等待。这大大降低了总的代码编写和维护成本。

- Playwright 除了支持 web 自动化测试外，还支持 RESTFul API 测试。这使测试人员可以灵活地使用 Playwright 测试他们的后端服务。

- 最后，Playwright 可以跟浏览器的开发者工具进行集成，这使得用 Playwright 编写开发测试非常容易和简单。

![Untitled](playwright%E4%BC%9A%E6%88%90%E4%B8%BA%E4%B8%8B%E4%B8%80%E4%B8%AAselenium%E5%90%97%EF%BC%9F%20b17dbf0f72044cd9bbdc0ea07cc75e31/Untitled.png)

原文地址：[https://medium.com/testleaftechblog/will-playwright-become-next-selenium-b41eebfa5d25](https://medium.com/testleaftechblog/will-playwright-become-next-selenium-b41eebfa5d25)
