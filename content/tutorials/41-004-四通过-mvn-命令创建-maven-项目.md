---
weight: 4
title: （四）通过 mvn 命令创建 Maven 项目
date: '2017-11-25T12:40:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1531815288026-1946892d24df?w=300
tags: []
categories:
- maven简明教程
lightgallery: true
toc:
  auto: false
---



#### 通过 mvn 命令创建项目
---
Maven官方文档：[Maven Getting Started Guide](https://maven.apache.org/guides/getting-started/)

通过 mvn 命令创建一个 Maven 项目。

```
mvn -B archetype:generate \
  -DarchetypeGroupId=org.apache.maven.archetypes \
  -DgroupId=com.mycompany.app \
  -DartifactId=my-app
```

* -B ：该参数表示让Maven使用批处理模式构建项目，能够避免一些需要人工参与交互而造成的挂起状态。

* archetype:generate : 创建 Maven 项目的命令。

* DarchetypeGroupId ： 指定 Apache maven 组织名。

* DgroupId ： 指定项目或公司组名。

* DartifactId ：指定项目名。

例如：

> mvn -B archetype:generate -DgroupId=com.myapp.pro -DartifactId=myapp -DarchetypeArtifactId==maven-archetype-quickstart -DinteractiveMode=false

将，该命令复制到 Windows 命令提示符（Linux 终端）下执行。

![](http://img.testclass.net/maven_create_project.png)

继续通过`mvn idea:idea`命令生成 IntelliJ IDEA 项目工程。

```
> cd myapp\

..\myapp> mvn idea:idea

```

然后，通过 [IntelliJ-IDEA](/idea/) 打开 __myapp__ 项目。

![](http://img.testclass.net/maven_idea_project.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1531815288026-1946892d24df?w=300)

