---
weight: 1
title: "放弃postman？一个月4k star？接口测试工具hoppscotch评测"
date: 2024-03-08T09:04:03+08:00
lastmod: 2024-03-08T09:04:03+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "天下苦postman久矣！"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

天下苦 postman 久矣！

记得当初 potman 刚横空出世时，其形态只是一个浏览器扩展而已，尽管功能简单，不过却带来了另一个非常大的优势，那就是软件体积非常小，安装到浏览器上以后可以借助于浏览器同步的功能，实现各种跨平台支持，特别是对我我这种拥有 win/mac/iinux 的人来说，方便快捷是第一位的。

后来 postman 推出了独立的桌面版本，功能逐渐迭代，性能差的慢慢变态，现在劝退我的是两点：启动速度慢和我用不到的功能慢慢变多；当然除了这两点外还有个相当大的槽点是：postman 会想方设法让你登录，如果你不小心使用了同步功能的话，你的测试文件会公开分享到 postman 上供人品评，这是一个巨大的安全隐患。

D 轮融了 2.25 亿美金，postman 注定要在商业化的道路上越走越远，注定会增加很多我不需要的功能，各种同步，花式协作，满屏的效率提升，不厌其烦的提示我升级等等，对我来说其实需求很简单，只要可以让我朴素的调试接口就可以了。

于是各种 postman 的替代工具应运而生，比如 postwoman，insomnia 等等，这种工具的技术栈都差不多，都是用 js 开发的类似于原生客户端的跨平台工具，今天给大家带来的是一款很火的开源 postman 替代工具: hoppscotch，这个工具在 github 上目前有 40,000 的 star，3 月份新增 4000 的 star，应该是目前最火的测试工具了。

### 安装

hoppscotch 只需要安装一个浏览器扩展就可以了，支持 chrome 和 firefox。比 postman 动则上百兆的安装包来说，安装过程简单了不少。

安装好扩展之后访问[https://hoppscotch.io/](https://hoppscotch.io/)就可以使用了。

### UI

hoppscotch 的界面跟 postman 差不多，会用 postman 的同学应该会感到比较亲切。

### 功能

功能上 hoppscotch 也跟 postman 不相上下

- 支持 rest api 调试
- 支持 GraphQL 语法
- 支持 websocket 和 socket.io
- 支持从 collection 生成文档，这个我不会用
- 支持 collection 的创建及导出
- 支持多种 Authorization 方式
- 支持 pre-request script
- 支持断言，跟 postman 的写法不能说很像，只能说是一摸一样
- 完善的快捷键支持
- 支持 pwa，轻量化的网页解决方案，让网页应用的体验跟 desktop 一样，再也不用忍受 postman 的龟速启动了
- 支持 proxy，支持自建 proxy
- 个性化定制：白天模式和暗夜模式，各种颜色主题，可以调整字体大小
- 支持 cli，这个真是没想到，看了一眼是 go 写的，功能有限，不过可以在命令行运行 collection 了，不过似乎不支持 websocket
- 完全开源，前端应该是 vue 写的，有开发能力的同学可以进行定制

### 部署

我们可以在远程服务器上部署个 hoppscotch 版本，然后远程进行访问。不过用 docker 部署的话似乎有点问题，就是浏览器插件无法识别的问题，于是就需要部署个 proxy 用来转发请求，这样就会出现本地 localhost 无法解析的问题，所以如果不是必须的话，用 pwa 的版本体验上就已经很好了。

### 总结

总的来说 hoppscotch 是可以替代 postman 的，这里推荐大家去试一试。另外 hoppscotch 也可以登录上传 workspace，我也试过也不想试，还是那句话，能不登录就不登录，如果遇到需要协作进行 collecton 的场景，可以试着用 git 去管理。
