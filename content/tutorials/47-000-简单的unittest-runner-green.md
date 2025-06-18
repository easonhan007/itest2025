---
weight: 0
title: '简单的unittest runner: green'
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1523978591478-c753949ff840?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



首先来个截图。

![](https://raw.githubusercontent.com/CleanCut/green/master/img/screenshot.png)

green是unittest 众多runner中功能比较丰富的一个。

官方的featrue介绍如下：

```
Clean - Low redundancy in output. Result statistics for each test is vertically aligned.
Colorful - Terminal output makes good use of color when the terminal supports it.
Fast - Tests run in independent processes. (One per processor by default. Does not play nicely with gevent)
Powerful - Multi-target + auto-discovery.
Traditional - Use the normal unittest classes and methods for your unit tests.
Descriptive - Multiple verbosity levels, from just dots to full docstring output.
Convenient - Bash-completion and ZSH-completion of options and test targets.
Thorough - Built-in integration with coverage.
Embedded - Can be run with a setup command without in-site installation.
Modern - Supports Python 3.5+. Additionally, PyPy is supported on a best-effort basis.
Portable - macOS, Linux, and BSDs are fully supported. Windows is supported on a best-effort basis.
Living - This project grows and changes. See the changelog
```

简单来说，green的一些优势有：

* 简单高效
* 命令行输出支持各种高亮
* 一直在维护
* 支持python3
* 集成了代码覆盖率

### 安装

```
pip install green
```

### 简单使用

我们可以用官方的例子来简单玩一下。

```
git clone https://github.com/CleanCut/green.git
cd green/example/proj
green -vvv --run-coverage
```

### 运行结果

```
Green 3.0.0, Coverage 4.5.4, Python 2.7.15

proj.test.test_foo
  TestAnswer
.   answer() returns 42
.   answer() returns an integer
  TestSchool
.   test_age
.   test_food

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
__init__.py              0      0   100%
foo.py                   7      0   100%
subpkg/__init__.py       0      0   100%
--------------------------------------------------
TOTAL                    7      0   100%

Ran 4 tests in 0.123s using 8 processes

OK (passes=4)
```

因为我是纯文本贴出来的，所以没能体现出高亮的效果。大家可以自己试着运行一下，在mac上还是很好看的。windows上表现怎么样还不是很清楚。

### 适用场景

* green支持跟django集成，可以替换django的默认testrunner
* green支持的配置很多，可以敲```green -h```来看，可以作为自己测试项目的基础框架，从而实现更多功能










原始封面

![课程图片](https://images.unsplash.com/photo-1523978591478-c753949ff840?w=300)

