---
weight: 11
title: （十一）Docker Compose创建Wordpress应用
date: '2018-01-22T14:22:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1468324231521-5bb8d15ff471?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



wordpress是最常见博客系统，一般部署需要LAMP/WAMP环境，这介绍通过Docker compose对它进行编排和部署。

Docker Hub地址: https://hub.docker.com/_/wordpress/


#### wordpress 应用部署
---

##### 1、 建立一个应用的目录

```
$ mkdir wordpress
$ cd wordpress
```

##### 2、创建 docker-compose.yml

```
version: '3.1'

services:

  wordpress:
    image: wordpress
    restart: always
    ports:
      - 8081:80
    environment:
      WORDPRESS_DB_PASSWORD: pw123

  mysql:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: pw123

```

* images 镜像名
* restart 指定版本
* ports  `80`为镜像端口， 映射的`8081`为主机端口。
* environment 环境配置，例，`WORDPRESS_DB_PASSWORD` 为wordpress数据库密码。

##### 3、启动应用

`docker-compose`执行编排脚本，分别制作和抓取web，redis镜像，启动容器。

```
$ sudo docker-compose up

……

Creating wordpress_mysql_1     ... done
Creating wordpress_wordpress_1 ... done
```

整个过程会比较漫长。。。


##### 5、访问应用

打开浏览器方位: http://0.0.0.0:5081/

进入wordpress安装配置界面：

![](http://img.testclass.net/docker_wordpress.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1468324231521-5bb8d15ff471?w=300)

