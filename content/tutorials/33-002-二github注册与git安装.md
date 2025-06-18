---
weight: 2
title: （二）GitHub注册与Git安装
date: '2017-08-31T03:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1581093202218-980a6769202b?w=300
tags: []
categories:
- git简明教程
lightgallery: true
toc:
  auto: false
---



#### 注册GitHub
----
GitHub官方地址：https://github.com。

在浏览器中打开GitHub网址，通过首页进行注册，如下图所示。

![](http://img.testclass.net/github_page.png)

#### 安装Git
----
Git官方下载地址：http://git-scm.com/download/。

Git支持多平台（Mac OS X/Windows/Linux/Solaris）,读者可根据自己的平台选择相应的版本下载。

Linux 各版本下安装Git：

      Debian/Ubuntu $ apt-get install git-core

      Fedora $ yum install git

      Gentoo $ emerge --ask --verbose dev-vcs/git

      Arch Linux $ pacman -S git

下载并安装完成后，我们通常在Mac OSX及Linux平台下用终端工具(Terminal)来使用Git，而在Windows平台下用Git Bash工具，如下图所示。

![](http://img.testclass.net/git_menu.png)

#### 建立链接
----
本地Git与GitHub服务器之间保持通信时，我们使用SSH key认证方式来保证通信安全，所以在使用GitHub前你必须先建创自已的SSH key。
我们后续操作以Windows为例，打开Git Bash，如下图所示。

![](http://img.testclass.net/git_window.png)

（1）__进入 SSH 目录。__

    fnngj@FNNGJ-PC ~
    $ cd ~/.ssh

    fnngj@FNNGJ-PC ~/.ssh
    $ pwd
    /c/Users/fnngj/.ssh

（2）__生成新的 SSH 秘钥。__

如果你已经有了一个秘钥（默认秘钥位置~/.ssh/id_rsa文件存在。）

    fnngj@FNNGJ-PC ~/.ssh
    $ ssh-keygen -t rsa -C "fnngj@126.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/c/Users/fnngj/.ssh/id_rsa):  --回车
    Enter passphrase (empty for no passphrase):        --回车
    Enter same passphrase again:            --回车
    Your identification has been saved in /c/Users/fnngj/.ssh/id_rsa.
    Your public key has been saved in /c/Users/fnngj/.ssh/id_rsa.pub.
    The key fingerprint is:
    78:51:9b:2c:6c:fb:74:0b:6b:b9:c4:23:8f:5e:10:6b fnngj@126.com
    The key's randomart image is:
    +--[ RSA 2048]----+
    |          .         |
    |       . o o       |
    |        * +         |
    |       o *          |
    |      . E o .      |
    |       o = = .     |
    |        . X .      |
    |         B o        |
    |       .o o         |
    +-----------------+

    fnngj@FNNGJ-PC ~/.ssh
    $ ls
    id_rsa  id_rsa.pub


查看目录下会生成两个问题，id_rsa 是私钥，id_rsa.pub 是公钥。记住千万不要把私钥文件id_rsa 透露给任何人。

__（3）添加 SSH 公钥到 GitHub。__

用文本工具打开公钥文件 ~/.ssh/id_rsa.pub ，复制里面的所有内容到剪贴板，如下图所示。

![](http://img.testclass.net/git_id_rsa.png)

登录GitHub，__单击右上角个人头像→Settings→SSH Keys→Add SSH Keys__ ,在 Title 文本框中输入任意字符，在 Key文本框粘贴刚才复制的公钥字符串，单击“Add key”按钮完成操作，如下图所示。

![](http://img.testclass.net/add_ssh_key.png)

__（4）测试连接。__

以上步骤完成后，你就可以通过以下命令来测试是否可以连接 GitHub服务器了。

    fnngj@FNNGJ-PC ~/.ssh
    $ ssh -T git@github.com
    The authenticity of host 'github.com (192.30.252.129)' can't be established.
    RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'github.com,192.30.252.129' (RSA) to the list of know
    n hosts.
    Hi defnngj! You've successfully authenticated, but GitHub does not provide shell
     access.




原始封面

![课程图片](https://images.unsplash.com/photo-1581093202218-980a6769202b?w=300)

