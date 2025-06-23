---
weight: 1
title: "Selenium 4.9.0 发布"
date: 2024-03-08T09:02:22+08:00
lastmod: 2024-03-08T09:02:22+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "api稳定才是第一生产力"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1651403984845-03c9c2d1ecb9?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

我们非常高兴地宣布支持 Java、.NET、Ruby、Python 和 Javascript 及 Grid 和 Internet Explorer Driver 的 Selenium 4.9.0 版本发布。所有内容的链接可以在我们的下载页面找到。

### 重点如下:

- Chrome DevTools 支持现在是:v110、v111 和 v112(Firefox 仍然对所有版本使用 v85)
- Java 绑定的 Maven BOM。
- 通过 Selenium Grid 现在可以远程下载文件。
- 首先， Firefox 开始逐步废除 CDP，并用双向实现 (BiDi implementation) 替代它。
- InvalidSelectorException 现在继承自 WebDriverException 而不是 NoSuchElementException。
- 发布了 Selenium Manager, 这个工具可以使用浏览器选项中设置的信息来获取正确的浏览器 driver。
- 在 Selenium Grid 中可以设置子路径,以获得自定义的 Grid URL。
- 在 Java 版本和 Grid 中完全移除 Json Wire Protocol 支持。
