---
weight: 6
title: （六） mockito 常用方法
date: '2017-11-25T12:40:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=300
tags: []
categories:
- mockito简明教程
lightgallery: true
toc:
  auto: false
---



#### doReturn()、doThrow()、doAnswer()、doNothing()、doCallRealMethod()系列方法的运用

通过`when(Object)`为无返回值的函数打桩有不同的方法,因为编译器不喜欢void函数在括号内...

使用`doThrow(Throwable)` 替换`stubVoid(Object)`来为void函数打桩是为了与`doAnswer()`等函数族保持一致性。

当你想为void函数打桩时使用含有一个exception 参数的`doAnswer()` :

```Java
import org.junit.Test;
import java.util.LinkedList;
import static org.mockito.Mockito.*;


public class MockitoDemo {

    @Test(expected = RuntimeException.class)
    public void when_doThrow() throws RuntimeException {

        LinkedList mockedList = mock(LinkedList.class);
        doThrow(new RuntimeException()).when(mockedList).clear();

        //following throws RuntimeException:
        // 下面的代码会抛出异常
        mockedList.clear();
    }
}
```
当你调用`doThrow()`, `doAnswer()`, `doNothing()`, `doReturn()` 和 `doCallRealMethod()` 这些函数时可以在适当的位置调用`when()`函数，例如下面这些功能时这是必须的:

* 测试void函数
* 在受监控的对象上测试函数
* 不知一次的测试为同一个函数，在测试过程中改变mock对象的行为。

但是在调用when()函数时你可以选择是否调用这些上述这些函数。




原始封面

![课程图片](https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=300)

