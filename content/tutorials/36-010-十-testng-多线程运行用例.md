---
weight: 10
title: （十） TestNG 多线程运行用例
date: '2017-11-25T12:15:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



TestNG 是我接触过的唯一自身支持多程技术的单元测试框架。虽然代码级别的单元测试运行得很快，多线程的意义并不大。但如果是UI自动化测试的话运行速度就会非常慢，这个时候多线程技术就会变得很重要。

#### 多线程配置
---
这里只介绍 __testng.xml__ 文件，其中的使用到的测试用例，请参考前面的章节创建。
```
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="测试套件" parallel="classes" thread-count="2" >
    <test name="简单测试">
        <classes>
            <class name="test.sample.FirstTest" />
            <class name="test.sample.SecondTest" />
        </classes>
    </test>
</suite>
```
* parallel 设置多线程的级别划分。
 * parallel="methods": TestNG将在不同的线程中运行所有的测试方法。依赖方法也将在单独的线程中运行，但它们将尊重你指定的顺序。

 * parallel="tests": TestNG 将在同一个线程中运行相同的<test>标记的所有方法，但是每个<test>标记将在一个单独的线程中。这允许你将所有非线程安全的类分组在同一个<test>中，并保证它们将在同一个线程中运行，同时利用尽可能多的线程来运行测试。

 * parallel="classes": TestNG将在同一个线程中运行同一个类中的所有方法，但是每个类都将在一个单独的线程中运行。

 * parallel="instances": TestNG将在同一个线程中运行相同实例中的所有方法，但是在两个不同实例上的两个方法将在不同的线程中运行。

* thread-count 用于指定线程的个数。




原始封面

![课程图片](https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=300)

