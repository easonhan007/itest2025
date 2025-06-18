---
weight: 11
title: （十一）ActionSequence
date: '2017-08-03T02:49:18+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1442524986896-a2cedd8cd26a?w=300
tags: []
categories:
- selenium javascript教程
lightgallery: true
toc:
  auto: false
---



### 组合事件

当页面的交互比较复杂的时候，我们可能会使用到组合事件。比如先把鼠标移动到某个元素上，然后按住鼠标，将该元素拖到另一个地方。为了完成这种操作，我们就需要使用组合事件[ActionSequence](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/index_exports_ActionSequence.html)

组合事件中，我们可以组合鼠标和键盘的操作，这些操作将根据我们组合的顺序依次执行。

### 基本用法

* 直接使用```WebDriver.actions()```进行调用，不需要额外的初始化工作;
* 只有显示调用了```perform()```方法才让所有动作真正得到执行；简而言之，一定要调用```perform()```;

```javascript
driver.actions().
     keyDown(Key.SHIFT).
     click(element1).
     click(element2).
     dragAndDrop(element3, element4).
     keyUp(Key.SHIFT).
     perform();
```

### 实例方法

* click( opt_elementOrButton, opt_button ): 单击，相当于把鼠标移动到元素的中心，然后点击左键

* doubleClick( opt_elementOrButton, opt_button ): 双击, 相当于把鼠标移动到元素的中心，然后双击左键

* this.dragAndDrop( element, location ): 拖拽，第1个参数是拖谁(WebElement)，第2个参数是拽到哪里，可以是WebElement，也可以是坐标```{x: number, y: number}```

* this.keyDown( key ): 按下一个键，必须是{ALT, CONTROL, SHIFT, COMMAND, META}中的一个， 会一直按着，除非调用keyUp()进行松开

* this.keyUp( key ): 松开一个键，必须是{ALT, CONTROL, SHIFT, COMMAND, META}中的一个

* this.mouseDown( opt_elementOrButton, opt_button ): 按下鼠标，除非mouseUp，否则不松开

* this.mouseMove( location, opt_offset ): 把鼠标移动到元素的中心或者具体位置，当然，第2个参数可以也可以增加1个偏移量, ```{x: number, y: number}```

* this.mouseUp( opt_elementOrButton, opt_button ): 松开鼠标

* this.sendKeys( ...var_args ): 除了具体的Key以外，该方法也可以接受Array<Stirng|Key>，这样模拟组合键就容易多了




原始封面

![课程图片](https://images.unsplash.com/photo-1442524986896-a2cedd8cd26a?w=300)

