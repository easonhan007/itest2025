---
weight: 1
title: "在2023使用playwright进行自动化测试"
date: 2024-03-01T02:04:39+08:00
lastmod: 2024-03-01T02:04:39+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "playwright一直是我最看好的新一代自动化测试框架"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/1/macbook-air-iphone-moleskin.jpg?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

playwright 一直是我最看好的新一代自动化测试框架，2022 年底 playwright 在 npm 上的下载量超过了 100 万，尽管不如 selenium 和 cypress，不过势头还是相当强劲的。最近正好发现一篇文章简单的介绍了使用 typescript，pageobject 和 fixture 配合 playwright 进行用例编写的文章，这里把里面的精华拿出来分享一下。

## 老生常谈，playwright 的优势

- 有个好爹，微软出品，看好长期更新维护和迭代，但也可能突然被砍掉，毕竟大公司都在裁员
- 运行速度快
- 自动等待元素出现
- 报告的呈现很多元化，可以设置重试机制，捕获执行日志，截屏录屏等
- 支持多个浏览器并行执行
- 提供自动生成代码能力以及 Inspector GUI
- 一套代码，跨浏览器执行的能力

## 目录结构

框架整体的目录结构如下。

```java
.
├── config
│   ├── global-setup.ts
│   └── playwright.config.ts
├── package-lock.json
├── package.json
└── src
    ├── data
    │   └── data.json
    ├── fixtures
    │   ├── AxeFixture.ts
    │   └── TodoFixture.ts
    ├── pages
    │   └── TodoPage.ts
    └── tests
        ├── a11y.spec.ts
        └── demo-pom-todo-app.spec.ts
```

### config 目录

- **_playwright.config.ts_** playwright 的配置文件
- **\*\***global-setup.ts**\*\*** 在所有用例执行前运行一次，主要的目的是登录一次被测系统并保存浏览器的全局状态到 storageState.json 文件中。这样就不需要每个用例都去单独登录一次了。更多信息可以参考文档。[https://playwright.dev/docs/test-advanced#global-setup-and-teardown](https://playwright.dev/docs/test-advanced#global-setup-and-teardown)

### Page Object

po 基本上是自建框架的必选项了。具体的实现如下

```tsx
import { expect, Locator, Page } from '@playwright/test';

export class TodoDemoPage {
  readonly page: Page;
  readonly newTodoInput: Locator;
  readonly todoTitle: Locator;
  readonly todoCount: Locator

  constructor(page: Page) {
    this.page = page;
    this.newTodoInput = page.getByPlaceholder('What needs to be done?');
    this.todoTitle = page.getByTestId('todo-title');
    this.todoCount = page.getByTestId('todo-count');
  }

  async goto() {
    await this.page.goto('https://demo.playwright.dev/todomvc');
  }

  async addTodo(data: string) {
    await this.newTodoInput.fill(data)
    await this.newTodoInput.press("Enter")
  }

  async addDefaultTodos(todosItems: string[]) {
    for (const todo of todosItems) {
      await this.addTodo(todo)
    }
  }
...
}
```

关于 po 需要注意几点

- 命名规则，确保页面上的元素和一些页面方法都有合适的名称
- 一个方法只做一件事情，而且可以通过方法名推测出来
- 对页面呈现的一些结果进行断言
- dry，don’t repeat yourself

### **Fixtures**

fixture 可以简单理解为准备数据，设置上下文环境

```tsx
import { test as base } from "@playwright/test";
import { TodoDemoPage } from "../pages/TodoPage";

type MyFixtures = {
  todoDemoPage: TodoDemoPage;
  noneExistingPage: any;
};

export const todoDemoPage = async ({ page }, use) => {
  const todoDemoPage = new TodoDemoPage(page);
  // Set up the fixture.
  await todoDemoPage.goto();
  // Use the fixture value in the test.
  await use(todoDemoPage);
};

// we can create as many fixtures as we want, but I prefer to store them in separate files
export const noneExistingPage = async ({ page }, use) => {
  // Let's imagine we have another fixter-page set up here
};

export const test = base.extend<MyFixtures>({ todoDemoPage, noneExistingPage });
```

上面的代码其实就是创建了 TotoDemoPage，后面用例里就可以直接使用这个页面了。

fixture 的好处还是很多的。

- fixture 让 setup 和 teardown 钩子函数在同一个地方进行定义，这样就比较好维护了
- fixture 可以重复使用
- fixture 按需使用，定义了你也可以不用
- fixture 可以组合使用

### 测试用例

用例相对就比较简单的，因为难的部分已经搞完了。

```tsx
import { test } from "../fixtures/TodoFixture";

const TODO_ITEMS = [
  "buy some cheese",
  "buy bottle of wine, or two",
  "celebrate",
];

// our test is imported from fixtures folder
// so we can have access to tododDempPage and noneExistingPage objects
// in callback function trhough destructuring and we can use it for our needs
test.describe("New Todo", () => {
  test("should allow me to add todo items", async ({ todoDemoPage }) => {
    await todoDemoPage.addTodo(TODO_ITEMS[0]);
    await todoDemoPage.checkInputIsEmpty();
    await todoDemoPage.addTodo(TODO_ITEMS[1]);
    await todoDemoPage.checkAddedTodos([TODO_ITEMS[0], TODO_ITEMS[1]]);
    await todoDemoPage.checkNumberOfTodosInLocalStorage(2);
  });

  test("should clear text input field when an item is added", async ({
    todoDemoPage,
  }) => {
    await todoDemoPage.addTodo(TODO_ITEMS[0]);
    await todoDemoPage.checkInputIsEmpty();
    await todoDemoPage.checkNumberOfTodosInLocalStorage(1);
  });

  test("should append new items to the bottom of the list", async ({
    todoDemoPage,
  }) => {
    await todoDemoPage.addDefaultTodos(TODO_ITEMS);
    await todoDemoPage.checkDefaultAddedTodods(TODO_ITEMS);
    await todoDemoPage.checkAddedTodos(TODO_ITEMS);
    await todoDemoPage.checkNumberOfTodosInLocalStorage(3);
  });
});
```

用例很简洁易懂对吧。这里断言都封装在了 page object 里，所以整个流程全是对 po 实例进行调用，很统一，不过我不是很喜欢这种方式，我更喜欢把原生断言放在用例里，这样 po 层会更简洁一些，要不需要绞尽脑汁去给封装断言的方法取名。

### CICD

可以在官方文档找到方法。[https://playwright.dev/docs/ci](https://playwright.dev/docs/ci)

### 总结

[https://github.com/eugeniuszG/playwright-starter](https://github.com/eugeniuszG/playwright-starter) 这里有框架模板，大家可以下载下来进行二次开发，最后感谢作者的总结和示例。
