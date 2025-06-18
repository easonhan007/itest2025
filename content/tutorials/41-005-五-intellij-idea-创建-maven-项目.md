---
weight: 5
title: （五） IntelliJ-IDEA 创建 Maven 项目
date: '2017-11-25T12:35:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1577412647305-991150c7d163?w=300
tags: []
categories:
- maven简明教程
lightgallery: true
toc:
  auto: false
---



IntelliJ IDEA 默认集成的就有 Maven 插件，所以，我们也可以直接使用它来创建 Maven 项目。

#### 修改 Maven 配置
---
首先， 打开 IntelliJ IDEA 开发工具， 菜单栏： __“File” --->“Settings...”__ ， 搜索“Maven” 选项， 如下图。

![](http://img.testclass.net/maven_idea_setting.png)

设置参数：

* Maven home directory： 设置本地安装的 Maven 目录。 如“__D:/java/apache-maven-3.5.0__”。

* User settings file： 选择 Maven 目录下的配置文件。 如“__D:\java\apache-maven-3.5.0\conf\settings.xml__” ，需要勾选“__Override__” 选项才能设置。

* Locla repository： 设置本地仓库地址。 上一个选项设置好后， 该选项自动设置。

<font color="red"> __注：__ 这里也可以不用设置，直接使用 IntelliJ IDEA 的默认配置。</font>

#### 创建 Maven 项目
---

接下来在 IntelliJ IDEA 中创建 Maven 项目。 菜单栏： __“File” --->“New” --->“Project...”__ ， 打开创建 Maven 。

![](http://img.testclass.net/maven_idea_create_01.png)

在左侧项目类型中选择“__Maven__” ， 然后点击“__Next__” 。

![](http://img.testclass.net/maven_idea_create_02.png)

* GoupId： 指定项目或公司组名。

* ArifactId： 指定项目名称。

然后， 继续点击“__Next__” 。

![](http://img.testclass.net/maven_idea_create_03.png)

* Project name： 设置项目名称。

* Project Iocation： 设置项目的在本地磁盘的位置。

最后， 点击“__Finish__” 完成 Maven 项目创建。




原始封面

![课程图片](https://images.unsplash.com/photo-1577412647305-991150c7d163?w=300)

