---
weight: 6
title: （六）TestNG 用例分组
date: '2017-11-25T12:35:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1573496130407-57329f01f769?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



有时候我们的测试用例并不想以测试包、类和用例为单位去运行。测试用例可以有多个纬度去标识。

例如，可以根据用例的重要程度划分：

* 重要程度：__低——>中——>高__

或者，根据用例的类型划分：

* 类型：__正常——>异常__


TestNG 允许我们给测试用例贴标签。我们可以根据这些标签有选择地的跳过或执行这些用例。

#### 实例
---

```java
import org.testng.annotations.Test;

import static org.testng.AssertJUnit.assertEquals;


@Test(groups = {"功能测试"})
public class TagTest {

    @Test(groups={"高", "正常"})
    public void testCase1(){
        assertEquals(2+2, 4);
    }

    @Test(groups = {"高", "正常"})
    public void testCase2(){
        assertEquals(5-3, 2);
    }
    @Test(groups = {"中", "正常"})
    public void testCase3(){
        assertEquals(2/1, 2);
    }

    @Test(groups = {"低", "异常"})
    public void testCase4(){
        assertEquals(2/0, 1);
    }

}
```
接下来配置 __testng.xml__ ，根据标签筛选要运行的测试用例。
```
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="测试套件" verbose="1" >
    <test name="简单测试">
        <groups>
            <run>
                <exclude name="异常"  />   <!-- 排除不执行的测试用例 -->
                <include name="高"  />  <!-- 指定执行的测试用例 -->
            </run>
        </groups>

        <classes>
            <class name="test.sample.TagTest"/>
        </classes>
    </test>
</suite>
```

* `<groups>...</groups>` 测试组标签。
* `<run>...</run>` 运行测试。
* `<exclude>`  根据groups的设置，排除不执行的用例。
* `<include>`  根据groups的设置，指定执行的测试用例。

根据上面的配置，运行测试： testCase1 和 testCase2 两条用例将被执行。

不要忘了，我们给 __TagTest__ 测类同样也划分了组（`groups = {"功能测试"}`）,现在修改 __testng.xml__ 配置。

```
……
<groups>
    <run>
        <exclude name="异常"  />   <!-- 排除不执行的测试用例 -->
        <include name="功能测试"  />  <!-- 指定执行的测试用例 -->
    </run>
</groups>
……
```
再次运行测试：testCase1、testCase2 和 testCase3 三条用例将被执行。




原始封面

![课程图片](https://images.unsplash.com/photo-1573496130407-57329f01f769?w=300)

