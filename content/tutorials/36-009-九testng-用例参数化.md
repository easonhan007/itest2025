---
weight: 9
title: （九）TestNG 用例参数化
date: '2017-11-25T12:20:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1502810190503-8303352d0dd1?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



参数化也测试用例中常用的技巧之一，它可以增加用例的可配置性和减少相同用例的编写。

#### 通过 @Parameters 实现参数化
---
```java
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import static org.testng.AssertJUnit.assertEquals;

public class DataProviderTest {

    @Test
    @Parameters({"add1","add2","result"})
    public void testAdd1(int add1, int add2, int result){
        assertEquals(add1+ add2, result);
    }

}
```
* @Parameters 获取参数化数据，作为 testAdd1() 测试方法的参数。

具体的测试数据在 __testng.mxl__ 文件中设置。

```
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="测试套件">
    <test name="简单测试">
        <parameter name="add1" value="3"/>
        <parameter name="add2" value="2"/>
        <parameter name="result" value="5"/>
        <classes>
            <class name="test.sample.DataProviderTest" />
        </classes>
    </test>
</suite>
```
* `<parameter.../>` 定义测试数据
 * name 定义数据的名字，在测试用例中通过该名字来获取对应的vlaue。
 * value 定义测试数据，通过对应的name来获取该值。


#### 通过 @DataProvider 实现参数化
---

```java
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import static org.testng.AssertJUnit.assertEquals;

public class DataProviderTest {

    // 定义对象数组
    @DataProvider(name = "add")
    public Object[][] Users() {
        return new Object[][] {
                { 3, 2, 5 },
                { 2, 2, 4 },
                { 3, 3, 7 },
        };
    }

    @Test(dataProvider="add")
    public void testAdd2(int add1, int add2, int result){
        assertEquals(add1+add2, result);
    }

}
```
* @DataProvider 定义对象数组，数组的名称为：add 。

在 testAdd2() 中通过 `dataProvider="add"` 调用定义的对象数组，并通过参数获取相应的测试数据。

执行结果如下：

![](http://img.testclass.net/testng_run_result2.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1502810190503-8303352d0dd1?w=300)

