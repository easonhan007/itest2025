---
weight: 1
title: "Selenium 4.11 正式发布，支持chrome for testing"
date: 2022-03-19T09:03:15+08:00
lastmod: 2022-03-19T09:03:15+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "稳定迭代"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1510746001195-0db09655b6db?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

Selenium 4.11.0 正式发布了，先来看一下主要特性。

- Chrome DevTools 支持的版本现在是：v113、v114 和 v115（Firefox 仍然对所有版本使用 v85）
- 通过 Selenium Manager 支持 Chrome For Testing（CfT）
- Selenium Manager 现在可以在 PATH 或配置的路径上定位 driver 的二进制文件，检查潜在的不兼容性，并提供更好的警告和错误信息。
- 每晚都会推送 Ruby 和 Java 的构建版本。对其他语言的支持即将推出。
- 在查找窗口句柄时忽略进程 ID 匹配 - Edge 上的 IE 模式。

这里最重要的更新是支持了 Chrome For Testing.

### Chrome For Testing

这是 chrome 推出的专门针对测试场景使用的浏览器，为了解决下面一些痛点

- chrome 的自动化更新。自动更新：对用户来说很方便，对开发者来说很痛苦，特别是测试同学，应为我们希望(a)在重复的测试运行中获得一致且可重复的结果，但如果浏览器可执行文件或二进制文件在两次运行之间决定自行更新，这会毁了一切。(b)我们想要固定一个特定的浏览器版本，并将该版本号添加到你的源代码仓库中，这样你就可以检出旧的提交和分支，并重新运行测试，以便使用那个时间点的浏览器二进制文件进行测试。基于上面两个原因，自动更新让人欲除之而后快。

- 下载不到特定版本的 chrome 浏览器。除了自动更新之外，你可能也发现很难找到特定版本的 Chrome 二进制文件。谷歌故意不提供带有版本号的 Chrome 下载，因为用户不应该关心版本号，他们应该尽快更新到最新版本。这对用户来说很好，但对于需要在旧版本的 Chrome 中重现错误报告的开发人员来说很痛苦。这个问题的一个更具体的例子是当你想要使用 ChromeDriver 进行浏览器自动化时。你不仅需要以某种方式下载 Chrome 二进制文件，还需要一个相应版本的 ChromeDriver 二进制文件，以确保这两个二进制文件是兼容的。

在这样的背景下，chrome for testing 应运而生。官方的说法是

> 为了解决这些问题，Chrome for Testing 是 Chrome 的一个专用版本，针对测试用例进行了优化，不会自动更新，与 Chrome 发布流程集成，每个 Chrome 版本都可用。这个版本的二进制文件尽可能接近常规的 Chrome，同时不会对测试用例产生负面影响。

> 为了创建用于测试的 Chrome，我们已经对 Chromium 和 Chrome 代码库进行了修改，并建立了基础设施来构建和上传这些二进制文件到一个公开可用的存储桶，与 Chrome 的发布过程保持同步，覆盖所有渠道（稳定版、测试版、开发版和灰度版）。

具体的安装方式是通过 npm

```bash
# Download the latest available Chrome for Testing binary corresponding to the Stable channel.
npx @puppeteer/browsers install chrome@stable

# Download a specific Chrome for Testing version.
npx @puppeteer/browsers install chrome@116.0.5793.0

# Download the latest available ChromeDriver version corresponding to the Canary channel.
npx @puppeteer/browsers install chromedriver@canary

# Download a specific ChromeDriver version.
npx @puppeteer/browsers install chromedriver@116.0.5793.0
```

在 selenium 4.11 中，我们可以直接通过 Selenium Manager 来进行 chrome for testing 的安装，具体的方式在https://www.selenium.dev/blog/2023/whats-new-in-selenium-manager-with-selenium-4.11.0/ 这篇里有介绍。

### 其他细节

Java

- Make user defined SlotMatcher used everywhere in Grid code (#12240)
- Add support for FedCM commands (#12096)

JavaScript

- BiDi Add Network module events (#12197)

.NET

- Implementation of event wrapped shadow root element (#12073)
- Allow setting a different pointer, keyboard, or wheel on input device (#11513)
- Add move to location method to Actions (#11509)
- Add support for Safari Technology Preview (#12342)
- Fix error when we send non-base64 data for fetch command (#12431)
- Fix continueResponse method in CDP (#12445)

Python

- removed redundant attributes capabilities and set_capability in wpewebkit/options.py (#12169)
- improve driver logging, implement log_output() for flexibility and consistency of driver logging (#12103)
- let users pass service args to IE driver (#12272)
- Expose WPEWebKitService and WebKitGTKService in the public API
- Remove deprecated ActionChains.scroll(...)
- Add creation flag for windows in selenium_manager (#12435)

Ruby

- Made network interception threads fail silently (#12226)
- Remove deprecated code (#12417)
