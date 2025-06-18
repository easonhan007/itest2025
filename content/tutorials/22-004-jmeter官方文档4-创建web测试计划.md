---
weight: 4
title: JMeter官方文档：4. 创建web测试计划
date: '2017-08-24T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1659102264035-0bb2210d92e3?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---


[《JMeter官方文档--翻译计划》](/2017/08/24/jmeter-translation-plans/) [原文地址](http://jmeter.apache.org/usermanual/build-web-test-plan.html)



## 4. 创建web测试计划
----

在这一章，我们将学习如何创建基本的[测试计划](http://jmeter.apache.org/usermanual/build-test-plan.html)来测试一个web网站。您将创建五个用户并发送请求到JMeter网站的两个页面。同时，设置用户运行测试两次。因此，请求的总数是（5个用户）x（2个请求）x（重复2次）＝20个HTTP请求。要构建测试计划，您将使用以下元素：[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)、[HTTP请求](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request)、[HTTP请求默认值](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults)和[图表结果](http://jmeter.apache.org/usermanual/component_reference.html#Graph_Results)。

想要创建一个更深层次的测试计划，请查看[建立一个更高级的web测试计划](/jmeter/jmeter-doc-05/)。

### 4.1 添加用户
---

做每一个测试计划之前的第一步是添加一个[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)。在JMeter的线程组中设置要模拟的用数量，请求发送的频率，以及请求发送的次数。

在添加线程组之前先鼠标选中测试计划，然后单击鼠标右键，选择 __“ 添加 → 线程组 ”__。

你现在应该看到在测试计划下的线程组元素。如果您没有看到元素，你需要单击“测试计划”来展开‘测试计划树’。

接下来，你需要修改默认的属性。在树中选中该线程组，如果你已经选择。你现在应该在JMeter窗口右部看到线程组控制面板（见下面的图4.1）

![](http://img.testclass.net/http://img.testclass.net/thread_group.png)
图4.1 线程组默认值

我们为线程组提供一个更具体的描述性名称，在名称栏里输入：__JMeter Users__。

接下来，设置用户数量（线程数量）为5.

在下一个字段中，设置过渡时期，保留默认值1，这个属性告诉Jmeter启动每个用户需要多长时间.例如，如果你设置过渡时期为5s，Jmeter将会在5s之内完成所有用户的启动，所以，如果你设置了5个线程数，过渡期为5s，那么启动线程之间的过渡期将是1s（5用户/5s=每秒1个用户）.如果你设置这个值为0，那么JMeter将立即开启你所有的线程，中间没有间隔。

最后一行，选择循环2次，这个属性是告诉JMeter要重复测试多少次，如果你设置的值是1，JMeter将就跑一遍，如果选择‘永远’复选框的话，JMetre将重复运行测试计划。

 >在大多数应用程序中，你必须手动保存才能生效，然而，在JMeter中，控制面板会在你进行更改时自动保存。如果你改变了一个元素的名称，那么在你离开控制面板上之后，新元素、就会生效（例如，当我们在选择其它树元素时）

查看图4.2已经设置好的JMeter线程组

![](http://img.testclass.net/04_jmeter_create_web_plan.png)


### 4.2添加HTTP请求默认值
---
现在我们已经定义了我们的用户，是时候来定义他们将要执行的任务了。在本节中，您将指定你的HTTP请求的默认设置。然后，在第4.3节中，您将添加使用此处指定的默认设置的HTTP请求元素。

首先选择JMeter用户（线程组）。点击你的鼠标右键来添加菜单，然后选择 __“添加→配置元件→HTTP请求默认值”__。然后选中HTTP请求默认值以查看其控制面板（见图4.3）。

![](http://img.testclass.net/04_jmeter_http_requestd_defaults.png)
图4.3，HTTP请求默认值

像很多JMeter元素一样，[HTTP请求默认值](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults)的控制面板都有一个修改名字的地方，你可以修改名字。在本例中，将此字段保留为默认值

然后跳到下一行,是web服务器的服务器名称或ip。为了你建立的测试计划，所有的HTTP请求将被发送到相同的Web服务器，__jmeter.apache.org__。将这个域名输入到字段中。这是唯一一个我们将指定默认值的字段，所以剩下的字段保留它们的默认值。

 >HTTP请求默认元素不告诉JMeter发送HTTP请求。它只定义了使用HTTP请求的元素的默认值

![](http://img.testclass.net/04_jmeter_http_requestd_defaults2.png)

查看图4.4 HTTP请求默认值


### 4.3 加入Cookie支持
---
几乎所有的Web测试都应该使用cookie支持，除非你的应用程序不支持使用cookie，要添加cookie支持，只需在测试计划中为每个[线程组](http://jmeter.apache.org/usermanual/test_plan.html#thread_group)添加一个[HTTP cookie管理器](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager)即可。这将确保每个线程都有自己的cookie，但可以在所有[HTTP请求](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request)对象之间共享。

添加HTTP cookie管理器，只需选择线程组，并选择 __添加 → 配置元素 → HTTP Cookie管理器__，无论是从编辑菜单，还是从右键弹出菜单都可以。

### 4.4 添加HTTP请求
----
在我们的测试计划里，我们需要做两个HTTP请求。第一个是JMeter的home page（http://jmeter/apache.org/），另一个是changs page（http://jmeter.apache.org/changes.html）。

>当他们出现在树的时候JMeter发送订单请求

为JMeter线程组添加的第一个[HTTP请求](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request)（__添加 → 采样器 → HTTP请求__）。然后，在树中选择HTTP请求元素并编辑以下属性（参见图4.5）：

1.将名称字段更改为“Home Page”。

2.将路径字段设置为“/”。请记住，您不必设置服务器名称字段，因为您已经在HTTP请求默认请求中指定了这个值

![](http://img.testclass.net/04_jmeter_http_request.png)
图4.5 Jmeter home page 的HTTP请求

接下来，添加第二个HTTP请求编辑以下属性（参考图4.6）

1.修改名字为‘changs’.

2.设置路径为’/changes.html’

![](http://img.testclass.net/04_jmeter_http_request2.png)
图4.6 JMeter changs page的HTTP请求

### 4.5增加一个结果监听器
---
你需要为你的测试计划增加的最后一个元素是[监听器](http://jmeter.apache.org/usermanual/component_reference.html#listeners)，此元素负责将HTTP请求的所有结果存储在文件中，并将数据以报表的形式呈现出来。

选择JMeter Users然后新增一个[图标结果](http://jmeter.apache.org/usermanual/component_reference.html#Graph_Results)监听器（__添加 → 监听器 → 图形结果__），接下来，你需要指定输出文件的目录和文件名，你也可以选择浏览按钮并浏览到目录，然后输入文件名。

![](http://img.testclass.net/04_jmeter_graph_results.png)

图4.7 报表结果监听器

### 4.6 登录web站点
----
一般不用不必担心这个，但是一些网站要求你在允许你执行某些动作之前先登录。在Web浏览器中，登录将以表单显示为用户名和密码，以及提交的按钮。按钮生成一个POST请求，将表单项的值作为参数传递。

在JMeter要这样做，添加一个HTTP请求，并设置方法为POST。您需要知道表单和目标页面使用的字段的名称。这些可以通过检查登录页的代码来发现。__如果这是很难做到，你可以使用 [JMeter代理记录器](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Proxy_Server)记录登录序列。__ 设置提交按钮的目标路径。点击Add按钮两次并输入详细的用户名和密码。有时登录表单包含额外的隐藏字段。这些必须要加上

![](http://img.testclass.net/04_jmeter_login.png)

图4.8，简单http登录请求




原始封面

![课程图片](https://images.unsplash.com/photo-1659102264035-0bb2210d92e3?w=300)

