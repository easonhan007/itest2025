---
weight: 3
title: 3.入门级接口测试工具:postman的安装
date: '2017-08-28T04:41:43+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1457612928689-a1ab27da0dad?w=300
tags: []
categories:
- python接口测试实践教程
lightgallery: true
toc:
  auto: false
---



### 关于postman

postman是跨平台的接口调试及测试工具，非常适合初学者使用。

### 安装postman

[下载地址](https://www.getpostman.com/)

请选择相应的版本下载，windows版下载完成后双击安装就好了。

### postman的界面

![](http://oriphg3yh.bkt.clouddn.com/postman1.png)

### 发送第一个请求

我们发送上一节里提到的获取v2ex节点信息的api。

```
https://www.v2ex.com/api/nodes/show.json?name=python
```

具体步骤如下

![](http://oriphg3yh.bkt.clouddn.com/send_req.gif)

### postman是如何工作的

![](http://oriphg3yh.bkt.clouddn.com/postman_2.png)

从原理图上可以看出，postman发送请求给服务器，然后从服务器接受响应，最后在postman中展示出来。


### 服务器响应

上图就是服务器的响应详情，这里包含了一些重要信息

* 状态码: 200，表示响应是ok的
* Body: 返回的主体
* Headers: 可以简单的理解为一些键值对，对请求的主体起到了补充的作用
* Time: 响应时间
* Size: 响应的大小

### json字符串

有基础的同学可以看出来，响应的主体是json格式的字符串，那么什么是json格式字符串呢？下一节我们将详细讲解。




原始封面

![课程图片](https://images.unsplash.com/photo-1457612928689-a1ab27da0dad?w=300)

