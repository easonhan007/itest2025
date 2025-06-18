---
weight: 3
title: （三）TestNG 之 FixTrue
date: '2017-11-25T12:45:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1600275669439-14e40452d20b?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---




#### 什么是Fixture
----
Test Fixture 是指一个测试运行所需的固定环境，准确的定义：

> The test fixture is everything we need to have in place to exercise the SUT

在进行测试时，我们通常需要把环境设置成已知状态（如创建对象、获取资源等）来创建测试，每次测试开始时都处于一个固定的初始状态；测试结果后需要将测试状态还原，所以，测试执行所需要的固定环境称为 Test Fixture。

#### TestNG 提供的 Fixture 方法
---

表：

|   注解    |   说明    |
|:----------|:----------|
|@BeforeSuite| 注解的方法在测试套件（中的所有用例）开始前运行一次|
|@AfterSuite | 注解的方法在测试套件（中的所有用例）结束后运行一次。|
|@BeforeClass| 注解的方法在当前测试类（中所有用例）开始前运行一次。|
|@AfterClass | 注解的方法在当前测试类（中所有用例）结束后运行一次。|
|@BeforeTest | 对于套件测试，在运行属于<test>标签内的类的所有测试方法之前运行。|
|@AfterTest  | 对于套件测试，在运行属于<test>标签内的类的所有测试方法之后运行。|
|@BeforeGroups| 在调用属于该组的所有测试方法之前运行。|
|@AfterGroups | 在调用属于该组的所有测试方法之后运行。|
|@BeforeMethod| 注解的方法将在每个测试方法之前运行。|
|@AfterMethod | 注释的方法将在每个测试方法之后执行。|

#### 实例
---

接下来通过例子演示上面部分注解的用法。
```java
import org.testng.annotations.*;


public class FixtureTest {

    //在当前测试类开始时运行。
    @BeforeClass
    public static void beforeClass(){
        System.out.println("-------------------beforeClass");
    }

    //在当前测试类结束时运行。
    @AfterClass
    public static void afterClass(){
        System.out.println("-------------------afterClass");
    }

    //每个测试方法运行之前运行
    @BeforeMethod
    public void before(){
        System.out.println("=====beforeMethod");
    }

    //每个测试方法运行之后运行
    @AfterMethod
    public void after(){
        System.out.println("=====afterMethod");
    }

    @Test
    public void testCase1(){
        System.out.println("test case 1");
    }

    @Test
    public void testCase2(){
        System.out.println("test case 2");
    }


}

```

运行上面的测试，执行结果如下。

```
-------------------beforeClass
=====beforeMethod
test case 1
=====afterMethod
=====beforeMethod
test case 2
=====afterMethod
-------------------afterClass

===============================================
Default Suite
Total tests run: 2, Failures: 0, Skips: 0
===============================================
```



原始封面

![课程图片](https://images.unsplash.com/photo-1600275669439-14e40452d20b?w=300)

