---
weight: 5
title: （五）Java数据结构：数组和HashMap
date: '2018-01-17T14:38:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1588522621257-23648044339e?w=300
tags: []
categories:
- Java语言基础教程
lightgallery: true
toc:
  auto: false
---



Java的数据结构包含的数接口和类分好多种，不过，我觉得最常用的就是数组和HashMap（反正是我最常用的），所以，将他们拿出来介绍一下。


#### 数组
---

__数组__ 保存的是一组有顺序的、具有相同类型的数据。在Java的数组中，所有数据元素的数据类型都是相同的，可以通过数组的下标来访问数组。

```Java

public class JavaList {

    public static void main(String[] args) {

        String[] group = new String[5];
        group[0] = "小明";
        group[1] = "老师";
        group[2] = "老王";
        group[3] = "张三";
        group[4] = "李四";

        for (int i = 0; i < group.length; i++) {
            System.out.println(group[i]);
        }
    }
}
```
在创建数组的时候需要为其分配空间大小， 在本例子中， 通过循环将 0~4 之间的 5 个数放到的数组 group 中。

针对 group 进行循环时，借助 `length` 可计算出数组的长度。

在访问数组时，需要指定数组的下标，例：`group[2]` 取到的结果就是“老王”。

另外一种数组的创建方式：

```Java

String[] fruits = {"bananas", "apples", "pears", "oranges"};

```

__实例: 冒泡排序__

有一个数组，里面存放的数据是不规则的，从大小到重新排序。实现代码如下：

```Java
public class BubbleSort {

    public static void main(String[] args) {

        //排序数组
        int[] intArray = {12, 11, 45, 6, 4, 8, 43, 40, 57, 3, 22};

        System.out.println("排序前的数组:");
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i] + " ");
        }
        System.out.println();

        // 冒泡排序
        int temp;
        for (int i = 0; i < intArray.length; i++) {

            for (int j = i + 1; j < intArray.length; j++) {

                //当后一个数大于前一个，交换位置
                if (intArray[i] < intArray[j]) {
                    temp = intArray[i];
                    intArray[i] = intArray[j];
                    intArray[j] = temp;
                }
            }
        }

        System.out.println("排序后的数组:");
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i] + " ");
        }
        System.out.println();
    }
}
```

运行结果：

```
排序前的数组:
12 11 45 6 4 8 43 40 57 3 22
排序后的数组:
57 45 43 40 22 12 11 8 6 4 3
```

#### HashMap
---

HashMap 是一个散列表，它存储的内容是键值对(key-value)映射。 其实，我们一般叫 “字典”。

```Java
import java.util.HashMap;
import java.util.Iterator;

public class JavaHashMap {

    public static void main(String[] args) {

        //定义HashMap
        HashMap<String, String> hm = new HashMap<String, String>();
        //添加字典
        hm.put("username", "password");
        hm.put("Jim", "1155689");
        hm.put("Jane", "1255669");
        hm.put("Kevin", "1165669");

        //测试 key 是否包含 username,返回值为 true/false
        System.out.println(hm.containsKey("username"));
        System.out.println("===================>");

        //获取 key 所对应的 vlaue
        System.out.println(hm.get("Jim"));
        System.out.println("===================>");

        //获取整个字典数据
        System.out.println(hm.entrySet());
        System.out.println("===================>");

        //循环打印每一对 key:value
        Iterator<?> it = hm.entrySet().iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        System.out.println("===================>");

        //分别获取 key 的值， 和 value 的值。
        Iterator<String> it2 = hm.keySet().iterator();
        while (it2.hasNext()) {
            //获得字典的 key(username)
            String username = (String) it2.next();
            System.out.println(username);
            //获得字典的 value(节点)
            String password = hm.get(username);
            System.out.println(password);
        }
    }
}
```

该例子中包含了 HashMap的基本操作。“字典”的定义需要引用（import）HashMap类。

在遍历字典中的每个key:value时，用到了迭代器（Iterator）。




原始封面

![课程图片](https://images.unsplash.com/photo-1588522621257-23648044339e?w=300)

