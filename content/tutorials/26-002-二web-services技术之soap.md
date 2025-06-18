---
weight: 2
title: （二）Web Services技术之SOAP
date: '2017-09-21T01:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1523224042829-4731dd15a3bb?w=300
tags: []
categories:
- SoupUI实用教程
lightgallery: true
toc:
  auto: false
---



<br>
__早前的 Web Services 技术由 SOAP、WSDL 和 UDDI 就构成。__

#### SOAP
----
Simple Object Access Protocol，简称 SOAP，简单对象访问协议。

SOAP 是基于 XML 在分散或分布式的环境中交换信息的简单的协议。允许服务提供者和服务客户经过防火墙在互联网上进行通信。

SOAP 的设计是为了在一个松散的、分布的环境中使用 XML 对等地交换结构化的和类型化的信息提供了一个简单且轻量级的机制。

XML是可以扩展标记语言。

    <bookstore>
        <book category="COOKING">
            <title lang="en">Everyday Italian</title>
            <author>Giada De Laurentiis</author>
            <year>2005</year>
            <price>30.00</price>
        </book>
    </bookstore>


SOAP 消息的基本结构

    <?xml version="1.0"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
    soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

      <soap:Header>
          ...
          ...
      </soap:Header>

      <soap:Body>
          ...
          ...
          <soap:Fault>
            ...
            ...
          </soap:Fault>
      </soap:Body>

    </soap:Envelope>

当 SOAP 消息真正需要在网络上传输的时候，SOAP 消息能够与不同的底层传输协议进行绑定，同时，SOAP 消息也可以在很多种消息传输模式中使用。包括超文本传输协议（HTTP），简单邮件传输协议（SMTP），多用途网际邮件扩充协议（MIME）。它还支持从消息系统到远程过程调用协议（RPC）等大量的应用程序。

<font color=#DC143C> 当然，大多的情况还是绑定在 HTTP 协议上面传输。所以，这就导致许多人认为 SOAP 就是 HTTP + XML，或者认为 SOAP 是 HTTP 的 POST 请求的一个专用版本，遵循一种特殊的 XML 消息格式。虽然，我们看到的情况确实如此，但显然这些观点对SOAP的解释是错误和片面的。</font>

![](http://img.testclass.net/sopaui_soap_interface.png)

如图，为 SOAP 消息实例，利用 HTTP 协议向手机号码查询服务请求的 SOAP 消息。


#### WSDL
----

Web Services Description Language，网络服务描述语言，简称 WSDL。它是一门基于 XML 的语言，用于描述 Web Services 以及如何对它们进行访问。

WSDL 文档主要使用以下几个元素来描述某个 Web Services：

* <portType>  Web Services执行的操作。
* <message>  Web Services使用的消息。
* <types>     Web Services使用的数据类型。
* <binding>   Web Services使用的通信协议。

```
<wsdl:definitions xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing" xmlns:tns="tns" 
xmlns:plink="http://schemas.xmlsoap.org/ws/2003/05/partner-link/" xmlns:xop="http://www.w3.org/2004/08/xop/include"
xmlns:senc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s12env="http://www.w3.org/2003/05/soap-envelope/" 
xmlns:s12enc="http://www.w3.org/2003/05/soap-encoding/" xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:senv="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
targetNamespace="tns" name="Application">
<wsdl:types>
  <xs:schema targetNamespace="tns" elementFormDefault="qualified">
  <xs:import namespace="http://www.w3.org/2001/XMLSchema"/>
    <xs:complexType name="say_hello">
      <xs:sequence>
        <xs:element name="name" type="xs:string" minOccurs="0" nillable="true"/>
      </xs:sequence>
    </xs:complexType>
    <xs:complexType name="say_helloResponse">
      <xs:sequence>
        <xs:element name="say_helloResult" type="xs:string" minOccurs="0" nillable="true"/>
      </xs:sequence>
    </xs:complexType>
  <xs:element name="say_hello" type="tns:say_hello"/>
  <xs:element name="say_helloResponse" type="tns:say_helloResponse"/>
  </xs:schema>
</wsdl:types>
<wsdl:message name="say_hello">
<wsdl:part name="say_hello" element="tns:say_hello"/>
</wsdl:message>
  <wsdl:message name="say_helloResponse">
    <wsdl:part name="say_helloResponse" element="tns:say_helloResponse"/>
  </wsdl:message>
<wsdl:portType name="Application">
<wsdl:operation name="say_hello" parameterOrder="say_hello">
<wsdl:input name="say_hello" message="tns:say_hello"/>
<wsdl:output name="say_helloResponse" message="tns:say_helloResponse"/>
</wsdl:operation>
</wsdl:portType>
  <wsdl:binding name="Application" type="tns:Application">
  <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
  <wsdl:operation name="say_hello">
    <soap:operation soapAction="say_hello" style="document"/>
      <wsdl:input name="say_hello">
        <soap:body use="literal"/>
      </wsdl:input>
    <wsdl:output name="say_helloResponse">
    <soap:body use="literal"/>
  </wsdl:output>
  </wsdl:operation>
  </wsdl:binding>
<wsdl:service name="Application">
  <wsdl:port name="Application" binding="tns:Application">
    <soap:address location="http://10.2.70.10:7789/SOAP/?wsdl"/>
  </wsdl:port>
</wsdl:service>
</wsdl:definitions>
```

* WSDL 端口

<portType> 元素是最重要的 WSDL 元素。

它可描述一个 Web Services 可被执行的操作，以及相关的消息。可以把 <portType> 元素比作传统编程语言中的一个函数库（或一个模块、或一个类）。

* WSDL 消息

<message> 元素定义一个操作的数据元素。

每个消息均由一个或多个部件组成。可以把这些部件比作传统编程语言中一个函数调用的参数。

* WSDL types

<types> 元素定义 Web Services 使用的数据类型。

为了最大程度的平台中立性，WSDL 使用 XML Schema 语法来定义数据类型。

* WSDL Bindings

<binding> 元素为每个端口定义消息格式和协议细节。

对于接口来说，接口文档非常重要，它描述如何访问接口。WSDL 就可以看作 Web Services 接口的一种标准格式的“文档”。我们通过阅读 WSDL 就知道如何调用 Web Services 接口。



#### UDDI
----
Universal Description，Discovery and Integration，简称 UDDI，可译为 “通用描述、发现与集成服务”。

WSDL用来描述访问特定的 Web Services 的一些相关的信息，那么在互联网上，或者在企业的不同部门之间，如何来发现我们所需要的 Web Services 呢？而 Web Services 提供商又如何将自己开发的 Web Serivce 公布到因特网上呢？这就需要使用到 UDDI 了。

* UDDI 是一个独立于平台的框架，通过使用 Internet 来描述服务，发现企业，并对企业服务进行集成。
* UDDI 指的是通用描述、发现与集成服务。
* UDDI 是一种用于存储有关 Web Services 的信息的目录。
* UDDI 是一种由WSDL描述的 Web Services 界面的目录。
* UDDI 经由 SOAP 进行通信。
* UDDI 被构建入了微软的 .NET 平台。

UDDI 可以帮助 Web 服务提供商在互联网上发布 Web Services 的信息。UDDI 是一种目录服务，企业可以通过 UDDI 来注册和搜索 Web Services 。

![](http://img.testclass.net/sopaui_uddi_server.png)

![](http://img.testclass.net/sopaui_uddi_server2.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1523224042829-4731dd15a3bb?w=300)

