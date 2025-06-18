---
weight: 0
title: 选读：Selenium的发展史
date: '2017-08-25T02:20:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1511576661531-b34d7da5d0bb?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---



![](http://img.testclass.net/selenium-logo.png)

Jason Huggins在2004年发起了Selenium项目，当时身处ThoughtWorks的他，为了不想让自己的时间浪费在无聊的重复性工作中，幸运的是，所有被测试的浏览器都支持Javascript。Jason和他所在的团队采用Javascript编写一种测试工具来验证浏览器页面的行为；这个JavaScript类库就是Selenium core，同时也是seleniumRC、Selenium IDE的核心组件。Selenium由此诞生。

关于Selenium的命名比较有意思，当时QTP mercury是主流的商业自化工具，是化学元素汞（俗称水银），而Selenium是开源自动化工具，是化学元素硒，硒可以对抗汞。



### Selenium 1.0

![](http://img.testclass.net/selenium_1.jpg)

用简单的公式：

```
Selenium 1.0 = Selenium IDE + Selenium Grid + Selenium RC
```
__Selenium IDE__

Selenium IDE是嵌入到Firefox浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能。

__Selenium Grid__

Selenium Grid是一种自动化的测试辅助工具，Grid通过利用现有的计算机基础设施，能加快Web-App的功能测试。利用Grid可以很方便地实现在多台机器上和异构环境中运行测试用例。

__Selenium RC__

Selenium RC（Remote Control）是Selenium家族的核心部分。Selenium RC 支持多种不同语言编写的自动化测试脚本，通过Selenium RC的服务器作为代理服务器去访问应用，从而达到测试的目的。

Selenium RC分为Client Libraries和Selenium Server。Client Libraries库主要用于编写测试脚本，用来控制Selenium Server的库。Selenium Server负责控制浏览器行为。

所以，我们在学习Selenium1.0的时候，核心应该是学习RC，它的工作原理是这样的：

![](http://img.testclass.net/selenium_RC.jpg)


在2006年的时候，Google的工程师Simon Stewart发起了WebDriver的项目；因为长期以来Google一直是Selenium的重度用户，但却被限制在有限的操作范围内。

Selenium RC 是在浏览器中运行JavaScript应用，使用浏览器内置的JavaScript翻译器来翻译和执行selenese命令（selenese是Selenium命令集合）。

WebDriver是通过原生浏览器支持或者浏览器扩展来直接控制浏览器。WebDriver针对各个浏览器而开发，取代了嵌入到被测Web应用中的JavaScript，与浏览器紧密集成，因此支持创建更高级的测试，避免了JavaScript安全模型导致的限制。除了来自浏览器厂商的支持之外，WebDriver还利用操作系统级的调用，模拟用户输入。

Selenium与WebDriver原是属于两个不同的项目，WebDriver的创建者Simon Stewart早在2009年8月的一份邮件中解释了项目合并的原因。

<font color=#0099ff >
Selenium与WebDriver合并原因：为何把两个项目合并？部分原因是WebDriver解决了Selenium存在的缺点（例如能够绕过JavaScript沙箱，我们有出色的API），部分原因是Selenium解决了WebDriver存在的问题（例如支持广泛的浏览器），部分原因是因为Selenium的主要贡献者和我都觉得合并项目是为用户提供最优秀框架的最佳途径。
</font>

### Selenium 2.0
因为Selenium和Webdriver的合并，所以，Selenium 2.0由此诞生。简单用公式表示为：

```
Selenium 2.0 = Selenium 1.0 + WebDriver
```

需要强调的是，在Selenium 2.0中主推的是WebDriver，可以将其看作Selenium RC的替代品。因为Selenium为了保持向下的兼容性，所以在Selenium 2.0中并没有彻底地抛弃Selenium RC。

所以，我们在学习Selenium2.0的时候，核心是学习WebDriver。它的工作原理是这样的：

![](http://img.testclass.net/selenium_wd.jpg)


大概是在2013年的时候，那一年我刚开始深入的学习和使用Selenium，我通过Selenium官方博客上了解到，Selenium团队将会在圣诞节发布Selenium3.0，然后，我开始期待即将到来的3.0版，后来就没有了后来，很多年过去了，依然没等到Selenium3.0。

直到2016年7月，Selenium3.0悄悄发布第一个beta版。惊不惊喜，意不意外？他们是这么解释的：

<font color=#0099ff >
“在seleniumconf 2013，我们宣布，Selenium的一个新的主要版本将在‘圣诞节’发布。幸运的是，我们从来没有说过哪个圣诞节，因为我们已经花了一段时间来做我们想做的所有改变！我们很兴奋地宣布第一个bate版--Selenium 3.0 - beta1的发布。”
</font>

### Selenium 3.0

Selenium 3.0做了一些不大不小的更新：

1、终于去掉了RC，简单用公式表示为：

```
Selenium 3.0 = Selenium 2.0 - Selenium RC（Remote Control）
```

2、Selenium3.0只支持Java8版本以上。

3、Selenium3.0中的Firefox浏览器驱动独立了，以前装完selenium2就可以驱动Firefox浏览器了，现在和Chrome一样，必须下载和设置浏览器驱动。

4、MAC OS 集成Safari的浏览器驱动。默认在/usr/bin/safaridriver 目录下。

5、只支持IE 9.0版本以上。




原始封面

![课程图片](https://images.unsplash.com/photo-1511576661531-b34d7da5d0bb?w=300)

