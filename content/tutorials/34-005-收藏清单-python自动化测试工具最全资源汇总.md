---
weight: 5
title: '收藏清单: python自动化测试工具最全资源汇总'
date: '2017-10-22T08:19:06+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1642543492457-39a2ce63bb59?w=300
tags: []
categories:
- 测试工具合集
lightgallery: true
toc:
  auto: false
---



## Web UI test automation Web UI 自动化

- libraries 各种库
    * [selenium webdriver](https://pypi.python.org/pypi/selenium) - 浏览器自动化工具
    * [splinter](https://github.com/cobrateam/splinter) - 简单的web自动化工具，让元素定位，表单提交等更加容易
    * [mechanize](https://pypi.python.org/pypi/mechanize/) - 有状态可编程的浏览器
- frameworks and wrappers 框架和封装 
    * [py.saunter](https://github.com/element-34/py.saunter) - 有主见的自动化测试框架，使用了selenium RC和webdriver api
    * [moz-web-qa](https://github.com/davehunt/pytest-mozwebqa) - py.test的插件，为Mozilla的WebQA项目提供了额外功能
    * [testutils sst](http://testutils.org/sst) - A web test framework that uses Python to generate functional browser-based tests.
    * [wtframework](https://github.com/wiredrive/wtframework) - 让web测试可以配置的框架
    * [holmium.core](https://github.com/alisaifee/holmium.core) - Page Object及其他工具库支持
    * [robotframework-selenium2library](https://github.com/rtomac/robotframework-selenium2library) - Robot Framework的selenium扩展
    * [gocept.selenium](https://pypi.python.org/pypi/gocept.selenium) - selenium RC的API, 适合编写基于WSGI, Plone, Zope 2, ZTK, or Grok 应用的测试用例
    * [webium](https://github.com/wgnet/webium) - 基于python的一个Page Object实现
    * [robotframework-anywherelibrary](https://github.com/luisxiaomai/robotframework-anywherelibrary) - Robot Framework的扩展库，使用selenium2测试web应用，使用appium测试移动应用
    * [robotframework-pageobjects](https://github.com/ncbi/robotframework-pageobjects) - 一个不错的Page Object实现，可以脱离robot framework单独使用。 具体看[这里](http://kahunacohen.com/2014/12/03/new-testing-paradigm-robotframework-pageobjects/)
    * [elementium](https://github.com/actmd/elementium) - 用jQuery风格的语法糖来实现浏览器的自动化测试用例
    * [slickqa](http://www.slickqa.com/webdriver/python/) - slick-webdriver-python 项目是python selenium binding的一个封装
    * [selene](https://github.com/yashaka/selene/) - Concise UI 测试用例，使用python实现支持Ajax,PageObjects和Widgets
    * [hitch](http://hitchtest.com/) - 编写基于service的应用的测试用例
    * [Needle](http://needle.readthedocs.org/en/latest/) - Needle是基于图片比对的测试工作，它可以对web应用的一部分进行截图，然后跟预期结果的图片进行比对
    * [PyPOM](https://github.com/mozilla/PyPOM) - PyPOM是另一个Page Object库，适用于Selenium和Splinter测试
    * [POM](https://github.com/schipiga/pom) - POM是Page-Object-Model 微框架，目的是让Web UI测试更加简单，快速和有乐趣
    * [websmith](https://github.com/omaciel/websmith) - Web测试的一套DSL
    * [pages](https://github.com/Skyscanner/pages) -  轻量的page object库和组建
    * [widgetastic](https://github.com/nextQE/widgetastic.core) - RedHat UI widget 组建框架
    * [navmazing](https://github.com/nextQE/navmazing) - PageObjects based navigation from RedHat
    * [nightwatch](https://github.com/nextQE/nightwatch) - 基于python和selenium的UI 自动化测试框架. 灵感来源于nightwatch.js
- extensions 扩展
    * [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) - 主要目的是让不同版本的浏览器driver管理起来更加方便
    * [pytest_splinter](https://github.com/pytest-dev/pytest-splinter) - pytest spinter 和 selenium的集成 
    * [lettuce_webdriver](https://github.com/bbangert/lettuce_webdriver) - Selenium webdriver 的 lettuce封装
    * [Browsermob Proxy](https://github.com/AutomatedTester/browsermob-proxy-py) - python的Browsermob Proxy封装 
    * [FireRobot](https://github.com/joao-carloto/FireRobot) - 一个Firefox的扩展,让你可以更高效的编写基于robot framework的selenium用例
    * [pytractor](https://github.com/kpodl/pytractor) - Python的selenium扩展，以便更好的测试angular.js应用
    * [Selenium-Requests](https://github.com/cryzed/Selenium-Requests) - 扩展 Selenium WebDriver类，包含了Requests库的一些功能，可以更方便的处理cookie和请求头
    * [selenium-respectful](https://github.com/SerpentAI/selenium-respectful) - selenium的封装，可以并行访问站点

## Mobile test automation 移动端自动化测试工具

* [appium](http://appium.io/) - 开源的自动化测试框架，可以测试native/hybrid/mobile web应用。核心是基于webdriver协议进行了扩展
* [Winium.StoreApps](https://github.com/2gis/Winium.StoreApps/) - 开源的自动化测试用具，用来测试Windows Store应用，实现了Selenium Remote WebDriver
* [robotframework-androidlibrary](https://github.com/lovelysystems/robotframework-androidlibrary) - Robot Framework用来测试android应用的扩展库
* [robotframework-appiumlibrary](https://github.com/jollychang/robotframework-appiumlibrary) - appium的RobotFramework扩展
* [robotframework-ioslibrary](https://github.com/lovelysystems/robotframework-ioslibrary) -Robot的ios测试扩展库
* [uiautomator](https://github.com/xiaocong/uiautomator) - Android uiautomator的python封装, 支持 Android 4.1+ 
* [ATX](https://github.com/NetEaseGame/ATX) - 智能机自动化测试工具. 支持 iOS, Android, WebApp 和游戏

## Windows UI test automation Windows的UI测试工具

* [Winium.Desktop](https://github.com/2gis/Winium.Desktop/) - 测试Windows应用(主要是基于WinForms和WPF平台)的自动化测试工具. 实现了Selenium Remote WebDriver协议
* [PyAutoGUI](https://pypi.python.org/pypi/PyAutoGUI) - 跨平台的GUI测试工具，支持通过python脚本控制键盘和鼠标
* [robotframework-autoitlibrary](https://code.google.com/p/robotframework-autoitlibrary/) - Robot Framework的windows GUI测试扩展
* [autopy](https://github.com/msanders/autopy) - 简单跨平台的GUI测试工具集
* [UISoup](https://pypi.python.org/pypi/UISoup/) - 支持windows和MacOS平台的UI自动化(仅工作在x86平台)
* [pywinauto](http://pywinauto.github.io/) - 非常有python面向对象风格的GUI测试库，现已支持64位机器以及py2和py3
* [SikuliX](http://sikulix.com/) - 基于OpenCV的 GUI 测试框架, 使用图片识别技术，支持python2.7

## Unix \ Linux UI test automation

* [ldtp](https://pypi.python.org/pypi/ldtp) - 跨平台的linux GUI测试项目
* [fMBT](https://github.com/01org/fMBT) - 支持多平台的python GUI测试库
* [SikuliX](http://sikulix.com/) - 基于OpenCV的 GUI 测试框架, 使用图片识别技术，支持python2.7

## MacOS UI test automation MacOS UI自动化测试工具

* [ATOMac](https://github.com/pyatom/pyatom) - 通过Apple Accessibility API来测试Mac应用的python库
* [PyAutoGUI](https://pypi.python.org/pypi/PyAutoGUI) - 跨平台的GUI测试工具，支持通过python脚本控制键盘和鼠标
* [SikuliX](http://sikulix.com/) - 基于OpenCV的 GUI 测试框架, 使用图片识别技术，支持python2.7



原始封面

![课程图片](https://images.unsplash.com/photo-1642543492457-39a2ce63bb59?w=300)

