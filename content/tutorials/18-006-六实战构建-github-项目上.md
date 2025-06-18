---
weight: 6
title: （六）实战：构建 GitHub 项目(上)
date: '2017-10-16T11:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1631475012097-d074e8a92597?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



Jenkins 不是一个对开发零基础的人去用的工具。不管你要构建什么样的项目，首先要有这么个项目存在，而且还要知道如何运行该项目。

#### 快速创建 GitHub 项目
---

如果你想快速的使用 GitHub 来维护你的自动化测试项目，请阅读该教程。

[（一）认识Git与GitHub](/git/git-github-start/)

[（二）GitHub注册与Git安装](/git/registration-and-installation/)

[（三）Git提交代码到GitHub](/git/git-commit-code/)

[（四）Git克隆与更新代码](/git/git-github-used/)


#### Jenkins 配置 Git
----
首先，登录 Jenkins ，在首页找到 “__系统管理 -> Global Tool Configuration -> Git__ ”

![](http://img.testclass.net/jenkins_github_git.png)

__Path to Git executable__ ：设置 Git 执行文件的位置。从你Git的安装目录中查看 “__git.exe__” 可执行文件的位置。

设置完成后点击 “__Save__” 保存设置。




原始封面

![课程图片](https://images.unsplash.com/photo-1631475012097-d074e8a92597?w=300)

