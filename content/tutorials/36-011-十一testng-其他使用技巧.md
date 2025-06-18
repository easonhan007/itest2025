---
weight: 11
title: （十一）TestNG 其他使用技巧
date: '2017-11-25T12:10:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1515965885361-f1e0095517ea?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



除了前面介绍的功能外，TestNG 还有一些使用技巧，相对比较简单，这里通过一个例子来演示。

#### 其它使用技巧
---
```
import org.testng.annotations.Test;
import static org.testng.AssertJUnit.assertEquals;


public class OtherTest {

    // 该条用例跳过执行
    @Test(enabled = false)
    public void testCase1(){
        assertEquals(2+2, 4);
    }

    // 设定用例超时时间
    @Test(timeOut = 3000)
    public void testCase2() throws InterruptedException {
        Thread.sleep(3001);
    }

    // 预设用例抛出的异常类型
    @Test(expectedExceptions = RuntimeException.class)
    public void testCase3(){
        assertEquals(2/0,1);
    }

}
```
* enabled  设置用例是否跳过执行，默认为：__true__ ，表示不跳过。__false__ 表示跳过执行。

* timeOut 设置用例运行的超时间，3000 单位为毫秒，当用例运行时间超过 3000 毫秒则判定为失败。不管用例本身是否运行失败。

* expectedExceptions 用来预设用例运行会出现的异常。例如 2/0 将会抛出 RuntimeException 类型的异常，如果出现异常则表示用例执行成功。




原始封面

![课程图片](https://images.unsplash.com/photo-1515965885361-f1e0095517ea?w=300)

