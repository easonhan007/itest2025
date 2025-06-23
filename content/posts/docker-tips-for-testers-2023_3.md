---
weight: 1
title: "测试人员必会的docker秘籍"
date: 2024-03-08T09:01:37+08:00
lastmod: 2024-03-08T09:01:37+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "收藏先"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

[Docker](https://www.docker.com/)现在是许多 QA 工程师的常用工具。它用于生产环境和测试环境或两者兼而有之。docker 的文档[制作精良](https://docs.docker.com/get-started/)，相对容易理解，但有时我们需要一些常用命令来解决问题。

在这里我列举一下对于测试同学来说比较值得去弄明白的 docker 秘籍。

### \***\*如何使用不同的参数运行已经启动的 docker 容器？\*\***

可以用这个工具：[https://github.com/lavie/runlike/](https://github.com/lavie/runlike/)

使用方法: `runlike -p <container_name>` ，这样就可以拿到该容器第一次启动时候用的具体命令了。

```bash
runlike -p testservice
docker run \
--name=testservice \
--user=test \
--env=KAFKA_HOST=172.17.0.1:9092 \
--env=PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin \
--env=LANG=en_US.UTF-8 \
--workdir=/home/testapp \
-p 8015:8080 \
--restart=always \
--log-driver=journald \
--runtime=runc \
--detach=true \
myrepo/testservice:master-1374
```

这时候我们就可以修改一些参数，比如端口号信息，生活变得容易了一些。

### \***\*如何在 docker 容器中运行本地 bash 脚本？\*\***

```bash
cat local_script.sh | docker exec <container_name> /bin/bash
```

### 如何重启或移除所有的容器？

这个技巧非常管用，推荐牢记。

```bash
docker stop $(docker ps -a -q)
docker restart $(docker ps -a -q)
```

### \***\*如何清理旧的 docker 镜像、容器和卷？\*\***

```bash
docker system prune -a
```

### \***\*如何过滤 docker ps 命令，以仅获取所需的信息，例如容器名称、状态和镜像？\*\***

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"
```

### \***\*如何保存和恢复 docker 容器？\*\***

```bash
docker commit -p <CONTAINER_ID> <YOUR_BACKUP_NAME>
docker save -o <CONTAINER_FILE>.tar <YOUR_BACKUP_NAME>
docker load -i <CONTAINER_FILE>.tar
```

### 如何将常用的 docker 命令简化成别名？

如果你是 docker 的重度用户的话，这个能力非常实用。

```bash
dexec() { docker exec -i -t $@ /bin/bash ;}
dlogs()  { docker logs --tail=all -f $@ ;}
dport() { docker port $@ ;}
dvol()  { docker inspect --format '{{ .Volumes }}' $@ ;}
dip()   { docker inspect --format '{{ .NetworkSettings.IPAddress }}' $@ ;}
```

### 总结

希望以上的命令会对大家有所帮助。
