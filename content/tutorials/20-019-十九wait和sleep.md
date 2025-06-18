---
weight: 19
title: （十九）wait和sleep
date: '2017-07-29T02:48:18+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1454817481404-7e84c1b73b4a?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### wait<T>( condition, opt_timeout, opt_message )

wait方法一般用来等待页面上某些条件得到满足后才继续执行脚本。比如等待页面上某个弹出框出现，等某个元素可以被定位到之类。

wait方法中可以传入[Condition](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/webdriver_exports_Condition.html)表示一般性条件和[WebElementCondition](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/webdriver_exports_WebElementCondition.html)。

如果传入的元素级条件被满足，那么wait方法会返回[ WebElementPromise](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/webdriver_exports_WebElementPromise.html)，也就是说可以直接返回满足条件的元素。

如果在规定的时间内(也就是第2个参数)没有等到条件被满足，那么该方法会抛出异常。

一般性用法示例：

```javascript
// 在10s内id是foo的元素被定位到，然后点击之
var button = driver.wait(until.elementLocated(By.id('foo')), 10000);
button.click();

```

另外wait还可以将执行中的脚本暂停住一段时间，直到第1个参数中的异步操作处理完毕，如下所示

```javascript
var started = startTestServer();
driver.wait(started, 5 * 1000, 'Server should start within 5 seconds');
driver.get(getServerUrl());
```

### sleep

sleep可以不管任何情况直接将执行中的脚本直接暂停一段时间。

```javascript
console.log('start')
driver.findElement(By.css('.kls')).click();
// 等待3s
driver.sleep(3000)
driver.quit()
```

sleep在某些时候非常好用，但是希望大家不要乱用，因为这会拖慢脚本的执行速度。




原始封面

![课程图片](https://images.unsplash.com/photo-1454817481404-7e84c1b73b4a?w=300)

