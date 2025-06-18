---
weight: 2
title: （二）Jenkins 环境搭建
date: '2017-10-16T14:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1514513452089-17f8a9771ee8?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



Jenkins 是基于Java开发的一种持续集成工具，所以，Jenkins需要Java环境。关于Java环境的配置我们在第9章使用Selenium Grid 时已经作了介绍，这里不在讲解。

### 安装 Tomcat
----
Tomcat是针对Java的一个开源中间件服务器（容器），基于Java Web的项目需要借助Tomcat 才能运行起来。

Tomcat官方网站：http://tomcat.apache.org/ ，打开后首页如图2.1所示

![](http://img.testclass.net/jenkins_tomecat.png)
图2.1  下载Tomcat

单击页面左侧Tomcat 版本进行下载，对下载的压缩包进行解压，目录结构如图2.2所示。
![](http://img.testclass.net/jenkins_tomecat2.png)
图2.2  webapps目录用于web项目
通常将需要运行的应用放到webapps/目录下，进入bin/目录下，双击startup.bat，启动Tomcat服务器。

#### 安装 Jenkins
----
Jenkins官方网站：https://jenkins.io/ ，打开后首页如图2.3所示。

![](http://img.testclass.net/jenkins_dwonload.png)
图2.3  下载Jenkins

点击“Download” 链接进入下载页面，根据自己的系统选择对应的 Jenkins 版本进行下载。

下载完成，双击进行安装，如图2.4所示。

![](http://img.testclass.net/jenkins_install.png)
图2.4  双击Jenkins安装

单击“next”按钮，我们直接将其安装到Tomcat的 __webapps__ 目录下，如图2.5所示。<font color='red'>一定要选择TomCat 的 webapps 目录。</font>

![](http://img.testclass.net/jenkins_install2.png)
图2.5  选择Tomcat的webapps目录

#### 配置 Jenkins
---
Jenkins 安装完成会自动启动 TomCat , 并通过默认浏览器打开：http://localhost:8080/。

（你也可以手动进Tomcat的bin/目录下启动startup.bat ，通过浏览器访问：http://localhost:8080/） 如图2.6所示。

![](http://img.testclass.net/jenkins_first_run.png)
图2.6  开如Jenkins

根据提示，打开：
__D:\Java\apache-tomcat-9.0.0.M26\webapps\Jenkins\secrets\initialAdminPassword__ 文件查看密码。将密码填写到输入框中，点击 __“Continue”__ 按钮。

接下来根据提示进行安装。

![](http://img.testclass.net/jenkins_first_run2.png)

上图，运行需要一些时间，Jenkins 正在帮我们安装各种主流插件。

最后一步配置，创建 管理员账号。

![](http://img.testclass.net/jenkins_first_run3.png)

整个 Jenkins 安装配置完成。操作界面如下。

![](http://img.testclass.net/jenkins_run_success.png)

Jenkins 的安装比以前复杂了些，但功能也变得更为强大了。




原始封面

![课程图片](https://images.unsplash.com/photo-1514513452089-17f8a9771ee8?w=300)

