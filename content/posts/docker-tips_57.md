---
weight: 1
title: "推荐：Docker备忘录"
date: 2024-03-08T09:02:58+08:00
lastmod: 2024-03-08T09:02:58+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "很实用"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1533162518830-e683192f365b?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

项目源地址：[https://github.com/wsargent/docker-cheat-sheet](https://github.com/wsargent/docker-cheat-sheet)

## docker 的安装

略，windows 上可以用 docker desktop，具体可以参考官方文档。[https://hub.docker.com/editions/community/docker-ce-desktop-windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

安装之后用 admin 身份打开 powershell，输入

```powershell
#Display the version of docker installed:
docker version

##Pull, create, and run 'hello-world' all in one command:
docker run hello-world
```

## 容器相关

### 容器的生命周期

- `[docker create](https://docs.docker.com/engine/reference/commandline/create)`  创建但未启动
- `[docker rename](https://docs.docker.com/engine/reference/commandline/rename/)`  重命名容器
- `[docker run](https://docs.docker.com/engine/reference/commandline/run)`  一个命令创建并启动容器
- `[docker rm](https://docs.docker.com/engine/reference/commandline/rm)`  删除容器
- `[docker update](https://docs.docker.com/engine/reference/commandline/update/)`  更新容器的资源限制

几个有用的点

- 一般启动容器我们用 docker run -td container_id, -t 表示分配 TTY session，-d 表示后台运行并打印容器 id
- docker run --rm 用来运行容器后自动删除
- docker run -v $HOSTDIR:$DOCKERDIR 用来做 volume 的映射

### 容器的启动和停止

- `[docker start](https://docs.docker.com/engine/reference/commandline/start)`  运行容器
- `[docker stop](https://docs.docker.com/engine/reference/commandline/stop)`  停止一个运行中的容器
- `[docker restart](https://docs.docker.com/engine/reference/commandline/restart)`  重启容器
- `[docker pause](https://docs.docker.com/engine/reference/commandline/pause/)`  暂停容器
- `[docker unpause](https://docs.docker.com/engine/reference/commandline/unpause/)`  继续运行一个暂停了的容器
- `[docker wait](https://docs.docker.com/engine/reference/commandline/wait)`  等待直到容器停止
- `[docker kill](https://docs.docker.com/engine/reference/commandline/kill)`  发送 SIGKILL 信号给容器
- `[docker attach](https://docs.docker.com/engine/reference/commandline/attach)`  连接运行中的容器

### 限制 cpu 和内存

```powershell
docker run -it -c 512 agileek/cpuset-test
```

上面的命令限制了 cpu 使用率为 50%，看起来很奇怪对不对？因为 100%使用率用的参数是-c 1024，所以 50%就是 512

我们还可以限制容器的内容使用

```powershell
docker run -it -m 300M ubuntu:14.04 /bin/bash
```

### 容器信息

- `[docker ps](https://docs.docker.com/engine/reference/commandline/ps)`  展示运行中的容器
- `[docker logs](https://docs.docker.com/engine/reference/commandline/logs)`  从容器中拿日志
- `[docker inspect](https://docs.docker.com/engine/reference/commandline/inspect)`  展示容器的具体信息
- `[docker events](https://docs.docker.com/engine/reference/commandline/events)`  从容器获得事件
- `[docker port](https://docs.docker.com/engine/reference/commandline/port)`  展示容器的公共端口
- `[docker top](https://docs.docker.com/engine/reference/commandline/top)`  展示容器中运行的进程
- `[docker stats](https://docs.docker.com/engine/reference/commandline/stats)`  展示容器的资源使用情况
- `[docker diff](https://docs.docker.com/engine/reference/commandline/diff)`  展示容器的 file system 中变更的文件

docker ps -a：展示所有的容器，包括运行中和已停止的

docker stats --all： 展示所有的容器，不仅仅是运行中的容器的资源使用情况

### 导入和导出

- `[docker cp](https://docs.docker.com/engine/reference/commandline/cp)`  本地和容器进行文件和文件夹拷贝的方式
- `[docker export](https://docs.docker.com/engine/reference/commandline/export)`  导出容器到 STDOUT，一般是以压缩包的方式了

### 执行命令

docker exec -it foo /bin/bash 去容器中执行命令
