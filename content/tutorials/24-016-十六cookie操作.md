---
weight: 16
title: （十六）cookie操作
date: '2017-06-15T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/uploads/1412026095116d2b0c90e/3bf33993?w=300
tags: []
categories:
- selenium python 综合教程
lightgallery: true
toc:
  auto: false
---


<br>
有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的。WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息。

WebDriver操作cookie的方法：

* get_cookies()：			获得所有cookie信息。

* get_cookie(name)：		返回字典的key为“name”的cookie信息。

* add_cookie(cookie_dict)	：	添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

* delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

* delete_all_cookies()：		删除所有cookie信息。

下面通过get_cookies()来获取当前浏览器的cookie信息。
```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie= driver.get_cookies()
# 将获得cookie的信息打印
print(cookie)

driver.quit()
```

从执行结果可以看出，cookie数据是以字典的形式进行存放的。知道了cookie的存放形式，接下来我们就可以按照这种形式向浏览器中写入cookie信息。
```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 向cookie的name 和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()


输出结果：
======================== RESTART: =========================
YOUDAO_MOBILE_ACCESS_TYPE -> 1
_PREF_ANONYUSER__MYTH -> aGFzbG9nZ2VkPXRydWU=
OUTFOX_SEARCH_USER_ID -> -1046383847@218.17.158.115
JSESSIONID -> abc7qSE_SBGsVgnVLBvcu
key-aaaaaaa -> value-bbbbbb
```
从执行结果可以看到，最后一条cookie信息是在脚本执行过程中通过add_cookie()方法添加的。通过遍历得到所有的cookie信息，从而找到key为“name”和“value”的特定cookie的value。




原始封面

![课程图片](https://images.unsplash.com/uploads/1412026095116d2b0c90e/3bf33993?w=300)

