---
weight: 1
title: （一）安装selenium
date: '2017-06-30T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1504893524553-b855bce32c67?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---



<br>
### 安装python

打开 [Python官网](https://www.python.org/)，找到“Download”, 在其下拉菜单中选择自己的平台（Windows/Mac）,一般的Linux平台已经自带的Python，所以不需要安装，通过打开“终端” ，输入“python”命令来验证。

如果你是第一次接触Python，一定会迷惑Python为什么会提供Python2.x 和 Python3.x两个版本？那么，直接使用Python3.x的最新版本就好了。因为Python2.x预计到2020年不在维护。

如果你是Windows平台用户，会遇到一个版本为什么会提供多种个下载链接。例如：

* Python 3.6.1 - 2017-03-21
  * Download Windows x86 web-based installer
  * Download Windows x86 executable installer
  * Download Windows x86 embeddable zip file
  * Download Windows x86-64 web-based installer
  * Download Windows x86-64 executable installer
  * Download Windows x86-64 embeddable zip file
  * Download Windows help file

x86 只支持32位的系统； x86-64 支持64位的系统。 web-based 在安装的过程中需要联网；executable 可执行文件(.exe)方式安装；embeddable zip file 嵌入式版本，可以集成到其它应用中。

注意：在安装的过程中需要勾选：“Add Python 3.x to PATH” , 如果没有勾选，需要在安装完成之后，将Python的安装目录（如：C:\Python36）添加到环境变量PATH下面。

打开Windows命令提示符（cmd）/ Linux终端输入：
```
C:\Users\name>python
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

<br>
### 安装selenium

首先，在Windows命令提示符（cmd）/ Linux终端输入：
```
C:\Users\name>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
……

```
确保pip命令可用，如果提示“pip不是内部或外部命令”，需要将将pip的安装目录（如：C:\Python36\Scripts）添加到环境变量PATH下面。


接下来通过pip命令安装Selenium:

```
C:\Users\name>pip install selenium
Collecting selenium
  Downloading selenium-3.4.3-py2.py3-none-any.whl (931kB)
    26% |████████                       | 245kB 576kB/s eta 0:00:02    
    27% |█████████                      | 256kB 570kB/s eta 0:00:02    
    28% |██████████                     | 266kB 536kB/s eta 0:00:0    
    29% |███████████                    | 276kB 530kB/s eta 0:00:0    
    30% |████████████                   | 286kB 586kB/s eta 0:00:0
……

```

<br>
### 测试

打开一款Python编辑器，默认Python自带的IDLE也行。创建 baidu.py文件，输入以下内容：

```python
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

print(driver.title)

driver.quit()

```

如果执行报错，请看下一节，[Selenium3浏览器驱动](/selenium_python/selenium3-browser-driver/)。




原始封面

![课程图片](https://images.unsplash.com/photo-1504893524553-b855bce32c67?w=300)

