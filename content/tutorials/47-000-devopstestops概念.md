---
weight: 0
title: DevOps/TestOps概念
date: '2018-01-08T10:20:22+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1523712999610-f77fbcfc3843?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



天下大势分久必合合久必分，早期的软件开发只有软件工程师一人完成，为了提高效率逐渐实行分工模式：开发、测试、运维。不同角色担任不同的任务。分工越来越细之后带来了问题也越来越突出，那就是各角色之间的沟通成本越来越高。而全栈工程师、DevOps/TestOps相关职位和概念的提出，本质就是把不同的工作集中在一个人身上，或者让一个人涉及到更多方面的工作，从而来降低这种沟通成本。



要想了解TestOps，必须要先了解DevOps。



### DevOps 介绍
---

wikipedia解释：DevOps是一种软件工程文化和实践，旨在统一软件开发(Dev)和软件运维(Ops)。DevOps运动的主要特点是在软件构建的所有步骤中极力提倡自动化和监控，从集成、测试、发布到部署和基础设施管理。DevOps的目标是缩短开发周期，增加部署频率，更可靠的发布，与业务目标紧密结合。

![](http://img.testclass.net/tc_Devops.png)

Dev、QA、Ops的交汇处我们认为就是DevOps。实际上，DevOps就是把产品开发过程中各角色交汇处的活给干了，让各部门都专注于干他们自己的活儿。



#### DevOps与持续集成

DevOps是一个完整的面向IT运维的工作流，以IT自动化以及持续集成（CI）、持续部署（CD）为基础，来优化程式开发、测试、系统运维等所有环节。



#### DevOps 技术栈与工具链

只讲理论是非常空洞的，我们必须通过技术和工具将DevOps落地。这里整理了主流的工具，其中包括版本控制&协作开发工具、自动化构建和测试工具、持续集成&交付工具、部署工具、维护工具、监控，警告&分析工具等等，这里补充了一些国内的服务，可以让你更好的执行实施 DevOps 工作流。

* __版本控制&协作开发：__ GitHub、GitLab、BitBucket、SubVersion、Coding、Gitee

* __自动化构建和测试：__ Apache Ant、Maven、Selenium、UnitTest、JUnit、JMeter、Gradle、PHPUnit

* __持续集成&交付：__ Jenkins、Capistrano、BuildBot、Fabric、Tinderbox、Travis CI、flow.ci Continuum、LuntBuild、CruiseControl、Integrity、Gump、Go

* __容器平台：__ Docker、Rocket、Ubuntu（LXC）、第三方厂商如（AWS/阿里云）

* __配置管理：__ Chef、Puppet、CFengine、Bash、Rudder、Powershell、RunDeck、Saltstack、Ansible

* __微服务平台：__ OpenShift、Cloud Foundry、Kubernetes、Mesosphere

* __服务开通：__ Puppet、Docker Swarm、Vagrant、Powershell、OpenStack Heat

* __日志管理：__ Logstash、CollectD、StatsD、ElasticSearch、Logstash

* __监控，警告&分析：__ Nagios、Ganglia、Sensu、zabbix、ICINGA、Graphite、Kibana

除了这种技术和工具外，在项目中制定出符合DevOps的工作流程是关键，但是，这个东西没有固定模板的，不同的项目、不同的团队和公司文化流程和可能有所不同，只要符合DevOps的理念和思想，你们需要走出一条自己的路。



### TestOps 介绍
---

TestOps主要目的是推动整个研发体系与发布体系更多在质量方面。可以这样理解DevOps是从研发推动配合运维和测试，而TestOps是从测试角度推动研发和运维。所以TestOps才是真正把测试落地到整个研发体系的关键岗位。

关于TestOps定义：测试运维，测试角度推动研发、运维、持续测试到持续集成。



新的趋势图：

![](http://img.testclass.net/tc_TestOps.gif)

测试与开发交叉的工作，通过测试驱动开发（TestDev）来进行。

测试与运维交叉的工作，通过TestOps来完成。

开发与运维交叉的工作，通过DevOps来完成。

三个角色交叉的部分工作，由god来做吧！哈哈。



#### TestOps技能

“TestOps”团队的本质是专注于提供所需的基础设施和平台所有级别的测试，从功能测试到集成测试，再到低级单元和API测试。

Dev能力：Java、Python、PHP、Shell

Ops能力：Jenkins、Docker、Maven、Ansible、Git、Linux

Test能力：测试用例、测试方法、缺陷生命周期、单元测试、接口测试、Selenium



#### TestOps未来的价值

团队价值：推动先进的团队协作方式，持续交付生命周期的把控，持续集成高质量要求。

个人价值：DevOps和TestOps技能，自动化测试推动持续交付，主导开发流程的生命周期。

DevOps能推动整个测试和运维团队统一整个研发流程，帮助团队更敏捷的提交产品。他能解决流程问题，但无法发现开发过程中的测试的缺陷。只有更专业TestOps的站在专业的测试角度推动开发和运维一起进行。TestOps和DevOps形成一个完整的持续集成和持续交付体系，才是真正提升整个团队的效率。



### 总结

最后，抛开这些概念，我觉得测试人员提升自己的综合能力才是关键：培养自己的编程能力，更早的介入项目测试（单元、接口），提高自己的（接口/UI）自动化能力，提升测试效率。学习运维技术，能够独立部署和维护测试环境。




原始封面

![课程图片](https://images.unsplash.com/photo-1523712999610-f77fbcfc3843?w=300)

