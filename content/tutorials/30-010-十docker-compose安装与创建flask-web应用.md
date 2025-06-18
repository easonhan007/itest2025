---
weight: 10
title: （十）Docker Compose安装与创建Flask web应用
date: '2018-01-22T14:25:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1444487233259-dae9d907a740?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



Docker Compose 是 Docker 官方编排（Orchestration）项目之一， 负责快速在集群中部署分布式应用。

Dockerfile 可以让用户管理一个单独的应用容器；而	Compose	则允许用户在一个模板（YAML	格式）中定义一组相关联的应用容器（被称为一个 project，即项目），例如一个Web服务容器再加上后端的数据库服务容器等。

#### 安装
---

该项目由 Python 编写，实际上调用了 Docker 提供的	API	来实现。 通过`pip`安装。

```
$ python3 -m pip install docker-compose
```

安装成功后，可以查看`docker-compose`命令的用法。
```
$ docker-compose
Define and run multi-container applications with Docker.

Usage:
  docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
  docker-compose -h|--help

Options:
  -f, --file FILE             Specify an alternate compose file (default: docker-compose.yml)
  -p, --project-name NAME     Specify an alternate project name (default: directory name)
  --verbose                   Show more output
  --no-ansi                   Do not print ANSI control characters
  -v, --version               Print version and exit
  -H, --host HOST             Daemon socket to connect to

  ……

```

#### 创建 Flask 应用
---

创建使用Flask web应用，并将数值记入Redis。

##### 1、创建 Web 应用

创建一个Flask web 应用，app.py 文件：

```Python
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

创建依赖文件 `requirements.txt `， 内容如下：

```
flask
redis
```


##### 2、创建 Dockerfile

在同一目录下，创建 `Dockerfile`。

```
FROM python:3.5
ADD . /code
WORKDIR /code
RUN python3 -m pip install -r requirements.txt
CMD python3 app.py
```

对上面的Dockerfile做一下简单说明：

* 容器使用Python 3.5的镜像
* 将当前目录下文件拷贝到容器内/code
* 指定工作目录为/code
* 安装python需要的库：flask, redis
* 容器执行命令 python3 app.py


##### 3、创建编排脚本

在同一目录下，创建 `docker-compose.yml`

```
version: '1'
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
    depends_on:
     - redis
  redis:
    image: redis
```

对上面的编排脚本做一下简单说明：

* 这个应用定义了两个服务：web, redis
* web容器通过当前路径下的Dockerfile生成
* web容器内的5000端口映射到主机的5000端口
* 将当前目录挂载到web容器内/code
* web容器依赖于redis容器
* redis容器从Docker Hub获取镜像

所有文件都已经准备就绪。
```
$ ls
app.py  docker-compose.yml  Dockerfile  requirements.txt
```


##### 4、启动应用

`docker-compose`执行编排脚本，分别制作和抓取web，redis镜像，启动容器。

```
$ sudo docker-compose up

……

redis_1  | 1:M 02 Feb 04:13:15.129 * Ready to accept connections
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1    |  * Restarting with stat
web_1    |  * Debugger is active!
web_1    |  * Debugger PIN: 170-376-971
```

整个过程会比较漫长。。。


##### 5、访问应用

打开浏览器方位: http://0.0.0.0:5000/

效果如下：

![](http://img.testclass.net/docker_flask_redis.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1444487233259-dae9d907a740?w=300)

