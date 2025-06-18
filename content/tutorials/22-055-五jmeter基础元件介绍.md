---
weight: 55
title: （五）JMeter基础元件介绍
date: '2017-07-23T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1697477357925-60fca4698c76?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
### 测试计划
----

#### Test Plan (测试计划)

用来描述一个性能测试，包含与本次性能测试所有相关的功能。也就说JMeter创建性能测试的所有内容是于基于一个计划的。

下面看看一个计划下面都有哪些功能模块（右键单击“测试计划”弹出菜单）。

![](http://img.testclass.net/test_plan.png)


#### Threads （Users）线程 用户

![](http://img.testclass.net/threads_user.png)

虽然有三个添加线程组的选项，名字不一样， 创建之后，其界面是完全一样的。在Jmeter之前的版本只有一个线程组的名字。现在多一个 __setUp theread Group__ 与 __tearDown Thread Group__

* setup thread group  

一种特殊类型的ThreadGroup的，可用于执行预测试操作。这些线程的行为完全像一个正常的线程组元件。不同的是，这些类型的线程执行 __测试前__ 进行定期线程组的执行。

* teardown thread group  

一种特殊类型的ThreadGroup的，可用于执行测试后动作。这些线程的行为完全像一个正常的线程组元件。不同的是，这些类型的线程执行 __测试结束后__ 进行定期的线程组。

可能你还是不太理解他们与普通的线程组有什么不同。 如果您用过Junit单元测试框架，想必你不会对setUp(before) ，tearDown(after) 这两个关键字不陌生。 即使没用过，也没关系。 熟悉loadrunner的应该知道，loadrunner的脚本除了action里是真正的脚本核心内容，还有初始化“环境”的初始化脚本和测试完毕后对应的清除信息的脚本块。 那么这里 setup thread group 和 teardown thread group 就是分别指这两部分。 其实从本质上来看，他们并没有什么不同。

* thread group(线程组)

这个就是我们通常添加运行的线程。通俗的讲一个线程组，可以看做一个虚拟用户组，线程组中的每个线程都可以理解为一个虚拟用户。线程组中包含的线程数量在测试执行过程中是不会发生改变的。


#### 测试片段（Test Fragment）

![](http://img.testclass.net/test_fragment.png)

测试片段是在JMeter2.5版本之后新加的一个选项。

测试片段元素是控制器上的一个种特殊的线程组，它在测试树上与线程组处于一个层级。它与线程组有所不同，因为它不被执行，除非它是一个模块控制器或者是被控制器所引用时才会被执行。

#### 配置元件（Config Element）

![](http://img.testclass.net/config_element.png)

配置元件（config element）用于提供对静态数据配置的支持。CSV Data Set config 可以将本地数据文件形成数据池（Data Pool），而对应于HTTP Request Sampler和 TCP Request Sampler等类型的配制元件则可以修改Sampler的默认数据。（例如，HTTP Cookie Manager 可以用于对 HTTP Request Sampler 的 cookie 进行管理）

#### 定时器（Timer）

![](http://img.testclass.net/timer.png)

定时器（Timer）用于操作之间设置等待时间，等待时间是性能测试中常用的控制客户端QPS的手段。类似于LoadRunner里面的“思考时间”。JMeter 定义了Bean Shell Timer、Constant Throughput Timer、固定定时器等不同类型的Timer。

#### 前置处理器（Pre Processors）

![](http://img.testclass.net/per_processors.png)

用于在实际的请求发出之前对即将发出的请求进行特殊处理。例如，HTTP URL重写修饰符则可以实现URL重写，当RUL中有sessionID 一类的session信息时，可以通过该处理器填充发出请求的实际的SessionID 。

#### 后置处理器（Post Processors）

![](http://img.testclass.net/post_processors.png)

用于对 __Sampler__ 发出请求后得到的服务器响应进行处理。一般用来提取响应中的特定数据（类似LoadRunner测试工具中的关联概念）。例如，XPath Extractor 则可以用于提取响应数据中通过给定XPath值获得的数据。

#### 断言（Assertions）

![](http://img.testclass.net/assertions.png)

断言用于检查测试中得到的相应数据等是否符合预期，断言一般用来设置检查点，用以保证性能测试过程中的数据交互是否与预期一致。

#### 监听器（Listener）

![](http://img.testclass.net/listener.png)

这个监听器可不是用来监听系统资源的元件。它是用来对测试结果数据进行处理和可视化展示的一系列元件。 图形结果、察看结果树、聚合报告等都是我们经常用到的元件。


<br>
## 控制器
----
JMeter有两种类型的控制器：取样器（Sampler）和逻辑控制器（Logic Controller），用这些元件来驱动处理一个测试。

#### 取样器（Sampler）

![](http://img.testclass.net/sampler.png)

取样器（Sample）是性能测试中向服务器发送请求，记录响应信息，记录响应时间的最小单元，JMeter原生支持多种不同的sampler ，如 __HTTP Request Sampler 、 FTP  Request Sample 、TCP  Request Sample 、JDBC Request Sampler__ 等，每一种不同类型的 sampler 可以根据设置的参数向服务器发出不同类型的请求。（在JMeter的所有sampler中，Java Request Sampler 和 Beanshell Request Sampler 是两种特殊的可定制的 Sampler ，后面会深入讨论。）


#### 逻辑控制器（Logic Controller）

![](http://img.testclass.net/logic_controller.png)

逻辑控制器，包括两类无件，一类是用于控制test plan 中 sampler 节点发送请求的逻辑顺序的控制器，常用的有 如果（If）控制器 、switch Controller 、Runtime Controller、循环控制器等。另一类是用来组织可控制 sampler 来节点的，如 事务控制器、吞吐量控制器。

<br>
到此，我们已经简单介绍了JMeter中的所有元件，后序的性能测试工作也就是使用这些元件来创建测试任务。所以，你现还不理解这些元件具体使用，没关系！先有个印象。




原始封面

![课程图片](https://images.unsplash.com/photo-1697477357925-60fca4698c76?w=300)

