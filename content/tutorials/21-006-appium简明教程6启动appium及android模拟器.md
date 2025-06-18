---
weight: 6
title: appium简明教程（6）——启动appium及android模拟器
date: '2017-08-15T07:33:41+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1511553677255-ba939e5537e0?w=300
tags: []
categories:
- appium简明教程
lightgallery: true
toc:
  auto: false
---



一般情况下，我们都从命令行启动appium。

windows下，dos命令窗口输入

```
appium
```

如果该命令报错，那么请重装appium

```
npm install -g appium
```

如果安装出错，请使用淘宝源。

[淘宝源地址](http://npm.taobao.org/)

**然后请打开android的模拟器，如果没有请新建一个虚拟设备。请自行解除设备锁定（手动把屏幕解锁了），以防万一。**

下面的代码以启动android原生的计算器程序为例

### ruby篇

```ruby
require 'appium_lib'

caps   = { caps:       { platformName: 'Android', appActivity: '.Calculator', appPackage: 'com.android.calculator2' },
           appium_lib: { sauce_username: nil, sauce_access_key: nil } }
driver = Appium::Driver.new(caps).start_driver
```

讨论：可以看出ruby lib里面的Appium::Driver类实际上就是原生的webdriver类的子类，当然了，由于ruby语法灵活，也可以使用monkey patch来实现类似功能。


### python篇

```python
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```

讨论：webdriver.Remote实际上就是原生webdriver的子类，另外Remote()构造函数的第一个参数中需要显示指定appium server监听的端口

### java篇

新建java项目时候，请注意将selenium-webdriver以及appium client的jar包导入

```java
import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

DesiredCapabilities capabilities = new DesiredCapabilities();
capabilities.setCapability(CapabilityType.BROWSER_NAME, "");//这句不是必须的
capabilities.setCapability("deviceName","Android Emulator");
capabilities.setCapability("platformVersion", "4.4");
capabilities.setCapability("platformName","Android");
capabilities.setCapability("appPackage", "com.android.calculator2");
capabilities.setCapability("appActivity", ".Calculator");
AppiumDriver driver = new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
```

讨论:AppiumDrvier是原生webdriver的子类。

在这里我们可以看到，新建driver的时候必须要指定一个DesiredCapabilities 对象，该对象究竟是何方神圣，我们下一节会仔细讲解。

本文版权归乙醇所有，欢迎转载，但请注明作者与出处，严禁用于任何商业用途




原始封面

![课程图片](https://images.unsplash.com/photo-1511553677255-ba939e5537e0?w=300)

