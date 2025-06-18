---
weight: 0
title: puppeteer:官方出品的chrome浏览器自动化测试工具
date: '2018-07-26T07:54:13+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1503435980610-a51f3ddfee50?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



puppeteer发布应该有一段时间了，这两天正好基于该工具写了一些自动化解决方案，在这里抛砖引给大家介绍一下。

官方描述：

> Puppeteer is a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol. Puppeteer runs headless by default, but can be configured to run full (non-headless) Chrome or Chromium.

简单来说，puppeteer的特点如下

* 是node的库
* 基于DevTools Protocol协议
* 默认是无界面模式运行

### 安装

```
npm i puppeteer
# or "yarn add puppeteer"
```

### 基本使用方式

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```

上面代码的作用是打开一个页面，然后给这个页面截图，最后关闭浏览器。

### 想象空间

* 可以做一些界面的自动化工作
* 可以做爬虫
* 可以在服务器上稳定运行，方便容器化

### 更多例子

将页面保存成pdf的例子

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://news.ycombinator.com', {waitUntil: 'networkidle2'});
  await page.pdf({path: 'hn.pdf', format: 'A4'});

  await browser.close();
})();
```

在页面上下文执行js的例子

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Get the "viewport" of the page, as reported by the page.
  const dimensions = await page.evaluate(() => {
    return {
      width: document.documentElement.clientWidth,
      height: document.documentElement.clientHeight,
      deviceScaleFactor: window.devicePixelRatio
    };
  });

  console.log('Dimensions:', dimensions);

  await browser.close();
})();
```

在亚马逊搜索商品的例子

```javascript
/**
 * @name Amazon search
 *
 * @desc Looks for a "nyan cat pullover" on amazon.com, goes two page two clicks the third one.
 */
const puppeteer = require('puppeteer')
const screenshot = 'amazon_nyan_cat_pullover.png'
try {
  (async () => {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.setViewport({ width: 1280, height: 800 })
    await page.goto('https://www.amazon.com')
    await page.type('#twotabsearchtextbox', 'nyan cat pullover')
    await page.click('input.nav-input')
    await page.waitForSelector('#resultsCol')
    await page.screenshot({path: 'amazon_nyan_cat_pullovers_list.png'})
    await page.click('#pagnNextString')
    await page.waitForSelector('#resultsCol')
    const pullovers = await page.$$('a.a-link-normal.a-text-normal')
    await pullovers[2].click()
    await page.waitForSelector('#ppd')
    await page.screenshot({path: screenshot})
    await browser.close()
    console.log('See screenshot: ' + screenshot)
  })()
} catch (err) {
  console.error(err)
}

```

登陆github的例子

```javascript
/**
 * @name Github
 *
 * @desc Logs into Github. Provide your username and password as environment variables when running the script, i.e:
 * `GITHUB_USER=myuser GITHUB_PWD=mypassword node github.js`
 *
 */
const puppeteer = require('puppeteer')
const screenshot = 'github.png';
(async () => {
  const browser = await puppeteer.launch({headless: true})
  const page = await browser.newPage()
  await page.goto('https://github.com/login')
  await page.type('#login_field', process.env.GITHUB_USER)
  await page.type('#password', process.env.GITHUB_PWD)
  await page.click('[name="commit"]')
  await page.waitForNavigation()
  await page.screenshot({ path: screenshot })
  browser.close()
  console.log('See screenshot: ' + screenshot)
})()
```

### 常见问题

**谁在维护puppeteer?**

Chrome DevTools 团队

**Puppeteer可以替换selenium/webdriver吗?**

不可以。这2个工具的目的是不一样的。

selenium的目的是一套脚本运行在不同浏览器上，可以做兼容性测试;

puppeteer专注于Chromium的功能测试。

### 相关资料

* [项目主页](https://github.com/GoogleChrome/puppeteer)
* [api文档](https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md)




原始封面

![课程图片](https://images.unsplash.com/photo-1503435980610-a51f3ddfee50?w=300)

