---
weight: 2
title: （二）Hello world
date: '2018-01-17T14:45:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1551033406-611cf9a28f67?w=300
tags: []
categories:
- Java语言基础教程
lightgallery: true
toc:
  auto: false
---



#### Hello world
---

按照管理先用Java写一个 "Hello world" 。

```Java
package Base;

public class HelloWrold {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

__main()方法的定义：__

`main()`方法是Java应用程序的入口方法，也就是程序运行时的第一个方法。声明为：`public static void main()`。

* public static：由于JVM在运行这个Java应用程序的时候，首先会调用main()方法，调用时不实例化这个类的对象，而是通过类名直接调用因此需要是限制为`public static` 即 `main()` 方法是一个公共的（public）静态（static）方法。

* void ： JVM有限制，因此不能有返回值类型为void。

* String[] args : main()方法中必须有一个入参，必须是字符串数组（`String[]`），这个是java的规范。至于字符串数组的名字，是可以随便取的。但根据习惯，这个字符串数组的名字一般和SUN Java规范范例中main参数名保持一致，取名为args。

__println()方法输出__

因为Java不允许独立于类外的方法存在，所以在命名空间内不存在直接的类函数调用。

`System`是`java.lang`中的一个类。 `System.out`中的`out`代表了`System`类中的静态对象`PrintStream`，`println()`是`PrintStream`中的方法。




原始封面

![课程图片](https://images.unsplash.com/photo-1551033406-611cf9a28f67?w=300)

