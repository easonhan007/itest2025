---
weight: 9
title: selenium爬虫
date: '2017-12-11T02:52:34+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1464983953574-0892a716854b?w=300
tags: []
categories:
- 如何实现网络爬虫
lightgallery: true
toc:
  auto: false
---



### why

从上一节的反爬虫建议来看，降低访问频率和将爬虫伪装成真实的用户访问可以对抗大部分的反爬虫策略。

因为selenium是完全操作真实的浏览器，所以发爬虫策略比较难察觉异常，对于一些反爬虫策略非常严酷的网站，用selenium爬虫有时候会起到意想不到的效果。

但是selenium爬虫也有一些局限性，比如效率低下等。

### 需求

我们使用selenium爬虫来获取[知乎今日最热](https://www.zhihu.com/explore)的问题列表。跟之前的知乎爬虫差不多。

### 搭建开发环境

我们需要使用selenium和chrome driver，具体的安装方式请参考[这里](http://www.testclass.net/selenium_python/install-selenium/)

### 代码

在这里我们就不分析html代码了，打开页面用开发者工具可以看到，今日最热的内容实际上就是找到```data-type="daily"```的div下，所有的```class=question_link```的a元素。

```python
# se_zhihu.py

from selenium import webdriver

url = 'https://www.zhihu.com/explore'
dr = webdriver.Chrome()
dr.get(url)

daily_div = dr.find_element_by_css_selector('div[data-type="daily"]')

for link in daily_div.find_elements_by_css_selector('.question_link'):
    print(link.text)

dr.quit()
```

### 运行

命令行中直接运行

```
python se_zhihu.py
```

### 结果

由于动态内容的关系，结果可能不尽相同。

```
如何看待美税改通过后各大公司的发福利提最低工资追加投资等行为？


全球变暖是必然吗？


主播进行游戏直播并从中获得打赏盈利涉及侵犯版权吗？


如何看待张召忠（局座）于12月22日在b站的《荒野行动》直播？


影史上有哪些经典的即兴表演镜头？

```

### 我们可以学到什么

* selenium操作浏览器可以实现一些爬虫行为
* selenium爬虫的效率很低
* 可以使用headless(无界面的浏览器)来提升selenium爬虫的效率
* 如果你对selenium的api不熟悉，可以直接使用Puppeteer来做爬虫，详情请看[这篇文章](https://blog.fundebug.com/2017/11/01/guide-to-automating-scraping-the-web-with-js/)




原始封面

![课程图片](https://images.unsplash.com/photo-1464983953574-0892a716854b?w=300)

