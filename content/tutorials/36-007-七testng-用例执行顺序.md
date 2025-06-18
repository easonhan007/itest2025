---
weight: 7
title: （七）TestNG 用例执行顺序
date: '2017-11-25T12:30:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1542831371-d531d36971e6?w=300
tags: []
categories:
- TestNG教程
lightgallery: true
toc:
  auto: false
---



有时候，我们希望用例按照我们要求的顺序来执行。TestNG 同样可以满足这一点要求。

#### 实例
---
```Java
import org.testng.annotations.Test;
import static org.testng.AssertJUnit.assertEquals;


public class CaseRunTest {

    @Test
    public void testCase1(){
        assertEquals(2+2, 4);
    }

    @Test
    public void testCase2(){
        assertEquals(2+2, 4);
    }

    @Test
    public void testCase3(){
        assertEquals(2+2, 4);
    }
}
```

通过 __testng.xml__ 文件修改配置。

```
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="测试套件">
    <test name="简单测试" preserve-order="false">
        <classes>
            <class name="test.sample.CaseRunTest">
                <methods>
                    <include name="testCase3" />
                    <include name="testCase1" />
                    <include name="testCase2" />
                </methods>
            </class>
        </classes>
    </test>
</suite>
```
* preserve-order 参数用于控制测试用例的执行顺序。如果为：__true__，测试用例的顺序为：testCase > testCase1 > testCase2。如果为:__false__ ，那么默认会按照用例的名称的有字母/数字的顺序执行：testCase1 > testCase2 > testCase3。

不设置的情况下默认为 __true__ 。




原始封面

![课程图片](https://images.unsplash.com/photo-1542831371-d531d36971e6?w=300)

