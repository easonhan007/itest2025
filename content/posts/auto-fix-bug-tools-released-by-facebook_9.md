---
weight: 1
title: "Faceboook创建了一个可以自动修复bug的工具 "
date: 2024-03-08T09:01:46+08:00
lastmod: 2024-03-08T09:01:46+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "很神奇"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

最近 Facebook 的工程师们撰写了一份文档，解释了他们如何编写了一个可以自动修复 bug 的工具。在这篇论文中，他们介绍了 𝗦𝗔𝗣𝗙𝗜𝗫，这是一个自动检测和修复软件 bug 的工具。该工具对 Facebook App Family 中的六个重要安卓应用程序提供了修复建议，这些应用程序包括 Facebook、Messenger、Instagram、FBLite、Workplace 和 Workchat。

## 工作原理

**步骤 1：检测崩溃 -** 另一个名为 𝗦𝗮𝗽𝗶𝗲𝗻𝘇 的工具用于查找应用程序崩溃情况。当 Sapienz 识别出崩溃时，它会被记录到数据库中。

**步骤 2：确定问题 -** SAPFIX 可以准确定位导致问题的代码行。它首先检查崩溃是否可重现。如果不可重现，崩溃将被丢弃。它使用一种称为"基于频谱的错误定位"的技术来确定最可能导致崩溃的代码行。

**步骤 3：提供修复建议 -** 使用预定义的模板或代码变异，SAPFIX 提出了一个解决方案。在确定故障位置后，SAPFIX 尝试生成一个补丁。它采用了以下两种策略：

- **基于模板的修复 -** SAPFIX 使用预定义的模板为常见 bug 提供修复建议。这些模板是根据标准开发者实践设计的。
- **基于变异的修复 -** 如果基于模板的方法失败，SAPFIX 将采用基于变异的系统。它会对故障位置应用一系列代码变异，生成潜在的修复方案。

**步骤 4：测试修复 -** 提议的解决方案会经过测试以确保其有效性。它使用 𝗦𝗮𝗽𝗶𝗲𝗻𝘇 的测试用例来检查补丁的有效性。如果补丁通过所有测试，则被视为有效的修复方案。在补丁验证完成后，SAPFIX 使用 𝗜𝗻𝗳𝗲𝗿（一种静态分析工具）对提议的修复方案进行进一步分析。Infer 会检查补丁是否引入了任何新的潜在问题。

**步骤 5：审查 -** 开发人员拥有最终决定权，对修复方案进行审查和批准。

论文地址是: https://ieeexplore.ieee.org/document/8804442
