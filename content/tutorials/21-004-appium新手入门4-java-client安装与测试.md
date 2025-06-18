---
weight: 4
title: appium新手入门（4）—— java-client安装与测试
date: '2017-09-07T10:24:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=300
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

当你点击这一章时，说明你是打算使用 Java 语言编写 appium 自动化测试脚本的。

1、安装 [Java 环境](/selenium_java/install-java/) ,我想这一步你已经搞定了

2、安装 [IntelliJ IDEA](/selenium_java/install-idea/) , 当然，你喜欢用 Eclipse 也可以，不过，我仍然推荐 IDEA。

3、安装 [Maven](/selenium_java/install-selenium/), Java开发必备啊！


#### Maven 安装 Java-client
----

首先，启动IntelliJ IDEA，创建Maven项目（参考selenium java教程），然后在maven配置文件中添加Java-client配置。

    <dependency>
        <groupId>io.appium</groupId>
        <artifactId>java-client</artifactId>
        <version>5.0.0-BETA9</version>
        <scope>test</scope>
    </dependency>

最新版本号可以到 github [Java-client开源项目](https://github.com/appium/java-client)上查看。


![](http://img.testclass.net/appium_idea_maven.png)


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

* __第三步__，编写第一个Appium测试程序。在appium.tests项目下创建，AppiumDemo类。

```java
package com.example;

import org.openqa.selenium.*;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;

import java.net.MalformedURLException;
import java.net.URL;


public class CalculatorTest {

    public static void main(String[] args) throws MalformedURLException, InterruptedException {

        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("deviceName", "Android Emulator");
        capabilities.setCapability("automationName", "Appium");
        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("platformVersion", "6.0");
        capabilities.setCapability("appPackage", "com.android.calculator2");
        capabilities.setCapability("appActivity", ".Calculator");

        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);

        driver.findElement(By.name("1")).click();
        driver.findElement(By.name("5")).click();
        driver.findElement(By.name("9")).click();
        driver.findElement(By.name("delete")).click();
        driver.findElement(By.name("+")).click();
        driver.findElement(By.name("6")).click();
        driver.findElement(By.name("=")).click();
        Thread.sleep(2000);

        String result = driver.findElement(By.id("com.android.calculator2:id/formula")).getText();
        System.out.println(result);

        driver.quit();
    }

}
```

通过 IDEA 运行程序。将会看到 Android 模拟器如下运行界面：

![](http://img.testclass.net/appium_run_calculator.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=300)

