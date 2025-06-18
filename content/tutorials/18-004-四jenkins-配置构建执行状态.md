---
weight: 4
title: （四）Jenkins 配置构建执行状态
date: '2017-10-16T13:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1652987086659-2662433aed85?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



#### 运行构建
----

在项目 左侧列表点击 __“立即构建”__ ，在 “Build History” 列表，你会得到一个红色的小圆点，表示构建失败。

![](http://img.testclass.net/jenkins_build_run.png)

点击 构建失败的任务（红色的小圆点）。然后点击“Console Output” 就可以查看失败的 log 了。

![](http://img.testclass.net/jenkins_control_print_error.png)

提示：``` 'python' 不是内部或外部命令，也不是可运行的程序或批处理文件。```

我们明明在 Windows 提示符下运行是没有问题的。这是因为 Jenkins 缺少环境配置。

#### 配置构建执行状态
----
回到 Jenkins 首页，点击 __“构建执行状态”__ ,右则会列出本机信息，点击本机信息，配置 Python 的 path 环境变量。同时还需要添加浏览器驱动文件所在目录，[参考](/selenium_python/selenium3-browser-driver/) 。

![](http://img.testclass.net/jenkins_build_run_status.png)

<font color='red'> 如果你明白这块的话，说明你不懂 Python 语言，或不熟悉 Python 运行环境的配置。（不同技术的之间的配合使用存在一定的依赖关系！我们无法做到零基础。）</font>

配置完成，点击 __“保存”__ , 再来运行 __“立即构建”__ ，这次看到 py_tests.py 自动化脚本被执行了。

查看控制台输出：

![](http://img.testclass.net/jenkins_control_print.png)

好了！一个简单的 selenium + python 自动化测试的构建任务就创建完成了。

但对于 Jenkins 的学习，我们才刚刚开始。




原始封面

![课程图片](https://images.unsplash.com/photo-1652987086659-2662433aed85?w=300)

