---
weight: 10
title: 10.使用flask实现mock server
date: '2017-08-21T04:41:43+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1551434678-e076c223a692?w=300
tags: []
categories:
- python接口测试实践教程
lightgallery: true
toc:
  auto: false
---



### flask

flask是python实现的简单的web框架，与django互补。

### flask教程

* [官方文档](http://flask.pocoo.org/)
* [flask大型项目教程](http://www.pythondoc.com/flask-mega-tutorial/index.html)

### 如何理解flask

* 路由 -> /request/uri

* handler -> 路由进来之后处理request并返回response的逻辑

### 最简单的例子

```python
from flask import Flask
app = Flask(__name__)

@app.route("/") # 路由
def hello(): # handler
    return "Hello World!"
```

### 实现mocked smile task api


获取所有的任务

```
GET /api/tasks # get all tasks
```

查看一个任务的详情

```
GET /api/tastks/:task_id # get a task with task_id
```

完成一个任务

```
PUT /api/tastks/:task_id # complete a task
```

### 代码

```python

from flask import Flask, jsonify, g
import copy
app = Flask(__name__)

@app.before_request
def set_up_data():
    g.data = [
        {'id': 1, 'title': 'task 1', 'desc': 'this is task 1'},
        {'id': 2, 'title': 'task 2', 'desc': 'this is task 2'},
        {'id': 3, 'title': 'task 3', 'desc': 'this is task 3'},
        {'id': 4, 'title': 'task 4', 'desc': 'this is task 4'},
        {'id': 5, 'title': 'task 5', 'desc': 'this is task 5'}
    ]

    g.task_does_not_exist = {"msg": "task does not exist"}

@app.route('/api/tasks')
def get_all_tasks():
    return jsonify(g.data)

@app.route('/api/tasks/<int:task_id>')
def get_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        return jsonify(g.data[task_id])
    else:
        return jsonify(g.task_does_not_exist)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        tmp = copy.deepcopy(g.data[task_id])
        tmp['done'] = True
        return jsonify(tmp)
    else:
        return jsonify(g.task_does_not_exist)

```

### 运行

```
set FLASK_APP=smile_task_mock_server.py

flask run
* Serving Flask app "smile_task_mock_server"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

浏览器打开localhost:5000就好了




原始封面

![课程图片](https://images.unsplash.com/photo-1551434678-e076c223a692?w=300)

