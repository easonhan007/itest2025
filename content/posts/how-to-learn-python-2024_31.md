---
weight: 1
title: "2024年如何学习python"
date: 2024-03-08T09:02:19+08:00
lastmod: 2024-03-08T09:02:19+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "2024也可以这么学"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1581089781785-603411fa81e5?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

这几天 hack news 上比较热烈的讨论是这一套 python 教程：https://github.com/dabeaz-course/python-mastery。

作者是 Dabeaz, David Beazley 的别名，他是一位计算机科学家、教育家和研究员，拥有超过 35 年的经验。Dave 在 Python 社区中非常活跃，他创建了多个软件包，参加了会议演讲和教程，并且以《Python Distilled》（Addison-Wesley）、《Python Essential Reference》（Addison-Wesley）和《Python Cookbook》（O'Reilly Media）的作者而闻名。他通过提供各种高级计算机科学和编程课程来支持这些工作。

来头很大的，毕竟是《Python Cookbook》 的作者，所以专业性上是有背书的。

简单的把项目的 readme 文件翻译了一下，这个项目的核心学习理念就是手动操作，完成课程练习，多写代码总是有收获的。

## 简介

这是一门高级 Python 编程的练习驱动课程，经过十多年的企业培训实战验证数百次。由 David Beazley 撰写，他是《Python Cookbook, 3rd Edition》（O'Reilly）和《Python Distilled》（Addison-Wesley）的作者。课程采用了知识共享许可协议，无广告、无追踪、无弹窗、无新闻通讯和 AI。

## 目标受众

这门课程适合希望进一步提高 Python 编程水平，从编写简短脚本转向编写更复杂程序的 Python 程序员。课程主要关注常用库和框架中使用的编程技巧。主要目标是更好地理解 Python 语言本身，以便理解他人的代码，并将新学到的知识应用于自己的项目中。

## 先决条件

你已经掌握一些 Python 知识。这不是一门面向初学者的课程。如果你需要更多入门材料，你可以考虑参加 Practical Python Programming(https://dabeaz-course.github.io/practical-python)课程。

## 如何参加课程

首先，你应该将 GitHub 仓库 fork 或克隆到自己的机器上。

我们假设你在本地有一个合适的 Python 开发环境。这意味着你已经正确安装了 Python，有一个编辑器/集成开发环境和其他常用于 Python 开发的工具。由于课程使用了多个文件和模块导入，不推荐使用 Notebooks。

[`PythonMastery.pdf`](PythonMastery.pdf) 文件包含了详细的演示幻灯片。课程练习和建议的时间安排都有清楚的标示。你应该将它放在身边（我建议你下载并在本地 PDF 阅读器中查看）。从这里开始吧！

[Exercises/](Exercises/index.md) 目录包含了所有的课程练习。

[Solutions/](Solutions/) 目录包含了完整的练习解决代码。

[Data/](Data/) 目录包含了课程中使用的一些数据文件。

课程最初在面对面的教室环境中进行了 4-5 天的教学，包括讲座和实践练习。成功完成课程可能需要 30-50 小时的学习时间。练习通常是基于前一练习的，遇到困难时，可以参考提供的解决方案。

## 附加资料

高级 Python 掌握课程经常推荐更深入的选题教程。这些内容曾在 PyCon 大会上展示过，可能会对你有兴趣：

- [Generator Tricks for Systems Programmers](https://www.dabeaz.com/generators/)
- [A Curious Course on Coroutines and Concurrency](http://dabeaz.com/coroutines/index.html)
- [Python3 Metaprogramming](https://dabeaz.com/py3meta/index.html)
- [Generators: The Final Frontier](https://dabeaz.com/finalgenerator/index.html)
- [Modules and Packages: Live and Let Die](https://dabeaz.com/modulepackage/index.html)

## 问题与回答

**Q: 有视频教程吗？**

**A:** 没有。你可以更快地阅读包含技术信息的演示幻灯片。然而，与本课程内容密切相关的视频教程是[Python Programming Language: LiveLessons](https://www.safaribooksonline.com/library/view/python-programming-language/9780134217314/)，可以在 O'Reilly 的 Safari 网站上找到。

**Q: 我可以在我的课程中使用这些材料吗？**

**A:** 可以。我只是恳请你给予适当的署名。

**Q: 你接受错误报告或 Pull Request 吗？**

**A:** 如果你发现了错误，请报告给我！然而，我并不打算通过新主题或练习来扩展或重新组织课程内容。

**Q: 演示幻灯片有除 PDF 之外的其他格式吗？**

**A:** 没有。

**Q: 有任何可以讨论课程的论坛或聊天室吗？**

**A:** 你可以使用[GitHub 讨论区](https://github.com/dabeaz-course/python-mastery/discussions)来讨论课程内容。

**Q: 为什么没有涵盖主题/工具/库 X？**

**A:** 该课程被设计为在 4 天的集中式面授形式下完成。不可能涵盖绝对所有的内容。因此，该课程主要侧重于核心 Python 语言，而不涉及第三方库或工具。

**Q: 为什么没有涵盖诸如 typing、async 或模式匹配等特性？**

**A:** 主要是时间和范围的问题。该课程的材料主要是在疫情前开发的，代表了当时的 Python 情况。一些主题（例如 typing 或 async）非常复杂，最好在单独的课程中进行更深入的讲解。

**Q: 我如何提供帮助？**

**A:** 如果你喜欢这门课程，最好的支持方式就是向其他人推荐它。

---

## 总结

所以这个教程适合有一定的 python 基础的同学，学习的路线图是：先看 pdf，看完做练习，最后通过 solution 来检查答案。
