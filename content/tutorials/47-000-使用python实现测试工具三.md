---
weight: 0
title: 使用python实现测试工具(三)
date: '2018-08-01T06:55:32+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1435732960391-11053ee5e6b6?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



本系列教程使用的python版本是**3.6.3**。

### 背景

这一节我们实现一个简单的寻找页面上无效链接的工具。

我们这样定义无效链接: http响应的返回状态码 **>=400**的链接。 为什么？大家可以去搜索一下。

该工具的作用是访问某个页面，然后找到页面上所有的链接，依次对这些链接进行访问，通过返回的状态码来确定该链接是不是无效链接。

### 工具设计

我们设计一个命令行工具，给工具传1个参数，也就是该被测页面的url


所以工具大概是这样用的: ``` python dead_link.py www.example.com ```

### 代码实现

简单起见，我们会用到requests-html库。安装文档在[这里](http://html.python-requests.org/)。

```python
from requests_html import HTMLSession
import requests
from sys import argv
from urllib.parse import urlparse, urljoin
DEBUG = True

USAGE = '''
USAGE:
python dead_link.py www.itest.info
'''

if len(argv) != 2:
  print(USAGE)
  exit(1)

script_name, url = argv 

if url[:4] != 'http':
  url = 'http://' + url

res = urlparse(url)
if res.netloc == '':
  print('无法获取站点的domain信息')
  exit(1)

domain = res.netloc
print(f"站点domain: {domain}")

session = HTMLSession()
r = session.get(url)

links = r.html.find('a')

for link in links:
  if 'href' in link.attrs:
    href = link.attrs['href']
  else:
    continue
  result = urlparse(href)
  if result.netloc == '':
    href = urljoin(url, href)
    url_type = '内链'
  else:
    if domain in href:
      url_type = '内链'
    else:
      url_type = '外链'
  try:
    response = requests.get(href)
    if response.status_code >= 400:
      print(f"{url_type} {href} 失败")
    else:
      print(f"{url_type} {href} 成功")
  except:
    print("出现异常")

```

### 精讲

* 我们需要注意的是内链的情况，也就是有些链接是```/xxx/yyy/zzz```的情况，这种情况下需要将域名或者ip补全再访问
* requests-html库的基本使用参考[这里](http://html.python-requests.org/#tutorial-usage)

### 运行示例

```
python dead_link.py www.itest.info

站点domain: www.itest.info
内链 http://www.itest.info/ 成功
内链 http://www.itest.info/ 成功
内链 http://www.itest.info/newclass 成功
内链 http://www.itest.info 成功
内链 http://www.itest.info/courses/8 成功
内链 http://www.itest.info/courses/7 成功
内链 http://www.itest.info/courses/6 成功
内链 http://www.itest.info/courses/3 成功
内链 http://www.itest.info/courses/2 成功
内链 http://www.itest.info/faq 成功
内链 http://www.itest.info/videos 成功
外链 http://www.testclass.net 成功
外链 http://www.testpub.cn 成功
内链 http://www.itest.info/about 成功
内链 http://www.itest.info/courses/2 成功
内链 http://www.itest.info/courses/7 成功
内链 http://www.itest.info/courses/7 成功
内链 http://www.itest.info/courses/6 成功
内链 http://www.itest.info/courses/6 成功
内链 http://www.itest.info/courses/3 成功
内链 http://www.itest.info/courses/3 成功
内链 http://www.itest.info/courses/2 成功
内链 http://www.itest.info/courses/2 成功
内链 http://www.itest.info/about 成功
外链 http://www.cnblogs.com/fnng/ 成功
外链 http://www.cnblogs.com/nbkhic/ 成功
外链 http://testpub.cn/ 成功
外链 http://www.testclass.net/ 成功
内链 http://www.itest.info/about 成功
```

### 动手时间

* 抄一遍代码，看自己能不能运行起来
* 给这段代码每一行都加上注释，理解代码做了些什么
* 试着将上面的脚本改为实现判断页面上是否有无效图片的工具

### 扩展阅读

* [最新的爬虫工具REQUESTS-HTML](http://www.testclass.net/2018/04/25/requests-html/)

### 源码地址

[github地址](https://github.com/easonhan007/simple_test_tools)




原始封面

![课程图片](https://images.unsplash.com/photo-1435732960391-11053ee5e6b6?w=300)

