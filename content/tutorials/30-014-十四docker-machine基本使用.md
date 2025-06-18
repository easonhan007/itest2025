---
weight: 14
title: （十四）Docker Machine基本使用
date: '2018-01-22T14:18:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1675536464237-9b4c0446494b?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



这一小节演示Machine的基本使用。

以 __macOS__ 系统为例：


##### 创建一个machine

指令：
```python
$ docker-machine create --driver virtualbox my-machine

Creating CA: /Users/fnngj/.docker/machine/certs/ca.pem
Creating client certificate: /Users/fnngj/.docker/machine/certs/cert.pem
Running pre-create checks...
Creating machine...
(my-machine) Copying /Users/fnngj/.docker/machine/cache/boot2docker.iso to /Users/fnngj/.docker/machine/machines/my-machine/boot2docker.iso...
(my-machine) Creating VirtualBox VM...
(my-machine) Creating SSH key...
(my-machine) Starting the VM...
(my-machine) Check network to re-create if needed...
(my-machine) Found a new host-only adapter: "vboxnet0"
(my-machine) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: docker-machine env my-machine
```

#### 查看machine列表

指令：
```
$ docker-machine ls

NAME         ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
my-machine   -        virtualbox   Running   tcp://192.168.99.100:2376           v18.01.0-ce   

```

可以看到我们刚创建的“my-machine”已出现在 machine 的列表当中。

#### 查看 machine 的环境变量的配置信息。

指令：
```
$ docker-machine env my-machine

export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/fnngj/.docker/machine/machines/my-machine"
export DOCKER_MACHINE_NAME="my-machine"
# Run this command to configure your shell:
# eval $(docker-machine env my-machine)
```


#### 连接到machine的shell。

指令：
```
$ eval "$(docker-machine env my-machine)"
```

如果没有任何错误提示说明连接该 machine 成功了，因为该 machine 已安装了docker client，所以此时你可以执行 docker 的相关操作。如查看 Docker 版本指令：
```
$ docker --version

Docker version 18.01.0-ce, build 03596f5
```


##### 用 docker run 启动一个容器验证前面的安装和设置没有问题。

指令：
```
$ docker run hello-world
```

##### 获取指定 machine 的 ip

指令：
```
$ docker-machine ip my-machine

192.168.99.100
```


##### 在容器中运行一个页面服务器(Nginx)

指令：
```
$ docker run -d -p 8080:80 --name web-server nginx
```
通过浏览器访问：http://192.168.99.100:8080

![](http://img.testclass.net/docker_mac_nginx.jpg)


##### 访问上面获取到的 ip 和映射的端口号组成的网址，这里是192.168.99.100:8080

指令：
```
$ curl $(docker-machine ip my-machine):8080

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

通过同样的方法你可以创建和管理很多运行着 Docker 的本地 Machine(VMs)；只需运行“docker-machine create”指令；而运行“docker-machine ls”则可以显示所有的 machine 组成的列表。

##### 启动和停止 machines

停止指令：
···
$ docker-machine stop my-machine
···

启动指令：
```
$ docker-machine start my-machine
```

##### docker-machine 的指令列表：

- docker-machine config
- docker-machine env
- docker-machine inspect
- docker-machine ip
- docker-machine kill
- docker-machine provision
- docker-machine regenerate-certs
- docker-machine restart
- docker-machine ssh
- docker-machine start
- docker-machine status
- docker-machine stop
- docker-machine upgrade
- docker-machine url




原始封面

![课程图片](https://images.unsplash.com/photo-1675536464237-9b4c0446494b?w=300)

