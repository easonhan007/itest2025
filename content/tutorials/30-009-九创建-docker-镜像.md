---
weight: 9
title: （九）创建 Docker 镜像
date: '2018-01-22T14:30:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1692942193915-4edb50f65ff2?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---




创建镜像有很多方法，用户可以从 Docker Hub 获取已有镜像并更新，也可以利用本地文件系统创建一个。

#### 修改已有的镜像
---

查看已有的镜像：

```
$ sudo docker images
REPOSITORY  TAG       IMAGE ID            CREATED             SIZE
ubuntu      latest    2a4cca5ac898        9 days ago          111MB
```

下面进入到ubuntu容器中:

```
$ sudo docker run -t -i ubuntu /bin/bash
root@543a324ea841:/#
```
__注意：__ 记住容器的	ID，稍后还会用到。

在容器中添加 添加 `Python3` 开发环境。

```
root@543a324ea841:/# apt update   // 更新软件源

root@543a324ea841:/# apt install python3   // 安装 python3

root@543a324ea841:/# exit  // 退出 Ubuntu 容器
exit
```
当结束后，我们使用	`exit` 来退出，现在我们的容器已经被我们改变了，使用 `docker	commit`	命令来提交更新后的副本。

```
$ sudo docker commit -m "Add python3" -a "Docker Newbee" 543a324ea841  ubuntu

sha256:7c0cf1cc5ef36a86252e94eea39c645f53be7dfda87bdcded6d2999917190ffd
```
* -m	来指定提交的说明信息，跟我们使用的版本控制工具一样；

* -a	可以指定更新的用户信息；

之后是用来创建镜像的容器的	ID；最后指定目标镜像的仓库名。 创建成功后会返回这个镜像的ID信息。

查看镜像:

```
$ sudo docker images

REPOSITORY   TAG         IMAGE ID            CREATED              SIZE
ubuntu       latest      7c0cf1cc5ef3        About a minute ago   111MB
ubuntu       <none>      2a4cca5ac898        9 days ago           111MB
```

之后，可以使用新的镜像来启动容器
```
$ sudo docker run -t -i ubuntu:latest /bin/bash
root@8e40ef590fb1:/#
```



#### 利用 Dockerfile 来创建镜像
---

使用 `docker commit` 来扩展一个镜像比较简单，但是不方便在一个团队中分享。我们可以使用 `docker build` 来创建一个新的镜像。为此，首先需要创建一个Dockerfile，包含一些如何创建镜像的指令。

新建一个目录和一个	Dockerfile
```
$ mkdir py
$ cd py
py$ touch Dockerfile
```

Dockerfile	中每一条指令都创建镜像的一层，例如：
```
$ vim Dockerfile

# this is a comment
FROM ubuntu:16.04
MAINTAINER Docker py <pyuser@docker.com>
RUN apt-get install -y	python3
RUN apt-get install -y python3-pip
RUN python3 -m pip install selenium
```
Dockerfile	基本的语法是

* 使用	`#` 来注释
* FROM	指令告诉 Docker 使用哪个镜像作为基础
* 接着是维护者的信息
* RUN	开头的指令会在创建中运行，比如安装一个软件包，在这里使用`apt` 来安装了一些软件

编写完成	Dockerfile	后可以使用 `docker build` 来生成镜像。

```
sudo docker build -f Dockerfile -t ubuntu-py:v1 .

```

* -t标记来添加	tag，指定新的镜像的用户信息。 	

* __“.”__	是	Dockerfile	所在的路径（当前目录），也可以替换为一个具体的	Dockerfile	的路径

可以看到build	进程在执行操作。它要做的第一件事情就是上传这个	Dockerfile	内容，因为所有的操作都要依据	Dockerfile	来进行。 然后， Dockfile	中的指令被一条一条的执行。每一步都创建了一个新的容器，在容器中执行指令并提交修改（就跟之前介绍过的`docker	commit`一样）。当所有的指令都执行完毕之后，返回了最终的镜像	id。所有的中间步骤所产生的容器都被删除和清理了。




原始封面

![课程图片](https://images.unsplash.com/photo-1692942193915-4edb50f65ff2?w=300)

