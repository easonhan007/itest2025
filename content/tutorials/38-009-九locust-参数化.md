---
weight: 9
title: （九）Locust 参数化
date: '2017-10-16T07:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



使用 LoadRunner 和 JMeter 的同学都知道，性能测试工具设置参数化颇为麻烦，但对于 Python 来说，生成点数据再简单不过了。

#### 参数化系统登录
---

这里以某系统登录为例，简单介绍登录用户名密码的参数化实现

```python
from locust import HttpLocust, TaskSet, task
from random import randint

# Web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    # 随机返回登录用户
    def login_user():
        users = {"user1":123456,"user2":123123,"user3":111222}
        data = randint(1, 3)
        username = "user"+str(data)
        password = users[username]
        return username, password

    @task
    def login(self):
        username, password = login_user()
        self.client.post("/login_action", {"username":username, "password":password})


class User(HttpLocust):
    task_set = UserTask
    min_wait = 1000
    max_wait = 3000
    host = "http://www.xxx.com"

```

创建 login_user() 方法，定义登录字典 users , 通过randint 随机获取字典中的用户数据。

在 login() 登录任务中，调用 login_user() 方法实现 随机用户的登录。

关于参数化方式很多，这里起一个抛砖引玉作用。

----
<font color="red">关于 Locust 工具就介绍到这里，能否把 Locust 在工作中用好，取决于你对性能测试业务的理解，其次是灵活的运行 python 语言。</font>




原始封面

![课程图片](https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=300)

