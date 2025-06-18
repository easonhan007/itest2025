---
weight: 4
title: （四）Docker 容器
date: '2018-01-22T14:42:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1494086540177-cb524d1bc2f8?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



简单的说，容器是独立运行的一个或一组应用，以及它们的运行态环境。 如果把镜像看成面向对象中的 __类__ 的话，那么容器就是 类 的实例化 __对象__。

#### 容器
---

##### 启动容器

启动容器有两种方式，一种是基于镜像新建一个容器并启动， 另外一个是将在终止状态（stopped）的容器重新启动。

通过`docker run` 命令来启动容器。

查看运行帮助：
```
$ sudo docker run --help
```

下面的命令输出一个	“Hello	World”，之后终止容器。

```
$ sudo docker run ubuntu /bin/echo "hello world"
hello world
```
这跟在本地直接执行 `/bin/echo	'hello	world'`几乎感觉不出任何区别。只不过，这里的输入是由通过 ubuntu 容器执行。

下面进入到ubuntu容器中。

```
$ sudo docker run -t -i ubuntu /bin/bash
root@543a324ea841:/#
```

* -t	选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上。

* -i	则让容器的标准输入保持打开。

此时，你已经在ubuntu容器中了。这是一个独立的ubuntu 系统。通过 __root@543a324ea841__ 标识可以看出。

当利用`docker run`	来创建容器时，Docker在后台运行的标准操作包括：

* 检查本地是否存在指定的镜像，不存在就从公有仓库下载
* 利用镜像创建并启动一个容器
* 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
* 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
* 从地址池配置一个IP地址给容器
* 执行用户指定的应用程序
* 执行完毕后容器被终止

退出容器，可以使用exit命令。
```
root@543a324ea841:/# exit  
exit
fnngj@ubuntu:~$
```

##### 守护状态运行

更多的时候，需要让	Docker容器在后台以守护态（Daemonized）形式运行。

```
$ sudo docker run -d ubuntu /bin/echo "hello docker"
839fee657bfe893b9b2c76aebbb2b620efefc091a04fd90b1c5eda82b9e36730
```
* -d  表示容器以守护态（Daemonized）形式运行。


##### 查看容器

通过 `docker ps` 命令查看当前运行的所有容器。

```
$ sudo docker ps -a

CONTAINER ID    IMAGE         COMMAND                  CREATED         STATUS                         PORTS    NAMES
839fee657bfe    ubuntu        "/bin/echo 'hello do…"   About a minute ago Exited (0) About a minute ago        musing_golick
543a324ea841    ubuntu        "/bin/bash"              6 minutes ago   Exited (0) About a minute ago           relaxed_shannon
578639b30db9    ubuntu        "/bin/bash"              7 minutes ago   Exited (0) 7 minutes ago                sad_ritchie
9797d4bcb1f6    ubuntu        "/bin/echo 'hello wo…"   9 minutes ago   Exited (0) 9 minutes ago                cranky_keller
4d2cd63632c7    hello-world   "/hello"                 20 minutes ago  Exited (0) 20 minutes ago               keen_stallman

```

##### 获取容器的输出信息

通过`docker	logs`命令。

```
$ sudo docker logs musing_golick
hello docker

$ sudo docker logs 839fee657bfe
hello docker
```
`musing_golick` 为容器的 NAMES , `839fee657bfe` 为容器的ID。通过 `docker ps -a` 命令查看。


##### 停止容器

可以使用`docker	stop`来终止一个运行中的容器。

```
$ sudo docker stop 0fc49a885fc2
```

##### 重动容器

可以使用`docker	start` 重动容器。

```
$ sudo docker start 0fc49a885fc2
```

##### 删除容器

通过 `docker rm` 删除指定的容器。

```
sudo docker rm 0fc49a885fc2
```
0fc49a885fc2 为容器有 ID 。




原始封面

![课程图片](https://images.unsplash.com/photo-1494086540177-cb524d1bc2f8?w=300)

