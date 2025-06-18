---
weight: 0
title: 轻量级Selenium测试框架pyse
date: '2017-12-04T10:10:24+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1508163223045-1880bc36e222?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



#### 前言
---
在2015年的时候，我新进入了一家公司，刚去没什么工作安排，老大让我熟悉一下当前部门的产品，看有什么可以做自动化的产品，然后就试着做做。

然后，我就开始对一个论坛产品下手，写了一个多月的UI自动化，近三百条测试用例，在此过程中，对Selenium开发有了更深一层的认识。顺手基于Selenium写了个框架 pyse。

Pyse的命名分别取了“Python”和“Selenium”的前两个字母。现在看来这名字起得过于随意了，其实，它也只是我对Selenium二次开发的一点尝试。后来，我被分配去负责测试一个接口平台，论坛的自动化项目由于没人能接手，就丢一边了。这其中原因很多，Python +Selenium开发自动化测试有一定的门槛；测试任务比较重，没时间去接手自动化，还有，主动学习意愿不强，不是每个测试同学都对技术有追求的，对吧？！

最近对pyse进行了一些重构，所以拿来分享一下。

#### 为什么要对Selenium进行封装和二次开发？
---
对于原生的Selenium，我们用它来开发Web UI自动化测试，当你自动化测试用例写多了，就会发现，这TM就是一体力活，大部分时间就是拿个前端开发者工具（FireBug等）在尝试定位元素。比起手工测试毫无优越感好吧！

当你的自动化测试用例达到一定规模的时候，逐渐就会意识原生Selenium的不好用。隐式等待不起作用，显式等待写起来太麻烦，sleep太耗时。

单个用例运行好好的，放到一起运行，每次总有那么一两条用例“调皮”，运行不通过！

还有每条用例都打开和关闭一次浏览器，严重拖慢用例的运行速度。

还有....

总之，遇到的各种问题，不是只会Selenium API就能解决的。接下来，你就要考虑对Selenium进行封装和二次开发了。

#### Pyse特点
---
项目地址：https://github.com/defnngj/pyse

Pyse正是我为了解决前面的部分问题而设计的，它主要基于Selenium和unittest单元测试框架。

* 支持多种定位方法（id\name\class\link_text\xpath\css）。
* 本框架只是对selenium（webdriver）原生方法进行了简单的封装，精简为大约30个方法，这些方法基本能够胜任于我们的web自动化测试。
* 以测试类为单位，自动打开和关闭浏览器，减少浏览器的打开/关闭次数，节省时间。
* 自动生成/report/目录，以及HTML测试报告生成。
* 针对Selenium的特点封装断言方法：assertTitle、assertUrl 和 assertText。


#### 安装：
---
把整个项目克隆（下载）下来，进入pyse/目录，执行:

> python setup.py install

#### Demo:
---
创建 test_case.py 文件。
```Python
import pyse

class BaiduTest(pyse.TestCase):

    def test_baidu(self):
        ''' baidu search key : pyse '''
        self.driver.open("https://www.baidu.com")
        self.driver.clear("id=>kw")
        self.driver.type("id=>kw", "pyse")
        self.driver.click("css=>#su")
        self.assertTitle("pyse")

if __name__ == '__main__':
    runner = pyse.TestRunner()
    runner.run()
```

1、首先导入 pyse库。
2、创建BaiduTest类继承 pyse的TestCase类。
3、创建test_baidu()测试方法（用例）。
4、接下来就是通过self.driver（默认使用 Chrome浏览器）来做百度搜索的操作；最后，使用assertTitle() 来断言浏览器标题是否包含“pyse”。
5、调用pyse的TestRunner() 类，通过它提供的 run() 方法来运行测试。

__注意__：这里的测试用例文件（test_case.py）和测试方法（test_baidu()）必须以“test”开头

最后，运行上面的测试用例，pyse 自动生成/report 目录，以及 HTML测试报告。

![](https://raw.githubusercontent.com/defnngj/pyse/master/test_report.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1508163223045-1880bc36e222?w=300)

