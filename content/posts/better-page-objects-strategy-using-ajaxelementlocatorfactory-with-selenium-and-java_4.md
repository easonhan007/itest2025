---
weight: 1
title: "在selenium中使用AjaxElementLocatorFactory来优化PO模式"
date: 2024-03-08T09:01:39+08:00
lastmod: 2024-03-08T09:01:39+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "代码很有启发"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1484349296292-552da537bd3a?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

之前看到的一篇对于 po 的改进的文章，非常有启发，简单翻译改写了一下，希望对大家有帮助。本文基于 java，至于其他语言是否有类似的实现，没有具体研究过。

原文地址: [http://www.eliasnogueira.com/better-page-objects-strategy-using-ajaxelementlocatorfactory-with-selenium-and-java](http://www.eliasnogueira.com/better-page-objects-strategy-using-ajaxelementlocatorfactory-with-selenium-and-java/?utm_campaign=Software%2BTesting%2BWeekly&utm_medium=email&utm_source=Software_Testing_Weekly_135)

PO 模式是 page object factory 设计模式的简称，主要是以页面为维度来聚合一些元素的定位，让代码有更好的维护性和重用性，具体细节可以看这里：[https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models)。这里是官方文档，非常值得精读。

### Page Factory

如果你已经对 po 很熟悉了，下面的内容可以放心跳过。

下面是最基本的 Page Factory 套路，本质上是按页面去封装元素定位和操作。

```java
public class PageObjectExample {

    private final WebDriver driver;

    public PageObjectExample(WebDriver driver) {
        this.driver = driver;
    }

    public void login(String email, String password) {
        driver.findElement(By.id("email")).sendKeys(email);
        driver.findElement(By.id("password")).sendKeys(password);
        driver.findElement(By.name("next")).click();
    }
}
```

上面的代码只能说懂的都懂，不过这里有个问题，在 login 方法里，我们频繁使用`driver.findElement`方法，这会显得有一些的啰嗦，下面是改进版本，优雅了很多。

```java
public class PageObjectExample {

    @FindBy(id = "email")
    private WebElement email;

    @FindBy(id = "password")
    private WebElement password;

    @FindBy(name = "next")
    private WebElement next;

    public PageObjectExample(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    public void login(String email, String password) {
        this.email.sendKeys(email);
        this.password.sendKeys(password);
        next.click();
    }
}
```

这里要注意的是在进行初始化的时候，需要调用`PageFactory.initElements(driver, this);`

本质上这行代码的作用是将上面的注解@FindBy 转换成基本的`findElement`形式。

参考资料：[https://github.com/SeleniumHQ/selenium/wiki/PageFactory](https://github.com/SeleniumHQ/selenium/wiki/PageFactory)

### PO 模式的常见问题

等待策略。selenium 提供了 3 种测试，分别是显示，隐式，以及流利等待(fluent wait)，一般情况下隐式等待是不推荐的。

在 po 中，我们会在 2 种情况下用到等待，分别是初始化 po 对象时以及在 action 方法时，action 方式其实就是指的包含有元素操作的方法。

**初始化时等待**

如果操作的对象在页面加载时候就会渲染完毕的话，那么在初始化时等待将会是一个非常好的实践。总体的实现思路是在初始化时告诉 po，我们明确希望等待哪个元素出现，并且最多等待多久。

```java
public class PageObjectExample {

    private WebDriver driver;

    @FindBy(id = "email")
    private WebElement email;

    @FindBy(id = "password")
    private WebElement password;

    @FindBy(name = "next")
    private WebElement next;

    public PageObjectExample(WebDriver driver) {
        this.driver = driver;

        PageFactory.initElements(driver, this);
        new WebDriverWait(driver, Duration.of(5, ChronoUnit.SECONDS))
            .until(ExpectedConditions.visibilityOf(email));
    }

    public void login(String email, String password) {
        this.email.sendKeys(email);
        this.password.sendKeys(password);
        next.click();
    }
}
```

上面的代码中我们希望在初始化页面对象时，其实也就是在页面加载的时候明确等待 email 这个元素出现，超时时间为 5s。

**操作时等待**

这里的做法是先等待再操作，比如

```java
public class PageObjectExample {

    private WebDriver driver;

    @FindBy(id = "email")
    private WebElement email;

    @FindBy(id = "password")
    private WebElement password;

    @FindBy(name = "next")
    private WebElement next;

    public PageObjectExample(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    public void fillEmail(String email) {
        new WebDriverWait(driver, Duration.of(5, ChronoUnit.SECONDS))
            .until(ExpectedConditions.visibilityOf(this.email));

        this.email.sendKeys(email);
    }
}
```

其实就是把等待的代码换了个位置而已。

### 简化等待操作

上面方式可以运行的很好，不过还是有点太啰嗦了，下面的做法可以缓解一下

- 在`PageFactory.initiElements`中调用 AjaxElementLocatorFactory 方法，这样可以无脑等待；
- 继承 PageFactory.initiElements 方法，这样子类里就不用反复写了

下面是基本的代码

```java
public class PageObjectExample {

    private WebDriver driver;

    // WebElements ignored

    public PageObjectExample(WebDriver driver) {
        PageFactory.initElements(new AjaxElementLocatorFactory(driver, 5), this);
    }
}
```

**使用继承来简化代码**

```java
public abstract class AbstractPageObject {

    private WebDriver driver;

    protected AbstractPageObject(WebDriver driver) {
        PageFactory.initElements(new AjaxElementLocatorFactory(driver, 5), this);
    }
}

public class PageObject extends AbstractPageObject {

    // WebElements ignored

    protected PageObject(WebDriver driver) {
        super(driver);
    }

   // action steps ignored
}
```

### 总结

大家可以通过[https://github.com/eliasnogueira/selenium-java-lean-test-architecture](https://github.com/eliasnogueira/selenium-java-lean-test-architecture)这个项目来熟悉上面的概念，如果你使用 java 的话，该项目可以直接做脚手架使用，写框架的同学可以参考。
