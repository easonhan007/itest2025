---
weight: 1
title: "AI自动化探索之gpt4与playwright"
date: 2024-03-08T09:03:07+08:00
lastmod: 2024-03-08T09:03:07+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "原理比较简单"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1522198684868-88edd8463fc9?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

之前介绍过一个使用 chatgpt4 分析 dom，然后生成 puppeteer 代码进行自动化的测试工具 Taxy AI。今天发现有人推荐了一个使用 chatgpt4 生成 playwright 代码的测试工具[BrowserGPT](https://github.com/mayt/BrowserGPT)，稍微看了一下，原理比较简单，比较适合我们去研究一下，顺便打开思路。

### 演示动画

![](https://github.com/mayt/BrowserGPT/raw/master/public/browsergpt.gif)

### 具体使用

因为我没有 chatgpt4 的 key，所以没办法直接上手使用，只能通过文档去猜测一下具体用法。

BrowserGPT 设置了 openai 的 key 以及 start url 之后就可以在命令行里运行了，大致的使用方式是输入一些自然语言，然后 BrowserGPT 执行 AI 生成的 playwright 代码，实现自然语言自动化的功能。

```
go to hn
click on the abc article
```

比如上面的一些描述就实现了去 hacknews 网站点击 abc 这篇文章的功能。

### 原理分析

大致看了一下，执行的流程是这样的，代码在[这里](https://github.com/mayt/BrowserGPT/blob/master/index.js)

- 获取初始化的 url，打开 chrome 浏览器，跳转到这个 url
- 在命令行里启动 prompt，也就是给用户一个输入的 ui
- 初始化 openai 的 api
- 写个死循环，每次用户输入之后调用`doAction`函数
- 在`doAction`函数里简化当前页面的 dom 元素
- 将简化过的 dom 元素传给 chatgpt，让 gpt 根据 playwright 的示例生成代码
- 执行 chatgpt 生成的代码

这里最有意思的部分是`doAction`函数

```javascript
async function doAction(chatApi, page, task, options = {}) {
  const systemPrompt = `
You are a programmer and your job is to write code. You are working on a playwright file. You will write the commands necessary to execute the given input. 

Context:
Your computer is a mac. Cmd is the meta key, META.
You are on the website ${page.evaluate("location.href")}

Here is the overview of the site
${await parseSite(page, options)}

Your output should just be the code that is valid for PlayWright page api. When given the option to use a timeout option, use 1s. Except when using page.goto() use 10s. For actions like click, use the force option to click on hidden elements.

User: click on show hn link
Assistant:
\`\`\`
const articleByText = 'Show HN';
await page.getByText(articleByText, { exact: true }).click(articleByText, {force: true, hidden: true});
\`\`\`
`;
  let code = "";
  try {
    code = await queryGPT(chatApi, [
      new SystemChatMessage(systemPrompt),
      new HumanChatMessage(task),
    ]);
  } catch (e) {
    console.log(e.response.data.error);
  }
  try {
    const func = AsyncFunction("page", code);
    await func(page);
  } catch (e) {
    console.log(e);
  }
}
```

可以看到给 chatgpt 的提示词是两个部分合成的，一个是预先定义的，另一个是用户输入的指令。

简单分析一下系统的提示词，大概分这几个部分

- 角色和任务定义: `You are a programmer and your job is to write code. You are working on a playwright file. You will write the commands necessary to execute the given input.`，让 chatgpt 去扮演程序员，
- 环境描述: `Your computer is a mac. Cmd is the meta key, META.`，运行环境是 mac
- 提供主要信息: `Here is the overview of the site;${await parseSite(page, options)}`，这里把当前页面的 html 元素的 body 简化了一下，再喂给了 AI
- 提供示例: 最后提供一个示例，让 ai 按照例子生成代码，并且让 ai 不要废话，只需要生成代码就好了

**一句话描述就是把当前的网页的 html 减肥一下，把页面的 dom 和用户的命令传给 ai，让 ai 生成 playwright 代码，最后执行 ai 生成的代码。**

### 泛化

泛化一下，使用 ai 进行一些测试工具的设计我们可以有下面的一些尝试

- 压缩信息。把页面/api 的描述用尽量简化的方式描述出来，作为输入的一部分喂给 ai，尽量不要基于 ai 自身的先验（也就是学习过的）知识来进行任务的执行，这样可能会产生幻觉
- 定义好的提示词。一般来说好的提示词包含：角色定义，任务描述，示例以及规范的输出描述
- 利用 ai 生成代码或其他文本（比如手工测试用例）
- 利用执行 ai 的生成的代码或者保存 ai 生成的内容

其实按道理来说还应该使用 ai 去检查之前的生成的代码或内容，让 ai 提供改进方案或者建议，这样输出的代码可能准确性会更高，不过忽略掉这个步骤问题也不大。更泛化一点看，其实这个工具有点简单的 ai agent 的样子，把 agent 与测试结合起来应该是未来一个不错的尝试方向。

### 可能会遇到的问题

这个工具目前看来实用性是有限的，这是因为当前时间节点，也就是 2023 年 10 月份，ai 可能会存在下面的问题

- 输出不稳定。同样的提示词可能每次生成的代码是不稳定的，不过之前看到 openai 的 dalle 3 提示词洋洋千言似乎每次得到的结果都很稳定，估计后面的模型在输出稳定性上会有极大的提升，另外好的提示词也能提升输出的稳定性；
- 无法生成最新 api 的代码。playwright 的 api 变化很快，我记得半年前写的一些代码现在就可能跑不起来了，不过因为 gpt4 的训练内容并不是最新的，所以生成的代码可能是基于旧的 api，有点鸡肋。不过如果是生成 selenium 的代码的话可能实用性会更强一点，毕竟 se 的主要接口这些年都没怎么变过；

最后大家可以头脑风暴一下，除了让 ai 把自然语言转成代码进行自动化测试之前，ai 还能在测试领域有什么样的应用呢？
