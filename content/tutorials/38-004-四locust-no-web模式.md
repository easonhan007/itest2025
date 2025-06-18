---
weight: 4
title: （四）Locust no-web模式
date: '2017-10-16T12:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507208773393-40d9fc670acf?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



熟悉 Apache ab 工具的同学都知道，它是没有界面的，通过命令行执行。 Locust 同样也提供的命令行运行，好处就是更节省客户端资源。

#### 命令行运行 Locust 测试
----

以上一节的 baidu 首页测试（load_test.py）为例 通过 __no-web__ 模式运行测试。

```
> locust -f load_test.py --host=https://www.baidu.com --no-web -c 10 -r 2 -t 1m

[2017-10-30 22:17:30,292] DESKTOP-SMGQBBM/INFO/locust.main: Run time limit set to 60 seconds
[2017-10-30 22:17:30,302] DESKTOP-SMGQBBM/INFO/locust.main: Starting Locust 0.8
[2017-10-30 22:17:30,302] DESKTOP-SMGQBBM/INFO/locust.runners: Hatching and swarming 10 clients at the rate 2 clients/s...
 Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s

....


 [2017-10-30 22:18:30,301] DESKTOP-SMGQBBM/INFO/locust.main: Time limit reached. Stopping Locust.
 [2017-10-30 22:18:30,302] DESKTOP-SMGQBBM/INFO/locust.main: Shutting down (exit code 0), bye.
  Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s
 --------------------------------------------------------------------------------------------------------------------------------------------
  GET /                                                            117     0(0.00%)      31      17      96  |      28    2.10
 --------------------------------------------------------------------------------------------------------------------------------------------
  Total                                                            117     0(0.00%)                                       2.10

 Percentage of the requests completed within given times
  Name                                                           # reqs    50%    66%    75%    80%    90%    95%    98%    99%   100%
 --------------------------------------------------------------------------------------------------------------------------------------------
  GET /                                                             117     28     30     36     37     49     62     69     72     96
 --------------------------------------------------------------------------------------------------------------------------------------------
  Total                                                             117     28     30     36     37     49     62     69     72     96

```

__启动参数：__

--no-web  表示不使用Web界面运行测试。

-c        设置虚拟用户数。

-r        设置每秒启动虚拟用户数。

-t        设置设置运行时间。




原始封面

![课程图片](https://images.unsplash.com/photo-1507208773393-40d9fc670acf?w=300)

