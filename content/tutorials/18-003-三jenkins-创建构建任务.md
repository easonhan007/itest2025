---
weight: 3
title: （三）Jenkins 创建构建任务
date: '2017-10-16T13:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1599486858190-a56a25d4616b?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



#### 构建项目类型
----

点击 Jenkins 首页 __“创建一个新任务”__ 的链接，弹出如图3.1所示页面。

![](http://img.testclass.net/jenkins_project_type.png)


图3.1  选择Jenkins任务类型

__Jenkins 提供了六种类型的任务。__

* 构建一个自由风格的软件项目

这是Jenkins的主要功能。Jenkins 会结合任何 SCM 和任何构建系统来构建你的项目, 甚至可以构建软件以外的系统。

* Pipeline

Orchestrates long-running activities that can span multiple build slaves. Suitable for building pipelines (formerly known as workflows) and/or organizing complex activities that do not easily fit in free-style job type. -- 很难用一两句话说清 Pipeline, [参考](https://github.com/jenkinsci/pipeline-plugin/blob/master/TUTORIAL.md) , 后面另起一文来介绍。

* 构建一个多配置项目

适用于多配置项目,例如多环境测试、平台指定构建,等等。

* GitHub Organization

Scans a GitHub organization (or user account) for all repositories matching some defined markers. --这个主要针对由 Github 托管的项目。

* Multibranch Pipeline

Creates a set of Pipeline projects according to detected branches in one SCM repository.
根据一个SCM存储库中检测到的分支创建一组 __Pipeline__ 项目。

* 文件夹

创建一个可以嵌套存储的容器。利用它可以进行分组。 视图仅仅是一个过滤器，而文件夹则是一个独立的命名空间， 因此你可以有多个相同名称的的内容，只要它们在不同的文件 夹里即可。

这里选择第一个：构建一个自由风格的软件项目， 输入项目名称：python test project ，点击 “OK”按钮。

#### 构建 Windows 测试任务
----

假设，我们有一个 Python 编写的测试脚本 py_tests.py ，位于电脑 __D盘__ 根目录，内容如下：

```python
import unittest, time
from selenium import webdriver


class TestClass(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.base_url = "http://www.testclass.net"

	def tearDown(self):
		time.sleep(2)
		self.driver.quit()

	def test_case(self):
		self.driver.get(self.base_url)
		search_input = self.driver.find_element_by_name("q")
		search_input.send_keys("selenium")
		search_input.submit()

	def test_case2(self):
		self.driver.get(self.base_url)
		search_input = self.driver.find_element_by_name("q")
		search_input.send_keys("jenkins")
		search_input.submit()


if __name__ == '__main__':
	unittest.main()
```

如果是在 Windows 下应该如何执行这个测试用例呢？ 打开 Windows 命令提示符（CMD）。

```
Microsoft Windows [版本 10.0.15063]
(c) 2017 Microsoft Corporation。保留所有权利。

C:\Users\name> python d:/py_tests.py
..
----------------------------------------------------------------------
Ran 2 tests in 22.371s

OK

D:\>

```
<font color='red' >不明白什么意思？ 那么你记清我上面运行 python 程序时所敲的一行 dos 命令。</font>

下接来回到 Jenkins 的配置过程中，

![](http://img.testclass.net/jenkins_project_describe.png)

添加项目的描述：selenium 自动化测试项目。

剩下的选项都不要管，拖到页面底部，__构建__ 选项。

![](http://img.testclass.net/jenkins_project_build_type.png)

选择 __“Execute Windows batch command”__ 选项，执行Windows批处理命令。

![](http://img.testclass.net/jenkins_project_build_command.png)

如上图，输入你在 windows 命令提示符下所输的命令（__python d:/py_tests.py__）。 点击 __“保存”__。

![](http://img.testclass.net/jenkins_project_complete.png)

一个极简的，基于 Windows 系统的，Python 脚本测试的 持续集成项目就创建完成了。

<font color='red'> 继续下一篇幅。</font>




原始封面

![课程图片](https://images.unsplash.com/photo-1599486858190-a56a25d4616b?w=300)

