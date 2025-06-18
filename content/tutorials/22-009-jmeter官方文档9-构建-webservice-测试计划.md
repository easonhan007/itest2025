---
weight: 9
title: JMeter官方文档：9. 构建 WebService 测试计划
date: '2017-08-24T09:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1578115173568-4537ca0635cc?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---


[《JMeter官方文档--翻译计划》](/2017/08/24/jmeter-translation-plans/) [原文地址](http://jmeter.apache.org/usermanual/build-ws-test-plan.html)


### 9. 构建 WebService 测试计划

---
在本章节，你将学习如何创建一个 [测试计划](http://jmeter.apache.org/usermanual/build-test-plan.html) 去测试 WebService。先创建5个用户请求同一个页面，同时每个请求重复2次，因此总数为（5个用户）X（1次请求）X（重复请求）= 10 次 HTTP 请求。构建测试计划过程中，会使用到以下几个元素：[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)、[HTTP 请求](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request)、[聚合报告](http://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Graph)

如果采样器使用Web服务时出现错误，请仔细检查 SOAP 消息，并确保格式正确。 特别要确保 **xmlns** 属性与WSDL完全相同。 如果xml命名空间不同，则 webservice 可能会返回错误。

### 9.1 构建 WebService 测试计划
---
在测试计划中，将会用到 .NET 语言写的web服务，在此就不详细介绍web 服务的编写方法了。如果不会，请自行谷歌 web 服务并尝试用 java 或 .NET熟练起来。必须强调的是，使用 .NET 和 Java 实现 web 服务是有较大差别。该主题太广泛无法写到用户手册里，所以想了解具体差异可参考其他资料。

> Jmeter是按照树状的排列方式去发送请求的

找到菜单中的 __文件 → Templates__ ,  Select Template 中的 __“Building a SOAP Webservice Test Plan”__，点击 __“Creat”__ 按钮。

![图9.1.0 WebService 模版](http://img.testclass.net/09_ws_template.png)
图9.1.0 WebService 模版

__以国内手机号码归属地查询接口为例__
http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl

修改下列选项：

1. 在 "HTTP Request Defaults" 元件中， "__服务器名或IP：__" 选项 填写网址或IP（ws.webxml.com.cn）。
2. 在 "Soap Request" 元件中，"__路径:__" 选项 填写接口路径（/WebServices/MobileCodeWS.asmx）。

![image](http://img.testclass.net/09_ws_http_request1.png)
图9.1.1 WebService 路径

接下来，右键目录栏的 test plan，选择"HTTP Header Manager"，并更新 “SOAPAction” 头以匹配你的 webservice ，如果这个 webservice 不需要 SOAPAction 那就移除掉。目前，只有.NET需要用到 SOAPAction ，所以对于其他Web服务包括JWSDP，Weblogic，Axis，Mind Electric Glue和gSoap等是不需要用到的。

![image](http://img.testclass.net/09_ws_header1.png)

图9.1.2 Webservice信息头

这里需要将 SOAPAction 修改：__"http://WebXml.com.cn/getMobileCodeInfo"__


最后一步就是把 SOAP 信息粘贴到 "Body Data" 的文本框。（参考：图 9.1.1）

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:web="http://WebXml.com.cn/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:getMobileCodeInfo>
         <!--Optional:-->
         <web:mobileCode>186xxxxxxxx</web:mobileCode>
         <!--Optional:-->
         <web:userID></web:userID>
      </web:getMobileCodeInfo>
   </soapenv:Body>
</soapenv:Envelope>
```
9.1.3 Webservice请求默认值

注：将186xxxxxxxx 替换为具体手机号。


### 9.2 增加用户组

---

[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group) 将告诉JMeter需要模拟的用户数量，用户发送请求的频率以及发送请求的数量。

如果还未设置线程组的元素，应该在JMeter窗口右侧部分的线程组控制面板进行选择（参见下图9.2）

![image](http://img.testclass.net/thread_group.png)

图9.2 线程组默认值

首先为线程组提供一个更具描述性的名称。 在名称字段中，输入 JMeter 用户。

接下来，将用户数（有名线程）增加到10。

在下一个字段中，准备时长默认值为0秒。 此属性告诉JMeter启动每个用户需要多长时间。 例如，如果你输入5秒，JMeter将在5秒之后完成所有用户的启动。 因此，如果我们有5个用户和5秒的准备时长，则启动用户之间的延迟将为1秒（5个用户/ 5秒=每秒1个用户）。 如果将值设置为0，那么JMeter将立即启动所有用户。

最后，去掉 __"永远"__ 的勾选并填写数字2，代表jmeter将重复执行2次；如果默认填写0，Jmeter只会执行一次；如果勾选 __"永远"__，代表Jmeter会重复执行。

>在大多数应用程序中，你必须手动更改并保存才能生效。 但是，在JMeter中，控制面板会在你进行更改时自动保存生效。 比如你更改元素的名称，则在离开控制面板后，新的元素名称就会生效。

完整的JMeter用户线程组参见图9.2

![image](http://img.testclass.net/09_ws_threadgroup.png)

图9.3 Jmeter用户线程组

### 9.3 增加监听器查看测试结果
---
最后一步是添加监听器到测试计划。 监听器的左右是负责将HTTP请求的所有结果存储在文件中，并呈现数据的可视化模型。

选择JMeter Users元素并添加一个聚合图监听器（添加 → 监听器 → Aggregate Graph）。 然后指定输出文件的目录和文件名。 也可以选择浏览按钮并浏览到目录，然后输入文件名。

![image](http://img.testclass.net/09_ws_listener.png)

图9.4 图表结果监听器

### 9.4 Rest Webservice
---
测试REST Webservice手法与上述相似，只需要在HTTP请求中进行修改即可。

方法：选择要测试的一个
参数设置：可以是JSON，XML或任何自定义文本

你可能还需要修改 “HTTP头管理器” 来选择正确的 "Content-Type"。




原始封面

![课程图片](https://images.unsplash.com/photo-1578115173568-4537ca0635cc?w=300)

