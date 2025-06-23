---
weight: 1
title: "python requests的替代者？httpx初体验"
date: 2024-03-08T09:01:58+08:00
lastmod: 2024-03-08T09:01:58+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "现在用的人比较多了"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1653363411414-c002ff2f0f86?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

python 的 requests 库由于其使用简单，文档丰富成为了很多人在发送 http 请求时候的优选选择。前几天看到了一个类似的实现 httpx，在这里简单使用体验一下，顺便简单分享一下体验心得。

相比较 requests，httpx 支持 sync 和 async 的 API，支持 http1.1 和 http2。httpx 尽最大努力兼容 requests 的 API，这样一来用户从 requests 转换到 httpx 的成本就相对较为低廉了。

### 基本 API

```python
>>> import httpx
>>> r = httpx.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

简单扫一圈，满眼都是 requests 当年的样子。下面是 requests 的 API，大家来找茬，看看哪里不一样。

```python
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>> r.status_code
200
>> r.headers['content-type']
'application/json; charset=utf8'
>> r.encoding
'utf-8'
>> r.text
'{"type":"User"...'
>> r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
```

不能说非常相似，只能说是一模一样。

### httpx client

requests 为一组 http 请求提供了 session 对象来进行统一设置和管理，httpx 则相应的提供了 client 对象。我们来对比一下使用方式先。

首先使用 starlette 来创建一个简单的 python api 服务。starlette 项目可以想象成是 async 版本的 flask，跟 httpx 系出同门。

```python
# example.py
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def homepage(request):
    await asyncio.sleep(0.1) # 加一点点等待，不加也可以
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/", endpoint=homepage)
]

# app = Starlette(debug=True, routes=routes)
app = Starlette(debug=False, routes=routes)
```

使用 uvicorn 运行。

```bash
$ uvicorn example:app
```

上面的服务提供了 1 个接口 localhost:8000，返回值如下

```bash
http :8000

HTTP/1.1 200 OK
content-length: 17
content-type: application/json
date: Thu, 11 Aug 2022 07:10:07 GMT
server: uvicorn

{
    "hello": "world"
}
```

我们先用非 client/session 方式来访问该接口 30 次，顺便统计一下运行时间

requests 先出场。

```python
# without_session
import requests

for i in range(0,30):
	res = requests.get('http://localhost:8000/').json()
	print(res)
```

```bash
python without_session.py  0.24s user 0.08s system 9% cpu 3.500 total
```

上面是不用 session 的方式，3.5s 完成。

使用 session 试试。

```python
import requests

s = requests.Session()

for i in range(0,30):
	res = s.get('http://localhost:8000/').json()
	print(res)
```

```python
python with_session.py  0.22s user 0.08s system 8% cpu 3.443 total
```

3.44s，快了一点点。

下面是 httpx 不使用 client 的方式。

```python
python without_client.py  0.69s user 0.11s system 20% cpu 3.972 total
```

3.9s。

使用 client 试试

```python
import httpx

with httpx.Client() as client:
	for i in range(0, 30):
		res = client.get('http://localhost:8000/').json()
		print(res)
```

```python
python with_client.py  0.38s user 0.11s system 13% cpu 3.707 total
```

3.7s，也快了一些。

这里可以简单总结一下，使用 client/session 可以提升一组请求的发送效率，另外也提供了进行统一配置（比如修改 header 的）的快捷方式。上面的测试由于请求处理的太快效果不是很明显，在日常的测试中两种方式的区别可能会更加容易发现一些。

### async

还是 30 个请求，这次我们用 httpx 的 async 方式来试试。

```python
import asyncio
from asyncio import tasks
import httpx

async def send_requests(client):
	r = await client.get('http://localhost:8000')
	print(r.json())
	return r.json()


async def main():
	tasks = []
	async with httpx.AsyncClient() as client:
		for i in range(0, 30):
			tasks.append(send_requests(client))

		await asyncio.gather(*tasks)


asyncio.run(main())
```

```python
python httpx_async.py  0.47s user 0.13s system 71% cpu 0.848 total
```

0.84 秒，这大概就是 httpx 的最终奥义吧。

### 总结

作为下一代的 http client，httpx 出自名门望族(其开发团队开发了**[django-rest-framework](https://github.com/encode/django-rest-framework)**)，兼容了部分的 requests api，支持 async 操作等，是具有取代 requests 的能力的，在爬虫场景非常有潜力。
