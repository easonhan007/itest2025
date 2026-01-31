---
weight: 1
title: "如何在openclaw里修改Z智谱的 base url"
date: 2026-01-30T09:02:55+08:00
lastmod: 2026-01-30T09:02:55+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "openclaw的各种配置"
images: []
resources:
  - name: "featured-image"
    src: "2026-01-31-14-41-17.png"

tags: ["openclaw", "clawdbot", "moltbot"]
categories: ["openclaw", "AI", "自动化"]

lightgallery: true

toc:
  auto: false
---

我开始也比较懵，因为默认情况下openclaw调用的是国际版的api，所以国内的同学最好是修改成中国版本的api地址。

<!--more-->

### 手动修改

其实比较简单，直接修改`~/.openclaw/openclaw.json`就可以了。

在`models`里加入下面的配置。

```json
  "models": {
    "providers": {
      "zai": {
        "baseUrl": "https://open.bigmodel.cn/api/paas/v4",
        "apiKey": "zai",
        "api": "openai-completions",
        "models": [
          {
            "id": "glm-4.7",
            "name": "GLM-4.7",
            "reasoning": false,
            "input": [
              "text"
            ],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      }
    }
  },

```

然后再重启gatway。

```
openclaw gateway restart
```

### 自动修改

让openclaw自己改。

![](2026-01-31-14-15-43.png)

### 验证

用下面的命令验证一下是不是流量都过去了。

```
sudo tcpdump -i any -A host open.bigmodel.cn
```
