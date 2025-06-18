---
weight: 0
title: 最中二的性能测试工具--vegeta
date: '2025-06-17T17:29:15+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1534030665069-90e016e995e5?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



在github上翻到一个项目，名字叫vegeta，看到这个单词，你的第一反应是什么？

说来惭愧，我的第一反应是这个单词很奇怪，并不认识。

直到我往下翻，看到了这样一幅场景。

![](https://camo.githubusercontent.com/faf9be097f4731212debdd24210c750b2dc276d0a17df19c6a8ac026427c09e9/687474703a2f2f666330392e64657669616e746172742e6e65742f667334392f692f323030392f3139382f632f632f73736a325f7665676574615f62795f7472756e6b7332342e6a7067)

这......这不是儿时的回忆，七龙珠里的天字第一号配角，贝吉塔么？

贝吉塔，日本漫画及改编动画《龙珠》系列中的主要角色。是战斗民族赛亚人的王子，拥有极高的自尊心。过去贝吉塔行星被弗利萨毁灭后（不知情，一直以为是被陨石撞击而毁灭。）在弗利萨军团那儿做事。初登场时是个侵略地球的反派角色，后被孙悟空（赛亚人卡卡罗特）等人打败。弗利萨一战结束后听说悟空成为超级赛亚人，于是决定以超越悟空为目标，一直留在地球上努力修行。
多次和悟空保护地球。在人造人篇中学会了超级赛亚人变身，起初只是想着超越悟空才呆在地球，后来有了家人后慢慢的爱上了这颗星球，在与布欧一战中为了保护地球决定与布欧同归于尽。后复活为悟空制造元气弹争取时间，击败布欧后仍为了超越悟空而努力修行。

贝吉塔（Vegeta）与其弟弟塔布尔（Table）的名字合二为一（英文名）就是Vegetable（蔬菜）

上面的描述来自百度百科，所以贝吉塔在漫画中是一个出道即巅峰，登场超强，然后一直被悟空超越，并且打不过就加入你的角色。

可能对于很多读者来说，七龙珠这个上古漫画其实是熟悉而又陌生的，名字都听过，但至于漫画主要讲了什么，大家可能并不清楚。不过对于我这种老古董来说，七龙珠就意味着童年闲暇时愉快的阅读时光以及无数次的练习冲击波以求有朝一日能拯救地球的中二幻想。

怀着强烈的好奇心，我真心希望看看这个中二又复古的项目究竟是做什么的。

经过几分钟的探索，我发现vegeta其实是一个用go实现的性能测试工具，江湖上各种性能工具可谓是灿若星河，那么vegeta凭什么可以获得16.3k的star呢？

可能是因为名字，毕竟github上的中老年宅男还是非常多的。

不过玩笑归玩笑，作为性能测试工具，vegeta有个很不错的特性，那就是可以默认以一定的qps对被测服务进行压测。

### 固定qps的使用场景

比如我们经常需要对某个微服务进行单实例的容量评估，我们希望某个服务A他能承受的最大QPS是1000，这时候我们就需要有一个工具能持续产生1000qps的负载进行一段时间的压测，这段时间里，我们可能通过监控系统的核心指标来判断系统的健康度和稳定性，vegeta看上去是可以满足这个场景下的压测需求的。

### 安装

vegeta只支持linux以及mac系统，不支持windows。

vegeta只是一个可执行文件，所以直接下载就好了，下载地址是：https://github.com/tsenart/vegeta/releases

### 简单的使用

通过命令行使用，命令如下

```
echo "GET http://localhost:8080/api/articles/" | ./vegeta attack -duration=10s| tee results.bin | ./vegeta report
```

执行结果

```
Requests      [total, rate, throughput]         500, 50.10, 50.10
Duration      [total, attack, wait]             9.981s, 9.98s, 610.816µs
Latencies     [min, mean, 50, 90, 95, 99, max]  310.733µs, 549.662µs, 522.345µs, 706.005µs, 814.544µs, 912.57µs, 3.088ms
Bytes In      [total, mean]                     16500, 33.00
Bytes Out     [total, mean]                     0, 0.00
Success       [ratio]                           100.00%
Status Codes  [code:count]                      200:500  
```

看到这个结果我不禁陷入了深思，因为qps实在是太低了。

我测试的这个服务不出意外应该是有8000左右的qps的，但用vegeta只测出来50。

这是为什么？

### 默认固定qps

**原来vegeta默认的话是用50的qps对被测服务进行压测的。**

我们可以手动将rate设置成0，表示解开封印，变成超级赛亚人，用无限qps进行压测。

```
echo "GET http://localhost:8080/api/articles/" | ./vegeta attack -duration=10s -connections 100 -rate=0 -max-workers=30| tee results.bin | ./vegeta report
Requests      [total, rate, throughput]         28596, 2859.62, 2858.73
Duration      [total, attack, wait]             10.003s, 10s, 3.105ms
Latencies     [min, mean, 50, 90, 95, 99, max]  729.566µs, 8.073ms, 7.758ms, 10.441ms, 11.453ms, 14.532ms, 23.207ms
Bytes In      [total, mean]                     943668, 33.00
Bytes Out     [total, mean]                     0, 0.00
Success       [ratio]                           100.00%
Status Codes  [code:count]                      200:28596  

```

变身之后效果还是有一些的，qps变成2800。

我后来又尝试了一些参数，比如提高connections和worker，延长被测时间等，发现2800已经是天花板了。也就是说vegeta本身的压测性能是一般的，没办法将被测应用跑满。

### 强大的report功能

既然vegata的本身的攻击力有限，那么为什么还有那么多人给他star呢？

抱着研究的心态，我由稍微深入了解了一下。

原来vegeta有不错的报告生成能力。

vegeta可以生成纯文本/json/histogram/hdrplot/plot图表，基本可以满足日常的压测需求和二次开发需求。

其中histogram是长这样的

```
cat results.bin | vegeta report -type='hist[0,2ms,4ms,6ms]'
Bucket         #     %       Histogram
[0,     2ms]   6007  32.65%  ########################
[2ms,   4ms]   5505  29.92%  ######################
[4ms,   6ms]   2117  11.51%  ########
[6ms,   +Inf]  4771  25.93%  ###################
```

可以看到相应时间的区间分布。

### 分布式压测功能

vegeta可以通过pdsh来实现分布式压测功能，比如我们可以同时用3台机器运行vegata，对目标站点进行压测。

```
$ PDSH_RCMD_TYPE=ssh pdsh -b -w '10.0.1.1,10.0.2.1,10.0.3.1' \
    'echo "GET http://target/" | vegeta attack -rate=20000 -duration=60s > result.bin'
```

最后通过脚本把3台机器上的测试结果收集起来，通过vegata的report命令进行合并就好了。

```
$ for machine in 10.0.1.1 10.0.2.1 10.0.3.1; do
    scp $machine:~/result.bin $machine.bin &
  done

vegeta report *.bin
```

### 总结

* vegata是一个不错的压测选择，如果你需要使用不高的固定qps持续对目标服务进行压测的话；
* vegata的测试结果展示的选择性还是相对较多的；
* vegata的本身的命名风格比较中二，比如压测在vegata里称作attact，攻击，不过想想也挺有意思的，谁规定了测试工具必须中规中矩严肃认真呢？





原始封面

![课程图片](https://images.unsplash.com/photo-1534030665069-90e016e995e5?w=300)

