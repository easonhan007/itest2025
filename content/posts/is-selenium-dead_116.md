---
weight: 1
title: "Slenium已死？"
date: 2024-03-08T09:04:29+08:00
lastmod: 2024-03-08T09:04:29+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "其他的框架例如playwright, cypress当立？"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1553524913-efba3f0b533e?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

selenium 已死？其他的框架例如 playwright, cypress 当立？这是去年一个广泛讨论的话题。对于我来说这个观点很明显是偏颇的，因为

- selenium 本身已经成为了 w3c 规范的一部分，现在市面上所有的浏览器都遵循这个规范
- selenium 本来就不是一个纯测试工具，它是为自动化而生，除了浏览器测试之外，selenium 还有很广泛的用途，而 playwright/cypress 则更专精于测试领域
- selenium 的 api 相当稳定，对于一些需要长期维护的项目来说这是非常有诱惑力的，而我去年用 playwright 做了一个项目，今年由于 api 升级，去年的代码基本上已经完全不可用了

所以对我来说，selenium 尽管已经徐娘半老，吸引力大不如前，但在某些场景下，selenium 仍然会是我的首选工具，就像是 vb/php 一样，尽管大家都已经看衰很多年了，但这些技术一直没有落幕退场。

selenium 官方可能也察觉到了这些广泛的讨论，昨天他们官网 blog 发了一篇文章，直接讨论 selenium 与其他工具的情感纠葛，上下文可能是不少人发博文比较 selenium 与其他工具，然后标题党一下，使得大家产生错觉：selenium 真的已经快死翘翘了。这篇内容专业简洁，适合给大家消除误解，原文地址：https://www.selenium.dev/blog/2024/selenium-vs-blog-posts/。

下面是全文翻译。

这篇博文讨论了那些比较 Selenium、Cypress 和 Playwright 的标题党文章。这些文章没有意义，也没有帮助。

作者：David Burns (@AutomatedTester) | 2024 年 1 月 9 日星期二

在博文中，关于自动化测试的标题党文章最容易的方式就是将 Selenium 与其他工具进行比较，并配以一个吸引人的标题，尤其是当它贬低现有工具时。

不幸的是，这可能会使人们对这些产品中的哪些功能可用产生困惑，尤其是当我们进行同类的过度类比时。

Selenium 一直是一个很好的浏览器自动化工具。对于该项目来说，幸运的是，它已经成为测试 Web 应用程序的首选工具近 20 年。该项目专注于构建越来越复杂的浏览器自动化的难点。项目的重点一直是稳定的 API 和可扩展性，以保证 Selenium 的运行。它没有关注人们如何进行测试，因为有非常好的测试框架可用，并且为 5 种不同的编程语言进行测试是一项非常重要的工程工作。

然而，这些博文中经常出现一些误解。

### 与 Playwright 和 Cypress 相比，设置浏览器和驱动程序太困难

过去确实如此，因为您需要下载驱动程序。对于 GeckoDriver 和 SafariDriver 来说，这并不太糟糕，因为它们可以优雅地处理浏览器升级。另一方面，对于基于 Chromium 的浏览器，您需要为每个新版本更新驱动程序。

现在，Selenium 已经自动处理了这个问题。如果找不到 ChromeDriver 或 EdgeDriver，它将使用 Selenium Manager 进行下载。自首次发布以来，它已经有了很大的改进，现在可能是最好的选择，因为最新版本的 Selenium 甚至可以下载并使用浏览器。与 Playwright 和 Cypress 相比，您不需要更新对 Selenium 的依赖以更新浏览器和驱动程序，您仍然使用与您的客户相同的浏览器，并且切换版本变得轻而易举：您也不必更改您正在使用的测试框架。此外，让我们不要忘记它使用的是 Google 推荐用于测试的浏览器。

### 设置 Test Runner 是一项艰巨的工作，而 Playwright 和 Cypress 已经内置了...

嗯...也许吧？使用 Selenium 设置端到端测试框架并不像一些人所认为的那么困难。真正困难的部分实际上是确保驱动程序位于正确的位置，我们已经解决了上面讨论的问题。一旦完成了这一步骤，Selenium 的方法允许您使用您最熟悉的任何测试框架。如果您希望使用“全家桶”方法，将 Selenium 与 Test Runner 紧密集成，那么诸如 SeleniumBase、Nightwatch、Serenity 等使用 Selenium 的众多项目可能是适合您的工具。

需要注意的一点是，Playwright 是与 Selenium 类似的唯一的多语言浏览器自动化框架。然而，如果您不使用 TypeScript 或 JavaScript，仍然需要自己设置 Test Runner。一些测试框架具有自动设置可能需要的 Fixture 的插件。在 JavaScript/TypeScript 领域，如果您真的需要一个内置的 Test Runner，那么像 NightwatchJS 这样的下游项目和像 WebdriverIO 这样的相关项目就可以满足您的需求。下游项目使用我们的库，相关项目有自己的库，但仍遵循 WebDriver 标准。

### Playwright 和 Cypress 可以进行网络拦截，并允许我编写事件驱动的代码，而 Selenium 不能

自从 Selenium 4 发布以来，它已经能够提供这个功能。它非常好，以至于 Playwright 甚至建议您使用它来扩展您的测试。Selenium 项目不会很快删除这些功能，因为我们依赖于 WebDriver BiDi 规范的实现来替代它们。即使如此，Selenium 始终致力于确保升级不会在没有足够警告的情况下破坏任何功能。这就是为什么每种编程语言都提供了高级封装，例如 NetworkInterceptor，以隔离您的测试与底层技术的关系。

### 总结

从上面的内容可以看出，Selenium 仍然与市面上的产品一样出色。与 Cypress 或 Playwright 不同的是，Selenium 是一个由志愿者驱动的项目，而不是商业支持的项目。想要帮助我们吗？为什么不撰写一篇关于您如何使用上述功能的博文，或在社交媒体上发布这些功能如何使您的生活更轻松的帖子呢？
