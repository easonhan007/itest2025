---
weight: 7
title: TDD实战（七）Jacoco 代码覆盖率
date: '2018-01-08T12:35:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1564540574859-0dfb63985953?w=300
tags: []
categories:
- TDD测试驱动开发教程
lightgallery: true
toc:
  auto: false
---



最后一节，和TDD没有直关系，我这里要介绍代码覆盖率工具 Jacoco 。

#### 安装 Jacoco
---
由于整个TDD项目由 Gradle构建，所以在`build.gradle`文件中添加 Jacoco 插件。

```Java
group 'org.tdd.sample'
version '1.0-SNAPSHOT'

apply plugin: 'java'
apply plugin: "jacoco"   //Jacoco 插件

sourceCompatibility = 1.8

repositories {
    mavenCentral()
}

dependencies {
    testCompile group: 'junit', name: 'junit', version: '4.12'
}
```

#### 运行测试
---
切换到TDD 项目目录。执行：

```
TDD > gradle clean test jacocoTestReport

BUILD SUCCESSFUL in 2s
5 actionable tasks: 5 executed
```

#### 测试报告
---
在项目`...\TDD\build\reports\jacoco\test\html`目录下生成`index.html`报告，通过浏览器打开。

![](http://img.testclass.net/tdd_jacoco_report.png)

看到这样一张报告，不知道你是否为对开发的代码码充满了信心。我想这就是 TDD 的魅力。


### 项目代码

Java TDD demo：https://github.com/defnngj/TDD




原始封面

![课程图片](https://images.unsplash.com/photo-1564540574859-0dfb63985953?w=300)

