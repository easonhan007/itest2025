---
weight: 1
title: "selenium 4 0新特性及新旧api对比"
date: 2022-03-03T09:03:04+08:00
lastmod: 2022-03-03T09:03:04+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "区别不大"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1522198648249-0657d7ff242a?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

众所周知，java 语言版本的 selenium 一般被认为是最正宗的 selenium 版本，今天我们以 java 语言为例，来看看 selenium 4.0 的各种新特性以及新旧 api 的对比。

### **Capabilities**

如果你需要对浏览器进行一些全局设置，那么使用 Capabilities 是唯一的选择。说实话，旧的 Capabilities 有点不太符合直觉，具体用法如下。

```csharp
DesiredCapabilities capabilities = DesiredCapabilities.chrome();
capabilities.setCapability("platform", "Mac OS X");
capabilities.setCapability("version", "94");
driver = new RemoteWebDriver(capabilities);
```

在新版本中，我们直接设置 options 就可以了，语义上显得更为自然。

```csharp
ChromeOptions options = new ChromeOptions();
options.setBrowserVersion("94");
options.setPlatformName("Mac OS X");
driver = new ChromeDriver(options);
```

### Waits

在之前的版本里，我们实例化各种 wait 对象时候需要传入 2 个参数：time 以及 type of time，在新版本里我们只需要使用 Duration 类就可以了。

这是之前的做法

```csharp
driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
driver.manage().timeouts().setScriptTimeout(10, TimeUnit.SECONDS);
```

新的方式

```csharp
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
driver.manage().timeouts().pageLoadTimeout(Duration.ofMinutes(3));
driver.manage().timeouts().setScriptTimeout(Duration.ofHours(1));
```

当然，现在支持各式各样的 Duration 了，需要注意的是这里接受的是 long 型的参数。

```csharp
Duration.ofNanos(long nanos);
Duration.ofMillis(long millis);
Duration.ofSeconds(long seconds);
Duration.ofMinutes(long minutes);
Duration.ofHours(long hours);
Duration.ofDays(long days);
```

当然，我们还可以直接设置浏览器的各种全局等待时间，代码上看观感好了不少。

```csharp
ChromeOptions options = new ChromeOptions();
options.setImplicitWaitTimeout(Duration.ofSeconds(10));
options.setScriptTimeout(Duration.ofSeconds(10));
options.setPageLoadTimeout(Duration.ofSeconds(10));
```

### 相对定位器

一些哲学流派告诉我们，世界是变化的，相对的，没有绝对的静，也没有绝对的动，物体总是相对着其他物体进行着运动。

在之前的 selenium 版本里，我们大部分情况下只能通过绝对定位器来定位元素，比如

- 定位一个 id=xxx 的元素
- 定位所有 class=yyy 的元素
- 定位所有的 tag 那么=zzz 的元素

当然，还是有例外的，我们可以通过 xpath 或者 css 来不那么绝对的定位元素。比如

- .nav > li：定位 class 为 nav 的元素下所有的直接 li 子元素
- #nav .item：定位 id 是 nav 下面所有的 class 为 item 的元素

这也是我推荐用 css 定位的原因，更灵活更简洁，同时可以跟前端的技术栈保持相对统一，xpath 的定位能力更强一些，同时也带来了给多的复杂性和学习成本。

在 selenium 4.0 中，相对定位器终于千呼万唤始出来，我们可以省去相对复杂的 xpath 表达式，用更加直观的方式来定位元素了，举个例子，下面是一个登录页面。

![Untitled](selenium%204%200%E6%96%B0%E7%89%B9%E6%80%A7%E5%8F%8A%E6%96%B0%E6%97%A7api%E5%AF%B9%E6%AF%94%202805e5a829b74964afe8f263d7bb64ef/Untitled.png)

其 html 代码如下：

```csharp
<div class="row">
    <div class="large-6 small-12 columns">
        <label for="password">Password</label>
        <input type="password" name="password" id="password">
    </div>
</div>
```

我们试着去定位 input 之前的那个 label，经验丰富的你可以想象到页面上会有非常多 label，所以用 tagname 的方式应该不可取；另外这个 label 还没有其他更加独特的属性可以利用。不过我们可以发现，睡在他下铺的兄弟 input 有 id 属性，定位起来相对简单，很自然的会想到能不能利用 input 来定位 label 呢？现在都 2021 年了，这类的相对定位方式已经被支持了的。

```csharp
WebElement passwordArea = driver.findElement(By.id("password"));
WebElement labelOfPass = driver.findElement(with(By.tagName("label")).above(passwordArea));
System.out.println(labelOfPass.getText());
```

大家可以猜一猜上面代码的输出是什么？

### toLeftOf/toRightOf/near

除了上面所展示的 above 方式以外，selenium 4.0 还支持 below，toLeftOf/toRightOf/near 等方式，举个简单的例子。

```csharp
<tr>
    <td class="name">itest.info</td>
    <td class="website">itest.info</td>
    <td class="actions">
        <a href="#edit">Edit</a>
        <a href="#delete">Delete</a>
    </td>
</tr>
```

如果我们要定位上面的 delete 按钮，我们可以用下面的相对定位方式

```java
WebElement website = driver.findElement(By.xpath("(//td[text()='itest.info'])"));
driver.findElement(with(By.linkText("Delete")).toRightOf(website)).click();

// or
driver.findElement(with(By.linkText("Delete")).near(website)).click();
```

### 打开新窗口或者新标签页

在之前的 selenium 版本中，我们如果要打开新窗口或者是新标签页的话，我们需要先实例化 1 个 driver 对象，然后使用 window handler 来进行下一步的操作；在 4.0 以后，我们可以直接使用 switchTo()方法来打开新窗口。下面是具体的例子：

```java
WebDriver driver = Driver.get();
driver.get("http://www.itest.info/");

driver.switchTo().newWindow(WindowType.WINDOW);
driver.get("https://qq.com");
```

打开新标签页也很好办，我们只需要修改 WindowType 就好了。

```java
WebDriver driver = Driver.get();
driver.get("http://www.itest.info/");

driver.switchTo().newWindow(WindowType.TAB);
driver.get("https://qq.com");
```

### **DevTools 协议**

在 4.0 之后我们可以直接使用 chrome 的开发者工具接口来获取网络情况或者是性能数据了。下面的例子展示了如何使用 devtools 来设置自己的地理位置，自动化打卡签到有希望了。

```java
WebDriver driver = new ChromeDriver();
DevTools devTools = ((HasDevTools)driver).getDevTools();
devTools.createSession();
devTools.send(Emulation.setGeolocationOverride(Optional.of(38.89511),
                Optional.of(-77.03637),
                Optional.of(1)));
driver.get("https://my-location.org/");
```

### 总结

selenium 4.0 并没有带来特别多令人啧啧称奇的特性，不过从 api 的设计以及语义上，元素的定位上都有了不同程度的优化和提升，这也是 selenium 成熟的体现。作为 1 个从 selenium rc 时代就使用 selenium 的老用户，对这次大的版本更新我竟然觉得有一丝丝的感动，毕竟是一个开源项目，大家都有自己的工作和生活，能十几年如一日的维护和更新 selenium 本来就是一件不容易的事情，维护者们为了梦想和情怀还在努力，我们不妨也一起加油吧，学无止境，我独自迈步向前，让举步不前的人自己卷自己吧。
