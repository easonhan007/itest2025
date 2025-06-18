---
weight: 59
title: （九）JMeter基础知识点：集合点
date: '2017-07-22T12:59:10+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1634650872419-ac179857504a?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
### 集合点
----

简单来理解一下，虽然我们的“性能测试”理解为“多用户并发测试”，但真正的并发是不存在的，为了更真实的实现并发的操作，我们可以在需要压力的地方设置集合点。

关联阅读：
《[JMeter基础知识点：参数化](/jmeter/jmeter-parameterize/)》
《[JMeter基础知识点：检查点](/jmeter/jmeter-assertions/)》

还拿前面用户和密码的功能，每到输入用户名和密码登录的地方，所有的虚拟用户都相互之间等一等，然后一起访问。（连长说一声令下，大家一起冲啊！这样给敌人的压力会很大。）


__第一步__

接着在之前创建的脚本的基础上，右键点击 HTTP请求---->定时器---->Synchronizing Timer。

![](http://img.testclass.net/add_synchronizing_time.png)

__第二步__

设置集合点：

![](http://img.testclass.net/synchronizing_time_setting.png)

__Number of Simulated Users to Group by：__ 每次释放的线程数量。如果设置为0，等同于线程组中设置的线程数量。

__Timeout in milliseconds：__ 如果设置为0，Timer将会等待线程数达到了"Number of Simultaneous Users to Group"中设置的值才释放。如果大于0，那么超过Timeout in milliseconds中设置的最大等待时间(毫秒为单位)后还没达到"Number of Simultaneous Users to Group"中设置的值，Timer将不再等待，释放已到达的线程。

__注意：__

* 如果设置Timeout in milliseconds为0，且线程数量无法达到"Number of Simultaneous Users to Group by"中设置的值，那么Test将无限等待，除非手动终止。

* Synchronizing timer 仅作用于同一个JVM中的线程,所以，如果使用并发测试，确保"Number of Simultaneous Users to Group by"中设置的值不大于它所在线程组包含的用户数。

* Synchronizing Timer是在每个sampler（采样器）之前执行的，而不是之后，不管这个定时器的位置放在sampler之后，还是之前。

* 作用域：当执行一个sampler之前时，和sampler处于相同作用域的定时器都会被执行。

* 如果希望定时器仅应用于其中一个sampler，则把该定时器作为子节点加入，如上图：Synchronizing Timer 所属于 HTTP请求。




原始封面

![课程图片](https://images.unsplash.com/photo-1634650872419-ac179857504a?w=300)

