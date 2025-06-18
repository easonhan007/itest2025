---
weight: 5
title: （五）soapUI创建SOAP项目
date: '2017-09-20T22:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1491929007750-dce8ba76e610?w=300
tags: []
categories:
- SoupUI实用教程
lightgallery: true
toc:
  auto: false
---



#### 创建 SOAP 项目
----

打开 soapUI 工具。创建一个SOAP项目。

![](http://img.testclass.net/soapui_main_window.png)

在窗口左侧导航栏，右键 __Projects --> New SOAP Project__。

#### 添加SOAP接口
----
以国内手机号码归属地查询接口为例：

__Project Name__：MobileCodeWS为项目名称。

__Initial WSDL__：http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl 为接口URL。

![](http://img.testclass.net/soapui_new_soap_project.png)

点击 __OK__ 按钮，创建项目完成。

依次展开：__MobileCodeWS-->MobileCodeWSSoap-->getMobileCodeInfo/__，双击 __Request 1__，填写接口查询的手机号。如下图。

![](http://img.testclass.net/soapui_soap_if_data.png)

请求接口详细配置如下：

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://WebXml.com.cn/">
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
注：将 xxxxxxxx 替换为手机号。

#### 运行测试
----
点击 __Request 1__ 窗口左上角的绿色 __运行__ 按钮，发送 SOAP 请求。右侧窗口将会显示接口返回结果。

![](http://img.testclass.net/soapui_soap_if_request.png)


一个简单的 SOAP 接口测试完成了。




原始封面

![课程图片](https://images.unsplash.com/photo-1491929007750-dce8ba76e610?w=300)

