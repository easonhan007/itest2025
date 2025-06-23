---
weight: 1
title: "Postman越来越难用了"
date: 2024-03-08T09:03:29+08:00
lastmod: 2024-03-08T09:03:29+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "确实如此"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1457305237443-44c3d5a30b89?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

今天看到有个哥们吐槽 postman 的新版界面，这位是 Spotify 的资深工程师，所以他的槽点还是有些代表性，他是这么说的

> Uhhhh what happened to Postman? I just want to send, and inspect http requests?

> What is all this shit?

> Adam Rackis
> Senior Web Engineer at Spotify. Prev, Riot. Next, React, Svelte, C++ when I'm feeling nasty. Beer, whiskey, coffee snob. Book lover. Jr Developer for life.
> https://github.com/arackaf

怀着看热闹不嫌事大的心情，我把本机的 postman 更新了一下。对于更新这件事情我是能不更就不更，因为我一直觉得 postman 的旧版本就是比新版本要好用。

更新到最新版本之后，有趣的事情发生了，界面确实变化很大，之前 postman 的核心就是请求构造页面，现在我随便点了几下，结果 postman 频繁弹出登录页面，我大概点了 2 个菜单，分别是 Home 和 Explore，登录框弹出来 3 次，最无语的是在 home 页面的全屏登录框，我一时半会找不到 X 按钮，当时让我无比的慌乱，不登录难道就不配用你吗？幸好在一个不起眼的地方看到可以忽略登录的链接，终于让我这种不愿意透露姓名的 postman 忠实用户有了继续使用的权利。

其实很早之前 postman 在进行了几轮融资之后就已经变得越来越臃肿和让人看不明白了，但我还是在坚持使用，主要是因为下面的原因

- 习惯问题。之前我用的很熟练了，特别是变量和断言功能，其他工具似乎并没有类似的能力
- 代码导出功能。我习惯于在 postman 上调通接口，然后直接导出 python 或者是 go 的代码
- 请求导出及分享能力。把 collection 导出成 json 文件，然后到处分发，对小团队来说这是很方便的

然而现在我已经在慎重考虑放弃 postman 了，毕竟我要的是简单工具，而 postman 要的是建立社区，提高壁垒，提升用户粘性，然后让我交钱。我也不是不能付费，但是

- 首先我是个人用户，我不会为自己购买团队版本，所以很多付费功能对我来说是用处不大的
- 替代的产品很多，就像老罗说的，其他产品又不是不能用，甚至有些产品在某些方面做的比 postman 更好

人不能两次踏进同一条河流，我也不能每次小心翼翼的点掉 3 次登录窗口，所以是时候说再见了，我不会卸载 postman，毕竟我有一些关键的 collection 保存在上面，但我可以降低使用频率，非必要不去用，另外可以花时间去折腾其他替代品。

## 替代品

### mac 用户

对于 mac 用户来说首推 RapidAPI，这款产品我在大概十年前就已经使用过，当时 postman 做的并不好，那时候还叫做 paw 的 RapidAPI 前生是 mac 上最丝滑流畅的选择，而且 paw 是付费的，我买了，毕竟用的是公司的钱。

RapidAPI 相对 postman 比较轻量，不过也支持

- 导出为 python/go 等语言的代码
- 支持一些常见的鉴权方式
- 比 postman 要丝滑的多
- 支持 curl 导入

### windows 用户

windows 用户的话可以选择 insomnia，这个工具我记得之前有介绍过，作者当初写这个只是为了好玩，后来他靠这个赚了不少钱，最终卖给了 kong，可能已经财务独立了吧。项目是开源的，地址在这里: https://github.com/Kong/insomnia。

insomnia 的免费版本基本就够用了，功能基本跟 postman 差不多，除了下面这些

- 没看到直接写断言的地方，不过翻文档发现其实是支持 js unit test 的一些框架的，比如 mocha，具体的没有仔细研究了
- 导入功能非常直接且，比如可以直接贴 curl 命令到 url 栏里，工具会自动检测和导入，非常丝滑，不过我花了 20 分钟才能弄明白究竟如何导入
- 快捷键很好用

### VS code 用户

thunderclient 这个插件应该可以替代大部分 postman 的功能，如果你使用 vs code 的话，不妨尝试一下。

基本功能应该是不收费的，文档也比较齐全，还有个 github 仓库专门做客服用：https://github.com/rangav/thunder-client-support，稍微体验了一下，发现基本上可以替代postman百分之八十左右的功能。比如

- 导出为 python/go 等语言的代码
- 支持一些常见的鉴权方式
- 支持前置处理和断言
- 支持环境变量和系统变量
- 支持 curl 导入
- 支持 collection
- 支持导出为 postman 格式

反正日常使用基本上是够了的，而且没事不会弹登录框，比 postman 清爽多了。

## 总结

postman 变得流行的原因是作为一个工具，它解决了我们很多实际的问题。但自从商业化之后，postman 让我们这些老用户越来越搞不明白，其实不是 postman 变难用了，平心而论 postman 还是好用的，这也是为什么其他类似工具都跟 postman 长的差不多的原因，但加入太多的 to B 功能之后，我们这种纯粹的 C 端用户就变成了 postman 商业化转型的牺牲品。我们的诉求很简单，一个符合直觉的请求调试工具，然而 postman 通过各种更新主动的抛弃了我们，为了取悦企业采购而牺牲了用户体验，这不是 postman 一家的问题，基本上大多数的企业级应用都会有一些奇怪的功能去讨好真正的金主，比如钉钉的钉一下功能。

好在市场是自由的，我们仍然有大量的选择余地。

postman 我们不能否认其历史地位，它的创新让这一工具品类变得异常丰富，激烈的竞争也让我们用上了越来越好的产品，不过对于最终的独立用户来说，是时候跟 postman 渐行渐远了。
