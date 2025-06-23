---
weight: 1
title: "chrome上更好的录制回放工具？Jesteer介绍及试用"
date: 2024-03-08T09:04:20+08:00
lastmod: 2024-03-08T09:04:20+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "一款最新的的录制回放工具"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1553524913-efba3f0b533e?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

之前跟大家分享后 chrome 上原生的录制回放功能，今天看到了一款最新的的录制回放工具 jesteer，于是第一时间来了解和试用一下。

### 主要功能

- 不用写代码，直接可以录制和回放
- 可以录制基本的页面交互
- 自动创建基于 Puppeteer 的脚本
- 回放时的快照检查功能
- 简单舒适的 web ui

### 安装

jesteer 是一款 chrome 插件，直接去 chrome 商店里所有 jesteer 点击安装既可。

### 界面

jesterr 的界面很简单，就 3 个按钮

- Record：开始录制
- Take a snapshot：dom 高亮
- Copy to clipboard

### 简单上手使用

- 点击 Record 开始录制
- 录制过程中点击 Take a snapshot 进行断言
- 点击 Stop Recording 停止录制
- 点击 Copy to clipboard 拷贝生成的代码到剪切板

这几步还是非常简单的，后来我遇到了一个问题，怎么进行用例的回放呢？之前 chrome 自带的 Recorder 是可以录制完成后直接回放的，而 jesteer 则找不到回放按钮。折腾一小会后我终于找到了答案。

### 把生成的代码粘贴到测试项目中

为了可以运行生成的代码，我决定新建一个 nodejs 项目来进行尝试。

```jsx
mkdir jesteer_example
cd jesteer_example
npm init
npm install --save-dev jest
npm install --save-dev puppteer
touch example.test.js

```

修改 package.json

```jsx
{
  "scripts": {
    "test": "jest"
  }
}
```

我打开一个空白页，然后输入www.itest.info，跳转到搜索页面后，添加一个snapshot断言，最后结束录制。下面是录制出来的脚本。

```jsx
/* 
This test suite was created using JESTEER, a project developed by 
Tim Ruszala, Katie Janzen, Clare Cerullo, and Charissa Ramirez.

Learn more at https://github.com/oslabs-beta/Jesteer .
*/
const puppeteer = require("puppeteer"); // v13.0.0 or later

jest.setTimeout(10000);
describe("", () => {
  let browser, page, timeout;

  beforeAll(async () => {
    browser = await puppeteer.launch({
      headless: true,
    });
  });

  beforeEach(async () => {
    page = await browser.newPage();
    timeout = 5000;
    page.setDefaultTimeout(timeout);
  });

  afterEach(async () => {
    await page.close();
  });

  afterAll(async () => {
    await browser.close();
  });

  it("", async () => {
    {
      const promises = [];
      promises.push(page.waitForNavigation());
      await page.goto("chrome://newtab/");
      await Promise.all(promises);
    }

    await page.waitForNavigation();

    await page.keyboard.type("itest.info");

    await page.keyboard.press("Enter");

    {
      const element = await page.waitForSelector("#su");
      await element.click();
    }

    {
      const element = await page.waitForSelector("HTML > BODY:nth-child(2)");
      await element.click();
    }

    await page.waitForNavigation();

    {
      const snapped = await page.$eval(
        "#1 > DIV:nth-child(1) > DIV:nth-child(1) > H3:nth-child(1) > A:nth-child(1)",
        (el) => el.innerHTML
      );
      expect(snapped).toMatchSnapshot();
    }
  });
});
```

使用 npm run test 命令来运行，不出意外运行失败。

```jsx
FAIL  ./sum.test.js
    ✕  (297 ms)

  ●  ›

    net::ERR_INVALID_URL at chrome://newtab/

      37 | const promises = [];
      38 | promises.push(page.waitForNavigation());
    > 39 | await page.goto('chrome://newtab/');
         | ^
      40 | await Promise.all(promises);
      41 | }
      42 |

      at navigate (node_modules/puppeteer/src/common/FrameManager.ts:226:13)
      at FrameManager.navigateFrame (node_modules/puppeteer/src/common/FrameManager.ts:198:17)
      at Frame.goto (node_modules/puppeteer/src/common/FrameManager.ts:792:12)
      at Page.goto (node_modules/puppeteer/src/common/Page.ts:1781:12)
      at Object.<anonymous> (sum.test.js:39:1)
```

查了一下代码，应该是打开 chrome 的新 tab 页面之后自动等待的代码报错导致。

### 初步结论

初步结论现在应该有了，jesteer 录制出来的代码其实没办法自动识别上下文，也就是说如果在地址栏上输入 url 并按回车键打开一个新页面，我们期望的结果是直接录制成 goto url，但是 jesteer 只能忠实的还原我们的操作，而这些操作有可能导致回放失败。

### 总结

先说优点

- jesteer 作为一款纯录制工具，其提供的 snapshot 比对功能还是非常强大的，等于是支持了在录制时候直接录制断言的能力；
- jesteer 可以录制用户的一系列简单交互，对于一些页面来说还是很管用的；
- 根据 jesteer 的文档描述，jesteer 比 chrome 原生的 recorder 录制准确性更高；
- jesteer 录制出的脚本集成了 jest 框架，等于可以直接录制用例，而不是一系列的操作，省去了把脚本加工成用例的过程；

再说不足

- jesteer 需要用户对 nodejs 有一定的了解，不能直接录制完就一键回放；
- jesteer 录制出的脚本需要进行一些加工，比如上文可以感知到的修改 goto 的语句的工作；
- jesteer 帮助文档比较简单，想上手用起来需要发挥一点点的想象力

### 最后

对于一些简单的操作和场景，且不介意使用 jest 作为测试框架的话，jesteer 还是比较推荐的，可以极大的提升生产力；其他情况下就不推荐了。
