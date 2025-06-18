---
weight: 19
title: （十九）调用JavaScript代码
date: '2017-06-22T07:37:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1508161887025-ebd8f2813550?w=300
tags: []
categories:
- slenium java 语言教程
lightgallery: true
toc:
  auto: false
---



<br>
虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了executeScript()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：

```html
<!-- window.scrollTo(左边距,上边距); -->
window.scrollTo(0,450);
```

window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。其代码如下：

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.JavascriptExecutor;

public class JSDemo {

  public static void main(String[] args) throws InterruptedException{

    WebDriver driver = new ChromeDriver();

    //设置浏览器窗口大小
    driver.manage().window().setSize(new Dimension(700, 600));
    driver.get("https://www.baidu.com");

    //进行百度搜索
    driver.findElement(By.id("kw")).sendKeys("webdriver api");
    driver.findElement(By.id("su")).click();
    Thread.sleep(2000);

    //将页面滚动条拖到底部
    ((JavascriptExecutor)driver).executeScript("window.scrollTo(100,450);");
    Thread.sleep(3000);

    driver.quit();
  }
}

```
通过浏览器打开百度进行搜索，并且提前通过window().setSize()方法将浏览器窗口设置为固定宽高显示，目的是让窗口出现水平和垂直滚动条。然后通过executeScript()方法执行JavaScripts代码来移动滚动条的位置。




原始封面

![课程图片](https://images.unsplash.com/photo-1508161887025-ebd8f2813550?w=300)

