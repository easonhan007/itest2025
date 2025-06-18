---
weight: 3
title: （三）Git提交代码到GitHub
date: '2017-08-31T02:00:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1581091224003-01e7c2e69f6f?w=300
tags: []
categories:
- git简明教程
lightgallery: true
toc:
  auto: false
---



请先阅读：[GitHub注册与Git安装](/git/registration-and-installation/)

#### GitHub创建项目
----
在GitHub选择并创建一个项目。首先，登录 GitHub，单击页面右上角加号__“+”__ ，选择__“New repository”__ 选项。

填写项目名称及描述，默认项目为“Public”,如果想创建“Private”项目，GitHub需要收费。最后单击“Create repository”完成项目的创建，如下图所示。

项目名称为：__project-name__

![](http://img.testclass.net/git_create_project.png)

创建完一个项目之后，GitHub会提示我们如何提交项目到它上面。

    Quick setup — if you’ve done this kind of thing before
    HTTPS  https://github.com/defnngj/project-name.git
    SSH    git@github.com:defnngj/project-name.git

    …or create a new repository on the command line

    echo # project-name >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin git@github.com:defnngj/project-name.git
    git push -u origin master

    …or push an existing repository from the command line

    git remote add origin git@github.com:defnngj/project-name.git
    git push -u origin master

    …or import code from another repository

    You can initialize this repository with code from a Subversion, Mercurial, or TFS project.


#### 第一次提交代码到GitHub
----

首先进行初始化配置：设置仓库人员的用户名和邮箱地址，这一步必不可少。

    fnngj@FNNGJ-PC ~/.ssh
    $ git config --global user.name "username"

    fnngj@FNNGJ-PC ~/.ssh
    $ git config --global user.email "user@mail.com"


在本地创建一个 “__project-name__” 项目，与GitHub上创建的项目名 __保持一致__。

为了练习，我们在项目下创建一个test_case.py文件。

    fnngj@FNNGJ-PC /d/project-name
    $ ls

    test_case.py

__“ls”__ 为Linux命令，用于查看当前目录下的文件及文件夹。

    fnngj@FNNGJ-PC /d/project-name
    $ git init

    Initialized empty Git repository in d:/project-name/.git/

__“git init”__ 命令用于对当前目录进行初始化，使当前的project-name目录交由Git进行管理。

    fnngj@FNNGJ-PC /d/project-name (master)
    $ git status

    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            test_case.py

    nothing added to commit but untracked files present (use "git add" to track)

__“git status”__ 命令用于查看当前项目下所有文件的状态。

我们可以看到当前处于master（主）分支，罗列了当前目录下的文件（test_case.py），并且提示未对当前目录下的文件进行跟踪（跟踪文件增、删、改的状态）；并告诉我们可以通过 __“git add”__ 命令对文件进行跟踪。

    fnngj@FNNGJ-PC /d/project-name (master)
    $ git add .

    fnngj@FNNGJ-PC /d/project-name (master)
    $ git status

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

            new file:   test_case.py

__“git add”__ 命令可以对指定文件添加跟踪。如果后面跟空格加点号“.”，则表示对当前目录下的所有文件进行跟踪。

再次通过 __“git status”__ 命令查看当前Git仓库的信息。


    fnngj@FNNGJ-PC /d/project-name (master)
    $ git commit -m "first commit file"

    [master (root-commit) 9b4b839] first commit file
     1 file changed, 9 insertions(+)
     create mode 100644 test_case.py

__“git commit”__ 命令将文件（git add 进行管理的文件）提交到本地仓库。```-m``` 参数对本次的提交加以描述。一般提交的描述必不可少，从而方便追溯每次提交都做了哪些修改。

准备工作已经完成，下面提交代码到GitHub。这里GitHub提供了两种链接方式：HTTPS和SSH,提交的地址有所不同，请查看前面GitHub提示信息。

    fnngj@FNNGJ-PC /d/project-name (master)
    $ git remote add origin git@github.com:defnngj/project-name.git

    fnngj@FNNGJ-PC /d/project-name (master)
    $ git push -u origin master

    Warning: Permanently added the RSA host key for IP address '192.30.252.128' to t
    he list of known hosts.
    Counting objects: 3, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 354 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To git@github.com:defnngj/project-name.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.


* __“git remote add origin git@github.com:defnngj/project-name.git”__

如果是第一次提交项目，这一句非常重要，它会将本地的项目与远程的仓库之间建立连接。这里选择SSH协议方式进行连接。

*  __“git push -u origin master ”__

将本地的项目提交到远程仓库中。

#### GitHub查看提交代码
----

现在访问GitHub就看到我们提交的项目了，如下图所示。


![](http://img.testclass.net/git_look_project.png)

<br>
<font color=#0099ff>
看！你的项目代码已经提交到了GitHub上面，开心吧！？
</font>




原始封面

![课程图片](https://images.unsplash.com/photo-1581091224003-01e7c2e69f6f?w=300)

