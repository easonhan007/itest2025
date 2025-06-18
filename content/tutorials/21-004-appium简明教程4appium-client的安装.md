---
weight: 4
title: appium简明教程（4）——appium client的安装
date: '2017-08-17T07:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1462332420958-a05d1e002413?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



appium client是对webdriver原生api的一些扩展和封装。它可以帮助我们更容易的写出用例，写出更好懂的用例。

appium client是配合原生的webdriver来使用的，因此二者必须配合使用缺一不可。

从本节开始，教程的内容将涵盖3个语言，ruby/python/java。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途

### 安装appium client

#### ruby篇（一定要在线安装）

ruby的appium client叫做appium lib，为什么是这样就不解释了，总之是历史原因。

首先update rubygem和bundler(说老实话，真的不需要，但官方文档上这么写)

```
gem update --system ;\
gem update bundler
```

然后使用gem安装

```
gem uninstall -aIx appium_lib ;\(这个也不是必须的)
gem install --no-rdoc --no-ri appium_lib
```

#### python篇（尽量在线安装）

推荐使用pip安装

```
pip install Appium-Python-Client
```

当然了也可以在Pipy上下载源码安装

```
tar -xvf Appium-Python-Client-X.X.tar.gz（windows上用7zip可以解压）
cd Appium-Python-Client-X.X
python setup.py install
```

最后，也可以通过github安装（要git客户端）

```
git clone git@github.com:appium/python-client.git
cd python-client
python setup.py install
```

#### java篇（在线安装）

java的话用maven安装就可以了

```
<dependency>
  <groupId>io.appium</groupId>
  <artifactId>java-client</artifactId>
  <version>1.3.0</version>
</dependency>
```

当然了，也可以自己[下载jar包](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22io.appium%22%20AND%20a%3A%22java-client%22)，请自行选择最新版本。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1462332420958-a05d1e002413?w=300)

