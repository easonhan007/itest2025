---
weight: 1
title: （一）Docker介绍
date: '2018-01-22T14:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1606256485258-ae784908699f?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



#### 什么就Docker?
---

Docker是一个开源项目， 诞生于2013年初，最初是dotCloud公司内部的一个业余项目。它基于Google公司推出的Go语言实现。项目后来加入了Linux基金会，遵从了Apache 2.0协议，项目代码在[GitHub](https://github.com/docker) 上进行维护。

Docker项目的目标是实现轻量级的操作系统虚拟化解决方案。Docker的基础是Linux容器（LXC）等技术。在LXC的基础上Docker进行了进一步的封装，让用户不需要去关心容器的管理，使得操作更为简便。用户操作Docker的容器就像操作一个快速轻量级的虚拟机一样简单。


#### 为什么要使用Docker?
---

Docker 相比传统虚拟机有诸多优势。

* __启动速度更快：__ 秒级启动。

* __快速的部署和交付：__ 开发者可以使用一个标准的镜像来构建一套开发容器，开发完成之后， 运维人员可以直接使用这个容器来部署代码。

* __更高效的虚拟化：__ 它是内核级的虚拟化，因此可以实现更高的性能和效率。

* __高效的迁移：__ Docker可以运行在不同的平台，用户可以轻松的将一个应用从一个平台迁移到另一个平台。

* __节省开支：__ Docker容器除了运行其中应用外，基本不消耗额外的系统资源，一台设备可以运行上千个容器。


#### Docker基本概念
---

Docker包括三个基本概念

* 镜像（Image）

Docker提供了一个很简单的机制来创建镜像或者更新现有的镜像，用户甚至可以直接从其他人那里下载一个已经做好的镜像来直接使用。镜像可以用来创建Docker容器。

* 容器（Container）

容器是从镜像创建的运行实例。它可以被启动、开始、停止、 删除。每个容器都是相互隔离的、保证安全的平台。

* 仓库（Repository）

仓库是集中存放镜像文件的场所。仓库分为公开仓库（Public）和私有仓库（Private） 两种形式。

最大的公开仓库是 [Docker	Hub](https://hub.docker.com)，存放了数量庞大的镜像供用户下载。 [中国官方镜像加速](https://www.docker-cn.com/registry-mirror)




原始封面

![课程图片](https://images.unsplash.com/photo-1606256485258-ae784908699f?w=300)

