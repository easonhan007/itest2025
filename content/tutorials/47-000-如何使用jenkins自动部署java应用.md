---
weight: 0
title: 如何使用jenkins自动部署java应用
date: '2018-05-29T13:28:39+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



其实事情的经过是这样的。

最近在很短的时间内上线了一个小程序应用，在测试的过程中我们的开发同学很反感自己去测试环境的机器上更新部署java应用。

为什么反感呢？因为之前的团队有运维，现在单独拉出来做微信小程序，运维的同学没有带过来，部署什么的都要自己手工搞，被惯坏了开发同学哪里咽得下这口气，使用拖字诀，测试环境更新基本看心情，有一些影响测试进度。

那么就搞自动化部署好了，现在问题就来了，谁去搞？

开发说应该运维去搞。

运维说我不在项目组内心有余而力不足。

测试说你们开发就搞一下，一劳永逸。

开发说你们测试能不能自己搞，你行你上啊，你来搞给我们看看。

测试说，那我们用jenkins去建立个简单的任务，这个任务5分钟轮询一次代码库，如果代码有更新就自动build出jar包并部署启动。你们看怎么样？

开发说我们不管细节，你们随便怎么搞，只要能自动部署上去就好了。

测试说那麻烦给一下代码库的权限吧。

开发说自己找配置管理员申请吧。

测试说那配置管理员能不能帮忙安装一下jenkins。

开发说你行你上，自己搞定吧。

大概就是这样，后来测试同学找到一直忙于打杂的我，我就花了点时间帮忙配置了一下。

下面是我的大致的"作案过程"。

首先申请在测试环境的机器上安装了jenkins，也就是说如果测试环境是127.0.0.2，那么就在这台机器上装jenkins，这样这台机器就成了master。

使用下面的命令启动jenkins，因为我们希望jar包启动后常驻后台，而默认情况下jenkins会干掉job里所有的新启动的进程，所以我们必须关掉这个特性。参考[这里](https://wiki.jenkins.io/display/JENKINS/ProcessTreeKiller)

```
java -Dhudson.util.ProcessTree.disable=true -jar jenkins.war
```

因为项目是用maven构建的，所以在安装jenkins的机器上安装maven，保证```mvn```命令可以执行。

在测试机器上安装git，因为我们需要使用git来拉取最新的代码。

在测试机器上生成ssh公钥，加到代码管理平台的部署公钥上，这样做的目的是为了可以免密码直接使用git来拉取代码。

使用git在测试机器上拉取最新代码。确保git没有问题。

在测试机器上使用```mvn install```来build jar包，确保build的过程是没有问题的。

新建jenkins job，代码管理里填入git远程地址，配置5分钟轮询。

在构建步骤里选择执行linux shell脚本，脚本大概是下面这个样子。

```
pwd

/usr/local/maven/bin/mvn install

# 找到jar包的pid，其实用awk更简单，我这里是为了使用sed而使用sed，不要学我
java_pid=`ps -C java -o command -o pid | grep jar_name | sed -r "s/java -jar jar_name.jar\s*//g"`

if [[ "$java_pid"=="" ]]; then
        echo "pid do not exists"
        echo $java_pid
else
        echo "kill"
        echo $java_pid
        kill -9 $java_pid
fi

cd target

nohup java -jar jar_name.jar </dev/null >/dev/null 2>&1 &

```

嗯，差不多了，多调试几遍，fix一些小问题基本就可以了。

后来的事情是这样的。

测试：自动化部署弄好了。

开发: ......

运维: ......

配置管理: .......

测试: ......




原始封面

![课程图片](https://images.unsplash.com/photo-1500964757637-c85e8a162699?w=300)

