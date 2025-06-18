---
weight: 3
title: （三）Locust 创建性能测试
date: '2017-10-16T12:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1464029902023-f42eba355bde?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



<font color='red'> Locust 可没有傻瓜式的脚本录制功能，要想用它来做性能测试，必须撸起袖子来写代码。不过。它并不难！</font>


#### 编写简单的性能测试脚本

创建 load_test.py 文件，通过 Python 编写性能测试脚本。

```python
from locust import HttpLocust, TaskSet, task

# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
```
UserBehavior类继承TaskSet类，用于描述用户行为。

baidu_index() 方法表示一个用户为行，访问百度首页。使用@task装饰该方法为一个事务。client.get()用于指请求的路径“/”，因为是百度首页，所以指定为根路径。

WebsiteUser类用于设置性能测试。

* task_set ：指向一个定义的用户行为类。

* min_wait ：执行事务之间用户等待时间的下界（单位：毫秒）。

* max_wait ：执行事务之间用户等待时间的上界（单位：毫秒）。

### 执行性能测试
---

__启动性能测试__

```
> locust -f .\load_test.py --host=https://www.baidu.com

[2017-10-16 16:44:40,839] DESKTOP-SMGQBBM/INFO/locust.main: Starting web monitor at *:8089
[2017-10-16 16:44:40,842] DESKTOP-SMGQBBM/INFO/locust.main: Starting Locust 0.8

```

* -f 指定性能测试脚本文件。
* --host 指定被测试应用的URL的地址，注意访问百度使用的HTTPS协议。

通过浏览器访问：http://localhost:8089（Locust启动网络监控器，默认为端口号为: 8089）

__设置测试__

![](http://img.testclass.net/locust_run_setings.png)

Number of users to simulate 设置模拟用户数。

Hatch rate（users spawned/second） 每秒产生（启动）的虚拟用户数。

点击 “Start swarming” 按钮，开始运行性能测试。

__运行测试__

![](http://img.testclass.net/locust_runing_test.png)

__性能测试参数__

* Type： 请求的类型，例如GET/POST。

* Name：请求的路径。这里为百度首页，即：https://www.baidu.com/

* request：当前请求的数量。

* fails：当前请求失败的数量。

* Median：中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值。

* Average：平均值，单位毫秒，所有请求的平均响应时间。

* Min：请求的最小服务器响应时间，单位毫秒。

* Max：请求的最大服务器响应时间，单位毫秒。

* Content Size：单个请求的大小，单位字节。

* reqs/sec：是每秒钟请求的个数。




原始封面

![课程图片](https://images.unsplash.com/photo-1464029902023-f42eba355bde?w=300)

