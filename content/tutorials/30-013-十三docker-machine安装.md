---
weight: 13
title: （十三）Docker Machine安装
date: '2018-01-22T14:18:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1702501856530-4797dacc2de8?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



在macOS和Windows上，当你安装Docker for Mac，Docker for Windows或Docker Toolbox时，Machine将与其他Docker产品一起安装。

如果你只需要Docker Machine，则可以按照下一节中的说明直接安装Machine二进制文件。 你可以在GitHub上的[docker/machine release](https://github.com/docker/machine/releases/) 页面上找到最新版本的二进制文件。

#### 直接安装

##### 1、安装 Docker。

##### 2、下载Docker Machine二进制文件并将其解压到PATH。

如果你是 __macOS__ 系统，运行:
```
$ curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \
  chmod +x /usr/local/bin/docker-machine
```

如果你是 __Linux__ 系统，运行:

```
$ curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine && \
sudo install /tmp/docker-machine /usr/local/bin/docker-machine
```

如果你是 __Windows__ 系统，通过[Git BASH](https://gitforwindows.org/) 运行:

```
$ if [[ ! -d "$HOME/bin" ]]; then mkdir -p "$HOME/bin"; fi && \
curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-Windows-x86_64.exe > "$HOME/bin/docker-machine.exe" && \
chmod +x "$HOME/bin/docker-machine.exe"
```
 > 注意：只有当你使用像Git BASH这样的支持Linux命令（如chmod）的终端模拟器时，上面的命令才能在Windows上运行。



##### 3、查看 Machine 版本

```
$ docker-machine version
docker-machine version 0.13.0, build 9371605
```




原始封面

![课程图片](https://images.unsplash.com/photo-1702501856530-4797dacc2de8?w=300)

