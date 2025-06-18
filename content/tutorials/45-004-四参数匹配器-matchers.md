---
weight: 4
title: （四）参数匹配器 (matchers)
date: '2017-11-25T12:50:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=300
tags: []
categories:
- mockito简明教程
lightgallery: true
toc:
  auto: false
---




#### 参数匹配器 (matchers)
---
Mockito以自然的java风格来验证参数值: 使用equals()函数。有时，当需要额外的灵活性时你可能需要使用参数匹配器，也就是argument matchers :
例子
```java
import org.junit.Test;

import java.util.LinkedList;

import static org.mockito.Mockito.*;



public class MockitoDemo {

    @Test
    public void with_arguments(){

        LinkedList mockedList = mock(LinkedList.class);

        //stubbing using built-in anyInt() argument matcher
        // 使用内置的anyInt()参数匹配器
        when(mockedList.get(anyInt())).thenReturn("element");

        //following prints "element"
        // 输出element
        System.out.println(mockedList.get(1));

        //you can also verify using an argument matcher
        // 你也可以验证参数匹配器
        verify(mockedList).get(anyInt());
    }
}
```

参数匹配器使验证和测试桩变得更灵活。[点击这里](http://site.mockito.org/mockito/docs/current/org/mockito/Matchers.html)查看更多内置的匹配器以及自定义参数匹配器或者hamcrest 匹配器的示例。


如果仅仅是获取自定义参数匹配器的信息，查看[ArgumentMatcher类文档](http://site.mockito.org/mockito/docs/current/org/mockito/ArgumentMatcher.html)即可。

为了合理的使用复杂的参数匹配，使用equals()与anyX() 的匹配器会使得测试代码更简洁、简单。有时，会迫使你重构代码以使用equals()匹配或者实现equals()函数来帮助你进行测试。

同时建议你阅读[ArgumentCaptor类文档](http://site.mockito.org/mockito/docs/current/org/mockito/ArgumentCaptor.html)。ArgumentCaptor是一个能够捕获参数值的特俗参数匹配器。



__自定义参数匹配器__

例子：

```java
import org.junit.Test;
import org.mockito.ArgumentMatcher;

import java.util.LinkedList;

import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.*;

public class MockitoDemo {

    @Test
    public void with_arguments2(){

        LinkedList mockedList = mock(LinkedList.class);

        //stubbing using custom matcher (let's say isValid() returns your own matcher implementation):
        // 使用自定义的参数匹配器( 在IsValid()类中返回你自己的匹配器实现 )
        when(mockedList.contains(argThat(new IsValid()))).thenReturn(true);

        assertTrue(mockedList.contains(1));
        assertTrue(!mockedList.contains(3));

    }

    private class IsValid extends ArgumentMatcher<List> {
        @Override
        public boolean matches(Object o) {
            return o.equals(1) || o.equals(2);
        }
    }

}

```

上面的例子中我们自己定义了 IsValid 类，处理不同参数时的返回。




原始封面

![课程图片](https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=300)

