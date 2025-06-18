---
weight: 7
title: （七） 创建docker selenium容器
date: '2018-01-22T14:36:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1508094902356-db488e227d75?w=300
tags: []
categories:
- 写给初学者的docker教程
lightgallery: true
toc:
  auto: false
---




SeleniumHQ官方项目：https://github.com/seleniumHQ/docker-selenium
项目目前快速迭代中。



#### Selenium
---

这里主要针对的是 Selenium Grid，它用于分布式自动化测试，就是一套Selenium 代码可在不同的环境上运行。刚好，Docker可快速的创建各种环境。

__Selenium Grid 有两个概念__

hub ：主节点，你可以看作 “北京总公司的测试经理”。

node：分支节点，你可以看作 “北京总公司的测试小兵A” 和 “上海分公司的测试小兵B”，还有 “深圳分公司的测试小兵C” ...。

也就是说在Selenium Grid中只能有一个主hub，但可以在本地或远程建立 N 多个分支node，测试脚本指向主hub，由主hub 分配给本地/远程node 运行测试用例。


#### docker selenium 环境安装
---

以Ubuntu为例，在Ubuntu下安装Docker，请参考：[Docker安装（Ubuntu）](/docker/02-install/)

docker hub（仓库）：

https://hub.docker.com/r/selenium/hub/


1、下载主hub镜像（北京总公司的测试经理）

```
$ sudo docker pull selenium/hub
```

2、下载主node chrome 镜像（上海分公司的测试小兵B）

```
$ sudo docker pull selenium/node-chrome
```

3、查看镜像

```
$  sudo docker images

REPOSITORY            TAG       IMAGE ID         CREATED       SIZE
selenium/node-chrome  latest    1eba57bd3d79     12 days ago   823MB
selenium/hub          latest    d1437f7d9f87     12 days ago   285MB
```

4、启动主hub容器

```
$ sudo docker run -d -P --name selenium-hub selenium/hub
```
* -d 表示容器以守护态（Daemonized）形式运行。
* -P 表示 Docker 会随机映射一个 49000~49900 的端口到内部容器开放的网络端口。


5、启动分支node chrome 容器

```
$ sudo docker run -d --link selenium-hub:hub selenium/node-chrome
```
* --link 通过 link 关联 `selenium-hub` 容器，并为其设置了别名`hub`


6、查看容器
```
$ sudo docker images
CONTAINER ID     IMAGE                  COMMAND                  CREATED        STATUS        PORTS                     NAMES
9cd0dac69875     selenium/hub           "/opt/bin/entry_poin…"   12 hours ago   Up 12 hours   0.0.0.0:32768->4444/tcp   selenium-hub
18d139a6c36d     selenium/node-chrome   "/opt/bin/entry_poin…"   12 hours ago   Up 12 hours                             eloquent_gates
```
这里需要注意，Selenium/hub 容器的端口号为 `4444`，对Ubuntu映射的端口为 `32768`，前面通过 `-P` 参数自动分配。

__工作原理：__

> selenium Grid脚本 ->  ubuntu(32768) ->  Hub容器(4444)  ->  Node Chrome 容器


#### 创建Grid测试脚本与运行
---

1、编写Selenium Grid 脚本（grid_demo.py)

```Python
from selenium import webdriver
from time import sleep

driver = webdriver.Remote(
command_executor='http://127.0.0.1:32768/wd/hub',
desired_capabilities={'browserName': 'chrome'}
)

driver.get('https://www.baidu.com')
print("get baidu")

driver.find_element_by_id("kw").send_keys("docker selenium")
driver.find_element_by_id("su").click()

sleep(1)

driver.get_screenshot_as_file("/home/fnngj/mypro/baidu_img.png")

driver.quit()
print("end...")
```

注意访问的端口号和浏览器，因为我们只启动了node chrome容器，如果这里设置Friefox的话，需要你启动 `node firefox` 容器，hub找不到合适的node会报错。

另外，我们为了验证脚本是否真的执行加上了打印和截图。


2、运行脚本
```
$ python3 grid_demo.py

get baidu

end...
```

3、查看截图

![](http://img.testclass.net/docker_selenium.png)

百度页面是被渲染出来了，但中文有乱码。




原始封面

![课程图片](https://images.unsplash.com/photo-1508094902356-db488e227d75?w=300)

