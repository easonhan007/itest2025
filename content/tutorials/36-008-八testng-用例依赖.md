---
weight: 8
title: （八）TestNG 用例依赖
date: '2017-11-25T12:25:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/uploads/141103282695035fa1380/95cdfeef?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



当某一条用例运行失败时，其它用例必然也会失败，所以，我们就没有必要再运行其它用例了，这个时候我们就可以设置用例之间的依赖。

#### 测试方法依赖
---

```java
import org.testng.annotations.Test;
import static org.testng.AssertJUnit.assertEquals;


public class DependentMethodsTest {

    @Test
    public void testAdd1(){
        assertEquals(3+1, 5);
    }

    @Test(dependsOnMethods = {"testAdd1"})
    public void testAdd2(){
        assertEquals(3+2, 5);
    }

}
```
* dependsOnMethods 来设置用例的依赖，当 testAdd1() 运行失败时，则 testAdd2() 不再被执行。

#### 测试组依赖
---
```
import org.testng.annotations.Test;
import static org.testng.AssertJUnit.assertEquals;


public class DependentGroupsTest {

    @Test(groups={"funtest"})
    public void testAdd1(){
        assertEquals(3+1, 5);
    }

    @Test(groups={"funtest"})
    public void testAdd2(){
        assertEquals(3+2, 5);
    }

    @Test(dependsOnGroups = {"funtest"})
    public void testAdd3(){
        assertEquals(3+2, 5);
    }

}
```
* dependsOnGroups 来设置组的依赖，testAdd1()和 testAdd2() 同属于于 funtest组，testAdd3() 依赖于funtest组，该组有中有一条用例运行失败，则testAdd3() 不再执行。




原始封面

![课程图片](https://images.unsplash.com/uploads/141103282695035fa1380/95cdfeef?w=300)

