---
weight: 3
title: （三）Docker 镜像
date: '2018-01-22T14:45:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1487901155524-307f976ad775?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---




Docker 运行容器前需要本地存在对应的镜像，如果镜像不存在本地， Docker	会从镜像仓库下载（默认是Docker Hub公共注册服务器中的仓库）。

Docker Hub:https://hub.docker.com
阿里云镜像：https://dev.aliyun.com/search.html
灵雀云：https://hub.alauda.cn/

#### 镜像
---


##### 查看镜像

列出本地镜像：
```
$ sudo docker images

REPOSITORY     TAG         IMAGE ID         CREATED        SIZE
hello-world    latest      f2a91732366c     2 months ago
```

在列出信息中，可以看到几个字段信息：

* 来自于哪个仓库，比如	ubuntu
* 镜像的标记，比如	14.04
* 它的 	ID	号（唯一）
* 创建时间
* 镜像大小


##### 获取镜像

可以使用`docker pull` 命令来从仓库获取所需要的镜像。搜索 “ubuntu” 镜像。

```
$ sudo docker pull ubuntu

Using default tag: latest
latest: Pulling from library/ubuntu
8f7c85c2269a: Pull complete
9e72e494a6dd: Pull complete
3009ec50c887: Pull complete
9d5ffccbec91: Pull complete
e872a2642ce1: Pull complete
Digest: sha256:d3fdf5b1f8e8a155c17d5786280af1f5a04c10e95145a515279cf17abdf0191f
Status: Downloaded newer image for ubuntu:latest
```
该命令实际上相当于 `$	docker pull registry.hub.docker.com/ubuntu` 命令，即从注册服务器`registry.hub.docker.com`中的 `ubuntu`仓库来下载的镜像。

当然，官方的Docker hub 比较慢，我们也可以到国内的容器服务去下载镜像。


##### 创建镜像

创建镜像有很多方法，用户可以从 Docker Hub 获取已有镜像并更新，也可以利用本地文件系统创建一个。

做为一个 Docker 新手，我们先掌握如何使用别人的镜像，至于创建镜像放到后面介绍。




原始封面

![课程图片](https://images.unsplash.com/photo-1487901155524-307f976ad775?w=300)

