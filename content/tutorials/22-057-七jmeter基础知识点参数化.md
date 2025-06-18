---
weight: 57
title: （七）JMeter基础知识点：参数化
date: '2017-07-22T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1628198545577-adc03c610e3f?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
### 参数化
----
简单的来理解一下，我们录制了一个脚本，这个脚本中有登录操作，需要输入用户名和密码，假如系统不允许相同的用户名和密码同时登录，或者想更好的模拟多个用户来登录系统。

这个时候就需要对用户名和密码进行参数化，使每个虚拟用户都使用不同的用户名和密码进行访问。

__前提需求：__

我们有一个嘉宾管理系统，该系统需要登录。

![](http://img.testclass.net/guest_systme_login.png)

在Jmeter中添加一个登录HTTP请求，设置登录的用户名和密码。如下：

![](http://img.testclass.net/login_http_request.png)

配置参数：

```
* 协议：http
* IP（网址）：127.0.0.1
* 端口号：8000
* 请求方法：POST
* 请求路径：/login_action/
* 自动重定向
* 同请求一起发送参数: username=admin, password=admin123456
```
<br>
####  设置参数化

__第一步：__

我们需要“参数化”的数据，这里我用CSV格式的文件创建了五个用户名/密码，保存为.csv格式的文件。

![](http://img.testclass.net/login_user_csv.png)

将文件放在：__D:\login_user.csv__ 。关于如何得到成百上千的用户名和密码，可以使用SQL语句在数据库中创建，并将数据导出保存，这里就不深究。


__第二步：__

好，我们要编写函数来调用这个login_user.csv文件，点击菜单栏“选项”---->“函数助手对话框”，如下图。

![](http://img.testclass.net/function_helper.png)

<font color=#FF6347 >注：.csv文件第一列从0开始取得。</font>

__第三步：__

把我们写好的函数复制到“登录”页面用户名和密码的位置。

![](http://img.testclass.net/login_parameterize.png)

```python
username : ${__CSVRead(d:/login_user.csv,0)}  #取第一列的数据
password : ${__CSVRead(d:/login_user.csv,1)}  #取第二列的数据

```
好了，现在我们的参数化设置完成，在执行脚本的时候，会调用我们D盘下面的login_user.csv文件，第一列是用户，第二列是密码。


<br>
####  最后

在“线程组”中将线程数设置为5，刚好对应创建的5个用户，查看结果树：

![](http://img.testclass.net/look_result_tree.png)

5个请求所使用的用户名/密码均从csv文件中读取。




原始封面

![课程图片](https://images.unsplash.com/photo-1628198545577-adc03c610e3f?w=300)

