---
weight: 17
title: （十七）alert confirm 和 prompt
date: '2017-07-31T01:49:18+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1527467779599-34448b3fa6a7?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### alert confirm prompt

原生的javascript弹出框，各个浏览器的实现不一样，外观也不太一样。

这些弹出框会阻止页面上的所有操作，因此每次这些框弹出来以后，我们必须想办法让这些东西消失掉，否则脚本无法往下进行下去。

### 一般的处理方式

当alert弹出之后，我们可以通过类似下面的代码去处理alert

```javascript
driver.switchTo().alert().dismiss();
driver.switchTo().alert().accept();
```

切换到alert/confirm/prompt之后，我们可以进行如下的后续动作

* accept(): 接受,点ok
* dismiss(): 点取消
* getText(): 拿到提示文本
* sendKeys( text ): 如果是prompt的话，可以用该方法输入一些内容
* authenticateAs( username, password ): 如果是[basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)的话，可以通过该方法来输入用户名和密码

### 一劳永逸的处理方式

如果我们不在乎alert上提示的内容，只想页面上不弹出alert/confirm/prompt的话，可以通过js来覆盖这些方法的原生实现，从而达到**禁用**弹出框的效果，比如下面的代码就演示了如何禁用alert。

```javascript
var banAlert = 'window.alert = function(msg){}'
driver.executeScript(banAlert);
```

这样在测试过程中，所有的alert都不会弹出。




原始封面

![课程图片](https://images.unsplash.com/photo-1527467779599-34448b3fa6a7?w=300)

