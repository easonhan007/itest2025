---
weight: 1
title: "我把这个最好的test wiki全部翻译了一遍 💪"
date: 2024-03-30T03:46:30+08:00
lastmod: 2024-03-30T03:46:30+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "全程自动化"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1580835239846-5bb9ce03c8c3?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

之前给大家分享过这个测试 wiki，[https://ray.run/wiki](https://ray.run/wiki)

个人觉得还是非常全面好用的，不过因为是英文的，而且里面的内容不够直观，所以我直接翻译了一遍。最后的效果看[这里](/wiki)，一共翻译了 224 个主题，好在是全程自动化，效率还是比较可观的。

### 具体做法

首先我写了个爬虫把所有的英文内容都爬了下来，这一步不难，毕竟熟练工，三下五除二就搞定了。然后就是调用[openai](https://openai.com/blog/openai-api)或者是[gemini 的 api](https://ai.google.dev)做全文翻译，但是前者太贵，后者封我号，没办法，只能去打[deepl](https://www.deepl.com/en/translator)的主意。

不过 deeplx 的翻译接口经常触发限频，没办法了只能另辟蹊径。

无奈之下只能在本地部署了个[百川 2 7b](https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat-4bits)模型，调用百川 2 的 api 进行翻译，当然了，翻译时候尝试了很多策略，浪费了大量时间，最终才出来一个相对可用的版本。过程中发现了一些问题

- 有时候显存不足导致翻译结果为空
- 如果 baichuan2 翻译不了，那么它会直接返回原文，就会出现中英文混杂的情况

不过简单来说，翻译的结果凑合可用，而且我在 wiki 的详情页也给出了英文原文，也方便大家对照。

爬虫和翻译完成之后就是在 itest 上加个 wiki 模块，把爬下的内容导入到数据库之后，调整一下样式就可以上线了。

总的来说翻译很麻烦，毕竟 openai 和 gemini 的 api 都对我关上了大门，不过好在中文模型可以一战，这才做成了这个勉强可用的版本。

### 未来计划

- 有精力的话完善一下翻译
- 增加 wiki 搜索功能
