---
weight: 2
title: （二）环境安装之IntelliJ IDEA
date: '2017-07-06T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1529071242804-840f9a164b8b?w=300
tags: []
categories:
- slenium java 语言教程
lightgallery: true
toc:
  auto: false
---



<br>
### 安装IntelliJ IDEA

你可能会问，为什么不用Eclipse呢？随着发展IntelliJ IDEA有超越Eclipse的势头，JetBrains公司的IDE基本上已经一统了各家主流编程语言的江湖。考虑到 Java IDE的流行趋势，本书中决定选用IntelliJ IDEA。

当然， 选择什么样的IDE充满着个人喜好。你依然可以参考其它资料安装Java IDE。这不会影响你阅读该系列文章。
点击 [IntelliJ IDEA下载](https://www.jetbrains.com/idea)，根据自己的平台，选择相应的版本进行下载。

IntelliJ IDEA安装过程省略...

如果第一次打开IntelliJ IDEA，会看到如下界面。
![](http://orru5lls3.bkt.clouddn.com/idea.png)

点击"Create New Project"选项创建新的Java项目。选择项目类型为Java，然后，继续"Next"。
![](http://orru5lls3.bkt.clouddn.com/idea2.png)

* Project name: 项目名称。

* Project location: 项目在硬盘上的路径。

点击"Finish"结束项目创建完成。

<br>
### 编写Hello World！

首先，打开IntelliJ IDEA，点击左侧项目列表，在src下面创建__包__和__类文件__。

1)右键左侧项目列表 src--->New ---> Package 弹出窗口， 输入包的名：javaBase。

2)右键左侧创建的包名：java --->New ---> Java Class 弹出窗口， 输入类的名：HelloWorld。
![](http://orru5lls3.bkt.clouddn.com/idea4.png)

在 HelloWorld.java 文件中编写第一个 Java 程序。
```java
package com.java.base;

public class HelloWorld {
  public static void main(String[] args){
    System.out.println("hello world");
  }
}
```
输入完成， 点击工具栏 Run 按钮(或在代码文件中右键选择"Run 'HelloWorld.main()'")运行， 将会在控制台看到“hello word” 的输出。




原始封面

![课程图片](https://images.unsplash.com/photo-1529071242804-840f9a164b8b?w=300)

