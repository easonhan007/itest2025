---
weight: 6
title: （六）soapUI创建REST项目
date: '2017-09-20T21:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1519481116090-11a5d47f4c2f?w=300
tags: []
categories:
- SoupUI实用教程
lightgallery: true
toc:
  auto: false
---



#### 创建 REST 项目
----

打开 soapUI 工具。创建一个 REST 项目。

![](http://img.testclass.net/soapui_main_window.png)

在窗口左侧导航栏，右键 __Projects --> New REST Project__。

#### 添加REST接口
----
以本地查询发布会接口为例。

__URI__：http://127.0.0.1:8000/events/ 为接口URI。

![](http://img.testclass.net/soapui_new_rest_project.png)

点击 __OK__ 按钮，创建项目完成。

依次展开：__REST Project 1-->Events[/events/]-->Events-->Request 1__ , 为 REST 接口窗口。

![](http://img.testclass.net/soapui_rest_if_window.png)

点击 __Request 1__ 窗口中左上角的绿色 __运行__ 按钮，右则窗口显示接口查询结果。

#### 设置接口URI
----

如果想查询具体的某一条发布会信息，可以在 Resource 输入框中指定发布会 id，如下图。

![](http://img.testclass.net/soapui_rest_if_data.png)

点击 __Request 1__ 窗口中左上角的绿色 __运行__ 按钮，右则窗口显示接口查询结果，下图。

![](http://img.testclass.net/soapui_rest_if_result.png)

一个简单的 REST 接口测试完成了。




原始封面

![课程图片](https://images.unsplash.com/photo-1519481116090-11a5d47f4c2f?w=300)

