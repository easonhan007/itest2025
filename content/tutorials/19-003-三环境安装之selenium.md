---
weight: 3
title: （三）环境安装之Selenium
date: '2017-07-05T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1516572541403-d8d1ef5b8844?w=300
tags: []
categories:
- slenium java 语言教程
lightgallery: true
toc:
  auto: false
---



<br>
### 通过jar包安装


点击 [Selenium下载](http://docs.seleniumhq.org/download/) 链接
你会看到Selenium Standalone Server的介绍：

The Selenium Server is needed in order to run Remote Selenium
WebDriver. Selenium 3.X is no longer capable of running Selenium RC
directly, rather it does it through emulation and the WebDriverBackedSelenium interface.

Download version __3.4.0__

点击版本号进行下载，下载完成将会得到一个__selenium-server-standalone-3.4.0.jar__文件。

或者通过 [网盘下载](http://pan.baidu.com/s/1bFWaEa)。

打开IntelliJ IDEA，导入.jar包。

点击菜单栏 File --> Project Structure（快捷键Ctrl + Alt + Shift + s） ，点击 Project Structure界面左侧
的“Modules” 。在“Dependencies” 标签界面下，点击右边绿色的“+” 号，选择第一个选项“JARs or directories...” ，选择相应的 jar 包，点“OK” ，jar包添加成功。
![](http://orru5lls3.bkt.clouddn.com/idea5.png)


<br>
### 通过Maven安装

关于Maven安装又是另一个话题了。你可以参考其它资料学习在IntelliJ IDEA创建Maven项目。

[Maven官网](http://maven.apache.org/)

[idea & maven help](https://www.jetbrains.com/help/idea/maven.html)

[Maven仓库](https://mvnrepository.com/)


打开pom.xml 配置Selenium。

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.mvn.demo</groupId>
    <artifactId>MyMvnPro</artifactId>
    <version>1.0-SNAPSHOT</version>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.6</source>
                    <target>1.6</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <dependencies>

        <!-- selenium-java -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>3.4.0</version>
        </dependency>

    </dependencies>

</project>
```
虽然，学习Maven需要增加你的学习成本，但如果你需要长期使用Java编程语言，或者想用Java来做更多事情的话，越早使用Maven越好！因为它会让的第三方包管理变得非常简单。


<br>
### Hello Selenium

最后，少不了要写一个简单的Selenium Sample来验证Selenium安装是否成功，打开IntelliJ IDEA 创建一个新类Itest.java

```java
package javaBase;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Itest {
    public static void main(String[] args) {

        WebDriver driver = new ChromeDriver();
        driver.get("http://www.itest.info");

        String title = driver.getTitle();
        System.out.printf(title);

        driver.close();
    }
}
```
如果执行报错，请看下一节，[Selenium3浏览器驱动](/selenium_java/selenium3-browser-driver/)。




原始封面

![课程图片](https://images.unsplash.com/photo-1516572541403-d8d1ef5b8844?w=300)

