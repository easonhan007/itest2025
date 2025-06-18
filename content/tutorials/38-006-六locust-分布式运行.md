---
weight: 6
title: （六）Locust 分布式运行
date: '2017-10-16T10:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1457612928689-a1ab27da0dad?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



参考：[官方文档](https://docs.locust.io/en/latest/running-locust-distributed.html)

#### 分布式运行Locust
---
一旦单台机器不够模拟足够多的用户时，Locust支持运行在多台机器中进行压力测试。

为了实现这个，你应该在 master 模式中使用```--master```标记来启用一个 Locust 实例。这个实例将会运行你启动测试的 Locust 交互网站并查看实时统计数据。master 节点的机器自身不会模拟任何用户。相反，你必须使用 ```--slave``` 标记启动一台到多台 Locustslave 机器节点，与标记 ```--master-host``` 一起使用(指出master机器的IP/hostname)。

常用的做法是在一台独立的机器中运行master，在slave机器中每个处理器内核运行一个slave实例。

> 注意：master 和每一台 slave 机器，在运行分布式测试时都必须要有 locust 的测试文件。


#### 示例
---
在 master 模式下启动 Locust:

```
locust -f my_loucstfile.py --master
```

在每个 slave 中执行(192.168.0.14 替换为你 msater 的IP):

```
locust -f my_locustfile.py --slave --master-host=192.168.0.14
```

#### 参数说明
---
参数

--master

设置 Locust 为 master 模式。网页交互会在这台节点机器中运行。

--slave

设置 Locust 为 slave 模式。

--master-host=X.X.X.X

可选项，与 ```--slave``` 一起结合使用，用于设置 master 模式下的 master 机器的IP/hostname(默认设置为127.0.0.1)

--master-port=5557

可选项，与 ```--slave``` 一起结合使用，用于设置 master 模式下的 master 机器中 Locust 的端口(默认为5557)。注意，locust 将会使用这个指定的端口号，同时指定端口+1的号也会被占用。因此，5557 会被使用，Locust将会使用 5557 和 5558。

--master-bind-host=X.X.X.X`

可选项，与 ```--master``` 一起结合使用。决定在 master 模式下将会绑定什么网络接口。默认设置为*(所有可用的接口)。

--master-bind-port=5557

可选项，与 ```--master``` 一起结合使用。决定哪个网络端口 master 模式将会监听。默认设置为 5557。注意 Locust 会使用指定的端口号，同时指定端口+1的号也会被占用。因此，5557 会被使用，Locust 将会使用 5557 和 5558。

--expect-slaves=X

在 __no-web__ 模式下启动 master 时使用。master 将等待X连接节点在测试开始之前连接。

#### 效果
---
如下图，我启动了一个 master 和两个 slave，由两个 slave 来向被测试系统发送请求。

![](http://img.testclass.net/locust_distributed_slaves.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1457612928689-a1ab27da0dad?w=300)

