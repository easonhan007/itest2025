---
weight: 1
title: "不要再使用了mock了"
date: 2024-03-08T09:03:23+08:00
lastmod: 2024-03-08T09:03:23+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "mock确实有问题"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1573066283872-f8d863884fac?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

最近看到一篇关于 mock 的文章，觉得挺有道理的，，简单总结分享一下，原文在这里：[https://levelup.gitconnected.com/why-mocks-are-considered-harmful-b4e8fe60478d](https://levelup.gitconnected.com/why-mocks-are-considered-harmful-b4e8fe60478d)。 文章的观点很简单，就是 mock 其实是弊大于利的。

自动化测试涉及到很多技术，其中 mock 技术我们应该尽量避免使用。mock 用的好其实也只是锦上添花，用的不好的话则会给你带来一些过度的自信。

首先看下什么是 mock。mock 其实就是模拟代码中的一些外部访问行为，比如访问第三方的付款 api 或者是对数据库进行访问，这会给单元测试带来一些好处

- 运行加速，因为你不需要访问额外的服务；
- 提升稳定性，第三方服务提供商的一些不稳定因素被规避掉了

不过 mock 是为一些具有副作用的代码服务的，也就是说这些代码其实是依赖于外部服务，并不是依赖于各种参数的输入。我们可以把函数分成两类

- 纯粹的函数：没有外部依赖的函数
- 不纯粹的函数：有外部依赖的函数

### mock 带来的问题

**mock 不等同于其替换掉的服务。**

比如你把代码中数据库访问的部分给 mock 掉了，这意味着你的代码可能会在有 mock 的时候工作良好，然而你还是需要进行集成测试以确保在没有 mock 的时候也可以正常工作。

**不可能进行特性平替**

如果你使用的是简单的 mock 方式，那么 mock 可能不会返回一些有用的数据，你花在 mock 上的时间越多，mock 返回的 data 可能会约实用。然而 mock 不能平替被 mock 系统的方方面面。

**开发了 mock 但不使用其实就是浪费时间**

如果你开发了数据库的 mock 但从不使用的话，这就是浪费时间了。在现实世界中这是很有可能发生的，因为代码可能需要获取一些真实配置去做初始化，而 mock 的时候却很难满足这一条件。

### 如何去找到 mock 的替代方案

很简单，就是重构代码，把代码重构成纯粹的函数和不纯粹的函数两种，纯粹的函数是不需要 mock 就可以测试的，，不纯粹的函数则可以通过集成测试来进行验证。

举个例子

```python
def logic():
    x = addition(1, 3)
    y = multiplication(2, 4)
		z = x + y
		database_write(z)
    return
```

上面的函数就是不纯粹的函数，因为其访问了 db，然而我们还是可以把这个函数重构成 1 个纯粹函数和另一个不纯粹的函数

```python
def calc(a, b, c, d):
		x = addition(a,b)
		y = multiplication(c,d)
		return x + y

def logic():
		z = calc(1, 5, 2, 4)
		database_write(z)
		return
```

这样 calc 函数可以用单元测试覆盖了，而 logic 则留给集成测试去考虑吧。

最后尽可能的优化你的自动测试方案，让更多的代码都通过自动化进行覆盖。

### 总结

mock 短期来看可能是一种解决问题的方式，然而长期看来确是一个麻烦的问题。如果你想快速交付软件产品的话，那么你应该少花时间在 mock 上，多花点时间在重构和自动化测试上面。
