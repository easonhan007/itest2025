---
weight: 11
title: JMeter官方文档：11. 新建一个 JMS 主题的测试计划
date: '2017-08-24T08:55:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1567798067592-370ad70700a3?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---



[《JMeter官方文档--翻译计划》](/2017/08/24/jmeter-translation-plans/) [原文地址](http://jmeter.apache.org/usermanual/build-jms-topic-test-plan.html)

## 11.新建一个 JMS 主题的测试计划
---
> JMS 需要下载一些可选的jar 文件。详细信息请参阅 第一章：新手入门。

在本章节，将学习如何创建[测试计划](http://jmeter.apache.org/usermanual/build-test-plan.html)来测试JMS提供程序。创建5个订阅者和1个发布者。创建2个线程组并且设置每个线程组迭代10次。消息总数是（6个线程）x （1 个消息）x（重复10次）= 60 个消息。为了构建测试计划将使用以下元素：[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group) , [JMS 发布者](http://jmeter.apache.org/usermanual/component_reference.html#JMS_Publisher)， [JMS 订阅者](http://jmeter.apache.org/usermanual/component_reference.html#JMS_Publisher)， 和 [图结果](http://jmeter.apache.org/usermanual/component_reference.html#Graph_Results)。

关于JMS的一般注意事项：目前有两种 JMS 采样器(samplers)。一种使用 JMS 主题(topics)，另一种使用队列(queues)。主题消息通常被称为发布/订阅消息。主题消息传递通常用于消息由生产者发布并由多个订阅者消费的情况。队列消息传递通常用于发件人期望响应的事务。消息系统与普通的HTTP请求完全不同。在HTTP中，一个用户发送一个请求并得到一个响应。消息系统可以通过同步和异步模式工作。JMS采样器需要JMS实现的jar文件（由于JMeter不提供JMS实现的jar，需要下载后放置lib库）; 例如，来自Apache ActiveMQ。请参阅[这里](http://jmeter.apache.org/usermanual/get-started.html#libraries_activemq) 查看 ActiveMQ 提供的 jar 列表。

### 11.1添加用户
---
第一步是添加一个[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)元素。线程组告诉JMeter想要模拟的用户数量，发送请求的频率以及发送请求的数量。

添加线程组元素，首先选择测试计划，单击鼠标右键获取添加菜单，然后选择 __添加 → 线程组__。此时可以在测试计划下面看到线程组元素，如果不能，可以通过在测试计划元素上单击“展开”测试计划树。

接下来，你需要修改默认属性。如果尚未选择树中的线程组元素，请先选择。此时可以看到JMeter窗口右侧的线程组控制面板（请参见下面的图11.1）

![](http://img.testclass.net/thread_group.png)
图11.1. 线程组默认设置

首先为我们的线程组提供一个更具描述性的名称。在名称字段输入: __Subscribers__ 。

接下来，将用户（称为线程）的数量增加到 __5__。

在下一个字段 Ramp-Up Period 中，将该值设置为 __0__ 秒。这个属性告诉JMeter启动每个用户之间要延迟多久。例如，如果输入一个5秒的渐变周期，JMeter将在5秒钟内完成所有用户的启动。所以，如果我们有5个用户和一个5秒钟的Ramp-Up Period值，那么用户启动之间的延迟将是1秒（5个用户/ 5秒= 1个用户每秒）。如果将该值设置为0，则JMeter将立即启动所有用户。

清除循环计数字段标记为 “__永远__” 的复选框，并在此字段中输入值 __10__ 。这个属性告诉JMeter重复测试的次数。如果输入循环计数值0，那么JMeter将只运行一次测试。如果要让JMeter反复运行测试计划，请勾选 永远 复选框。

重复该过程并添加另一个线程组。对于第二个线程组，在名称字段中输入：__Publisher__，将线程数设置为1，迭代设置为10。

> 在大多数应用程序中，您必须手动接受在控制面板中所做的更改。但是，在JMeter中，控制面板自动接受所做的更改。如果更改元素的名称，则在离开当前控制面板后使用新文本更新树（例如，选择另一个树元素时）。

### 11.2增加JMS订阅者和发布者
---
确保需要的 jar 文件在JMeter的lib目录。如果不是，请关闭JMeter，将jar文件复制到对应的目录并重新启动JMeter。

首先添加 JMS Subscriber取样器到 Subscriber 线程组（__添加 → Sampler → JMS Subscriber__）。然后选择树中的JMS订阅者元素编辑如下参数：

1.修改名称字段值为："__Sample Subscriber__"

2.如果 JMS 提供使用 __jndi.properties__ 文件，则选中该框

3.在Initial Context Factory字段输入InitialContextFactory 类，例如：使用ActiveMQ 5.4，值为 "__org.apache.activemq.jndi.ActiveMQInitialContextFactory__"

4.在Provider URL字段输入提供程序URL。如果存在的话，是JNDI服务器的URL。例如：在本地机器使用默认端口的ActiveMQ 5.4 ，URL值是"__tcp://localhost:61616__"

5.在Connection Factory字段输入connection factory的名称。有关信息请参照JMS提供的官方文档。对于ActiveMQ，默认值是"__ConnectionFactory__"

6.在Destination字段输入消息主题的名称。对于ActiveMQ 动态主题（动态创建主题），示例值为"__dynamicTopics/MyStaticTopic1__"

>备注: Setup 选择At Startup 意味着JMeter 从测试开始监听此字段配置的消息主题而没有更改名称的可能。Setup 选择 Each sample意味着JMeter在每个JMS订阅者采样器运行前重新开始监听，此配置允许Destination字段值是变量。

7.如果JMS提供程序需要身份认证，选择“__required__”并输入用户名和密码。例如： Orion JMS 需要身份认证，但是ActiveMQ和MQSeries不需要

8.在 __Number of samples to aggregate__ 字段输入 __10__。通过采集器聚合消息，出于性能方面的考虑，小消息能够更快速的到达 。如果采集器不能聚合消息，JMeter不能够继续运行

9.如果想要读取响应消息，选中Read Response框

10.订阅者有两种客户端实现，如果其中一个客户端选项使得JMS 提供程序产生僵尸进程，则选中另一个

![](http://jmeter.apache.org/images/screenshots/jms/jms_sub.png)

图 11.2. JMS 订阅者

接下来添加 JMSPublisher 取样器到 Publisher 线程组（__添加 → Sampler → JMS Publisher__）。然后选择树中的JMS发布者元素编辑如下参数：

1.修改名称字段值为："__Sample Publisher__"

2.如果JMS 提供使用 __jndi.properties__ 文件，则选中该框

3.在Initial Context Factory字段输入InitialContextFactory 类，例如：使用ActiveMQ 5.4，值为 "__org.apache.activemq.jndi.ActiveMQInitialContextFactory__"

4.在Provider URL字段输入提供程序URL。如果存在的话，是JNDI服务器的URL。例如：在本地机器使用默认端口的ActiveMQ 5.4 ，URL值是"__tcp://localhost:61616__"

5.在Connection Factory字段输入connection factory的名称。有关信息请参照JMS提供的官方文档。对于ActiveMQ，默认值是"__ConnectionFactory__"

6.在Destination字段输入消息主题的名称。对于ActiveMQ 动态主题（动态创建主题），示例值为"__dynamicTopics/MyStaticTopic1__"

> 备注: Setup 选择At Startup 意味着JMeter 从测试开始监听此字段配置的消息主题而没有更改名称的可能。Setup 选择 Each sample意味着JMeter在每个JMS发布者采样器运行前重新开始监听，此配置允许Destination字段值是变量。

7.如果JMS提供程序需要身份认证，选择“__required__”并输入用户名和密码。例如： Orion JMS 需要身份认证，但是ActiveMQ和MQSeries不需要

8.在 __Number of samples to aggregate__ 字段输入 __10__。通过采集器聚合消息，出于性能方面的考虑，小消息能够更快速的到达 。如果采集器不能聚合消息，JMeter不能够继续运行

9.选择合适的配置生成发布的消息。如果希望随机的选择消息，则将消息放置在目录中，并且
通过浏览选择目录

10.选择消息类型。如果消息是object类型或者映射消息，确保消息正确生成


![](http://jmeter.apache.org/images/screenshots/jms/jms_pub.png)

图 11.3. JMS 发布者

### 11.3增加测试结果监听器
---
需要添加到测试计划的最后一个元素是一个 [监听器](http://jmeter.apache.org/usermanual/component_reference.html#listeners)。这个元素负责将所有的HTTP请求结果存储在一个文件中，并呈现数据的可视化模型。

选择 __测试计划__ 元素并添加一个 [图形结果](http://jmeter.apache.org/usermanual/component_reference.html#Graph_Results)监听器（__添加  →  监听器  →  图形结果__）。接下来，需要指定输出文件的目录和文件名。可以将其输入到文件名字段中，也可以选择浏览按钮并浏览到目录，然后输入文件名。


![](http://jmeter.apache.org/images/screenshots/graph_results.png)

图 11.4. 图形结果监听




原始封面

![课程图片](https://images.unsplash.com/photo-1567798067592-370ad70700a3?w=300)

