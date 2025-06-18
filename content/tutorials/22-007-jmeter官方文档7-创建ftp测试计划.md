---
weight: 7
title: JMeter官方文档：7. 创建FTP测试计划
date: '2017-08-24T10:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1603123597878-b14773424269?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---


[《JMeter官方文档--翻译计划》](/2017/08/24/jmeter-translation-plans/) [原文地址](http://jmeter.apache.org/usermanual/build-ftp-test-plan.html)

## 7.创建FTP测试计划
----

在这一章，你将学习如何创建一个基础的[测试计划](http://jmeter.apache.org/usermanual/build-test-plan.html)来测试FTP站点。你将在一个FTP站点上的两个文件中创建四个用户来发送请求。并且，你将告诉用户运行测试两次。所以，总的请求数是（4个用户）x（2个请求）x（重复2次）=16 FTP请求。

为了构造测试计划，你需使用以下元件：[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)，[FTP请求](http://jmeter.apache.org/usermanual/component_reference.html#FTP_Request)，[FTP默认请求](http://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_Defaults)和[用表格察看结果](http://jmeter.apache.org/usermanual/component_reference.html#View_Results_in_Table)。

### 7.1 添加用户
----
你要进行每一个JMeter测试计划的第一步是添加一个线程组元件。线程组告诉JMeter你想要模拟的用户数量，用户应该发送请求的频率，以及他们应该发送多少个请求。
继续添加线程组元件，首先选择测试计划，点击鼠标右键添加菜单，然后选择 __添加→线程组__。

现在你应该看到 __测试计划__ 下的 __线程组__ 元件。如果没有看到元件，单击测试计划元件“展开”测试计划树。

接下来，你需要修改默认配置。如果你还没有选择 __线程组__ 元件，在测试计划树里选择它。现在你应该在JMeter窗口右侧看到线程组控制面板(请参见下面的图7.1)

![](http://img.testclass.net/thread_group.png)

图7.1 默认值的线程组

首先为我们的线程组取一个更具描述性的名称。在名称文本域中，输入“FTP用户”。

接下来将用户数（线程数）增加到4。

在下一个文本域中，Ramp-Up Period（in seconds），使用默认值0秒。这个属性告诉JMeter在启动每个用户之间的时间间隔。例如，如果你在Ramp-Up Period（in seconds）中输入5秒，JMeter将在5秒内完成所有用户的启动。因此，如果我们有5个用户和一个5秒的Ramp-Up Period，那么启动用户之间的时间间隔将是1秒(5个用户/ 5秒= 1个用户每秒)。如果将值设置为0，则JMeter将立即启动所有用户。

最后，在循环次数中输入值2。这个属性告诉JMeter重复测试的次数。要让JMeter重复一直运行你的测试计划，勾选永远的复选框。

> 在大多数应用中你必须手动的保存你在控制面板中的改动。但是在JMeter中，控制面板能自动的保存你做的改动。比如你修改了一个元件的名称，在你离开控制面板后测试计划树会以新的文本来更新（比如选择另一个树元件时）。

看下图7.2 中完整的FTP Users线程组。

![](http://img.testclass.net/07_FTP_users_thread_group.png)

图7.2 FTP Users线程组

### 7.2 添加默认FTP请求配置
----

既然我们已经定义了我们的用户，那么是时候定义他们要执行的任务了。在本节中，你将为你的FTP请求指定默认设置。然后，在7.3节中，使用你在这里指定的一些默认设置中添加 __FTP请求__ 元件。

首先选择FTP用户元件。单击鼠标右键得到添加菜单，然后选择 __添加--配置元件—FTP默认请求__ 。然后，选择这个新元件来查看它的控制面板(参见图7.3)。


![](http://img.testclass.net/07_FTP_request.png)

图7.3 FTP默认请求

像大多数的JMeter元件，[FTP默认请求](http://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_Defaults)控制面板中有一个可修改名称的文本域。在这个例子中，使用默认值。

跳到下一个字段，是 FTP 服务器的服务器名或 IP。你正在构建的测试计划，所有的 FTP 请求将发送到相同的 FTP 服务器， ftp.domain.com，输入这个域名到这个文本域。这是唯一指定默认值的字段，所以其他的字段使用它们的默认值。

> FTP 默认请求元件没有告诉 JMeter 发送一个 FTP 请求。它只是简单定义了 FTP 请求元件使用的默认值。

看下图7.4中完整的FTP默认请求。

![](http://img.testclass.net/07_FTP_request_ip.png)

图7.4 测试计划中FTP默认请求

### 7.3添加FTP请求
----

在我们测试计划中，我们需要两个FTP请求。

> JMeter按照他们在树中出现的顺序发送请求。

首先在FTP Users元件中添加第一个[FTP请求](http://jmeter.apache.org/usermanual/component_reference.html#FTP_Request)（__添加—sampler—FTP请求__），然后，在树中选择FTP请求元件，再编辑下面的属性。

* 1.修改名称的文本域为“file1”；
* 2.修改remote file的文本域为“/directory/file1.txt”；
* 3.修改登录配置中用户名为“anonymous”；
* 4.修改登录配置中密码为“aonymous@test.com”。

因为你已经在 FTP 默认请求元件中指定了服务器名，所以你不需要设置这个值了。

![](http://img.testclass.net/07_FTP_request_file.png)

图7.5 FTP请求文件1

接下来，添加第二个 __FTP请求__ 并且编辑下面的属性：

* 1.修改名称的文本域为“file2”；
* 2.修改remote file的文本域为“/directory/file2.txt”；
* 3.修改登录配置中用户名为“anonymous”；
* 4.修改登录配置中密码为“aonymous@test.com”。

![](http://img.testclass.net/07_FTP_request_file2.png)

图7.6 FTP请求文件2

### 7.4 添加一个监听器浏览/保存测试结果
---

你需要加的测试计划中的最后一个元件是 [监听器](http://jmeter.apache.org/usermanual/component_reference.html#listeners)。这个元件是存储所有FTP请求的结果到文件并展示可视化数据模型。

选择FTP users元件，添加在[表格查看结果](http://jmeter.apache.org/usermanual/component_reference.html#View_Results_in_Table)（__添加→监听器→在表格查看结果__）。运行你的测试然后查看结果。

![](http://img.testclass.net/07_look_result.png)

图7.7 用表格查看结果树




原始封面

![课程图片](https://images.unsplash.com/photo-1603123597878-b14773424269?w=300)

