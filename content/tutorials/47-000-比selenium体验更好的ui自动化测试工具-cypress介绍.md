---
weight: 0
title: '比selenium体验更好的ui自动化测试工具: cypress介绍'
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1506773090264-ac0b07293a64?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



不小心发现了一个新的ui自动化测试工具:cypress，仔细品了一下之后，发现还是有很多有意思的地方的，我们也许可以从cypress里借鉴很多下一代测试工具的设计思想。

进入cypress的官网(https://www.cypress.io/)，引入眼帘的一句话让人血脉喷张。

**The web has evolved. Finally, testing has too.**

web已经进化了，最终，测试也会。

确实相较于这些年前端技术井喷式的增长来说，自动化测试技术的发展是相对缓慢的。

selenium一套api基本稳定了好多年，最终越走越抽象，由工具下沉到了协议，再由协议变成了各大浏览器厂商都公认的标准，尽快步子不大，但走的相当坚定。从招式套路演变成了内功心法，由懵懂少年变成了武林盟主，目前基本上母仪天下，催生了一些很有特点的测试工具。

selenium项目对web自动化测试最大的贡献就是统一了标准，曾几何时webdriver刚出道的时候，各大浏览器厂家对webdriver的支持力度是完全不一样的，比如在之前的很多年，官方维护的driver似乎只有google的chrome，微软的IE浏览器一直用的是民间的IE Driver。后来chrome把IE挤到了历史的垃圾堆里，微软的edge浏览器最终推出了官方维护的edge driver，safari的driver也由苹果官方推出，主流浏览器厂商全部支持了webdriver协议，江山一统，天下舍selenium其谁。

不过selenium的体验对于纯测试同学来说还是有一些硬核的，比如

* 首先必须安装一门语言，比如java/python/nodejs/ruby之类，这个过程如今在windows上面不算特别难，不过十多年前在windows上安装ruby确实不是一件轻松的事情
* 安装selenium。这时候大家会接触到诸如maven/pip(python -m pip/pip3)/rubygems/npm/yarn之类的概念，对于完全没有经验的同学来说，是有一定的挑战的，当然了，如果你具备基本的学习的自我学习能力，这个过程应该不会特别的难，除非你遇到了复杂的网络问题，那个另说
* 折腾IDE。很多同学喜欢折腾IDE，比如pycharm/IntelliJ之类的，搞完安装搞破解，搞好破解搞字体，搞到后来又去弄IDE内执行代码，各种一键配置，全套体验完，大好青春年华就白驹过隙了。另外IDE是为了提升开发效率的，代码写的越多效率提升越高，但是新手往往憋大招半天也写不出几行可以一次性运行通过的代码，IDE的优势基本发挥不出来，所以有这个时间去惆怅去彷徨，不如随便找个编辑器老老实实多敲几行代码吧。我基本上从来不去折腾IDE，因为这是可选项，并非必选，而且我智商有限，IDE的强大功能基本用不上，一直老实巴交的用文本编辑器加命令行，够用了
* 下载浏览器驱动。当年的selenium安装包里包含了firefox的驱动，稳定而高效，所以如果你用firefox做测试，那么安装好selenium就可以愉快的做自动化了。不过后来firefox换成了gecko引擎，并且由官方维护驱动后，下载浏览器驱动就成了必选项了。
* 写代码。这个相对简单，网上一堆教程。

所以虫师的selenium自动化测试书籍那么受欢迎是有很充分理由的，有他在前面带路，起码更多的人可以尝试着去用上selenium，至于用例能不能坚持写下去另说，但是入门的门槛是相对低了不少的。

上面列举了selenium的硬核操作，不知道大家会不会产生这样一个观点，那就是selenium似乎对手工测试同学不太友好。

这个想法其实在一定程度上是对的。selenium本身的使用对象就是有一定编程能力的测试同学，因为selenium是国外项目，它的诞生是符合国外的一些实际情况的，比如在国外有些地方，测试是懂开发的，同样开发也是做测试的。

所以selenium其实不是硬核，只是对于我们一些国内的测试同学来说，selenium有点曲高和寡了，并不是到手就用的傻瓜式的开源测试工具。另外selenium的一些核心用户其实是做会做自动化测试的开发同学，selenium的这种工具形态对于开发来说，相对是非常友好的。

所以我们可能忽略了一个事情，在自动化测试发展的很长一段时间内，开发其实是自动化测试的主力军，一些测试工具的设计风格偏开发的路子就很容易理解了。

今天介绍的cypress是一个比selenium还亲开发的自动化测试工具。

在官方文档的Testing Your App章节(https://docs.cypress.io/guides/getting-started/testing-your-app.html#Step-1-Start-your-server)，有这样的一段话，原文很长，摘几句重点

```
The last, and probably most important reason why you want to test against local servers, is the ability to control them. When your application is running in production you can’t control it.

When it’s running in development you can:

take shortcuts
seed data by running executable scripts
expose test environment specific routes
disable security features which make automation difficult
reset state on the server / database

With that said - you still have the option to have it both ways.

Many of our users run the majority of their integration tests against a local development server, but then reserve a smaller set of smoke tests that run only against a deployed production app.
```

大概意思是自动化测试要想做的爽，那么你就要在开发环境上做，这样你就可以随意控制你的测试环境，并且做一些可以让自动化测试进行的更加顺利的修改。当然了，你也可以在部署好的环境上做自动化测试，不过那样会比较难，可以考虑在这样的环境上执行一部分简单的冒烟测试用例。

所以cypress的核心使用人群应该是愿意做ui自动化测试的前端开发同学，因为只有他们才有项目的前端开发环境，可以改一些前端代码使得定位变得容易，另外也有能力去mock/stub掉后端server的返回，在后端服务还没有开发完成的时候就提前做测试。

对于测试同学来说，如果你想玩一下cypress，那么

1. 学会使用js以及jquery，因为cypress的一些命令使用方式跟jquery很像，学会使用js的一些测试框架和断言框架，比如mocha和chai，学会一些基本的前端概率，比如promise等
2. 争取变成半个前端，可以在本机搭建运行项目的前端代码，并且有前端代码权限，可以适量改一些无关痛痒的代码
3. 争取变成半个后端，可以比较熟练的对测试数据进行各种初始化和修改
4. 如果做不到2，3点，可以考虑在测试环境和生产环境仅保留一定数量的冒烟测试用例，这些用例的数据准备和清理要尽可能简单，流程和交互尽可能不要特别复杂

可以看到，万事开头难，2，3，3其实不重要，难的是第1点。

简单介绍一下这款工具的最基本使用，体验上还是相当不错的。

安装的话可以使用npm，如下图所示。

打开test runner，编写第一个用例。

访问一个站点，并进行元素定位。

点击元素。

一个相对完整的用例，带断言的例子。

```
describe('My First Test', function() {
  it('Gets, types and asserts', function() {
    cy.visit('https://example.cypress.io')

    cy.contains('type').click()

    // Should be on a new URL which includes '/commands/actions'
    cy.url().should('include', '/commands/actions')

    // Get an input, type into it and verify that the value has been updated
    cy.get('.action-email')
      .type('fake@email.com')
      .should('have.value', 'fake@email.com')
  })
})
```

截图里应该看不出来，不过cypress在一些体验方面做的很不错

* test runner运行方式所见即所得，用起来完全没有障碍
* 实时调试，selenium往往是重开浏览器才能调试，这一点cypress做的很不错
* 时间机器，任何一步都可以追踪
* 还有很多，不详细列出来了

最后想说明的是，cypress让我印象最深刻的一点是其追求对测试环境的完全控制，只有这样才能降低测试的难度和成本。

自动化ui测试是交互性的，带交互的东西往往纷繁复杂，处理起来难度很大，cypress的思路就是降维打击，在正式环境和测试环境不太好做的事情，我到开发环境去做，而且一做就要做到位，令人感到耳目一新，也算是一种不错的测试实践。




原始封面

![课程图片](https://images.unsplash.com/photo-1506773090264-ac0b07293a64?w=300)

