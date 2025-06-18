---
weight: 5
title: （五）Locust 参数说明
date: '2017-10-16T11:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1507831228884-93d43e81a99d?w=300
tags: []
categories:
- Locust实用教程
lightgallery: true
toc:
  auto: false
---



最时候该讲一下 locust 工具的参数了，虽然前面几节我们已经使用了不少参数，例如 __“-f”__ 、__“--host”__ 等。

#### Locust 参数
---
打开命令提示符（或Linux终端），输入 ```locust --help``` 。

```
> locust --help
Usage: locust [options] [LocustClass [LocustClass2 ... ]]

Options:
  -h, --help            show this help message and exit
  -H HOST, --host=HOST  Host to load test in the following format:
                        http://10.21.32.33
  --web-host=WEB_HOST   Host to bind the web interface to. Defaults to '' (all
                        interfaces)
  -P PORT, --port=PORT, --web-port=PORT
                        Port on which to run web host
  -f LOCUSTFILE, --locustfile=LOCUSTFILE
                        Python module file to import, e.g. '../other.py'.
                        Default: locustfile
  --csv=CSVFILEBASE, --csv-base-name=CSVFILEBASE
                        Store current request stats to files in CSV format.
  --master              Set locust to run in distributed mode with this
                        process as master
  --slave               Set locust to run in distributed mode with this
                        process as slave
  --master-host=MASTER_HOST
                        Host or IP address of locust master for distributed
                        load testing. Only used when running with --slave.
                        Defaults to 127.0.0.1.
  --master-port=MASTER_PORT
                        The port to connect to that is used by the locust
                        master for distributed load testing. Only used when
                        running with --slave. Defaults to 5557. Note that
                        slaves will also connect to the master node on this
                        port + 1.
  --master-bind-host=MASTER_BIND_HOST
                        Interfaces (hostname, ip) that locust master should
                        bind to. Only used when running with --master.
                        Defaults to * (all available interfaces).
  --master-bind-port=MASTER_BIND_PORT
                        Port that locust master should bind to. Only used when
                        running with --master. Defaults to 5557. Note that
                        Locust will also use this port + 1, so by default the
                        master node will bind to 5557 and 5558.
  --expect-slaves=EXPECT_SLAVES
                        How many slaves master should expect to connect before
                        starting the test (only when --no-web used).
  --no-web              Disable the web interface, and instead start running
                        the test immediately. Requires -c and -r to be
                        specified.
  -c NUM_CLIENTS, --clients=NUM_CLIENTS
                        Number of concurrent Locust users. Only used together
                        with --no-web
  -r HATCH_RATE, --hatch-rate=HATCH_RATE
                        The rate per second in which clients are spawned. Only
                        used together with --no-web
  -t RUN_TIME, --run-time=RUN_TIME
                        Stop after the specified amount of time, e.g. (300s,
                        20m, 3h, 1h30m, etc.). Only used together with --no-
                        web
  -L LOGLEVEL, --loglevel=LOGLEVEL
                        Choose between DEBUG/INFO/WARNING/ERROR/CRITICAL.
                        Default is INFO.
  --logfile=LOGFILE     Path to log file. If not set, log will go to
                        stdout/stderr
  --print-stats         Print stats in the console
  --only-summary        Only print the summary stats
  --no-reset-stats      Do not reset statistics once hatching has been
                        completed
  -l, --list            Show list of possible locust classes and exit
  --show-task-ratio     print table of the locust classes' task execution
                        ratio
  --show-task-ratio-json
                        print json data of the locust classes' task execution
                        ratio
  -V, --version         show program's version number and exit

```
__参数说明：__

| 参数           |    说明    |
|:-------------- | :---------- |
|-h, --help       |     查看帮助
|-H HOST, --host=HOST |  指定被测试的主机，采用以格式：http://10.21.32.33 |
|--web-host=WEB_HOST  |  指定运行 Locust Web 页面的主机，默认为空 ''。|
|-P PORT, --port=PORT, --web-port=PORT | 指定 --web-host 的端口，默认是8089
|-f LOCUSTFILE, --locustfile=LOCUSTFILE |  指定运行 Locust 性能测试文件，默认为: locustfile.py |
|--csv=CSVFILEBASE, --csv-base-name=CSVFILEBASE | 以CSV格式存储当前请求测试数据。|
|--master |            Locust 分布式模式使用，当前节点为 master 节点。 |
|--slave  |            Locust 分布式模式使用，当前节点为 slave 节点。  |
|--master-host=MASTER_HOST  |  分布式模式运行，设置 master 节点的主机或 IP 地址，只在与 --slave 节点一起运行时使用，默认为：127.0.0.1. |
|--master-port=MASTER_PORT  | 分布式模式运行， 设置 master 节点的端口号，只在与 --slave 节点一起运行时使用，默认为：5557。注意，slave 节点也将连接到这个端口+1 上的 master 节点。|
|--master-bind-host=MASTER_BIND_HOST | Interfaces (hostname, ip) that locust master should bind to. Only used when running with --master. Defaults to * (all available interfaces). |
|--master-bind-port=MASTER_BIND_PORT | Port that locust master should bind to. Only used when running with --master. Defaults to 5557. Note that Locust will also use this port + 1, so by default the master node will bind to 5557 and 5558. |
|--expect-slaves=EXPECT_SLAVES |  How many slaves master should expect to connect before starting the test (only when --no-web used). |
|--no-web   |   no-web 模式运行测试，需要 -c 和 -r 配合使用. |
|-c NUM_CLIENTS, --clients=NUM_CLIENTS | 指定并发用户数，作用于 __--no-web__ 模式。|
|-r HATCH_RATE, --hatch-rate=HATCH_RATE | 指定每秒启动的用户数，作用于  __--no-web__ 模式。|
|-t RUN_TIME, --run-time=RUN_TIME | 设置运行时间, 例如： (300s, 20m, 3h, 1h30m). 作用于  __--no-web__ 模式。|
|-L LOGLEVEL, --loglevel=LOGLEVEL | 选择 log 级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）. 默认是 INFO. |
|--logfile=LOGFILE  |   日志文件路径。如果没有设置，日志将去 stdout/stderr |
|--print-stats   |   在控制台中打印数据  |
|--only-summary  |   只打印摘要统计  |
|--no-reset-stats |   Do not reset statistics once hatching has been completed。|
|-l, --list       |   显示测试类, 配置 -f 参数使用 |
|--show-task-ratio |   打印 locust 测试类的任务执行比例，配合 -f 参数使用. |
|--show-task-ratio-json |  以 json 格式打印 locust 测试类的任务执行比例，配合 -f 参数使用. |
|-V, --version   |      查看当前 Locust 工具的版本. |


__个别参数，我没用过，也太清楚其含义，暂时就不翻译了。__




原始封面

![课程图片](https://images.unsplash.com/photo-1507831228884-93d43e81a99d?w=300)

