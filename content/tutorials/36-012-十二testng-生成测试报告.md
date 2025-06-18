---
weight: 12
title: （十二）TestNG 生成测试报告
date: '2017-11-25T12:10:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1501556424050-d4816356b73e?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



TestNG 默认自带的有HTML格式的测试报告。这也充分说明拿它来做 UI 自动化测试的优势。

#### 通过 Maven 生成报告
---
切换到 __TestngTest__ 项目的跟目录下，通过 `mvn test` 命令运行测试。

```
TestngTest> mvn test

[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building TestngTest 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO]
[INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ TestngTest
 --- [WARNING] Using platform encoding (GBK actually) to copy filtered resources,
  i.e. build is platform dependent!
[INFO] Copying 0 resource

...

-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running TestSuite
Configuring TestNG with: org.apache.maven.surefire.testng.conf.TestNG652Configurator@104e3b2
Tests run: 19, Failures: 5, Errors: 0, Skipped: 2, Time elapsed: 3.862 sec <<< FAILURE!
```
在该系列教程开始前，我已经说明了整个项目基于 [Maven](/maven/) 创建。

现在打开 __..\TestngTest\target\surefire-reports\index.html__ 将会看到整个项目的运行结果。

![](http://img.testclass.net/testng_run_report.png)

#### 通过 IntelliJ IDEA 生成测试报告
---
在 [IntelliJ IDEA](/idea/) 中默认运行测试用例是不会生成HTML报告的，需要进行简单的配置。

菜单栏： “Run” -->“Edit Configuraction...” 。

![](http://img.testclass.net/testng_idea_setting_report.png)

如上图，选择运行测试用例的 testng.xml 文件-->“Configuration”-->“Listeners”--> 勾选“Use default reporters” 选项， 最后点击“OK” 按钮， 完成设置。

好了！ 现在用 IntelliJ IDEA 运行 TestNG 测试用例一样可以生成报告了。




原始封面

![课程图片](https://images.unsplash.com/photo-1501556424050-d4816356b73e?w=300)

