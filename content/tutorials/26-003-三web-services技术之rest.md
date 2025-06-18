---
weight: 3
title: （三）Web Services技术之REST
date: '2017-09-21T00:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?w=300
tags: []
categories:
- SoupUI实用教程
lightgallery: true
toc:
  auto: false
---



<br>
REST 定义了一组体系架构原则，你可以根据这些原则设计以系统资源为中心的 Web Services ，包括使用不同语言编写的客户端如何通过HTTP处理和传输资源状态。如果考虑使用它的 Web Services 的数量，REST 近年来已经成为最主要的 Web Services 设计模型。事实上，REST 对 Web 的影响非常大，由于它的使用非常方便，已经普遍地取代了基于 SOAP 和 WSDL 的接口设计。

#### REST
----
Representational State Transfer，简称 REST ，中文翻译为  “表现层状态转化” 。

 REST 具有夸语言、夸平台的特点。所以，它是一种遵循 REST 风格的 Web Services。

 如果一个架构符合 REST 原则，就称它为 REST ful架构。要理解 REST ful架构，最好的方法就是去理解 Representational State Transfer 这个词组到底是什么意思，它的每一个词代表了什么涵义。如果你把这个名称搞懂了，也就不难体会 REST 是一种什么样的设计。

 __一、资源（Resources）__

 REST 的名称 “表现层状态转化” 中，省略了主语。 “表现层” 其实指的是 “资源” （Resources）的 “表现层” 。

所谓 “资源” ，就是网络上的一个实体，或者说是网络上的一个具体信息。它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的实在。你可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。

所谓 “上网” ，就是与互联网上一系列的 “资源” 互动，调用它的 URI。

__二、表现层（Representation）__

 “资源” 是一种信息实体，它可以有多种外在表现形式。我们把 “资源” 具体呈现出来的形式，叫做它的 “表现层” （Representation）。

比如，文本可以用txt格式表现，也可以用HTML格式、XML格式、JSON格式表现，甚至可以采用二进制格式；图片可以用JPG格式表现，也可以用PNG格式表现。

URI只代表资源的实体，不代表它的形式。严格地说，有些网址最后的  “.html”  后缀名是不必要的，因为这个后缀名表示格式，属于 “表现层” 范畴，而URI应该只代表 “资源” 的位置。它的具体表现形式，应该在HTTP请求的头信息中用Accept和Content-Type字段指定，这两个字段才是对 “表现层” 的描述。

__三、状态转化（State Transfer）__

访问一个网站，就代表了客户端和服务器的一个互动过程。在这个过程中，势必涉及到数据和状态的变化。

互联网通信协议 HTTP 协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生 “状态转化” （State Transfer）。而这种转化是建立在表现层之上的，所以就是 “表现层状态转化” 。

客户端用到的手段，只能是 HTTP 协议。具体来说，就是HTTP协议里面，四个表示操作方式的动词：GET、POST、PUT、DELETE。它们分别对应四种基本操作：GET 用来获取资源，POST 用来新建资源（也可以用于更新资源），PUT 用来更新资源，DELETE 用来删除资源。

综合上面的解释，我们总结一下什么是 RESTful 架构：

* （1）每一个URI代表一种资源；
* （2）客户端和服务器之间，传递这种资源的某种表现层；
* （3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现 “表现层状态转化” 。

[引用资料](http://www.ruanyifeng.com/blog/2011/09/restful)




原始封面

![课程图片](https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?w=300)

