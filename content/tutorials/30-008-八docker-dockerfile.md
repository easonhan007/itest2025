---
weight: 8
title: （八）Docker Dockerfile
date: '2018-01-22T14:32:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1697982890437-767ca101582d?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---



虽然，前面已经会 使用 Nginx 和 docker selenium 来启动容器，但也仅仅是会使用，Dcoker 中还有许多概念和细节需要我们继续学习。


##### Dockerfile 文件分析
---

Dockerfile	由一行行命令语句组成，并且支持以 `#` 开头的注释行。

一般的 Dockerfile	分为四部分：__基础镜像信息__、 __维护者信息__、 __镜像操作指令__ 和 __容器启动时执行指令__ 。

以Selenium/Hub 的 [Dockerfile](https://github.com/SeleniumHQ/docker-selenium/blob/master/Hub/Dockerfile) 文件为例:

```C
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE: DO *NOT* EDIT THIS FILE.  IT IS GENERATED.
# PLEASE UPDATE Dockerfile.txt INSTEAD OF THIS FILE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FROM selenium/base:3.8.1-erbium
LABEL authors=SeleniumHQ

USER seluser

#========================
# Selenium Configuration
#========================

EXPOSE 4444

# As integer, maps to "maxSession"
ENV GRID_MAX_SESSION 5
# In milliseconds, maps to "newSessionWaitTimeout"
ENV GRID_NEW_SESSION_WAIT_TIMEOUT -1
# As a boolean, maps to "throwOnCapabilityNotPresent"
ENV GRID_THROW_ON_CAPABILITY_NOT_PRESENT true
# As an integer
ENV GRID_JETTY_MAX_THREADS -1
# In milliseconds, maps to "cleanUpCycle"
ENV GRID_CLEAN_UP_CYCLE 5000
# In seconds, maps to "browserTimeout"
ENV GRID_BROWSER_TIMEOUT 0
# In seconds, maps to "timeout"
ENV GRID_TIMEOUT 30
# Debug
ENV GRID_DEBUG false
# As integer, maps to "port"
ENV GRID_HUB_PORT 4444

COPY generate_config \
    entry_point.sh \
    /opt/bin/
# Running this command as sudo just to avoid the message:
# To run a command as administrator (user "root"), use "sudo <command>". See "man sudo_root" for details.
# When logging into the container
RUN /opt/bin/generate_config > /opt/selenium/config.json

CMD ["/opt/bin/entry_point.sh"]
```

* FROM

Dockerfile 都必须以 `FROM` 命令开始。 `FROM`命令会指定镜像基于哪个基础镜像创建，接下来的命令也会基于这个基础镜像。

* USER

指定运行容器时的用户名或 UID，后续的RUN、CMD、ENTRYPOINT也会使用指定用户。

* EXPOSE

告诉 Docker 服务端容器对外映射的本地端口，需要在 docker run 的时候使用-p或者-P选项生效。

* ENV

指定一个环节变量，会被后续 `RUN` 指令使用，并在容器运行时保留。

* CMD

CMD 有三种使用方式:

* CMD "executable","param1","param2"
* CMD "param1","param2"
* CMD command param1 param2 (shell form)

CMD指定在 Dockerfile 中只能使用一次，如果有多个，则只有最后一个会生效。

CMD的目的是为了在启动容器时提供一个默认的命令执行选项。如果用户启动容器时指定了运行的命令，则会覆盖掉CMD指定的命令。

> CMD会在启动容器的时候执行，build 时不执行，而RUN只是在构建镜像的时候执行，后续镜像构建完成之后，启动容器就与RUN无关了，这个初学者容易弄混这个概念，这里简单注解一下。


#### 阅读 Dockerfile 文件的意义
---

阅读 Dockerfile 文件，可以帮助我们了解 容器启动时都做了哪些事情。我们还可以根据需求修改启动参数。

例如，Selenium/hub 的 Dockerfile 文件中定义，超时时间是30秒。

```
# In seconds, maps to "timeout"
ENV GRID_TIMEOUT 30
```

如果需要修改这个参数，可以在启动 selenium-hub 时修改 `GRID_TIMEOUT` 参数。

```
$ sudo docker run -d -P --name selenium-hub -e GRID_TIMEOUT=10 selenium/hub
```

Dockerfile 文件中还是其它参数，参考：http://www.docker.org.cn/dockerppt/114.html




原始封面

![课程图片](https://images.unsplash.com/photo-1697982890437-767ca101582d?w=300)

