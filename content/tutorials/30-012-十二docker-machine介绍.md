---
weight: 12
title: （十二）Docker Machine介绍
date: '2018-01-22T14:20:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1519393442487-7e8a19e4bb9b?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



官方文档：https://docs.docker.com/machine/overview/


__可以使用Docker Machine做什么？__

* 在Mac或Windows上安装并运行Docker
* 配置和管理多个远程Docker主机
* 提供Swarm集群

#### 什么是Docker Machine?
----
Docker Machine是一个工具，可以让你在虚拟主机上安装Docker Engine，并用docker-machine命令管理主机。你可以使用计算机在本地Mac或Windows计算机上，公司网络，数据中心或云提供商（如Azure，AWS或Digital Ocean）上创建Docker主机。

使用docker-machine命令，你可以启动，检查，停止和重新启动托管主机，升级Docker客户端和守护进程，并配置Docker客户端与主机通信。

将机器CLI指向正在运行的托管主机，并且可以直接在该主机上运行`docker`命令。例如，运行`docker-machine env default`指向一个名为`default`的主机，按照屏幕上的说明完成env设置，然后运行`docker ps`，`docker run hello-world`等等。

Machine是在Docker v1.12之前在Mac或Windows上运行Docker的唯一方法。从测试版和Docker v1.12开始，Docker for Mac和Docker for Windows作为本地应用程序提供，并且是更新桌面和笔记本电脑上更好的选择。我们鼓励你尝试这些新的应用程序。 Docker for Mac和Docker for Windows的安装程序包括Docker Machine和Docker Compose。

如果你不确定从哪里开始，请参阅Docker入门，它将指导您完成Docker的简要端到端教程。

##### 为什么要使用Docker Machine?
----

Docker Machine使你能够在各种类型的Linux上配置多个远程Docker主机。

此外，Machine允许你在旧版Mac或Windows系统上运行Docker，如上一主题中所述。

Docker Machine有这两个广泛的用例。

* __你有一个较旧的桌面系统，并希望在Mac或Windows上运行Docker__

![](http://img.testclass.net/docker_machine-mac-win.png)

如果你主要工作不符合新版Docker for Mac和Docker for Windows应用程序要求的较旧的Mac或Windows笔记本电脑或台式机上，那么需要在本地运行Docker机器运行Docker Engine。使用Docker Toolbox安装程序在Mac或Windows上安装Docker Machine可以为本地虚拟机配置Docker Engine，使您能够连接它并运行`docker`命令。


* __我想在远程系统上配置Docker主机__

![](http://img.testclass.net/docker_provision-use-case.png)

Docker Engine在Linux系统上本地运行。如果你有一个Linux系统作为你的主系统，并且想要运行`docker`命令，你只需要下载并安装Docker Engine。但是，如果你想要在网络上，云中甚至本地配置多个Docker主机，需要一种高效的方法，那么需要Docker Machine。

无论的主系统是Mac，Windows还是Linux，都可以在其上安装Docker Machine，并使用docker-machine命令来配置和管理大量的Docker主机。它会自动创建主机，在其上安装Docker Engine，然后配置Docker客户端。每个托管主机（“机器”）是Docker主机和配置的客户机的组合。

#### Docker Engine和Docker Machine有什么区别？
----
当人们说“Docker”时，他们通常指的是Docker Engine，由Docker守护进程组成的 __客户端-服务器__ 应用程序，指定与守护进程交互的接口的REST API，以及与守护进程交谈的命令行界面（CLI） （通过REST API包装）。 Docker Engine接受来自CLI的docker命令，如 `docker run <image>`，`docker ps`列出正在运行的容器，`docker image ls`列出镜像等等。

![](http://img.testclass.net/docker_engine.png)

Docker Machine是一个配置和管理Docker化主机的工具（Docker Engine上的主机）。通常，在本地系统上安装Docker Machine。 Docker Machine拥有自己的命令行客户端docker-machine和Docker Engine客户端 docker。 你可以使用Machine在一个或多个虚拟系统上安装Docker Engine。这些虚拟系统可以是本地的（例如当你使用计算机在Mac或Windows上的VirtualBox上安装和运行Docker引擎）或远程（如使用计算机在云提供程序上配置Docker化主机时）。Docker化主机本身可以被认为是有时被称为管理的“Machine”。

![](http://img.testclass.net/docker_machine.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1519393442487-7e8a19e4bb9b?w=300)

