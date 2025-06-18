---
weight: 18
title: （十八）浏览器cookie操作
date: '2017-06-23T07:37:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1504292004442-f285299403fa?w=300
tags: []
categories:
- slenium java 语言教程
lightgallery: true
toc:
  auto: false
---



<br>
有时候我们需要验证浏览器中Cookie是否正确， 因为基于真实Cookie的测试是__无法通过白盒测试和集成测试进行的__。WebDriver提供了操作Cookie的相关方法可以读取、 添加和删除Cookie信息。

WebDriver 操作Cookie的方法：

* getCookies() 获得所有 cookie 信息。

* getCookieNamed(String name) 返回字典的key为“name”的Cookie信息。

* addCookie(cookie dict) 添加Cookie。“cookie_dict”指字典对象，必须有 name和value值。
* deleteCookieNamed(String name) 删除Cookie 信息。 “name”是要删除的 cookie的名称；
“optionsString” 是该Cookie的选项，目前支持的选项包括“路径” ， “域” 。

* deleteAllCookies() 删除所有 cookie 信息。

下面通过 geCookies()来获取当前浏览器的 cookie 信息。
```java
import java.util.Set;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.Cookie;


public class CookieDemo {

  public static void main(String[] args){

    WebDriver driver = new ChromeDriver();
    driver.get("https://www.baidu.com");

    Cookie c1 = new Cookie("name", "key-aaaaaaa");
    Cookie c2 = new Cookie("value", "value-bbbbbb");
    driver.manage().addCookie(c1);
    driver.manage().addCookie(c2);

    //获得 cookie
    Set<Cookie> coo = driver.manage().getCookies();
    System.out.println(coo);

    //删除所有 cookie
    //driver.manage().deleteAllCookies();

    driver.quit();
  }
}
```
打印结果：
```
[BIDUPSID=82803D3E2DAD0F5342D22C8F96B9E088; expires=星期六, 24 二月 208512:40:10 CST; path=/; domain=.baidu.com, name=key-aaaaaaa; path=/;domain=www.baidu.com, PSTM=1486301167; expires=星期六, 24 二月 2085 12:40:10 CST;path=/; domain=.baidu.com,H_PS_PSSID=1437_21094_21943_22023; path=/;domain=.baidu.com, BD_UPN=12314753; expires=星期三, 15 二月 2017 09:26:04 CST;path=/; domain=www.baidu.com, value=value-bbbbbb; path=/;domain=www.baidu.com,BAIDUID=82803D3E2DAD0F5342D22C8F96B9E088:FG=1; expires=星期六, 24 二月 208512:40:10 CST; path=/; domain=.baidu.com, BD_HOME=0; path=/;domain=www.baidu.com, __bsi=16852840641557463410_00_0_I_R_1_0303_C02F_N_I_I_0;expires=星期日, 05 二月 2017 09:26:10 CST; path=/; domain=.www.baidu.com]
```




原始封面

![课程图片](https://images.unsplash.com/photo-1504292004442-f285299403fa?w=300)

