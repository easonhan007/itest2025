---
weight: 1
title: "Selenium Manager可以用起来了"
date: 2024-03-08T09:04:37+08:00
lastmod: 2024-03-08T09:04:37+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "推荐大家使用"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/1/work-station-straight-on-view.jpg?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

前几天随手写了几个 headless 的 selenium 爬虫脚本，运行的时候发现本地的 chromedriver 竟然不需要更新，一时间有点没反应过来，毕竟 selenium 有个痛点就是**chrome 浏览器自动升级之后需要下载新的 chromedrier**， 否则之前的脚本将会报错。当然了，之前也有一些规避的方式，比如

- 关掉 chrome 的自动升级
- 用 firefox，毕竟[geckodriver 一年也就更新个 2-3 个版本](https://github.com/mozilla/geckodriver/releases)
- 用第三方的 driver 管理工具，比如 python 有个[webdriver-manager](https://pypi.org/project/webdriver-manager/)

这些方法其实都挺好，都能解决核心问题，特别是 python 的 webdriver-manager，几行代码就可以保持 driver 永远自动更新，举个例子

```python
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
```

这次不用更新 driver 是因为使用了官方推出的[selenium manager](https://www.selenium.dev/documentation/selenium_manager/)，之前没留意，不过真到用的时候发现还是比较方便的。对我来说 selenium manager 最方便的就是初始化环境的功能，比如

- 自动安装浏览器
- 自动安装 driver
- 支持多架构多系统
- 可以配置代理，这点很重要
- 自动管理浏览器和 driver，其实就是把浏览器和 driver 放在了系统 PATH 里

如果我有一个脚本需要在 windows 和 macos 的最新版本 chrome 上跑，那么环境初始化就非常容易了，只需要下面的命令

```
selenium-manager --browser chrome
selenium-manager --driver chromedriver
```

selenium manager 会自动探测机器架构和系统，然后下载 chrome 浏览器和 driver，如果遇到下载不畅的情况，直接设置一下代理就可以了。

### 下载

selenium manager 让人一头雾水的地方是安装方法，其实 selenium manager 是不需要安装的，直接下载就好。
selenium manager 是用 rust 写的命令行应用(rust 现在势头很盛，比如 cloudflare 就用 rust 写了个 nginx 的平替 Pingora)，目前的下载方式还是直接下载二进制文件，下载地址是:https://github.com/SeleniumHQ/selenium_manager_artifacts/releases。该项目更新非常频繁，大家下最新的版本就好。

### 保持 driver 自动更新

思路很简单，如果是非 windows 机器的话可以使用 crontab。

```
0 5 * * * selenium-manager --driver chromedriver
```

### 总结

之前写过文章去介绍 selenium manager 的具体用法，大家有兴趣可以往回翻一下。这篇文章主要是感慨一下 selenium manager 给日常工作带来的便利。之前经常遇到的一段时间过后 selenium 代码执行报错的问题目前是有了工程化的解决方案了，推荐大家使用。
