---
weight: 7
title: （七）实战：构建 GitHub 项目(中)
date: '2017-10-16T11:50:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1589320011103-48e428abcbae?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



前提工作已经完成，接下来创建 GitHub 的项目构建。

## 创建 GitHub 项目的构建
---
#### 1、新建项目
---
在 Jenkins 首页，点击 “__新建__”。

![](http://img.testclass.net/jenkins_github_project.png)

设置项目名称：GitHub project

选择“__构建一个自由风格的软件项目__”

#### 2、添加 GitHub 上的项目
---
勾选 __* GitHub Project__ 选项

![](http://img.testclass.net/jenkins_github_project2.png)

* Project url ：设置 github 的项目地址。


#### 3、设置Git
---
勾选 __* Git__ 选项

![](http://img.testclass.net/jenkins_github_git_setting.png)

* Repository URL: 填写 GitHub 项目地址
* credentials ： 设置资格证书，听过 __add__ 添加账号。
* Branch Specifier(blank for 'any') ： 默认 `*/master` 不用修改。

#### 4、设置触发条件
---
![](http://img.testclass.net/jenkins_github_building_time.png)

* Github hook trigger for GITScm polling （触发 GitHub 项目轮询） ，勾选。

* Poll SCM  （设置每两分钟检测一次项目更新）[参考](/jenkins/setting-time/) ，勾选。

#### 5、添加构建命令
---

![](http://img.testclass.net/jenkins_github_command.png)

添加运行项目测试用例的命令。[参考](/jenkins/greating-tasks/)

项目创建完成，点击“__保存__”。




原始封面

![课程图片](https://images.unsplash.com/photo-1589320011103-48e428abcbae?w=300)

