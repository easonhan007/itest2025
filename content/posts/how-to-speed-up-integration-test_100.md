---
weight: 1
title: "如何加速执行集成测试"
date: 2024-03-08T09:04:05+08:00
lastmod: 2024-03-08T09:04:05+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "今天我看到了一个有趣的UI集成测试加速方法"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1549088521-94b6502fec3d?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

今天我看到了一个有趣的 UI 集成测试加速方法，该方法与我想的底层优化、分布式运行或多线程运行方式不同。该作者重新编排了测试用例的执行顺序，删除了一些代码，并从执行流程上进行了优化。这确实很有趣。在本文中，我将简单介绍他的原文，希望对大家有所帮助。

我们将展示如何加速一个客户的构建过程，这样他们可以在相同的预算下多运行 40%的构建。

我必须承认，我是单元测试的超级粉丝。我早期的一些博客文章就是关于单元测试的。

单元测试是快速的、可预测的、而且隔离的。它们被很好地隔离在一个沙盒中，这就是它们的可预测性和快速性。

我们推出了一个版本，用户无法进入登录页面，但这是另一个故事了。我把它命名为“一个没有集成测试和几十个单元测试的项目”。

并不是说我完全停止写单元测试，而是我很少使用它们。大部分是用于可以安全地进行隔离测试的功能，例如一个接受各种输入并返回各种输出的函数。用集成测试来测试可能的值矩阵是不值得的。

想象一下，有一个日历组件，用户可以输入一个日期，从一个下拉日历中选择数据，然后点击一个按钮来获得一个建议的日期。所有的日期都可以是不同的格式，这取决于用户如何输入它们。是否值得为每种可能的日期格式进行集成测试？也许不值得！

然而，我们把输入的日期发送到一个负责解释许多不同格式的输入日期的实用函数，但它总是返回一个 Date 对象。为这个实用函数写一个单元测试将是一个很好的主意！对于整个应用来说，就不是那么回事了。

假设你正在建立一个问题跟踪器。你有一个集成测试，打开一个对话框，试图保存一个里程碑而不指定名称。这将导致一个错误。你的另一个测试试图创建一个里程碑，但现在指定了一个名称。这不会导致错误，并显示消息“新的里程碑已保存”。

```jsx
beforeEach(async () => {
  await createNewProject();
});

it("cannot create milestone without a name", () => {
  clickNewMilestoneButton();
  newMilestoneDialog.clickSave();
  newMilestoneDialog.should("have.text", "Milestone name is required");
});

it("creates a milestone", () => {
  clickNewMilestoneButton();
  newMilestonDialog.getNameField().type("February Milestone");
  newMilestoneDialog.clickSave();
  newMilestoneDialog.should("have.text", "New milestone saved");
});
```

乍一看，上面的测试没有问题。然而，从零开始创建一个新项目涉及设置名称，填写一些起始/结束日期，键入描述，从下拉列表中选择项目所有者，为项目提供相同的标签，填写其他几个字段。我们的测试运行器（我现在使用 Cypress）必须单击所有这些字段，键入一些内容，等待一些建议出现，然后单击，再等待。

或者，将运行时间放在注释里，像这样想象：

```jsx
beforeEach(async () => {
  // 运行10秒
  await createNewProject();
});

it("cannot create milestone without a name", () => {
  // 运行2秒
  clickNewMilestoneButton();
  newMilestoneDialog.clickSave();
  newMilestoneDialog.should("have.text", "Milestone name is required");
});

it("creates a milestone", () => {
  // 运行3秒
  clickNewMilestoneButton();
  newMilestonDialog.getNameField().type("February Milestone");
  newMilestoneDialog.clickSave();
  newMilestoneDialog.should("have.text", "New milestone saved");
});
```

整个测试套件运行 25 秒（2x10 + 2 +3），但我们感兴趣的事情只占了其中的 5 秒（2 + 3）。

那么我们能做得更好吗？因为这两个操作都发生在同一个`newMilestonDialog`中，我们可以认为在填写名称之前，应该首先尝试不带名称的保存。

我们的测试将如下所示：

```jsx
it('creates a milestone', () => {
  // 运行10秒
  await createNewProject();

  // 运行2秒
  clickNewMilestoneButton();
  newMilestoneDialog.clickSave();
  newMilestoneDialog.should('have.text', 'Milestone name is required');

  // 运行3秒
  clickNewMilestoneButton();
  newMilestonDialog.getNameField().type('February Milestone');
  newMilestoneDialog.clickSave();
  newMilestoneDialog.should('have.text', 'New milestone saved');
});

```

现在，整个测试套件只需要 15 秒就能完成。这意味着速度提高了 40%！

我还去掉了 beforeEach。当你在一个 describe 块内只有一个 it 时，它是不必要的心理负担。

我们仍然在测试相同的功能，但我们承认了这样一个事实，即我们最初创建的隔离水平并不值得花费 CI 时间。我们可以用 60% 的 CI 时间来测试错误信息和成功保存，其信心与以前一样。

在我们的真实场景中，像这样的变化在整个应用中严重影响了我们的构建性能。

我们可以让 CI 时间从 11-17 分钟变成 9 分钟以下的构建时间。

我们在有限的 CI 时间内运行这个项目，所以 40% 的速度提升意味着我们可以在相同的预算下为客户多运行 40% 的构建。

### 写在最后

原文地址在这里：[https://akoskm.com/how-to-speed-up-your-integration-tests](https://akoskm.com/how-to-speed-up-your-integration-tests?utm_campaign=Software%2BTesting%2BWeekly&utm_medium=web&utm_source=Software_Testing_Weekly_156)

这篇文章除了开头部分是我写的之外，其他部分来自

- 直接使用 notion AI 把英文翻译成中文
- 使用 DeepL 把英文翻译成中文，再使用 Notion AI 进行改写
- 翻译有些不着边际的地方，我会进行一点点修改

我发现 AI 翻译的效果以及改写的通顺度比我自己翻译的要好的多。

果然，未来已来。
