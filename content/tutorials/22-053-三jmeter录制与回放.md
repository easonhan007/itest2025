---
weight: 53
title: （三）JMeter录制与回放
date: '2017-07-28T12:59:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1672822063901-72ebbac3f481?w=300
tags: []
categories:
- Jmeter综合教程
lightgallery: true
toc:
  auto: false
---




<br>
### 关于录制和回放功能

在JMeter2.1版本之前，JMeter应该是不支持录制和回放功能的，那时候如果需要录制jmeter的性能测试脚本的话，就需要使用第三方工具——[badboy](http://www.badboysoftware.biz/docs/jmeter.htm)。

现在jmeter已经支持脚本的录制功能了，但录制的体验相对于badboy来说还是差了一些。不过聊胜于无，对于性能测试的入门者来说，录制回放功能可以让大家对性能测试脚本开发的过程有个非常感性的认识。

不过录制脚本始终只是减轻工作量的一个手段，新手同学千万不要认为学会了录制回放就等于是学会了性能测试，学会录制回放只能代表你有机会真正的入门性能测试，这只是起点，而不是终点。

### 测试场景

在本节中，我们的测试场景是：在必应(bing)搜索引擎中搜索关键字```乙醇 selenium```。我们对搜索的结果并不关心，只要请求返回的状态码是200，我们就认为该请求是成功的，有效的。

### 准备录制

* 打开jmeter
* 工具栏点击**Templates...** ，选择**Recording**模版
* 点击WorkBench节点下的**HTTP(S) Test Script Recorder**
* 点击**启动**按钮，如下图所示

![recorder](http://img.testclass.net/recorder.png)

**此时应该会出现下图所示的警告对话框，我们可以简单的忽略掉，此警告不影响我们本节内容的准确性**

![warning](http://img.testclass.net/warning.png)

完成了以上的步骤之后，我们就成功的启动了jmeter的http代理，下面我们需要对配置系统，使得系统的http请求都通过jmeter代理发出。

*注意：如果启动代理的过程中遇到了一些意外情况，请参考[这里](https://wiki.apache.org/jmeter/TestRecording210)解决*

<br>
### 配置HTTP代理
----
#### Mac OS 系统

* 系统偏好设置 -> 网络 -> 代理 -> Web代理(HTTP)

* web代理服务器填写```localhost```，端口填写```8888```，如下图所示

![mac http proxy](http://img.testclass.net/mac_http_proxy.png)

* 保存配置


#### Windows 系统

Windows 10

* 通过**设置 -> 网络和INTERNET -> 代理**打开配置界面
* 打开**使用代理服务器**开关
* 地址文本框中填入```localhost```，端口填入```8888```，如下图所示

![win10 http proxy](http://img.testclass.net/win10_proxy.png)

Windows 7

* 通过 ** 控制面板 -> Internet属性 -> 局域网设**打开配置界面
* 地址文本框中填入```localhost```，端口填入```8888```，如下图所示

![win7 http proxy](http://img.testclass.net/win7_http_proxy.png)

<br>
### 开始录制
----
* 打开chrome浏览器的隐私模式。这是因为非隐私模式下浏览器发送请求时可能带有cookie，在录制过程中，我们是不希望已经保存的cookie对我们的录制过程产生影响的；

* 在地址栏中输入```www.bing.com```
* 待页面加载完毕后，在搜索框中输入 ```乙醇 selenium```
* 点击搜索
* 关闭chrome浏览器
* 关闭系统的http代理配置(**切记**)
* 在节点树的Thread Group下的Recording Controller下我们就可以看到我们录制的结果了，如下图所示

![recording result](http://img.testclass.net/recording_res.png)

<br>
### 回放
----
从上图我们可以看出，必应引擎在做搜索的时候，我们的客户端浏览器向服务器发送了很多的请求，这些请求大致分为下面几类

* 主要请求。比如打开必应首页的请求以及搜索```乙醇 selenium```的请求
* 静态资源请求。比如```cn.bing.com/fd/s/a/hp/bingcn.svg```这个请求就是返回了必应的icon
* 数据上报的请求。比如```/msnjv/counting```这个请求就有**可能**是数据上报和统计的请求
* 建议结果的ajax请求。每次我们输入不完整的关键字时搜索引擎都会返回给我们一些建议的结果，比如```/AS/Suggestions```这个请求就是从服务器返回建议结果的

在做一般的性能测试的时候我们需要明确我们的测试场景，如果我们的测试场景是需要精确模拟用户的行动的话，那么我们在回放请求时候是可以回放静态资源及数据上报的，因为这时候你测试的所关注的点可能是整体系统，而不是某台服务器。如果你的测试场景只是需要模系统的主要业务——在我们的例子里就是搜索——，那么在回放前我们可以删除掉录制脚本中的一些非主要业务的请求——比如搜索建议及数据上报。

在我们的例子中，我们不需要精确模拟用户的行为，我们将搜索的主要请求之外的请求都删除掉。结果如下图所示。

![recording result](http://img.testclass.net/only_search.png)

将这个脚本保存为bing_search.jxm，然后点击运行按钮(就是最上面一排绿色的三角形)

<br>
### 查看结果
----
点击View Results Tree我们发现结果树里有2个项目，第1个项目是我们真正发出的请求，第2个项目是第1个项目所属的事物控制器的结果，该结果仅仅用于展示，不代表事务控制器也发送了请求，这点需要注意一下。实际上我们的回放过程只发送了1个请求。

在结果树里选择search请求节点，该节点上方有个下拉菜单，通过该菜单我们可以选择让请求结果以什么格式展示，默认是纯文本(Text)格式。由于search请求返回的是html文本，所以我们选择HTML。点击**响应数据** tab，我们可以看到如下图所示的结果:

![html result](http://img.testclass.net/html_res.png)

从第一印象上看，这个结果说明了我们请求的回放是正确的。

实际上我们这个脚本的作用就是相当于在浏览器地址栏输入```http://cn.bing.com/search?q=%E4%B9%99%E9%86%87+selenium&go=%E6%8F%90%E4%BA%A4&qs=n&form=QBLH&pq=%E4%B9%99%E9%86%87+selenium&sc=1-11&sp=-1&sk=&cvid=A93B3CB2B248496EBA34A7E3EA5F15C5```这个地址，并获取结果，如下图所示。

![browser](http://img.testclass.net/browser.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1672822063901-72ebbac3f481?w=300)

