---
weight: 1
title: "如何从code review中获得最大的收益"
date: 2024-03-08T09:03:26+08:00
lastmod: 2024-03-08T09:03:26+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "翻译一篇关于code review的不错文章"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1541178735493-479c1a27ed24?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

翻译一篇关于 code review 的不错文章。

原文地址: https://shecodesthecosmos.co.uk/2023/04/11/how-do-you-get-maximum-benefit-from-code-reviews

Code Review 是软件开发中常用的质量关和最佳实践之一，也可以看作是一种软件测试形式。

当 Code Review 被设计和使用得当时，可以为软件产品质量带来巨大的好处：允许发现和修复缺陷、改善文档和对代码进行检查。但当 Code Review 被设计不当时，它们往往会成为开发人员和测试人员的负担和瓶颈。

那么如何确保 Code Review 为团队和产品质量带来最大的好处呢？我有三个建议。

### 自动化！自动化！自动化！

利用自动化工具来简化审查过程，减轻审查者的工作量。许多 Code Review 中更标准和重复的元素都可以自动化：

- 使用自动化测试套件检查功能，并确保在审查之前通过此套件。测试自动化工具通常会生成报告，如果需要，审查者可以快速分析这些报告。
- 使用 Linting 软件验证格式，以帮助确保代码按标准化和可读性的方式编写。
- 通过使用静态分析工具在编译之前分析代码，识别潜在的运行时缺陷。
- 通过自动化创建 Code Review 和需求之间的链接，确保代码的可追溯性。

这些检查可以集成到 CI/CD pipeline 中，并在代码提交或创建拉取请求等事件触发执行。在审查人员甚至看到代码之前自动执行这些检查可以极大地减少执行审查所需的时间，也使 Code Review 更少重复和行政性工作。

有许多 DevOps 和 CI/CD 软件可以支持这一点，可参考的示例包括 Azure DevOps、GitLab、Jenkins 和 Atlassian 工具套件。

### 定义一个过程

当然，有些代码质量方面是无法自动检查的：检查文档是否完整并且合理，查看代码架构等。这是审查发挥最大价值的地方。为确保从 Code Review 中获得最大的质量，定义一个流程、指南、标准或清单供审查者在审查时使用，可以很有帮助。制定一个标准的检查清单可以帮助防止在审查过程中漏掉任何东西。

这些流程或指导方针应该始终具备灵活性。Code Review 的范围、规模和风险可能会大不相同，因此并非每个审查都需要进行所有检查。可能包括以下一些内容的 Code Review 清单：

- 文档的合理性检查：文档是否有意义？是否存在任何漏洞？
- 代码是否结构合理？
- 代码中是否存在任何错误或潜在的安全风险？
- 所有自动检查是否都通过？
- 代码是否遵循您组织的最佳实践政策？（如果此检查无法自动化）
- 审查的代码大小是否过大？这非常重要！如果 Code Review 太大或太复杂，审查时间将大大增加。保持 Code Review 的简单性和小规模，可能使用单一职责原则来定义应被视为 Code Review 大小的项目。

### 利用审查作为学习机会

最后，不要忘记利用 Code Review 作为团队之间共享知识的机会。团队经常会陷入这样的习惯，即让同一组人员审查代码库的相似区域。这可能会导致两个问题：

- 让同一人员一直审查相似的代码区域可能会导致疏忽，增加审查期间漏检缺陷和其他问题的风险。
- 这可能会加强信息和知识的孤立，增加关键人员风险。如果只有团队的少部分人员了解一段代码，如果这些团队成员不可用，这可能会导致连续性问题。

为了避免出现这些问题，将 Code Review 重新构想为知识共享练习。确保 Code Review 与团队的其他成员共享，可以帮助他们学习代码库的新区域。对代码的新视角也可能会引发对假设的质疑，找到更多缺陷，创新新的工作方式。这也是同行导师的好机会，为团队成员提供机会发展他们的沟通技巧，提高他们的编程能力。
