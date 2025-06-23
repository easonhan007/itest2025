---
weight: 1
title: "web自动化测试的智能革命:AI如何推动软件质量保证的未来"
date: 2024-03-08T09:02:42+08:00
lastmod: 2024-03-08T09:02:42+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "标题是ai取的"
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

首先这个标题不是我取的，是我喂了关键字让 AI 给取的，果然非常的标题党，让人印象深刻。

先简单回顾一下 web 自动化测试的一些发展阶段

### QTP 时代

很多年前 QTP 横空出世的时候，没有人会怀疑这种工具将是自动化测试的未来形态。使用者理论上不需要掌握任何编程语言就可以通过录制回放的方式实现 web 端的自动化测试。后来事实证明 QTP 向人们证明了自动化测试的可行性，然而其自身的一些限制让其渐渐被主流市场所抛弃。看看 bing 是怎么说的

您好，这是 Bing。QTP 是 QuickTest Professional 的简称，是一种自动化软件测试工具，主要用于功能测试和回归测试 。QTP 的优点有：

- 支持多种编程语言和平台
- 基于关键字驱动的测试方法，易于编写和维护测试脚本
- 提供丰富的测试对象库和检查点，方便识别和验证被测系统的元素
- 可以与其他 HP 测试工具集成，实现全面的测试管理

QTP 的缺点有：

- 商业软件，价格昂贵
- 对于一些复杂的界面或控件，可能无法正确识别或操作
- 对于一些新技术或框架，可能需要安装额外的插件或补丁
- 对计算机资源的消耗较大，可能影响被测系统的性能

请注意，QTP 在官网已被改名为 UFT（Unified Functional Testing）统一功能测试 。

### selenium RC 和 waitir 时代

后来的一段时间 selenium 和 watir 渐渐流行起来，这一次一切似乎是发生了倒退，相较于 qtp 提供的足够简单的录制回放模式，selenium rc 和 watir 只能自己写代码去实现自动化里的每一步操作和断言，炫酷的未来似乎渐行渐远。看看 chatgpt 对 selenium rc 的评价，先声明这些评价内容不够准确，大家仅作为参考。

Selenium RC（Remote Control）是一个自动化测试工具，以下是 Selenium RC 的优缺点：

优点：

- 跨浏览器和跨平台：Selenium RC 支持在多种浏览器和操作系统上执行测试脚本，包括 Windows、Linux、Mac OS 等。
- 支持多种编程语言：Selenium RC 支持多种编程语言，如 Java、C#、Python 等，使得测试人员可以使用他们最熟悉的编程语言编写测试脚本。
- 可以与其他工具集成：Selenium RC 可以与其他测试工具和开发工具集成，如 JUnit、TestNG、Eclipse 等，以增强测试的效率和准确性。
- 适合大型项目：Selenium RC 可以测试大型项目，包括 Web 应用程序和企业应用程序。
- 可以模拟真实用户行为：Selenium RC 可以模拟真实用户的行为，如单击、输入文本、选择下拉列表等，以确保应用程序的稳定性和可靠性。

缺点：

- 速度较慢：Selenium RC 使用 JavaScript 与浏览器进行通信，速度比较慢，影响测试的执行效率。
- 对浏览器的支持有限：Selenium RC 支持的浏览器版本有限，对于最新的浏览器版本可能无法进行测试。
- 安装和配置较为繁琐：Selenium RC 的安装和配置相对比较繁琐，需要一定的技术知识和经验。
- 不支持并发测试：Selenium RC 不支持多线程和并发测试，可能需要在多台机器上进行测试。
- 不支持移动端应用测试：Selenium RC 不支持移动端应用程序测试，需要使用其他工具或者框架进行测试。

### webdriver 时代

后来就是 webdriver 一统江湖了，看看 claude(chatgpt 的竞品)对 webdriver 的评价。内容基本准确，不过没有提及 webdriver 的核心能力，就是统一了 web 自动化测试的标准，也就是所谓的 webdriver 协议。

Selenium WebDriver 的优点有:

1. 跨浏览器支持:支持 Chrome,Firefox,Safari,IE 等主流浏览器,测试代码可以跨浏览器运行。
2. 免费开源:Selenium 是开源免费工具,有很大的社区支持。
3. 丰富的 API:Selenium 提供丰富的 API 用于测试 web 应用,可以操作浏览器,元素,cookies 等。
4. 支持多种语言:Selenium 支持多种编程语言,如 Java,C#,Python,JavaScript 等。
5. 平台与操作系统无关:Selenium 可以运行在 Windows,Mac,Linux 等不同的操作系统。

Selenium 的缺点有:

1. 不能测试移动端浏览器:Selenium 主要用于测试 web 应用,不能用于测试移动端浏览器。
2. 学习曲线较陡:Selenium API 较多,学习起来比较困难,需要一定的学习成本。
3. 执行速度较慢:与其他自动化测试工具相比,Selenium 的执行速度会慢一些。
4. 无法处理 JS 库:Selenium 无法很好的处理某些 JS 库,如 React,Vue 等,在驱动这些界面时会有一定困难。
5. 无法测试无界面场景:Selenium 需要依赖浏览器界面,无法测试 API,服务等无界面场景。
6. 并发执行能力差:Selenium 驱动浏览器执行测试,如果测试用例量大并发执行会比较困难。

所以综上,Selenium 是一款优秀的自动化测试工具,但也有一定的不足之处,需要根据实际项目进行选择和使用

### playwright 及其他新一代工具

webdriver 聚集于 web 自动化本身，但 web 自动化测试需要涵盖更多的方面，比如用例的组织，数据的存储，多浏览器并行测试，重试机制以及用例稳定性提升等，这就给了新一代测试工具的崛起提供了很好的土壤，可以让微软的 bing 评价一下自家的 playwright。

Playwright 是一种新一代的自动化测试工具，由微软公司于 2020 年初发布 。

Playwright 的优点有：

- 支持多种主流浏览器，包括 Chromium、Firefox、WebKit 等
- 支持多种平台，包括 Windows、Linux、macOS 等
- 支持多种编程语言，包括 TypeScript、JavaScript、Python、.NET、Java 等
- 支持无头模式和有头模式，以及移动端的模拟
- 提供了丰富的 API 和文档，方便编写和维护测试脚本

Playwright 的缺点有：

- 相对于 Selenium 等成熟的测试工具，Playwright 还比较新，可能存在一些兼容性或稳定性的问题
- Playwright 需要安装额外的依赖包，可能增加了测试环境的复杂度
- Playwright 目前还不支持 IE 浏览器和 Safari 浏览器

### 二次开发的时代

无论我们选型的工具是 webdriver 还是 playwright，很多团队都喜欢进行一些定制化的二次开发，核心的诉求就是：**让不懂代码的人也可以进行 web 自动化测试**。比如

- 用配置文件去替代代码
- 提供录制回放能力
- 用写 excel 的方式编写用例
- 提供 web ui 编写用例的方式

### TaxyAI

总的看来，工具一直在进步，但自动化测试的核心诉求似乎一直都没有很好的被满足，或者说是自动化测试学习门槛相对比较高，从而参与到其中的测试人员相对较少，大部分情况下都是一群人的狂欢，大部分人的围观。

最近 gpt 大语言模型风靡全球，很多有意思的应用应运而生，无意间看到了一个能使用自然语言进行 web 自动化的实现，演示效果让人有些感叹：也许这才是 web 自动化测试的正确姿势。地址在这里：https://github.com/TaxyAI/browser-extension 。这是一个简单的 chrome 插件，安装好配置一下 chatgpt4 的 api key 之后就可以用了。

先看演示，这里直接让 AI`安排明天上午10点的站会，并且邀请david@taxy.ai参加`

![](https://user-images.githubusercontent.com/176426/228092695-1bc11ea9-bfb7-470d-bbc6-0026e93c23c3.gif)

因为我没有 gpt4 的 api key，我下载下来用 gpt3.5 跑了一下，在简单的页面上确实可以实现**用自然语言指挥浏览器干活**的功能。不需要写代码，不用理解 html 的 dom 结构，直接想要做什么就让浏览器去做，这种交互是自然而高效的。

### 奇妙的实现方式

因为项目是开源的，所以就简单的看了一下代码，结合文档上的解释，发现工具的实现方式非常的巧妙，以后这种奇妙的实现方式可能会产生出各式各样更多的产品实现。

1. Taxy 在网页上运行内容脚本来拉取整个 DOM。它简化所收到的 HTML,仅保留互动或语义上重要的元素,如按钮或文本。它为每个互动元素分配一个 ID。然后,它“模板化”DOM 以进一步减少 token 的消耗。
2. Taxy 发送简化的 DOM 以及用户的指令给所选的 LLM(当前支持 GPT-3.5 和 GPT-4)。Taxy 告知 LLM 有两种与网页互动的方法:

   - click(id)- 点击与该 id 关联的互动元素
   - setValue(id,text)- 聚焦在文本输入框,清除其现有文本,并在该输入框中键入指定的文本

3. 当 Taxy 从 LLM 获得完成时,它会解析响应以获取操作。如果满足以下任何条件,操作周期将在此阶段结束:
   - LLM 认为任务已完成。LLM 可以返回一个指示,表示基于 DOM 的状态和截至此时的操作历史,它认为用户的任务已完成。
   - 用户停止了任务的执行。用户可以在任何时间停止 LLM 的执行,而无需等待它完成。
   - 出现错误。Taxy 的安全优先架构会自动停止执行意外响应。
4. Taxy 使用 chrome.debugger API 执行操作。
5. 该操作添加到操作历史记录,Taxy 循环回到第 1 步,并解析更新的 DOM。所有先前的操作都作为用于确定下一个操作的提示的一部分发送给 LLM。Taxy 目前可以为单个任务完成最大 50 个操作,尽管在实践中,大多数任务需要少于 10 个操作。

简单总结一下就是：taxy 首先把网页的 html 变成一个简化版本，比如只保留 button，text 和 link 之类的，并为每个 dom 元素分配 1 个 id，然后把这个简化的 dom 和用户的意图发送给 gpt，gpt 根据提示给出具体的操作指令返回给 taxy，然后 taxy 解析指令，调用 chrome 的 api 进行点击和输入文本的操作。

直接看一下 taxy 的 prompt 吧，这里是用魔法打败魔法的地方。

```typescript
const systemMessage = `
You are a browser automation assistant.
You can use the following tools:
${formattedActions}
You will be be given a task to perform and the current state of the DOM. You will also be given previous actions that you have taken. You may retry a failed action up to one time.
This is an example of an action:
<Thought>I should click the add to cart button</Thought>
<Action>click(223)</Action>
You must always include the <Thought> and <Action> open/close tags or else your response will be marked as invalid.`;
```

所以 taxy 每次都把之前进行过的操作和 dom 发给 gpt4，然后然 gpt4 自己去判断下一步要怎么做，嗯，原来现在代码可以这样写，学习了。

### 亮点

taxy 目前还在进化中，所以暂时没上架 google 的扩展商店，不过最近看到代码有重构过，并加上了核心的单元测试，相信不久的将来我们是可以直接下载使用的。

taxy 的亮点非常让人印象深刻

- 把 html 简化后交给 gpt 进行行为的推断，让 gpt 决定下一步该怎么做，这可能是以后很多工具可能采用的方式。
- 天生支持多语言
- 实现方式的脑洞很大

### 不足

- dom 文本就算简化后也很大，每次使用特别费 token，其实就是费钱
- 我在试用过程中发现操作可能会没有办法终止

### 总结

> 我：写一段话描述一下人工智能技术会给自动化测试带来什么，要求专业简洁，100 个中文字符以内。

> Claude：人工智能技术将给自动化测试带来深度变革。人工智能可自动生成测试用例,智能识别测试目标,智能分析测试结果。智能机器可学习历史测试数据,推理判断当前测试需求,进行自主化测试。这将大大提高测试效率和质量,减轻测试人员工作量。这是自动化测试发展的必然方向。

> chatgpt 3.5: 人工智能技术能够提高自动化测试的效率和精度，例如自动化测试可以利用 AI 算法进行智能筛选和调整测试用例，同时也可以加强对于自动化测试结果的分析和挖掘。

> bing: 人工智能技术可以提高自动化测试的效率和质量，减少重复工作和人为错误，实现更智能的测试过程和结果 。人工智能技术可以通过图像识别、数据分析、自动化编码等方式，模仿人类的测试行为和思维。

> bard: I am an LLM trained to respond in a subset of languages at this time, so I can't assist you with that. Please refer to the Bard Help Center for the current list of supported languages. 😭
