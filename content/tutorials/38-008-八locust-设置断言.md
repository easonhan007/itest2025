---
weight: 8
title: （八）Locust 设置断言
date: '2017-10-16T08:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1513470270416-d3ff6f16b22f?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



性能测试也需要设置断言么？ 某些情况下是需要，比如你在请求一个页面时，就可以通过状态来判断返回的 HTTP 状态码是不是 200。

#### 设置响应断言
---
这里同样以测试百度首页为例。

```python
from locust import HttpLocust, TaskSet, task

class UserTask(TaskSet):

    @task
    def job(self):
        with self.client.get('/', catch_response = True) as response:
            if response.status_code == 200:
                response.failure('Failed!')
            else:
                response.success()

class User(HttpLocust):
    task_set = UserTask
    min_wait = 1000
    max_wait = 3000
    host = "https://www.baidu.com"

```


catch_response = True ：布尔类型，如果设置为 True, 允许该请求被标记为失败。

通过 client.get() 方法发送请求，将整个请求的给 response， 通过 response.status_code 得请求响应的 HTTP 状态码。如果不为 200 则通过 response.failure('Failed!') 打印失败！

__启动测试，运行情况：__

![](http://img.testclass.net/locust_run_fail.png)

至于，我上面的测试脚本为什么为失败，你自个分析一下吧！原因很简单。




原始封面

![课程图片](https://images.unsplash.com/photo-1513470270416-d3ff6f16b22f?w=300)

