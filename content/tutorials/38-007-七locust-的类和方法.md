---
weight: 7
title: （七）Locust 的类和方法
date: '2017-10-16T09:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1485988412941-77a35537dae4?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



针对你的业务，你如何进行测试测试，需要通过编写性能测试脚本实现。所以，我们要熟悉 Locust 提供了哪些类和方法，它们分别实现什么操作。

#### HttpLocust 类
---
```python
from locust import HttpLocust, TaskSet, task

class UserTask(TaskSet):

    @task
    def tc_index(self):
        self.client.get("/")

class UserOne(HttpLocust):
    task_set = UserTask
    weight = 1
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 5
    host = "https://www.baidu.com"

class UserTwo(HttpLocust):
    weight = 2
    task_set = UserTask
    host = "https://www.baidu.com"

```

每一个模拟的用户可以看做一个 HttpLocust 类的实例，HttpLocust 类有如下属性：

* task_set

指向一个 TaskSet 类，TaskSet 类定义了每个用户的行为。

* min_wait

用户执行任务之间等待时间的下界，单位：毫秒。如果TaskSet类中有覆盖，以TaskSet 中的定义为准。

* max_wait

用户执行任务之间等待时间的上界，单位：毫秒。如果TaskSet类中有覆盖，以TaskSet中的定义为准。

* host

如果是 Web 服务的测试，host 相当于是提供 URL 前缀的默认值，但是如果在命令行中指定了 ```--host``` 选项，则以命令行中指定的为准。如果不是 Web 服务测试，使用默认的 None 就好。

* stop_timeout

设置 Locust 多少秒后超时，如果为 __None__ ,则不会超时。

* weight

一个Locust实例被挑选执行的权重，数值越大，执行频率越高。在一个 locustfile.py 文件中可以同时定义多个 HttpLocust 子类，然后分配他们的执行权重，例如：

然后在终端启动测试：

```
> locust -f load_test.py UserOne UserTwo

```


#### TaskSet 类
---
TaskSet类定义了每个用户的任务集合，测试任务开始后，每个 Locust 用户会从 TaskSet 中随机挑选一个任务执行，然后随机等待 HttpLocust 类中定义的 min_wait和 max_wait 之间的一段时间，执行下一个任务。

```python
from locust import HttpLocust, TaskSet, task


class stay(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print("start test")

    @task(3)
    def readBook(self):
        print('I am reading a book.')

    @task(7)
    def listenMusic(self):
        print('I am listening to music.')

    @task(1)
    def logOut(self):
        self.interrupt()


class UserTask(TaskSet):
    tasks = {stay:2}

    @task(1)
    def leave(self):
        print('I don not like this page.')


class User(HttpLocust):
    task_set = UserTask
    host = "https://www.baidu.com"

```

* on_start()：

定义每个 Locust 用户开始做的第一件事。

* @task

通过@task()装饰的方法为一个事务。方法的参数用于指定该行为的执行权重。参数越大每次被虚拟用户执行的概率越高。如果不设置默认为1。

* interrupt(reschedule=True)

顶层的TaskSet（即被绑定到某个Locust类的task_set的第一层TaskSet）不能调用这个方法。reschedule置为True时，从被嵌套任务出来马上选择新任务执行，如果置为False，从被嵌套任务出来后，随机等待min_wait和max_wait之间的一段时间，再选择新任务执行。

* tasks 属性

tasks = {stay:2}  表示每个用户执行 stay 的频率是2，也就的 UserTask 的两倍。

__然后在终端启动测试：__

```
> locust -f tc_load_test2.py --no-web -c 10 -r 10 -t 10s

[2017-10-31 16:41:45,920] DESKTOP-SMGQBBM/INFO/locust.main: Run time limit set to 10 seconds
[2017-10-31 16:41:45,923] DESKTOP-SMGQBBM/INFO/locust.main: Starting Locust 0.8
[2017-10-31 16:41:45,923] DESKTOP-SMGQBBM/INFO/locust.runners: Hatching and swarming 10 clients at the rate 10 clients/s...
 Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
 Total                                                              0     0(0.00%)                                       0.00

[2017-10-31 16:41:45,924] DESKTOP-SMGQBBM/INFO/stdout: I don not like this page.
[2017-10-31 16:41:45,924] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,023] DESKTOP-SMGQBBM/INFO/stdout: start test
[2017-10-31 16:41:46,023] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,025] DESKTOP-SMGQBBM/INFO/stdout: I am listening to music.
[2017-10-31 16:41:46,025] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,124] DESKTOP-SMGQBBM/INFO/stdout: start test
[2017-10-31 16:41:46,125] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,125] DESKTOP-SMGQBBM/INFO/stdout: I am reading a book.
[2017-10-31 16:41:46,127] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,226] DESKTOP-SMGQBBM/INFO/stdout: start test
[2017-10-31 16:41:46,229] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,230] DESKTOP-SMGQBBM/INFO/stdout: I am reading a book.
[2017-10-31 16:41:46,232] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,325] DESKTOP-SMGQBBM/INFO/stdout: I don not like this page.
[2017-10-31 16:41:46,328] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,424] DESKTOP-SMGQBBM/INFO/stdout: I don not like this page.
[2017-10-31 16:41:46,424] DESKTOP-SMGQBBM/INFO/stdout:
[2017-10-31 16:41:46,525] DESKTOP-SMGQBBM/INFO/stdout: I don not like this page.

...

```
在这个例子中虽然指定的 host ,但我们并没有调用 client() 方法发送http 请求。只是在 TaskSet 类方法中简单做了简单的打印，通过后台的输出，你可以看到每个方法被调用的频率。




原始封面

![课程图片](https://images.unsplash.com/photo-1485988412941-77a35537dae4?w=300)

