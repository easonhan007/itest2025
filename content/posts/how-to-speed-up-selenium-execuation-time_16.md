---
weight: 1
title: "如何优化selenium webdriver的执行速度"
date: 2024-03-08T09:01:57+08:00
lastmod: 2024-03-08T09:01:57+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "非常管用"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1457305237443-44c3d5a30b89?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

让自动化测试脚本正常工作只是自动化测试的第一步，由于自动化脚本会经常执行并更新，因此测试脚本需要

- 可以快速执行
- 容易维护
- 容易阅读

本文会提供一些让 selenium 自动化脚本运行的更快的技巧。

### 在 page_source 中断言 text 比直接使用 text 属性断言要快

我们经常会需要断言页面中的某个部分包含一些具体的文本，下面的语句的输出结果是相同的

```ruby
driver.page_source
driver.find_element(:tag_name => ‘body') .
```

不过对于第二条语句来说，selenium 需要去分析页面的结构，最后再找到对应的元素并输入结果，这显然是需要花费时间的。如果页面比较小的化，那么二者的差距可能不大，不过对于大的页面来说，第一条语句速度明显会更快一些。

使用 page text 的情况

```ruby
expect(driver.find_element(:tag_name => "body").text).to include("platform- and language-neutral wire protocol")
```

使用 page source 的情况

```ruby
expect(driver.page_source).to include("platform- and language-neutral wire protocol")
```

来看一下差距

```ruby
Method 1: Search whole document text took 0.823076 seconds
Method 2: Search whole document HTML took 0.039573 seconds
```

当然两者的使用场景是不太相同的，不过我们这里只关注性能，显然 page source 要更快速一些。

### 元素越具体，获取 text 的速度越快

根据经验，我们可以通过缩小更具体的 Web 控件的范围来节省执行时间。下面的两个断言语句在很大程度上实现了相同的功能，但在执行时间上有很大的不同。

```ruby
expect(driver.find_element(:tag_name, “body”).text).to include(“language-neutral wire”)
```

这条语句的执行时间是 0.93s

```ruby
expect(driver.find_element(:id, “abstract”).text).to include(“language-neutral wire”)
```

这个断言只执行了 0.02s

很明显，第 2 个断言除了在执行速度上更快之外，断言也更加精确，更容易理解。

### 使用变量去缓存没有变化的元素

我经常看到有人编写如下测试来检查页面上的多个文本。

```ruby
driver.navigate.to(site_url + "/WebDriverStandard.html") expect(driver.find_element(:tag_name, "body").text).to include("Firefox")
expect(driver.find_element(:tag_name, "body") ").text).to include("chrome")
expect(driver.find_element(:tag_name, "body").text).to include("W3C")
```

执行时间 2.35s

上述三个测试语句非常低效，因为每个测试语句都调用`driver.find_element(:tag_name, 'body').text`，当网页很大时，这可能是费时费力的工作。

**解决方案**：使用一个变量来存储网页的文本，这是编程中很常见的做法。

```ruby
the_page_text = driver.find_element(:tag_name, “body”).text expect(the_page_text).to include("Firefox")
expect(the_page_text).to include("chrome")
expect(the_page_text).to include("W3C" )

```

执行速度 0.86s

无论我们在该页面上执行了多少断言（针对页面文本），只要我们检查的页面文本没有改变，我们都会获得恒定的执行时间。

### **快速在文本框中输入大文本**

我们通常用来`send_keys`在文本框中输入文本。当您发现要输入的文本字符串很大，例如数千个字符时，尽量避免使用，`send_keys`因为它不高效。下面是一个例子：

```ruby
long_str = “START” + ‘0’ * 1024 * 5 + “END” # just over 5K
text_area_elem = driver.find_element(:id, “comments”)
text_area_elem.send_keys(long_str)
```

执行时间 3.8s

其实解决方案很简单，用 js 来做

```ruby
driver.execute_script(“document.getElementById('comments').value = arguments[0];”, long_str)
```

执行时间 0.2s

### **使用动态等待进行动态/AJAX 操作而不是固定睡眠**

对于一些前后端分离的页面，由于操作之间页面不会刷新，我们就不能依赖 selenium 自带的页面刷新等待机制，所以我们经常需要去等待一个元素出现或者消失，下面的代码演示了这个过程。

```ruby
driver.find_element(:xpath,"//input[ @value ='Pay now']").click
sleep 10 # seconds
expect(driver.find_element(:id, "bn").text).to include("RN #")
```

这样无论这个页面的流畅程度如何，上面的代码都至少需要执行 10s，一个用例的话 10s 可以接受，但如果大部分用例里都有固定等待时间，那整个测试执行的过程将是非常缓慢的。

解决方案是使用动态等待。

```ruby
wait = Selenium::WebDriver::Wait.new(:timeout => 10) # seconds
wait.until{ driver.find_element(:id, "bn").text.include?("RN#") }
```

### 最后

如果用例是一个接一个串行执行的话，那么执行速度可以优化的空间也是有上限的，更好的方案是多组用例一起执行，多一些执行机，把串行该成并行，这样的优化效果将更加明显。总之时间太长，就想办法堆机器吧。
