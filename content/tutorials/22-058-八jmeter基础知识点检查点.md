---
weight: 58
title: （八）JMeter基础知识点：检查点
date: '2017-07-22T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1510227320292-0811fae44991?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
### 检查点
----
检查点不是太专的叫法，不管是在自动化测试还是性能测试工具中，应该叫：__断言__

简单的来理解一下，在《[JMeter基础知识点：参数化](/jmeter/jmeter-parameterize/)》中，我们对用户名和密码进行了参数化，那么怎样来判断JMeter参数化的用户有没真正的登录成功呢？或者有没有返回登录成功的页面。这就需要用到 __断言__ 了。

__前提需求：__

我们有一个嘉宾管理系统，该系统登录成功的页面。

![](http://img.testclass.net/guest_systme_login_success.png)

<br>
#### 添加断言
----

__第一步__

右键点击“HTTP请求”---->添加---->断言---->响应断言。

![](http://img.testclass.net/add_assertion.png)


__第二步__

打开响应断言，进行设置。

![](http://img.testclass.net/assert_login_info.png)

__要测试的响应字段：__ 响应文本、Document(text)、URL样本、响应信息、Response Headers、Lgnore Staus
等选项。虽然接口返回的是HTML页面，但对于JMeter来说返回数据为文本，所以，这里可以勾选“响应文本”。

__模式匹配规则：__ 包括、 匹配、 Equals、 Substring。这里只需要验证返回数据中是否包含主要的关键字，所
以， 这里勾选“包括” 。

__要测试的模式：__ 其实就是断言的数据。 点击“添加” 按钮， 输入要断言的数据。


<font color=#FF6347 > 我们怎么 __证明__ 登录是成功的？肯定是从登录成功的页面上抓取信息来判断了。那么，__Guest Manage System__ 和 __退出__ 看来不错，因为只有登录成功的页面上才有。</font>

接下来，你可以重新运行测试用例，查看结果树。然后，再故意把断言的信息弄错，再来运行测试，并查看结果树里的请求是否失败了。




原始封面

![课程图片](https://images.unsplash.com/photo-1510227320292-0811fae44991?w=300)

