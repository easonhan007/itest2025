---
weight: 1
title: "基于k8s的测试执行工具：TestKube"
date: 2024-03-08T09:02:52+08:00
lastmod: 2024-03-08T09:02:52+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "值得试一试"
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

之前我们自己开发过一些基于 k8s 的执行用例执行工具，原理大致是在用例执行的时候动态去 k8s 上创建容器，执行任务，上报指标，最后销毁容器，不过这些过程基本上与测试过程耦合在一起，难以平移扩展。最近发现了一款在开发早期的通用型的基于 k8s 的用例执行工具: TestKub。

### 有用的链接

- 项目主页：[TestKube (kubeshop.github.io)](https://kubeshop.github.io/testkube/)
- 代码库：[GitHub - kubeshop/testkube: Kubernetes-native framework for test definition and execution](https://github.com/kubeshop/testkube/)

### 特性

- 支持执行 postman collection
- 支持执行 cypress 的 ui 测试用例
- 支持执行基于 curl 的简单探活，比如站点，接口有没有挂的检测之类

### 工具希望解决的实际问题

- 避免 vender 锁定 CI/CD 管道中的测试编排和执行
- 在集群中轻松编排和运行任何类型的测试 - 功能、负载/性能、安全性、合规性等 - 无需将它们打包成在 docker-images 或提供网络访问
- 使测试执行与构建过程分离成为可能； 工程师应该能够在需要时运行特定的测试
- 以一致的格式集中所有测试结果，以实现“可操作的 QA 分析”
- 提供模块化架构以添加新类型的测试脚本和执行器

简单来说就是提供了与 ci/cd 解耦的纯测试容器编排和执行能力，并提供了统一的报告输出。

### 主要模块

- kubectl 插件
- API Server - 调度器，执行器，收集执行结果
- CRDs Operator - 观看 TestKube CR，处理与 API Server 通信的更改
- Executors - 运行为特定运行程序定义的测试，目前可用于 Postman、Cypress 和 Curl
- 结果数据库 - 用于集中测试结果管理
- 一个简单的基于浏览器的看板，用于监控测试结果

### 总结

这里就不列举如何安装以及简单使用该工具进行用例执行了，目前 TestKube 的版本是 0.6，还处在早起的开发阶段，不过项目的文档较为全面，而且模块化良好，有一定的扩展性，所以后面可能吸引一些使用者，有强烈需求的同学可以直接拿来就用，拿不定主意的同学建议再观察一定时间，等到 1.0 版本再入坑。
