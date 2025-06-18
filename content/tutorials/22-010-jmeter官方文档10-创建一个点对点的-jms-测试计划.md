---
weight: 10
title: JMeter官方文档：10. 创建一个点对点的 JMS 测试计划
date: '2017-08-24T08:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1634896709636-f0216dc27b57?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---


[《JMeter官方文档--翻译计划》](/2017/08/24/jmeter-translation-plans/) [原文地址](http://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html)

## 10.创建一个点对点的 JMS 测试计划
---

>确保所需的jar文件位于JMeter lib目录中。 如果没有，关闭JMeter，复制jar文件并重新启动JMeter。 [参见详细教程](http://jmeter.apache.org/usermanual/get-started.html#libraries_activemq)

在本节中，将学习如何创建[测试计划](http://jmeter.apache.org/usermanual/build-test-plan.html)来测试JMS点对点消息传递。 先设置1个线程组5个线程发送4个请求，通过队列的形式发送。 固定的回复队列将用于监听回复消息。 要构建测试计划，您将使用以下元素：[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)，[JMS点对点](http://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point)和[图形结果](http://jmeter.apache.org/usermanual/component_reference.html#Graph_Results)。

关于 JMS 的一般注意事项：目前有两个JMS采样器。 一个是使用 JMS Topic，另一个时使用 Queue。 Topic 通常被称为pub/sub消息。 Topic 消息通常用于生产者发布消息并由多个订阅者接收的情况。 JMS 采样器需要 JMS 实现 jar 文件，比如 Apache ActiveMQ 包。 [参见这里](http://jmeter.apache.org/usermanual/get-started.html#libraries_activemq)的 ActiveMQ 提供的 jar 的列表。

### 10.1 增加一个线程组
---
首先，对每个要执行的 JMeter 测试计划添加一个线程组。 线程组会告诉 JMeter 需要模拟的用户数量，发送请求的频率以及发送请求的数量。

然后，添加 ThreadGroup 元素，首先选择测试计划，单击鼠标右键获取添加菜单，然后选择添加→线程组。

接下来，需要修改默认属性。 现在可以在 JMeter 窗口的右侧部分看到线程组控制面板（参见下面的图10.1）

![image](http://img.testclass.net/thread_group.png)

图10.1 线程组默认设置

首先为我们的线程组提供一个更具描述性的名称。在名称字段中，输入点对点。

接下来，将用户数（称为线程）增加到5。

在下一个字段中，将 “Ramp-Up Period” 设置为0秒。 此属性告诉 JMeter 启动每个用户需要多长时间。 例如，如果您输入5秒的准备时长，JMeter 将在5秒之后完成所有用户的启动。 因此，如果我们有5个用户和5秒的准备时长，则启动用户之间的延迟将为1秒（5个用户/ 5秒=每秒1个用户）。 如果将值设置为0，那么 JMeter 将立即启动所有用户。

清除标记为 “永远” 的复选框，并在循环计数字段中输入值4。 该属性告诉 JMeter 重复测试多少次。 如果输入循环计数值为0，那么 JMeter 将只运行一次测试。 要让 JMeter 重复运行测试计划，请选中 “永远” 复选框。

>在大多数应用程序中，你必须手动更改并保存才能生效。 但是，在 JMeter 中，控制面板会在你进行更改时自动保存生效。 比如你更改元素的名称，则在离开控制面板后，新的元素名称就会生效。

### 10.2 增加一个 JMS 点对点采样器
---
首先将采样器 [JMS Point-to-Point](http://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point) 添加到点对点元素（__添加 → Sampler → JMS Point-to-Point__）。 然后，在树中选择 JMS Point-to-Point 采样器元素。 在构建示例中，将提供可与 ActiveMQ 3.0 一起使用的配置。

名称 | 值| 描述
---|---|---
|QueueConnectionFactory | ConnectionFactory |这是连接 ActiveMQ 的默认 JNDI 入口。
JNDI Name Request Queue| Q.REQ|在 JNDI 属性中定义的 JNDI 名称
|JNDI Name Reply Queue|Q.RPL|在 JNDI 属性中定义的 JNDI 名称
|Communication Style	|Request Response|	代表在 JMeter 外部运行的服务并响应请求。 此服务必须监听请求队列并将消息发送到由消息引用的队列.getJMSReplyTo()
|Content |test| 内容
|JMS Properties||ActiveMQ 不需要设置
|InitialContextFactory|org.apache.activemq.jndi.ActiveMQInitialContextFactory	| ActiveMQ 的标准 InitialContextFactory
|queue.Q.REQ	|example.A	|定义了一个名为 Q.REQ 的 JNDI 队列请求指向了 example.A
|queue.Q.RPL|	example.B|定义了一个名为 Q.RPL 的 JNDI 队列请求指向了 example.B
|Provider URL |tcp://localhost:61616| ActiveMQ 地址和端口

### 10.2 增加一个结果监听器
---
最后一步是添加监听器到测试计划。 监听器的作用是负责将HTTP请求的所有结果存储在文件中，并呈现数据的可视化模型。

选择JMeter Users元素并添加一个聚合图监听器（添加 → 监听器 → Aggregate Graph）。 然后指定输出文件的目录和文件名。 也可以选择浏览按钮并浏览到目录，然后输入文件名.

![image](http://img.testclass.net/10_graph_results.png)

图10.2 图形结果监听器




原始封面

![课程图片](https://images.unsplash.com/photo-1634896709636-f0216dc27b57?w=300)

