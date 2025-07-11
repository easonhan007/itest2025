---
weight: 1
title: "单元测试用例该如何设计"
date: 2024-03-08T09:04:38+08:00
lastmod: 2024-03-08T09:04:38+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "看看简单的单元测试用例究竟该如何设计"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/1/type-away.jpg?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

最近一些大公司在进行去测试化的操作，这一切的根源大概可以从几年前微软一刀切砍掉所有内部正式的测试人员开始说起，当时微软内部的测试工程师有一部分转职成了开发工程师，他们的职能中有很大一部分的职责是教会普通开发人员如何进行测试。我们都知道开发人员进行的测试一般以单元测试为主，假如有一天你所在的组织需要你转变成一名测试方面的教练，除了自动化测试之外还需要去推广单元测试，那么你该如何去定义单元测试用例的设计方法论呢？这里给大家一些思路，看看简单的单元测试用例究竟该如何设计。

一个方法可以有任意数量的有效测试用例；它最终取决于方法的结构。有两种简单的方式可以帮助我们设计单元测试用例。

- 参数方法
- 执行路径方法

我将通过提供真实的代码来进行演示。所有代码片段都将用 C# 编写，断言将使用我最喜欢的单元测试包 Fluent Assertions。

我们将为以下方法提供测试用例：

```csharp
public static bool ContainsNamelessItems(this List<Item> items)
{
  return items.Any(item => item.Name.IsNullOrEmpty())
}
```

此方法将项目集合作为参数。它遍历项目列表，并针对每个项目`Item`检查其 name 属性是否为空。如果 name 存在且不为空，我们返回`True`，否则我们返回`False`。

### **使用参数方法创建测试用例**

这种方式主要考虑的是入参可以传递哪些值。

查看该方法的参数 ContainsNamelessItems，我们有一个 List<Item>名为 items. 此参数可能有几个可能的值：

- items 是空的
- items 至少包含 1 个 Item 具有 Name 未定义的属性
- items 不包含具有未定义 Name 属性的项目
- items 是 null

这些可能的值中的每一个都可以作为单独的用例存在。

以下是一些可能的测试用例和断言：

1，当`List<Item>`为空时，我们期望返回值是`False`因为其的`List<Item>`无 name 属性。

```csharp
public void WhenItemsIsEmpty_ReturnFalse()
{
  var items = new List<Item>();

  var result = items.ContainsNamelessItems();

  result.Should()
    .BeFalse("because an empty collection cannot contain nameless items");
}
```

2，当`List<Item>`包含至少 1 项没有 name 属性的`Item`时，我们期望返回值是`True`

```csharp
public void WhenItemsContainsANamelessItem_ReturnTrue()
{
  var items = new List<Item>
  {
    { new Item { Name = "Item1" },
    { new Item { Name = string.Empty } // nameless item
  };

  var result = items.ContainsNamelessItems();

  result.Should()
    .BeTrue("because there is a nameless item in the collection");
}
```

3，当`List<Item>`不包含任何没有 name 属性的项目时，我们期望返回值是`False`，因为所有项目都有 name。

```csharp
public void WhenItemsDoesNotContainANamelessItem_ReturnFalse()
{
  var items = new List<Item>
  {
    { new Item { Name = "Item1" },
    { new Item { Name = "Item2" }
  };

  var result = items.ContainsNamelessItems();

  result.Should()
    .BeFalse("because there are no nameless items in the collection");
}
```

4，当`List<Item>`is `null`的时候，我们期望抛出`ArgumentNullException`异常，这往往是最难想到的。

```csharp
public void WhenItemsIsNull_ThrowArgumentException()
{
  List<Item> items = null;

  Action act = () => items.ContainsNamelessItems();

  act.Should()
    .Throw<ArgumentNullException>("because the collection is null");
}
```

### **使用执行路径方法创建测试用例**

路径方式需要遍历被测方法并找到所有不同的执行路径。

我们上面定义的方法只有一条执行路径，因为除了直接到达方法的末尾之外，没有任何条件驱动路径。要改变路径，我们就需要引入某种条件，可以通过 if...else、 switch 以及 try/catch 语句。在这些条件块中，方法可能会在达到某个条件的情况下直接退出，而不是运行到方法的最后一行。

下面我们就引入条件。假设我们不希望方法在入参为空时候抛出 ArgumentNullException 异常，而是想抛出一个我们自定义的 ArgumentException 异常。那么我们必须向检查项目列表是否为空的方法添加一个条件。

流程图如下：

![Untitled](%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%E8%AF%A5%E5%A6%82%E4%BD%95%E8%AE%BE%E8%AE%A1%20dc486bcdbe0746d988f477636b84de79/Untitled.png)

现在，如果项目为空，则有可能提前退出，而不是走到方法的末尾，具体实现如下

```csharp
public static bool ContainsNamelessItems(List<Item> items)
{
  if (items == null)
    throw new ArgumentException("The collection of items should not be null.");

  return items.Any(item => item.Name.IsNullOrEmpty())
}
```

这个测试用例的相应测试看起来像这样：

```csharp
public void WhenItemCollectionIsNull_ThrowArgumentException()
{
  List<Item> items = null;

  Action act = () => items.ContainsNamelessItems();

  act.Should().Throw<ArgumentException>()
    .WithMessage("The collection of items should not be null.");
}
```

### 总结

- 在入参的时候可以用等价类的方式构造任意参数，强类型语言里无效类用的会相对少一些，毕竟编译器会进行校验；而弱类型语言里无效类比较隐蔽，是测试的重点；
- 执行路径方法其实就是分支覆盖，通过不通的输入参数去覆盖所有分支，比如同样是有效类的输入情况下，空集合和非空集合可能会走到不通的路径；
- 在方法或函数特别复杂的情况下，可以试着去把方法拆小，从而获得更好的可测试性；
