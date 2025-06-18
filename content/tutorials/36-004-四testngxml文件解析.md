---
weight: 4
title: （四）testng.xml文件解析
date: '2017-11-25T12:45:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507209696998-3c532be9b2b5?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



TestNG 与 Junit 比较大的一个差异就是前者通过 testng.xml 文件来配置测试用例的执行。 testng.xml文件可以很好的控制要执行的测试用例的粒度，及各种运行策略。

目前testng.xml DTD（Document Type Definition; DTD是一种XML的约束方式。） 配置说明可以在：[这里](http://testng.org/testng-1.0.dtd.php)

#### testng.mxl 文件解析
---
```
<suite name="Suite1" verbose="1" >
  <test name="Nopackage" >
    <classes>
       <class name="NoPackageTest" />
    </classes>
  </test>

  <test name="Regression1">
    <classes>
      <class name="test.sample.ParameterSample"/>
      <class name="test.sample.ParameterTest"/>
    </classes>
  </test>
</suite>
```
* `<suite>...</suite>`  表示定义了的一个测试套件。
  *  name 定义测试套件的名称。
  *  verbose 定义命令行信息打印等级，不会影响测试报告输出内容；可选值(1|2|3|4|5) 
* `<test>...</test>` 表示定义了一个测试。
  *  name 定义测试的名称。
* `<classes>...</classes>`  表示定义一组测试类。
* `<class .../>` 表示定义一个测试类。
   * name 指定要运行的测试类


#### 实例
---
测试项目目录结果如下：

![](http://img.testclass.net/testng_project.png)

testng.mxl 配置文件如下：

```
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="测试套件" verbose="1" >
    <test name="简单测试">
        <classes>
            <class name="test.sample.FirstTest"/>
            <class name="test.sample.SecondTest"/>
        </classes>
    </test>
</suite>
```

* `<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >` 必须要添加，表示遵循的规范文件。

在 __testng.xml__ 文件上右键点击运行测试。

运行结果如下：

![](http://img.testclass.net/testng_run_result.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1507209696998-3c532be9b2b5?w=300)

