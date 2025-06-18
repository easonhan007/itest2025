---
weight: 8
title: （八）实战：构建 GitHub 项目(下)
date: '2017-10-16T11:45:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://plus.unsplash.com/premium_photo-1664298230305-9116cf510bed?q=80&w=2970&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



其实，到些为止，整个项目已经创建完成。这一小节，只是为了验证创建的项目是否有效。

#### 提交项目版本
---
修改 [pyse](https://github.com/defnngj/pyse) 开源项目,并提交代码到 GitHub .

```
D:\git\pyse (master)
λ git commit -m "verison 0.0.8"

[master 270de98] verison 0.0.8
 6 files changed, 36 insertions(+), 32 deletions(-)
 create mode 100644 test_report.png

 D:\git\pyse (master)
 λ git push origin master

 Counting objects: 12, done.
 Delta compression using up to 4 threads.
 Compressing objects: 100% (11/11), done.
 Writing objects: 100% (12/12), 33.80 KiB | 11.27 MiB/s, done.
 Total 12 (delta 5), reused 0 (delta 0)
 remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
 To https://github.com/defnngj/pyse
    c5b4c8a..270de98  master -> master

 ```


#### 查看构建日志
---

通过 Jenkins 查看项目构建历史。

![](http://img.testclass.net/jenkins_github_building_times.png)

查看构建的详细日志。

![](http://img.testclass.net/jenkins_github_building_log.png)

<br>
关于 GitHub 的项目实战到此完成。




原始封面

![课程图片](https://plus.unsplash.com/premium_photo-1664298230305-9116cf510bed?q=80&w=2970&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

