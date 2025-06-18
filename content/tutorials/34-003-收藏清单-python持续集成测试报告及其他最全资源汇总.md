---
weight: 3
title: '收藏清单: python持续集成测试报告及其他最全资源汇总'
date: '2017-10-25T08:19:06+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1456324504439-367cee3b3c32?w=300
tags: []
categories:
- 测试工具合集
lightgallery: true
toc:
  auto: false
---



## Continuous Integration 持续集成

* [buildbot](https://pypi.python.org/pypi/buildbot/) - 自动化编译发布系统。大部分的软件项目可用
* [jenkins](http://jenkins-ci.org/) - 可扩展的开源持续集成server
* [travis-ci](https://travis-ci.org) - 免费的持续集成平台

## Reporting 报告

* [allure pytest](https://github.com/allure-framework/allure-python) - PyTest的allure适配器
* [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html) - Python 标准库unittest的扩展. 生成简单好用的html报告
* [unittest-xml-reporting](https://github.com/xmlrunner/unittest-xml-reporting) - 一个unittest test runner可以将测试结果保存到 XML文件。可高度定制

## Documentation generation 文档生成

* [Sphinx](http://sphinx-doc.org/) - Python文档生成器
* [MkDocs](http://www.mkdocs.org/) - Markdown语法友好的文档生成器
* [Pycco](http://fitzgen.github.io/pycco/) - The original quick-and-dirty, hundred-line-long, literate-programming-style documentation generator.

## Editors, IDE, consoles 编辑器, IDE以及命令行工具

* [pycharm](https://www.jetbrains.com/pycharm/) - 智能的专业的python IDE
* [pydev](http://pydev.org/) - eclipse 上全功能的python插件
* [sublime](http://sublimetext.com/) - 简洁好用的文本编辑器
* [ipython](http://ipython.org/) - 支持多语言的交互式shell, 最初是为python开发

## Useful libs 有用的库

一些可以让你构建更好的自动化测试的库

* [requests](https://pypi.python.org/pypi/requests/) - Apache2 Licensed的HTTP库, python实现，api友好
* [WebTest](http://webtest.readthedocs.org/en/latest/) - WebTest帮助你测试 WSGI-based web应用
* [lxml](http://lxml.de/) - 功能强大使用简单的XML和HTML处理器
* [suds](https://fedorahosted.org/suds/) - 轻量的SOAP python客户端
* [fabric](http://www.fabfile.org/) - shh到目标机器执行管理任务的python库和命令行工具
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) - 解析html文档的包。可以用来从html里抓取数据，配合爬虫使用
* [Soupy](https://github.com/ChrisBeaumont/soupy) -  BeautifulSoup的封装，目的在做网页爬虫的时候可以更容易的构造复杂的查询
* [PyQuery](https://pythonhosted.org/pyquery/) - Pyquery 使用jquery语法处理xml文档. API跟jquery尽可能的相似. pyquery 使用lxml快速操作xml和html
* [waiting](https://github.com/vmalloc/waiting) - python utility library for waiting for predicates.
* [Comcast](https://github.com/tylertreat/Comcast/) - 弱网模拟
* [dateutil](https://pypi.python.org/pypi/python-dateutil) - Python 标准模块datetime的扩展
* [python-tesseract](https://code.google.com/p/python-tesseract/) - tesseract OCR 的封装(Linux & Mac & Windows)
* [pywinrm](https://github.com/diyan/pywinrm/) - Windows Remote Management (WinRM)的python客户端. 可以在任何按照了python的远程windows机器上执行命令. WinRM可以调用 Windows的native对象. 包括但不限于运行批处理脚本, powershell脚本和获取WMI变量. 更多关于 WinRM的信息请访问微软的 WinRM站点
* [fig](http://www.fig.sh/) - 使用[Docker](https://www.docker.com/)快速构建隔离的开发环境
* [gitapi](http://bitbucket.org/haard/gitapi) - 纯Python实现的git API
* [Pyro4](https://github.com/irmen/Pyro4) - Pyro 可以构建一种内部的objects通过网络进行通信的应用
* [keyboard](https://github.com/boppreh/keyboard) - 模拟全局的键盘事件，支持 Windows 和 Linux
* [Errbot](http://errbot.io/en/latest/) - Errbot 一个聊天机器人
* [tappy](https://github.com/python-tap/tappy) - tappy 是支持Test Anything Protocol (TAP)协议的一组Python工具库. TAP 是line based 测试协议，目的是使用标准的方式录制测试数据
* [pyscreenshot](https://github.com/ponty/pyscreenshot) - pyscreenshot 模块可以把屏幕的内容拷贝给PIL或Pillow库去处理。 可以用来替换ImageGrab模块（只支持Windows）,所以windows不需要使用该库
* [TBVaccine](https://github.com/skorokithakis/tbvaccine) - TBVaccine可以清晰打印出python的错误堆栈。 它可以自动高亮你关心的行，并将变量着色，让堆栈更容易分析
* [PyPattyrn](https://github.com/tylerlaberge/PyPattyrn) - PyPattyrn 是一个可以让你更快速和更容易实现设计模式的python包
* [Spyne](http://spyne.io/) - Spyne is a Python RPC toolkit that makes it easy to expose online services that have a well-defined API using multiple protocols and transports.
* [Pexpect](https://pexpect.readthedocs.io/en/stable/) - Pexpect 让 Python 可以更好的控制其他应用
* [devtools-proxy](https://github.com/bayandin/devtools-proxy) - Chrome DevTools的代理. 完全兼容Selenium和ChromeDriver

# Resources 资源

发现新的库，资讯以及工具

* [python books](https://github.com/Junnplus/awesome-python-books)

## Websites 网站

* [automated-testing.info](http://automated-testing.info) - 自动化测试社区
* [atinfo.github.io/at.info-knowledge-base](http://atinfo.github.io/at.info-knowledge-base/)  - 各种工具和技术实现的自动化测试的例子
* [测试教程网](http://www.testclass.net/): 最权威的中文测试教程汇总网站



原始封面

![课程图片](https://images.unsplash.com/photo-1456324504439-367cee3b3c32?w=300)

