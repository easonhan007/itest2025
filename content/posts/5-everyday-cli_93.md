---
weight: 1
title: "五款最值得日常使用的命令行应用"
date: 2024-03-08T09:03:54+08:00
lastmod: 2024-03-08T09:03:54+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "这里给大家推荐5款常见好用的命令行应用"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1524508762098-fd966ffb6ef9?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

、

命令行应用很多时候可以提升我们的工作效率，这里给大家推荐 4 款常见好用的命令行应用，希望对大家有所帮助。

### vim

大名鼎鼎的命令行编辑器，有时间的同学都可以尝试一下。

说起来比较惭愧，当初学习 vim 的原因有两个。第一个是十多年前的室友表示 vim 这种工具的学习成本底，因为学会以后键位几十年不变，学一次用终生，性价比极高，尽管入门的时候学习曲线非常的陡峭，甚至有点反直觉。第二个理由是学习 vim 可以让我比较方便的在线上环境改代码，是的，你没看错，很多年前我们用 php 的时候确实做过线上调试和改代码的极限操作。

如今随着运维的规范以及自动化发布的普及，线上改代码这种高危操作应该是被严令禁止了。不过使用 vim 仍然可以让你在任意机器 ssh 进远程服务器进行代码的编写和执行。配合上自定义的配置和第三方的插件，vim 也是日常代码编辑的一个不错选择。

另外很多编辑器都支持 vim 键位，比如 atom，vscode，这会让你在写代码的时候更有如鱼得水的感觉。

### tmux

tmux 之前是运维同学的钟意之物，因为该工具可以

- 分屏，将 1 个 terminal 分成多个部分
- 独立运行 session，每个部分都是独立的会话，互不干涉
- 快照，任意时刻退出 terminal，tmux 都会保存当前会话，下一次可以无缝恢复

> 命令行的典型使用方式是，打开一个终端窗口（terminal window，以下简称"窗口"），在里面输入命令。用户与计算机的这种临时的交互，称为一次"会话"（session） 。
> 会话的一个重要特点是，窗口与其中启动的进程是连在一起的。打开窗口，会话开始；关闭窗口，会话结束，会话内部的进程也会随之终止，不管有没有运行完。
> 一个典型的例子就是，SSH 登录远程计算机，打开一个远程窗口执行命令。这时，网络突然断线，再次登录的时候，是找不回上一次执行的命令的。因为上一次 SSH 会话已经终止了，里面的进程也随之消失了。
> 为了解决这个问题，会话与窗口可以"解绑"：窗口关闭时，会话并不终止，而是继续运行，等到以后需要的时候，再让会话"绑定"其他窗口。

![%E4%BA%94%E6%AC%BE%E6%9C%80%E5%80%BC%E5%BE%97%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%BA%94%E7%94%A8%20ec7a76e3ce004c3fbae198fe1c07aa7c/Untitled.png](%E4%BA%94%E6%AC%BE%E6%9C%80%E5%80%BC%E5%BE%97%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%BA%94%E7%94%A8%20ec7a76e3ce004c3fbae198fe1c07aa7c/Untitled.png)

> Tmux 就是会话与窗口的"解绑"工具，将它们彻底分离。
> （1）它允许在单个窗口中，同时访问多个会话。这对于同时运行多个命令行程序很有用。
> （2） 它可以让新窗口"接入"已经存在的会话。
> （3）它允许每个会话有多个连接窗口，因此可以多人实时共享会话。
> （4）它还支持窗口任意的垂直和水平拆分。

tmux 对于我来说的典型用法就是

- 把一个窗口分成几块，小的窗口运行 mysql，redis 之类的服务
- 用一个窗口运行主服务，比如 python 的 flask 开发服务器
- 用最大的窗口来运行 vim 编辑器，做代码的编辑

这样任意时刻我退出 ssh，上面的这些服务都会一直运行，下次我再 ssh 上去的话就可以无缝的继续工作了。

### howdoi

大家可能有这样的经验，在写代码或者工作的时候经常会需要去各种搜索引擎查找一些信息，比如搜索 python 如何便利目录，go 如何写文件并保存之类的。

如果你的工作环境是标准的桌面环境，也就是有 ui 的，有浏览器的，这一切似乎不是什么问题。不过如果你只是 ssh 到服务器上做一些操作，如何在没有 ui 的环境下进行面向百度或者是 google 的编程和工作呢？

howdoi 这个工具就解决了这个问题。敲命令 howdoi，然后再是你需要搜索的内容，howdoi 就可以很快的给你具体的信息。比如

```jsx
$ howdoi format date bash
> DATE=`date +%Y-%m-%d`
```

再比如

```jsx
$ howdoi print stack trace python
> import traceback
>
> try:
>     1/0
> except:
>     print '>>> traceback <<<'
>     traceback.print_exc()
>     print '>>> end of traceback <<<'
> traceback.print_exc()

$ howdoi convert mp4 to animated gif
> video=/path/to/video.avi
> outdir=/path/to/output.gif
> mplayer "$video" \
>         -ao null \
>         -ss "00:01:00" \  # starting point
>         -endpos 10 \ # duration in second
>         -vo gif89a:fps=13:output=$outdir \
>         -vf scale=240:180

$ howdoi create tar archive
> tar -cf backup.tar --exclude "www/subf3" www
```

howdoi 的安装方式很简单

```jsx
pip install howdoi
```

强烈推荐大家试一试，不需要频繁的从 terminal 切换到浏览器所带来的工作效率提升是非常明显的。

### htop

top 相信大家都很熟悉了，htop 其实是 top 的改进版本，是一款更加的简单实用的系统监控工具。

htop 可以更加方便的查看 cpu 和内存的使用率，然后根据各种指标，比如 cpu 使用率，内存使用率等对进程进行实时排序，最关键的一点是支持鼠标点击排序，指哪打哪的舒适度比 top 还是好不少的。

### ncdu

我的远程服务是最低配版本，这就意味着只有 1 核 cpu，1g 内存，以及 20g 的硬盘，而使用了一段时间以后这 20g 硬盘就会被占满，而且很难分析出哪些文件占用了大部分的空间。

这时候就需要使用 ncdu 了，这个工具可以很方便扫描目录，并且按照文件大小进行排序，大目录一目了然，一些缓存路径就可以非常快速的找出来并删除掉了。
