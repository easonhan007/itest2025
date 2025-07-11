---
weight: 1
title: "软件测试中7个令人震惊的真相"
date: 2024-03-08T09:02:24+08:00
lastmod: 2024-03-08T09:02:24+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "挺有意思"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1609619385076-36a873425636?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

这是最近看到的一篇比较有意思的文章，原文在这里：[https://medium.com/geekculture/seven-unspoken-truths-about-software-tests-4bcf0f720a04](https://medium.com/geekculture/seven-unspoken-truths-about-software-tests-4bcf0f720a04)，简单的加工翻译了一下，其中（）里的内容是我为了帮助大家理解夹带的私货，希望这篇文章会对大家有所启示。

1，当你是一个项目的的测试负责人的时候，你有没有过质问过项目成员为什么没测试出某个具体的 bug，或者因为某人没有测出 bug 而直接责备他？

2，当你提升了测试覆盖率的时候你有没有发现产品的 bug 数量其实没有发生变化？

3，你有没有在发布之前花费了大量的时间去进行测试却最终发现一无所获，而发布之后 bug 却不期而至？

4，开发可以测试他们自己的代码吗？

5，bug 真的是发现的越晚修复成本就越高吗？

6，你有没有过以不按套路出牌的方式来进行软件的测试，并称之为“探索性测试”？

7，你是否需要通过 QA 活动来提升产品质量？

## 真相 1：测试并不能找出所有的 bug

很不幸这是真的，没有任何一种测试方式可以保证找出所有的 bug。

一些测试活动跟直接上手点点点相比确实效率要低一些，所以我们可以不用那么关注测试的类型，相反我们要做的是选择合适的测试类型并综合使用，从而以最少的工作量打到较好的效果。（比如 ui 的自动化测试如果要做到非常复杂那么将花费相当大的开发和维护成本，但没有 ui 的自动化，每轮测试都靠人肉点来点去也不现实，所以比较合适的做法是一些稳定的核心路径可以用 ui 自动化去实现，平衡投入产出比，用较少的工作量达到效率最大化）

当有人抱怨为什么测试没有发现某些问题的时候麻烦提醒他们：测试确实没有办法保证一定会发现某些特定的缺陷。

我们会经常复盘测试的漏测情况，很不幸，这是落后的想法，这就像是在魔术揭秘了之后再马后炮的说其实这个戏法很简单，很容易被识破一样。事后做漏测复盘并不是一个有效的分析手段。

永远不要责备测试工程师，他们并没有写出 bug，相反，他们一直在努力找出开发过程中引入的缺陷。没有什么是完美的，测试同学在接受现实的同时也需要记住千万别立 flag，因为测试不可能发现所有的 bug。

## 真相 2：测试覆盖率与测试的效果几乎没有相关性

是的，你没有看错。我们已经有足够的科学证据表明，增加单元测试覆盖率不一定会提高我们测试套件发现 bug 的效率！也许是时候关注与测试相关的内容而不是正在测试的代码量了。（这里作者的原话是 We already have enough scientific evidence to say that increasing unit test coverage may not necessarily increase your test suite effectiveness in finding defects!直译过来就是单元覆盖率的提升并不会提升测试套件发现缺陷的效率，说实话，我觉得单元测试覆盖率跟测试中发现 bug 的效率本来就没有什么关系，覆盖率代表的是代码被测试的程度，而发现 bug 的效率指的是时间和产出的关系，发现 bug 的效率高并不代表着产品的质量就好，反之亦然。不过看下文引用资料时的描述，我们可以看到作者的举证基本上都透露了一个信息，那就是单元测试覆盖率与 bug 的数量之前没有太多的关联，换句话说就是并不是单元测试覆盖率越高，产品的质量就越好，因为产品的质量好一般意味着可被观察到的 bug 相对少，而 bug 又跟单元测试覆盖率无关。这里为了严谨，作者的引用我就不做翻译了。）

1. *A. Mockus, N. Nagappan, and T.T. Dinh-Trong, “Test Coverage and Post-verification Defects: A Multiple Case Study,” Proc. 3rd Int’l Symp. Empirical Software Eng. and Measurement (ESEM 09), 2009, pp. 291–301.*The correlation between coverage and defects was **none or very weak**. Moreover, the effort required to increase the coverage from a certain level to 100% increased exponentially.
2. *M.R. Lyu, J. Horgan, and S. London, “A Coverage Analysis Tool for the Effectiveness of Software Testing,” IEEE Trans. Reliability, vol. 43, no. 4, 1994, pp. 527–535.*Qualitative analysis found **no association** between the defects and coverage.
3. *B. Smith and L.A. Williams, A Survey on Code Coverage as a Stopping Criterion for Unit Testing, tech. report TR-2008–22, Dept. of Computer Science, North Carolina State Univ., 2008, pp. 1–6.*The results **did not support the hypothesis of a causal dependency** between test coverage and the number of defects when testing intensity was controlled for.
4. *L. Briand and D. Pfahl, “Using Simulation for Assessing the Real Impact of Test Coverage on Defect Coverage,” Proc. 10th Int’l Symp. Software Reliability Eng., 1999, pp. 148–157.*The results **did not support the hypothesis of a causal dependency** between test coverage and the number of defects when testing intensity was controlled for.
5. *P.S. Kochhar, F. Thung, and D. Lo, “Code Coverage and Test Suite Effectiveness: Empirical Study with Real Bugs in Large Systems,” Proc. IEEE 22nd Int’l Conf. Software Analysis, Evolution, and Reengineering (SANER 15), 2015, pp. 560–564.*A **moderate to strong correlation was found** between coverage and defects. However, the **coverage was manipulated and calculated manually**.
6. *L. Inozemtseva and R. Holmes, “Coverage Is Not Strongly Correlated with Test Suite Effectiveness,” Proc. 36th Int’l Conf. Software Eng. (ICSE 14), 2014, pp. 435–445.*A **weak to moderate correlation** was found between coverage and defects. The type of coverage did not have an impact on the results.
7. *X. Cai and M.R. Lyu, “The Effect of Code Coverage on Fault Detection under Different Testing Profiles,” ACM SIGSOFT Software Eng. Notes, vol. 30, no. 4, 2005, pp. 1–7.*A **moderate correlation** was found between coverage and defects, but the **defects were artificially introduced**. The correlation was different for different testing profiles.
8. *G. Gay et al., “The Risks of Coverage-Directed Test Case Generation,” IEEE Trans. Software Eng., vol. 41, no. 8, 2015, pp. 803–819.*Coverage measures were **weak indicators for test suite adequacy**. **High coverage did not necessarily mean effective testing**.

## 真相 3：测试工作量呈指数增加

许多消息来源指出，测试人员会在测试活动开始时发现更多缺陷，而在结束时发现缺陷则更少。有迹象表明，为了找到下一个缺陷，增加覆盖率和执行测试的工作量呈指数增长。

在论文“Test Coverage and Post-verification Defects: A Multiple Case Study,” (A. Mockus, N. Nagappan, and T.T. Dinh-Trong, Proc. 3rd Int’l Symp. Empirical Software Eng. and Measurement (ESEM 09), 2009, pp. 291–301.)中透露：将覆盖率从某个水平增加到 100% 所需的努力呈指数增长。

根据“Implementing automated software testing: How to save time and lower costs while raising quality.” (Dustin, E., Garrett, T., & Gauf, B. (2009). Pearson Education.),的阐述：软件可靠性模型表明，随着在测试中投入更多时间，每单位时间发现的缺陷数量呈指数减少。

![Untitled](%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B8%AD7%E4%B8%AA%E4%BB%A4%E4%BA%BA%E9%9C%87%E6%83%8A%E7%9A%84%E7%9C%9F%E7%9B%B8%207dd7b38224bf4c239e4bf5cbb8f348b6/Untitled.png)

## 真相 4：开发者偏差

如果开发人员在开发阶段直接把一个需求理解错了，那么他写出来的代码就是错的，对于测试人员来说情况也一样。

如果开发同学直接忘记在代码中处理某些情况，比如特定的条件验证，那么他也很可能不会记得对这种场景进行测试。

为了避免这种情况，开发人员可以互相测试彼此的代码，但他们最好不要测试自己的代码，这就是所谓的交叉测试。

在没有设计任何测试用例的情况下，开发同学还是可以测试自己的代码的，这样就可以尽可能的避免一些先入为主的偏差。

测试驱动开发可能会降低开发忘记做某事概率，但不会减少误解某些需求的概率。

### 真相 5：晚期**发现的缺陷可能不会花费更多来修复**

这是非常反直觉的，因为人们可能习惯于看到这样的图片：

![Untitled](%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B8%AD7%E4%B8%AA%E4%BB%A4%E4%BA%BA%E9%9C%87%E6%83%8A%E7%9A%84%E7%9C%9F%E7%9B%B8%207dd7b38224bf4c239e4bf5cbb8f348b6/Untitled%201.png)

这上面的数字可能是有水分的，Laurent Bossavit 是巴黎软件咨询公司 CodeWorks 的敏捷方法论专家和技术顾问，他在 github 上的文章“Degrees of intellectual dishonesty”就透露了这些信息可能是被捏造出来的。

在一篇名为“Are delayed issues harder to resolve? Revisiting cost-to-fix of defects throughout the lifecycle” (Menzies, T., Nichols, W., Shull, F. et al. Empir Software Eng 22, 1903–1935 (2017) [https://doi.org/10.1007/s10664-016-9469-x](https://doi.org/10.1007/s10664-016-9469-x))的论文指出：没有发现任何证据表明在代码投入生产后进行缺陷的修复需要花费更长的时间。

论文“What We Have Learned About Fighting Defects” (Forrest Shull, Vic Basili, Barry Boehm, et al., Proceedings of the 8th International Symposium on Software Metrics (METRICS ‘02). IEEE Computer Society, USA, 249. 2002.)中，作者指出：修复某些非关键 bug 的成本在整个生命周期阶段几乎保持不变（项目早期平均 1.2 小时，项目后期平均 1.5 小时）。

不过很多的研究都在度量定位错误和修复 bug 的工作量，那么他们忽略了什么？

- 回归测试：在发布之前我们要进行频繁的回归，为了验证某些重要的 bug 已经被修复了，我们就需要一次又一次的对主流程甚至是大部分的逻辑进行回归测试，这显然是很巨大的工作量；
- 机会成本：在项目的晚期发现问题的时候，很多人往往会将 bug 排到下一个版本或项目，这很可能导致项目延期交付；
- 企业商誉成本：企业可能会被罚款，客户可能会亏钱，用户体验自然也就不好。2020 年 12 月，游戏《[赛博朋克 2077》](https://www.forbes.com/sites/siladityaray/2020/12/18/cyberpunk-2077s-disastrous-launch-gets-worse-as-sony-removes-game-from-playstation-store-promises-refunds/)因发售时出现诸多技术问题而[从索尼商店下架](https://www.forbes.com/sites/siladityaray/2020/12/18/cyberpunk-2077s-disastrous-launch-gets-worse-as-sony-removes-game-from-playstation-store-promises-refunds/)。索尼提供全额退款。随后，开发商 CD Projekt Red 宣布对 PS4 和 Xbox 玩家进行退款。[在投资者电话会议上，CD Projekt Red 表示“与恢复公司声誉相比，《赛博朋克 2077》修复的成本“无关紧要”](https://www.gamesradar.com/the-cost-of-fixing-cyberpunk-2077-is-irrelevant-compared-to-restoring-company-reputation-says-cdpr/)。该公司的股票[已从 2020 年 12 月的每股 31 美元跌至 2021 年 6 月的每股 10 美元](https://www.denofgeek.com/games/cyberpunk-2077-sales-2021-cdpr-stock-price/)。
- bug 并不是在代码中引入的。比如在项目的初期做技术设计的时候就存在缺陷，或者需求本身就是个 bug，那么越晚发现灾难就越大。

因此，虽然发布后修复代码错误的工作量可能不会增加那么多，但早期修复 bug 可以节省大量精力、金钱和麻烦。

## 真相 6：**探索性测试需要流程和文档**

很多人认为如果他们对产品做一些无法预料结果的操作，比如在表单胡乱输入并且提交，那么他们就是在做探索性测试。

其实探索性测试并不意味着你要对系统或者产品做一些特别的事情，它往往意味着我们需要了解系统是如何真正工作的，并且与普通的功能测试同时进行。

换句话说探索性测试可以（并且最好应该）得到现有文档的支持，例如需求文档和设计文档。这里的区别在于探索性测试的测试用例不是预先编写好的。

探索性测试可以脚本化，一旦发现问题就可以把 bug 记录在案，然后可重复执行的脚本又可以在后面的测试过程中反复使用。（比如探索测试时可以使用浏览器自带的录制功能，发现 bug 之后就把录制好的脚本保存下来，给后面的回归测试使用，chrome 现在已经自带了录制能力了）。

测试用例仍然应该使用边界值分析、等价类划分等技术来设计。我们没有理由设计一些随机的测试用例，因为它们在检测缺陷方面可能不具有成本优势或有效性。

## 真相 7：**改进流程中的非质量保证活动可以提高产品质量**

（这里原文的论述我实在是没弄明白并且找不到合适的数据支持，所以就简单的粘贴英文版本了）

A 2009 [study in Brazil](http://www-di.inf.puc-rio.br/~kalinowski//publications/TravassosK09a.pdf) (in Portuguese) involving 135 software development organizations had their capacity to identify and fix defects increased by improving their processes. These companies were part of a Brazilian software process improvement program called “MPS.Br,” where they should adhere to a software process improvement model (the MPS Model).

This model has stages, and 58 of these companies were in the first stage, where they were required to improve their Project Management and Requirements Management processes.

While it’s unclear why this happened, we can reasonably expect that projects that identify the right people to participate in the team, training needs, and proper budget and schedule will likely have the people, the time, and other resources to improve quality.

## 奖励关（有趣的事实）：**百慕大计划**

好吧，这是一个有趣的，但没有解释的事实，它可能真的不起作用。

百慕大计划是更快完成项目的战略名称。将团队的一部分派往百慕大（即，将他们从项目中移除），项目会更快完成。

它被认为是对布鲁克斯定律（Brooks’s law）的回应（对软件项目管理的一种观察，根据该定律，“在延期的软件项目中增加人力会让项目交付的更慢一些”）。那么，如果您移除人员，项目是否应该进行的更加迅速？

根据我的经验，加入团队的每个新人都会占用一个老人工作时间的 1/3 左右，直到新人们逐渐提高生产力。

因此，踢走最近加入的人可能真的会提高工作效率。

如果团队中有太多冲突，它可以起作用的其他原因是：移除与团队目标不一致的人可能会对团队有所帮助。

如果团队中有太多人，那么沟通开销可能会大到足以阻碍生产力。在这种情况下，拆分团队可能效果很好（这在技术上与从项目中移除人员不同）。

否则，移除人员只会降低团队在短期内的输出。

无论如何，我只是在分享百慕大计划，因为谈论它总是很有趣。
