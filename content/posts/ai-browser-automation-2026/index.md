---
weight: 1
title: "2026年AI浏览器自动化已成熟：从测试到小红书自动发帖，效率与生财全攻略"
date: 2026-10-27T00:00:00+08:00
lastmod: 2026-10-27T00:00:00+08:00
draft: false
author: "乙醇"
authorLink: "https://zh.ethanhan.cc"
description: "从自动化测试到内容分发，分享 AI 浏览器自动化工具与真实实践，探索效率提升和生财的可能。"
images: []
resources:
  - name: "featured-image"
    src: "cover.jpg"
tags: ["AI", "浏览器自动化", "AI Agent"]
categories: ["AI", "自动化测试"]
lightgallery: true
toc:
  auto: true
---

在2026年的第三季度，浏览器自动化的问题应该是已经解决了。

目前我们可以通过AI Agent使用的自动化工具相当丰富，并且只要把需求描述清楚，Agent就可以自动操作浏览器，自主思考步骤，完成你想要的几乎任何操作。

可维护的，可复用的稳定浏览器自动化测试已经基本上可以实现了。

<!--more-->

## 常见的使用场景

除了自动化测试之外，下面是浏览器自动化的一些常见使用场景。

* RPA工具。比如电商的上货，自动退款，自动发货自动化工具；
* 爬虫。比如爬取竞品信息，一键复制竞品的所有产品（外贸自建站）；
* 内容分发自动化工具。比如小红书的自动发帖等；
* 其他自动化场景。比如每天自动签到薅羊毛工具等；

## 更多工具推荐

我用的最多的工具是ego lite + skill，配合上Chatgpt的定时任务功能，可玩性非常高，而且极其稳定。

除了ego lite之外，还有非常多的工具可供选择。

### 1. 完整 Agent 专用浏览器类

这类是独立浏览器应用，专为人和 AI Agent 并行使用设计，强调真实登录态复用、隔离空间（Spaces / 独立 tabs），不打断你自己的浏览。

- Ego Lite：基于 Chromium，人与 Agent 共享同一浏览器但隔离工作区，一键导入 Chrome 登录态，通过 ego-browser skill 控制，主要支持 macOS，最近也出了windows的beta版本，不过我没用过，不知道效果。
- BrowserOS neo：开源 Chromium 分支，专门给 Agent 用的“第二浏览器”，一键导入登录态，支持 MCP，Agent 在独立 tabs 并行运行，可回放会话，支持 macOS / Windows。
- Tabbit：AI 原生浏览器，支持外部 Agent 控制，登录态复用较好，Windows 体验更友好。

### 2. Agent Skill / CLI 类

这类不是完整浏览器，而是给现有 coding agent（Claude Code、Codex、Cursor 等）直接调用的 skill 或命令行工具，轻量、省 Token，专注控制浏览器。

- ego-browser：Ego Lite 官方配套 skill，让 agent 通过写 JavaScript 批量操作浏览器，压缩语义快照，速度快。
- agent-browser（Vercel Labs）：纯 CLI + MCP，语义化 accessibility 快照，可连接真实 Chrome profile，跨平台，适合已有 agent 快速加浏览器能力。
- Browser Harness：Browser Use 官方 CLI，让 agent 直接控制本机已登录 Chrome。

### 3. 代码框架类（纯编程驱动）

这类是库 / SDK，需要写代码或让 LLM 生成代码来驱动浏览器，适合构建自主 Agent 或可重复脚本。

- Browser Use：目前最火的 Python 库，给 LLM 一个自然语言任务，它自己规划并操作浏览器（DOM + 视觉），支持本地 / 云端，MIT 开源。
- Stagehand：基于 Playwright 风格的混合框架（TypeScript / Python / Go），支持自然语言指令（act / extract / observe），可混合确定性代码与 AI，方便调试和维护。
- Skyvern：视觉 + LLM 驱动，擅长复杂表单、动态页面、验证码，偏企业工作流自动化。
- Playwright / Puppeteer：经典底层框架，现在常配合 MCP 给 agent 用，适合确定性高的场景。

### 4. 代码 + Agent 混合类

既可写代码控制，也可让 agent 用自然语言驱动，灵活度高。

- Stagehand：代码优先，但内置自然语言原语，适合从脚本逐步加 AI。
- Browser Use + Playwright MCP：用 Browser Use 做高层自主任务，底层用 Playwright MCP 做精确控制。
- agent-browser + 真实 Chrome profile：CLI 方式复用登录态，同时可写脚本扩展。

### 5. 浏览器扩展类

直接安装在现有 Chrome 上，零切换成本，用你真实的已登录浏览器。

- Nanobrowser：开源 Chrome 扩展，侧边栏下指令，Agent 操作当前真实浏览器，登录态天然可用，适合轻量日常任务。

### 6. 基础设施 / 轻量浏览器引擎类

为上面工具提供底层运行环境，解决性能、反检测或高并发问题。

- Steel：开源浏览器 API / 沙箱，专为 AI Agent 设计。
- Lightpanda：超轻量无头浏览器（非 Chromium），内存极低、启动快，兼容 CDP，适合高并发 Agent。

## 真实实践

在日常工作和生活中，通过浏览器自动化，我们也做了不少的实践。

### 简单的书籍爬虫

老师布置任务，让去打印一本经典少儿读物作为晨读的素材。那本书的电子版本比较难下载，需要开网盘的会员，不值得。

不过有一些电子版本书网站有纯文字的网页版，于是让agent写了个基于浏览器自动化的爬虫，再把纯文字版转成pdf版，简单快速，脚本是用deepseek的网页版写的，几乎是零成本。

### H5游戏测试

我们有不少H5的游戏产品，目前一些长期执行的重复性测试都是通过Chatgpt + skill的方式去执行，而且是晚上跑，不耽误正常工作，效率提升非常明显。

### 测试辅助工具

我做了很多的cli工具，然后封装成skill，以提升造数据的效率，降低心智成本。这些cli工具本质就是调用各种api，组合起来，以实现丰富的业务流程。但api的token过一段时间之后就会过期，这时候就可以通过浏览器自动化工具自动登录，然后拿到token，自动进行登录态的刷新了。

### 小红书自动发帖工具

使用ego lite + chatgpt的定时任务可以实现小红书的自动化发帖功能。

不过这里有个问题，小红书每隔2周左右登录态就会失效，需要手动去登录一下。两周一次，其实频率不算高，可以接受。

## 总结

浏览器自动化可以极大的提升开发和测试效率，降低人力成本。

另外在一些RPA流行的领域，比如电商等，也可以极大的降低人力投入。

使用Agent + 自动化脚本结合的方式，也可以把token的消耗控制在一个较低的水平。

在浏览器自动化工具相对成熟的2026年，只要加上一些创意，满足一些特定的需求，通过浏览器自动化还是可以生财有道的。
