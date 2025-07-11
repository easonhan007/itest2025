---
weight: 1
title: "更多的测试人员，更多的报酬"
date: 2024-03-08T09:01:40+08:00
lastmod: 2024-03-08T09:01:40+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "兼听则明"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1533568749383-2b0bf33e53cb?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

关于 ai 与测试的讨论现在逐渐流行起来，目前看来观点基本是积极和激进的，大多数人认为 ai 会重新塑造测试行业，不过基于 ai 的测试探索目前看来还是有限的，我稍微总结了一下，大概分为两类。

- 利用大语言模型的推理能力进行驱动的自动化工具；这个之前的文章已经介绍过一些了，有兴趣的同学可以翻一下之前的存档；
- 对融合了 ai 功能的软件产品进行测试。推荐大家研究一下这篇文章，里面的一些标准步骤还是让人备受启发的。https://blog.scottlogic.com/2023/11/14/testing-LLM-based-applications-strategy-and-challenges.html。这些测试大多是对prompt的安全，边界条件以及输出的稳定性进行测试。

就这个时间节点看来，ai 在测试领域上的应用其实不算太多。另外目前对于大模型本身的测试工作也基本是众测模式，模型提供商经过基本的 fine tuning 和测试之后发布模型或者提供 api 接口，通过使用者的反馈来持续的改进模型，基本上走的是强化学习的路子，对模型的测试不依赖于测试行为，而依赖于更多样性的标记数据，所以哪家大模型能跑出来其实就是看哪家的显卡多和数据多。

最近看到一篇非常积极拥抱 ai 的测试文章，里面的观点基本没有数据佐证，先不去讨论正确与否，不过文章确实传递出了一种很强烈的乐观信号，因为这篇文章认为 ai 会带来更多的测试岗位和更高的报酬。下面是对这篇文章的翻译，https://jarbon.medium.com/ai-more-testers-more-money-045e1a34741d。先提前说明，对这种观点我持谨慎的乐观态度，尽管我一直认为从事ai其实跟我们当年做黑盒测试差不多，不过下文的描述在短期看来还是比较难达成的，未来是什么样确实比较难以预测，所以不如积极投身其中去创造未来吧。

下面是原文的翻译：

AI 裂变正在迅速到来。AI 将在软件测试领域创造新的有和无。将 AI 引入软件测试将改变测试人员、供应商和工具的工作方式。但是，这种变化不会如大多数人所担心或梦想的那样。声称 AI 很快就会简单地取代人工测试人员的工作是错误的。希望 AI 无法足够聪明地完成大部分测试工作也是错误的。将会有更多的测试工作，并且它们很快将得到更高的报酬。在这个过渡中，有些人会失去工作，但这取决于他们自己。只有思想开放、乐观的测试人员才能在这个过渡中生存下来，并且他们将得到丰厚的工作保障和报酬。

### AI 对测试工作的影响

在短期内，AI 不会减少测试工作的数量 - 对测试人员的需求将会增加。许多测试人员担心 AI 会消灭他们的工作 - 这对大多数人来说是不真实的。应用 AI 于工作的“AI 辅助”测试人员将更加高效。那些能够迅速做到这一点的人将获得最多的工作保障、进步和回报。

在 10 亿美元以上的测试领域中，最大的问题可能是如何衡量价值。工程团队知道他们需要测试，但很难量化，而事实是，大多数测试工作在今天没有 AI 的情况下几乎没有什么用处。当测试人员得到 AI 的辅助时，测试人员的速度、范围和价值将增长到明显的价值点。目前，大多数软件测试仅仅涵盖基本功能和一些边缘情况，成本高昂，并拖慢了工程团队的进展。

然而，AI 辅助测试将赋予这些人类测试人员“超能力”，他们的贡献将是压倒性的明显。正如测试领域的一位朋友上周所描述的那样 - 不久之后，测试人员将穿戴 AI-“钢铁侠”装备。企业将希望增加更多的 AI 测试人员，因为他们终于看到了明显的积极回报。这些 AI 辅助测试人员将足够快，以便在当前的开发周期内发挥作用，给人足够的信心进行发布，发现对业务有影响的问题，并揭示仍待测试的内容。对于 AI 辅助测试人员的需求将增加，因为他们将为企业增加明显的价值 - 就像开发人员增加功能和修复错误一样。

AI 还意味着开发人员正在创建更多的软件。AI 辅助工程师的加速是非常真实的，而且 AI 也意味着更多的人可以创建软件。所有这些新软件都需要由更多经过 AI 增强的测试人员进行测试。

在短期内，测试工作的数量将增加，但并非所有人都会受益。那些不接受 AI 的测试人员很快将被时间的洪流所淘汰。一些大声疾呼的测试人员将在技术进步的浪潮中哭泣，因为他们被吞噬了。有趣的是，他们的工作不会消失，他们只是为了一批对测试感到兴奋并渴望利用 AI 的新一批测试人员而被解雇。这些工作不会消失，但会由接受 AI 的测试人员来填补。

由于 AI 的存在，测试人员将获得更高的报酬。有效地利用 AI 来帮助测试任务并不容易，需要更好的测试人员。AI 将取代基本的测试 - 甚至可能进行大部分测试。AI 可以生成数百、数千甚至数百万个测试的排列组合 - 并在没有人类干预的情况下执行。工程团队将需要 AI 辅助测试人员决定如何在所有可能的覆盖范围内分配有限的计算/时间资源。基于 AI 的测试人员的一个关键角色是根据团队和业务目标定制测试机器人。这些 AI 辅助测试人员将在被 AI 自动化的开发人员之后仍然需要。

> “AI 基础测试人员的一个关键角色是根据团队和业务目标定制测试机器人。”

不再躲在小隔间或 JIRA 中 - 这些 AI 辅助测试人员将积极与团队中的其他人员进行沟通。高效和清晰的顶级沟通技巧将供不应求。目前的非 AI 测试意味着测试人员无法运用这些技能，因为基本的、不充分的覆盖范围很容易理解和执行。AI 辅助测试意味着工程团队将需要更多经验丰富的测试人员，并且需要更多这样的人。

> “预测：离开领域成为产品经理或开发人员的测试人员将很快回流到相对高薪和安全的高级测试工作。”

### AI 裂变

在向 AI 辅助测试的过渡期间，会有许多负面声音。“只有人类才能进行测试。”“AI 还不够可靠。”“测试自动化没有取代我的工作……”“我仍然需要，因为……”“AI 无法思考。”这些人不会一夜之间消失，但他们会逐渐安静下来。他们是自愿选择退出测试群体的人。

一些人会意识到他们的错误（金钱和市场是强大的力量），悄悄开始应用 AI，并删除他们反对 AI 的社交媒体帖子。更多的人将被礼貌地“解雇”，并越来越难找到另一个测试角色。

可悲的是，一些测试人员会屈服于他们在测试工作中所宣扬的偏见。他们不会承认对连续性的个人偏见。许多人会屈服于幸存者偏差。他们的团队和圈子是技术领域中情绪抵抗的回音室。讽刺的是，我们甚至看到许多自称为专家的测试人员在他们甚至没有“测试”新的 AI 辅助技术之前就认为 AI 还为时过早、太危险或者“没有用”。跟随这些负面的人和梗，风险自负！

> 提示：迟钝的采用者将继续迟钝，这对于在快速发展的 AI 世界中的工作保障并不好。

有些人对新技术的采用速度较慢，或者更加风险规避，仅仅是因为他们的生活状况。作为测试社区，我们应该尽力帮助这些人，确保他们了解我们领域中正在发生的事情。我们应该以易于采用和应用于测试的方式构建 AI 辅助测试。我们应该不断展示和分享 AI 辅助测试的价值。我们需要确保这些人不仅仅被留在那些声音嘈杂的老派测试人员和那些有个人议程和偏见维持现状的人的任性之中。

### 总结

AI 是对测试人员的试金石。AI 正在快速进行更多的测试，但也增加了对经验丰富的人类测试人员的需求。AI 还将揭示传统测试人员的负面情绪和偏见，他们很快就会消失。即使是测试人员对软件测试的现状也不满意，但是采用 AI 辅助测试的测试人员将迅速改变这个现实。

> AI 是对测试人员的试金石。

从长远来看，AI 将从所有 AI 辅助测试人员那里学习。AI 和 AI 辅助测试人员将不断提升，形成一个良性循环。这个良性循环将使软件变得更好，并改善那些积极接受它的软件测试人员的生活。
