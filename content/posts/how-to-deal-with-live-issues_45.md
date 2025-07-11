---
weight: 1
title: "线上发现了bug该如何处理"
date: 2024-03-08T09:02:40+08:00
lastmod: 2024-03-08T09:02:40+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "不要焦虑"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

今天在国外论坛看到了个很有意思的发帖，有人提问：线上发现了 bug 该如何处理。

> 我知道大家已经问过很多次类似的问题了，不过工作还是很让我失望。我在生产环境上漏掉了 1 个很明显的 bug 没测出来，我想知道你们是怎么处理这种情况的。我的项目经理发现了这个 bug。

大家的回答其实很暖心的。下面是一些高赞回答。

> 这就意味着你们在单元测试，集成测试和功能测试以及自动化测试的阶段就已经漏掉了这个问题，希望你们有做这些。其实开发跟你们的感受一下，我就是个开发，我一直为我写的 bug 感到抱歉，我认为责任应该由整个 team 承担。

> 事情都发生了，先承认错误。确定是否真的有测试遗漏，并在未来的发布中加入这个用例。

> 好的 devops team 需要有零责备文化（[https://www.releaseteam.com/the-importance-of-a-zero-blame-culture-in-devops/](https://www.releaseteam.com/the-importance-of-a-zero-blame-culture-in-devops/)），好的软件质量交付需要团队的努力。

> 这就是 QA 当下生存现状。如果你能忍受压力持续进步，那么你会成为一个好的 QA 的。

> 你并没有搞砸，是流程的锅。扔给你点资料去学习吧[https://www.amazon.com/Antifragile-Things-That-Disorder-Incerto/dp/0812979680](https://www.amazon.com/Antifragile-Things-That-Disorder-Incerto/dp/0812979680)。

总的看来大家的观点还是开明的，比较包容，不过事实上大家的看法是一回事，但最后处理问题的方式又是另外一回事了。假如发生了一个很严重的线上事故，还好有别人背锅，你是安全的，这时候你心里肯定是同情和理解，觉得 qa 其实有点无辜，是流程的锅，觉得需要整个团队努力一下以便改进交付质量，但是如果你是直接或相关责任人，处罚落到了你头上，你大概率就不会这么宽容的看问题了。

我的观点是发现线上问题不可怕，能不能迅速发现问题和迅速修复问题才是关键，而这两点光靠 qa 负重前行是无法得到根本上的改善的。
