---
weight: 7
title: （七）WebDriver常用方法
date: '2017-07-02T07:37:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1484417894907-623942c8ee29?w=300
tags: []
categories:
- slenium java 语言教程
lightgallery: true
toc:
  auto: false
---




前面我们已经学习了定位元素， 定位只是第一步， 定位之后需要对这个元素进行操作， 或单击（按钮） 或
输入（输入框） ， 下面就来认识这些最常用的方法。
<br>
### WebDriver 常用方法

下面先来认识 WebDriver 中最常用的几个方法：

* clear() 清除文本。

* sendKeys(*value) 模拟按键输入。

* click() 单击元素

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class BaiduDemo {

  public static void main(String[] args) {

    WebDriver driver = new ChromeDriver();
    driver.get("https://www.baidu.com/");

    WebElement search_text = driver.findElement(By.id("kw"));
    WebElement search_button = driver.findElement(By.id("su"));

    search_text.sendKeys("Java");
    search_text.clear();
    search_text.sendKeys("Selenium");
    search_button.click();

    driver.quit();
  }
}
```
clear()方法用于清除文本输入框中的内容。

sendKeys()方法模拟键盘向输入框里输入内容。 但是它的作用不仅于此， 我们还可以用它发送键盘按键， 甚至用它来指定上传的文件。

click()方法可以用来单击一个元素，前提是它是可以被单击的对象，它与 sendKeys()方法是Web页面操作中最常用到的两个方法。 其实click()方法不仅仅用于单击一个按钮，它还可以单击任何可以单击的文字/图片链接、复选框、单选框、下拉框等。

<br>
### 其它常用方法

* submit()

submit()方法用于提交表单。 例如，在搜索框输入关键字之后的“回车” 操作， 就可以通过 submit()方法模拟.

```java
……
WebElement search_text = driver.findElement(By.id("kw"));
search_text.sendKeys("Selenium");
search_text.submit();
……
```
* getSize()     返回元素的尺寸。

* getText()     获取元素的文本。

* getAttribute(name) 获得属性值。

* isDisplayed()     设置该元素是否用户可见。

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class BaiduDemo {

  public static void main(String[] args) {

    WebDriver driver = new ChromeDriver();
    driver.get("https://www.baidu.com/");

    //获得百度输入框的尺寸
    WebElement size = driver.findElement(By.id("kw"));
    System.out.println(size.getSize());

    //返回百度页面底部备案信息
    WebElement text = driver.findElement(By.id("cp"));
    System.out.println(text.getText());

    //返回元素的属性值， 可以是 id、 name、 type 或元素拥有的其它任意属性
    WebElement ty = driver.findElement(By.id("kw"));
    System.out.println(ty.getAttribute("type"));

    //返回元素的结果是否可见， 返回结果为 True 或 False
    WebElement display = driver.findElement(By.id("kw"));
    System.out.println(display.isDisplayed());

    driver.quit();
  }
}
```
打印结果：
```
(500, 22)
©2017 Baidu 使用百度前必读 意见反馈 京 ICP 证 030173 号 京公网安备 11000002000001 号
text
true
```




原始封面

![课程图片](https://images.unsplash.com/photo-1484417894907-623942c8ee29?w=300)

