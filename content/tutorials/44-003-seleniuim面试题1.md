---
weight: 3
title: seleniuim面试题1
date: '2017-07-18T09:44:38+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507206130118-b5907f817163?w=300
tags: []
categories:
- 面试题合集
lightgallery: true
toc:
  auto: false
---



### selenium中如何判断元素是否存在？

selenium中没有提供原生的方法判断元素是否存在，一般我们可以通过定位元素+异常捕获的方式判断。

```python
# 判断元素是否存在
try:
	dr.find_element_by_id('none')
except NoSuchElementException:
	print 'element does not exist'
```

### selenium中hidden或者是display ＝ none的元素是否可以定位到？

不可以，selenium不能定位不可见的元素。```display=none```的元素实际上是不可见元素。

### selenium中如何保证操作元素的成功率？也就是说如何保证我点击的元素一定是可以点击的？

* 被点击的元素一定要占一定的空间，因为selenium默认会去点这个元素的中心点，不占空间的元素算不出来中心点;
* 被点击的元素不能被其他元素遮挡;
* 被点击的元素不能在viewport之外，也就是说如果元素必须是可见的或者通过滚动条操作使得元素可见;
* 使用```element.is_enabled()```(python代码)判断元素是否是可以被点击的，如果返回false证明元素可能灰化了，这时候就不能点;

### 如何提高selenium脚本的执行速度？

* 使用效率更高的语言，比如java执行速度就快过python
* 不要盲目的加```sleep```，尽量使用[显式等待](/selenium_python/element-wait/)
* 对于firefox，考虑使用测试专用的profile，因为每次启动浏览器的时候firefox会创建1个新的profile，对于这个新的profile，所有的静态资源都是从服务器直接下载，而不是从缓存里加载，这就导致网络不好的时候用例运行速度特别慢的问题
* chrome浏览器和safari浏览器的执行速度看上去是最快的
* 可以考虑分布式执行或者使用selenium grid

### 用例在运行过程中经常会出现不稳定的情况，也就是说这次可以通过，下次就没办法通过了，如何去提升用例的稳定性？

* 测试专属profile，尽量让静态资源缓存
* 尽量使用[显式等待](/selenium_python/element-wait/)
* 尽量使用测试专用环境，避免其他类型的测试同时进行，对数据造成干扰

### 你的自动化用例的执行策略是什么？

* 每日执行：比如每天晚上在主干执行一次
* 周期执行：每隔2小时在开发分之执行一次
* 动态执行：每次代码有提交就执行

### 自动化测试的时候是不是需要连接数据库做数据校验？

一般不需要，因为这是单元测试层做的事情，在自动化测试层尽量不要为单元测试层没做的工作还债。

### id,name,clas,xpath, css selector这些属性，你最偏爱哪一种，为什么？

xpath和css最为灵活，所以其他的答案都不够完美。

### 如何去定位页面上动态加载的元素？

[显式等待](/selenium_python/element-wait/)

### 如何去定位属性动态变化的元素？

找出属性动态变化的规律，然后根据上下文生成动态属性。

### 点击链接以后，selenium是否会自动等待该页面加载完毕？

java binding在点击链接后会自动等待页面加载完毕。

### selenium的原理是什么？

selenium的原理涉及到3个部分，分别是

* 浏览器
* driver: 一般我们都会下载driver
* client: 也就是我们写的代码

client其实并不知道浏览器是怎么工作的，但是driver知道，在selenium启动以后，driver其实充当了服务器的角色，跟client和浏览器通信，client根据webdriver协议发送请求给driver，driver解析请求，并在浏览器上执行相应的操作，并把执行结果返回给client。这就是selenium工作的大致原理。

### webdriver的协议是什么？

client与driver之间的约定，无论client是使用java实现还是c#实现，只要通过这个约定，client就可以准确的告诉drier它要做什么以及怎么做。

webdriver协议本身是http协议，数据传输使用json。

[这里](https://www.w3.org/TR/webdriver/#list-of-endpoints)有webdriver协议的所有endpoint，稍微看一眼就知道这些endpoints涵盖了selenium的所有功能。

### 启动浏览器的时候用到的是哪个webdriver协议？

[New Session](https://www.w3.org/TR/webdriver/#new-session)，如果创建成功，返回sessionId和[capabilities](https://www.w3.org/TR/webdriver/#capabilities)。

### 什么是page object设计模式？

[官方介绍](https://github.com/SeleniumHQ/selenium/wiki/PageObjects)，简单来说就是用class去表示被测页面。在class中定义页面上的元素和一些该页面上专属的方法。

例子

```java
public class LoginPage {
    private final WebDriver driver;

    public LoginPage(WebDriver driver) {
        this.driver = driver;

        // Check that we're on the right page.
        if (!"Login".equals(driver.getTitle())) {
            // Alternatively, we could navigate to the login page, perhaps logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    // The login page contains several HTML elements that will be represented as WebElements.
    // The locators for these elements should only be defined once.
        By usernameLocator = By.id("username");
        By passwordLocator = By.id("passwd");
        By loginButtonLocator = By.id("login");

    // The login page allows the user to type their username into the username field
    public LoginPage typeUsername(String username) {
        // This is the only place that "knows" how to enter a username
        driver.findElement(usernameLocator).sendKeys(username);

        // Return the current page object as this action doesn't navigate to a page represented by another PageObject
        return this;
    }

    // The login page allows the user to type their password into the password field
    public LoginPage typePassword(String password) {
        // This is the only place that "knows" how to enter a password
        driver.findElement(passwordLocator).sendKeys(password);

        // Return the current page object as this action doesn't navigate to a page represented by another PageObject
        return this;
    }

    // The login page allows the user to submit the login form
    public HomePage submitLogin() {
        // This is the only place that submits the login form and expects the destination to be the home page.
        // A seperate method should be created for the instance of clicking login whilst expecting a login failure.
        driver.findElement(loginButtonLocator).submit();

        // Return a new page object representing the destination. Should the login page ever
        // go somewhere else (for example, a legal disclaimer) then changing the method signature
        // for this method will mean that all tests that rely on this behaviour won't compile.
        return new HomePage(driver);
    }

    // The login page allows the user to submit the login form knowing that an invalid username and / or password were entered
    public LoginPage submitLoginExpectingFailure() {
        // This is the only place that submits the login form and expects the destination to be the login page due to login failure.
        driver.findElement(loginButtonLocator).submit();

        // Return a new page object representing the destination. Should the user ever be navigated to the home page after submiting a login with credentials
        // expected to fail login, the script will fail when it attempts to instantiate the LoginPage PageObject.
        return new LoginPage(driver);
    }

    // Conceptually, the login page offers the user the service of being able to "log into"
    // the application using a user name and password.
    public HomePage loginAs(String username, String password) {
        // The PageObject methods that enter username, password & submit login have already defined and should not be repeated here.
        typeUsername(username);
        typePassword(password);
        return submitLogin();
    }
}
```

### 什么是page factory?

[Page Factory](https://github.com/SeleniumHQ/selenium/wiki/PageFactory)实际上是官方给出的java page object的工厂模式实现。

### 怎样去选择一个下拉框中的value＝xx的option？

使用select类，具体看[这里](/selenium_python/select/)

### 如何在定位元素后高亮元素（以调试为目的）？

使用javascript将元素的border或者背景改成黄色就可以了。

### 什么是断言？

可以简单理解为检查点，就是预期和实际的比较

* 如果预期等于实际，断言通过，测试报告上记录pass
* 如果预期不等于实际，断言失败，测试报告上记录fail

### 如果你进行自动化测试方案的选型，你会选择哪种语言，java，js，python还是ruby？

* 哪个熟悉用哪个
* 如果都不会，团队用哪种语言就用那种

### page object设置模式中，是否需要在page里定位的方法中加上断言？

一般不要，除非是要判断页面是否正确加载。

> Generally don't make assertions

### page object设计模式中，如何实现页面的跳转？

返回另一个页面的实例可以代表页面跳转。

```java
// The login page allows the user to submit the login form
public HomePage submitLogin() {
    // This is the only place that submits the login form and expects the destination to be the home page.
    // A seperate method should be created for the instance of clicking login whilst expecting a login failure.
    driver.findElement(loginButtonLocator).submit();

    // Return a new page object representing the destination. Should the login page ever
    // go somewhere else (for example, a legal disclaimer) then changing the method signature
    // for this method will mean that all tests that rely on this behaviour won't compile.
    return new HomePage(driver);
}
```

### 自动化测试用例从哪里来？

手工用例的子集，尽量

* 简单而且需要反复回归
* 稳定，也就是不要经常变来变去
* 核心，优先覆盖核心功能

### 你觉得自动化测试最大的缺陷是什么？

* 实现成本高
* 运行速度较慢
* 需要一定的代码能力才能及时维护

### 什么是分层测试？

画给他/她看。

![](http://wx1.sinaimg.cn/mw1024/726a2979gy1fho5jfxn6zj20dm09q74j.jpg)

### webdriver可以用来做接口测试吗？

不用纠结，不可以。



### selenium 是否可以调用js来对dom对象进行操作？

Could selenium call js for implementation dom object directly?

是

### selenium 是否可以向页面发送鼠标滚轮操作？

Could selenium send the action of mouse scroll wheel?

不能

### selenium 是否可以模拟拖拽操作？  

Does selenium support drag and drop action?

可以

### selenium 对下拉列表的中的选项进行选择操作时，需要被操作对象的标签是什么？   

When Selenium selects the option in selenium, What tag the DOM object should be?

select

### selenium 上传文件操作，需要被操作对象的type属性是什么？

When Selenium upload a file, what  value of type of the DOM object should be?

file




原始封面

![课程图片](https://images.unsplash.com/photo-1507206130118-b5907f817163?w=300)

