---
weight: 6
title: requests如何构造复杂的post请求?
date: '2017-11-22T03:23:57+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1577412647305-991150c7d163?w=300
tags: []
categories:
- requests从入门到精通
lightgallery: true
toc:
  auto: false
---



默认情况下，在post方法中使用 data 关键字参数，Requests的行为会表现的像是在发送一个html表单，比如

```
>>> payload = {'key1': 'value1', 'key2': 'value2'}

>>> r = requests.post("http://httpbin.org/post", data=payload)
>>> print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
```

如果需要为多个元素使用同一key的话，可以在data中传入元组，比如

```
>>> payload = (('key1', 'value1'), ('key1', 'value2'))
>>> r = requests.post('http://httpbin.org/post', data=payload)
>>> print(r.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
```

如果 data 中传的是string而不是dict的话，那么字符串将会被直接发送出去

```
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))
```

因为现在很多api接受json字符串格式的post data，Requests为这种方式提供了更简单的写法

```
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)
```




原始封面

![课程图片](https://images.unsplash.com/photo-1577412647305-991150c7d163?w=300)

