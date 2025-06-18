---
weight: 6
title: （六）Package 和 Import
date: '2018-01-17T14:36:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1453060113865-968cea1ad53a?w=300
tags: []
categories:
- Java语言基础教程
lightgallery: true
toc:
  auto: false
---



除非你写的代码超级简单，如：打印。大多数情况情，必须会导入依赖的类。这些类大体上分三类：

* 由我们自己创建的类。

* 由Java JDK提供的类。

* 由第三方库或框架提供。


#### package
---
其实， package 名称就像是我们的姓，而 class
名称就像是我们的名字。package 名称有很多点号“ . ”，就好像是复姓。 比如说java.lang.String，就是复姓 java.lang，名字为 String 的类别。

Java 会使用package这种机制的原因也非常明显，就像我们取姓名一样， 光是一间学校的同一届同学中，就有可能会出现不少同名的同学，如果不取姓的话，那学校在处理学生资料，或是同学彼此之间的称呼，就会发生很大的困扰。幸运的是，Java 的套件名称我们可以自己取，不像人的姓没有太大的选择， 如果依照 Sun 的规范来取套件名称，那理论上不同人所取的套件名称不会相同 ( 请参阅 "命名惯例"的相关文章 )， 也就不会发生名称冲突的情况。

如， 我们可以用下面的方法使用 Selenium 的相关包。

```Java
public class JavaPackage {

    public static void main(String[] args) {
        org.openqa.selenium.WebDriver driver = new org.openqa.selenium.chrome.ChromeDriver();
        // ……
    }
}

```

#### import
---

显然上面的例子使编程变得很麻烦，我想使用某个类或方法，就不得写又臭又长的“复姓” 。 于是，Sun（Sun 公司目前已被 Oracle 公司收购） 想到了一个方法用 import 来优雅的解决这个问题。这个 import 就是在程式一开头的时候，先说明程式中会用到那些类别的简称，也就是只称呼名字，不称呼他的姓。姓在程序开头声明。

```Java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class JavaImport {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();

        //……
    }

}
```




原始封面

![课程图片](https://images.unsplash.com/photo-1453060113865-968cea1ad53a?w=300)

