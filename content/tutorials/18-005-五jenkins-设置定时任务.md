---
weight: 5
title: （五）Jenkins 设置定时任务
date: '2017-10-16T12:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1647427060118-4911c9821b82?w=300
tags: []
categories:
- 'CI/CD工具: Jenkins基础教程'
lightgallery: true
toc:
  auto: false
---



每次都手动的构建项目显然不够方便，有时候需要定时地执行自动化测试脚本。例如，每天晚上定时执行 py_tests.py 文件来运行自动化测试项目。


#### 设置定时任务
---

前面已经创建的 __“python test project”__ 项目为例，单击项目左侧的 __“配置”__ 选项，修改项目的配置。

找到 __构建触发器__ ，勾选 __Build periodically__ 选项。

![](http://img.testclass.net/jenkins_setting_time.png)


通过查看设置说明，此处定时任务的格式遵循 cron 的语法（可以与 cron 的语法有轻微的差异）。具体格式，每行包含五个字段，通过 Tab 或空格分隔。

![](http://img.testclass.net/jenkins_crontab.png)


| 字段 | 说明|
|:----|:----|
|MINUTE |	Minutes within the hour (0–59)|
|HOUR	| The hour of the day (0–23)|
|DOM	| The day of the month (1–31)|
|MONTH	| The month (1–12)|
|DOW	| The day of the week (0–7) where 0 and 7 are Sunday.|


若要指定一个字段的多个值，可以使用以下运算符，按先后顺序。

* 指定所有值
* `M-N` 指定范围值
* `M-N/X` 或 `*/X` 在指定范围或整个有效范围内按 X 间隔的步骤
* `A,B,...,Z` 列举了多个值

__例子：__

* 每15分钟运行一次 (可能在 1:07分, 1:22分, 1:37分, 1:52分)

```
H/15 * * * *
```

* every ten minutes in the first half of every hour (three times, perhaps at :04, :14, :24)

```
 H(0-29)/10 * * * *
```

* 每周一至周五，上午9:45到下午3:45，每隔2小时45分钟运行一次

```
 45 9-16/2 * * 1-5
```

* 每两小时一次，每个工作日上午9点到下午5点(也许是上午10:38，下午12:38，下午2:38，下午4:38)

```
H H(9-16)/2 * * 1-5
```

* 除12月外，每月1号和15号每天一次

```
 H H 1,15 1-11 *
```




原始封面

![课程图片](https://images.unsplash.com/photo-1647427060118-4911c9821b82?w=300)

