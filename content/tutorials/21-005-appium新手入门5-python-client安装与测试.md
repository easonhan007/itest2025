---
weight: 5
title: appium新手入门（5）—— python-client安装与测试
date: '2017-09-07T10:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1437936251057-dfbf79980ce5?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



__关联阅读：__

[appium新手入门（1）—— appium介绍](/appium/appium-base-summary/)

[appium新手入门（2）—— 安装 Android SDK](/appium/appium-base-sdk/)

[appium新手入门（3）—— 安装 appium Server](/appium/appium-base-server/)

<br>
#### 前提条件
----

当你点击这一章时，说明你是打算使用 Python 语言编写 appium 自动化测试脚本的。

1、安装 [Python 语言](/selenium_python/install-selenium/) , Python的安装相对相简单得多。

2、Python 编辑器很多，推荐：PyCharm、Atom、Sublime text3等。这几款都是我常用的。


#### 安装 python-client
----

其实，[python-client](https://github.com/appium/python-client) 的项目名称叫：Appium-Python-Client。

推荐pip安装：

    (venv) λ pip install Appium-Python-Client
    Collecting Appium-Python-Client
      Using cached Appium-Python-Client-0.24.tar.gz
    Requirement already satisfied: selenium>=2.47.0 in d:\pyflask\venv\lib\site-packages (from Appium-Python-Client)
    Building wheels for collected packages: Appium-Python-Client
      Running setup.py bdist_wheel for Appium-Python-Client ... done
      Stored in directory: C:\Users\fnngj\AppData\Local\pip\Cache\wheels\2e\cf\10\0e3f177c9869147b16584d402f79d9007df1139105ea3ecc2c

    Successfully built Appium-Python-Client
    Installing collected packages: Appium-Python-Client
    Successfully installed Appium-Python-Client-0.24


<br>
#### 运行第一个Appium测试
----
* __第一步__，启动Android模拟器。

![](http://img.testclass.net/appium_android_system.png)

* __第二步__，启动 Appium Server。

![](http://img.testclass.net/appium_server_view.png)

点击右上角 __三角__ 按钮，注意Appium的启动日志。

    > Launching Appium server with command: D:\Program Files (x86)\Appium\node.exe lib\server\main.js --address 127.0.0.1 --port 4723 --platform-name Android --platform-version 23 --automation-name Appium --log-no-color
    > info: Welcome to Appium v1.4.16 (REV ae6877eff263066b26328d457bd285c0cc62430d)
    > info: Appium REST http interface listener started on 127.0.0.1:4723
    > info: [debug] Non-default server args:
     {"address":"127.0.0.1","logNoColors":true,"platformName":"Android","platformVersion":"23","automationName":"Appium"}
    > info: Console LogLevel: debug


Appium在启动时默认占用本机的4723端口，即：127.0.0.1:4723

* __第三步__，编写 appnium 测试脚本。

```python
#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()

```

运行上面的脚本，你将会看到 Android 模拟器如下运行界面：

![](http://img.testclass.net/appium_run_calculator.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1437936251057-dfbf79980ce5?w=300)

