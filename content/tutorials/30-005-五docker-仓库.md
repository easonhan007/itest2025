---
weight: 5
title: （五）Docker 仓库
date: '2018-01-22T14:40:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1705365212953-153ebe92cce3?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



前面在下载镜像的适应已经用到了Docker仓库，如果是镜像的一个托管平吧。

#### 仓库
---

一个容易混淆的概念是注册服务器（Registry）。 实际上注册服务器是管理仓库的具体服务器，每个服务器上可以有多个仓库，而每个仓库下面有多个镜像。从这方面来说， 仓库可以被认为是一个具体的项目或目录。例如对于仓库地址 	`registry.hub.docker.com/ubuntu`	来说，`registry.hub.docker.com`是注册服务器地址，`ubuntu`是仓库名。大部分时候，并不需要严格区分这两者的概念。

##### Docker Hub

目前Docker官方维护了一个公共仓库 Docker Hub：https://hub.docker.com

我们可以在Docker Hub上完成注册。这样就可以使用Docker Hub 来托管我们的镜像了。

通过`docker	search`命令来查找官方仓库中的镜像，并利用`docker pull` 命令来将它下载到本地。

```
$ sudo docker search ubuntu
```

#### 使用国内镜像

参考地址：https://www.docker-cn.com/registry-mirror

临时性的使用：

```
$ sudo docker pull registry.docker-cn.com/library/ubuntu:16.04

```
永久性的使用：

修改 /etc/docker/daemon.json文件（没有的话可以手动创建，需要通过`root`用户操作）并添加上 registry-mirrors 键值。

```
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
```
修改保存后重启Docker服务以使配置生效。

```
$ sudo service docker restart
```




原始封面

![课程图片](https://images.unsplash.com/photo-1705365212953-153ebe92cce3?w=300)

