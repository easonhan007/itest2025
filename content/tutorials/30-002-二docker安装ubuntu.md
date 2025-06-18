---
weight: 2
title: （二）Docker安装（Ubuntu）
date: '2018-01-22T14:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1519156892420-a61fb5543505?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



官方文档：https://docs.docker.com/

Docker 支持多平台的安装（Linux/Windows/OS X）。

因为Docker原生支持Linux，所以，可以直接在Linux上运行，而且在Windows和 OS X 平台则需要借助轻量级的 Linux VM 运行。

![](http://img.testclass.net/docker-platform.png)

### Ubuntu安装
---
在Ubuntu上安装Docker的说明取决于您使用的是Docker企业版（Docker EE）还是Docker社区版（Docker CE）。

参考文档：https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/

#### 使用仓库进行安装

首次在新的主机上安装Docker CE之前，需要设置Docker仓库。 之后，你可以从存储库安装和更新Docker。

##### 设置仓库

1、更新 `apt` 包索引:

```
$ sudo apt-get update
```

2、安装软件包，使它允许`apt`通过HTTPS使用仓库：

```
$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

3、添加Docker的官方GPG密钥：

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
通过搜索密钥的最后8个字符，确认您现在已经拥有指纹 `9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88` 的密钥。

```
$ sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      密钥指纹 = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

4、使用以下命令来设置 __stable__ 的仓库。即使你想从 __edge __ 或 __test__ 仓库安装构建，也总是需要 __stable__ 的仓库。要添加 __edge __ 或 __test__ 仓库，请在下面的命令中在单词stable之后添加edge或test（或两者）。

```
$ sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

注意:上面的`lsb_release -cs`子命令返回你的Ubuntu发行版的名字，比如xenial。


##### 安装Docker CE

1、更新 `apt` 包索引:

```
$ sudo apt-get update
```

2、安装最新版本有 Dcoker CE

```
$ sudo apt-get install docker-ce
```

3、在生产系统上，您应该安装特定版本的Docker CE，而不是始终使用最新版本。下面命令列出可用的版本。

```
$ apt-cache madison docker-ce

 docker-ce | 17.12.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.09.1~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.09.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.06.2~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.06.1~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.06.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.03.2~ce-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.03.1~ce-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
 docker-ce | 17.03.0~ce-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages

```
安装指定的版本：

```
$ sudo apt-get install docker-ce=<VERSION>
```

4、通过运行hello-world 镜像验证Docker CE是否正确安装。

```
$ sudo docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:66ef312bbac49c39a89aa9bcc3cb4f3c9e7de3788c944158df3ee0176d32b751
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/

```

#### 其它

查看 Docker 版本：

```
$ sudo docker version

Client:
 Version:	17.12.0-ce
 API version:	1.35
 Go version:	go1.9.2
 Git commit:	c97c6d6
 Built:	Wed Dec 27 20:11:19 2017
 OS/Arch:	linux/amd64

Server:
 Engine:
  Version:	17.12.0-ce
  API version:	1.35 (minimum version 1.12)
  Go version:	go1.9.2
  Git commit:	c97c6d6
  Built:	Wed Dec 27 20:09:53 2017
  OS/Arch:	linux/amd64
  Experimental:	false
```

显示 Docker 系统信息，包括镜像和容器数:

```
$ sudo docker info

Containers: 7
 Running: 0
 Paused: 0
 Stopped: 7
Images: 2
Server Version: 17.12.0-ce
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 20
 Dirperm1 Supported: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 89623f28b87a6004d4b785663257362d1658a729
runc version: b2567b37d7b75eb4cf325b77297b140ea686ce8f
init version: 949e6fa
Security Options:
 apparmor
 seccomp
  Profile: default
Kernel Version: 4.13.0-26-generic
Operating System: Ubuntu 16.04.3 LTS
OSType: linux
Architecture: x86_64
CPUs: 1
Total Memory: 1.924GiB
Name: ubuntu
ID: OXZY:HYGR:X6XJ:CLDF:H2UG:KXCY:J6MD:32WV:UORN:E2QY:TRTL:ISI6
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): false
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false

WARNING: No swap limit support
```




原始封面

![课程图片](https://images.unsplash.com/photo-1519156892420-a61fb5543505?w=300)

