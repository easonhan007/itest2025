---
weight: 1
title: "grpc简介"
date: 2024-03-08T09:04:00+08:00
lastmod: 2024-03-08T09:04:00+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "最流行的微服务框架了"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1488554378835-f7acf46e6c98?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

### RPC

试想这样一种场景，一个复杂系统中的两个模块之前需要互相调用，一般的做法是什么？

可能这两个模块是跑在同一个进程上，那么通信起来其实是非常方便的，也有可能这两个模块分别是跑在不同的进程之上，那么就涉及到复杂一点的跨进程通信的技术了。但这些都是模块部署在同一机器下的情景，大家想象起来也会比较容易。

更加深入一些，如果两个模块跑在不同的机器之间，那么模块之前的调用如何实现呢？这就需要使用 RPC 技术了。

RPC（Remote Procedure Call）— 远程过程调用，它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。RPC 协议假定某些传输协议的存在，如 TCP 或 UDP，为通信程序之间携带信息数据。在 OSI 网络通信模型中，RPC 跨越了传输层和应用层。RPC 使得开发包括网络分布式多程序在内的应用程序更加容易。

RPC 采用客户端/服务器模式。请求程序就是一个客户端，而服务提供程序就是一个服务器。首先，客户端调用进程发送一个有进程参数的调用信息到服务进程，然后等待应答信息。在服务器端，进程保持睡眠状态直到调用信息到达为止。当一个调用信息到达，服务器获得进程参数，计算结果，发送答复信息，然后等待下一个调用信息，最后，客户端调用进程接收答复信息，获得进程结果，然后调用执行继续进行。

简单来说 RPC 需要 server 端和 client 端，server 端定义一些函数，client 端通过网络请求去调用这些函数拿到返回值。server 端和 client 端跑在不同的机器上，结合微服务的概念就是 server 端就是一个独立的微服务，其他微服务需要通过启动 client 端来调用该微服务提供的服务。

### gRPC

gRPC 一开始由 Google 开发，是一款语言中立、平台中立、开源的远程过程调用(RPC)系统。

在 gRPC 里客户端应用可以像调用本地对象一样直接调用另一台不同的机器上服务端应用的方法，使得您能够更容易地创建分布式应用和服务。与许多 RPC 系统类似，gRPC 也是基于以下理念：定义一个服务，指定其能够被远程调用的方法（包含参数和返回类型）。在服务端实现这个接口，并运行一个 gRPC 服务器来处理客户端调用。在客户端拥有一个存根能够像服务端一样的方法。

### 组成

典型的 grpc 实现有两端组成，分别是

- server
- client

![grpc%E7%AE%80%E4%BB%8B%2082e57cd2e8434314addbe47d6725a434/Untitled.png](grpc%E7%AE%80%E4%BB%8B%2082e57cd2e8434314addbe47d6725a434/Untitled.png)

### gRPC 的特性

- 由于 client 和 server 需要通过网络进行消息的传递，那么网络协议成了 grpc 里重要的一环。grpc 协议是 HTTP/2，这是一种优化过的 http 协议，实现了连接多路复用、双向流、服务器推送、请求优先级、首部压缩等机制。可以节省带宽、降低 TCP 链接次数、节省 CPU，帮助移动设备延长电池寿命等。
- 服务端向外提供了一些可供调用的函数，这些函数的原型通过 ProtoBuf 协议来进行定义。ProtoBuf 是由 Google 开发的一种数据序列化协议（类似于 XML、JSON、hessian）。ProtoBuf 能够将数据进行序列化，并广泛应用在数据存储、通信协议等方面。压缩和传输效率高，语法简单，表达力强。
- 支持多种编程语言。比如支持 golang/java/c++/ruby/python/nodejs 等。

### gRPC 的优点

- 使用 protobuf 进行消息的序列化，压缩率高，性能好，毕竟压缩的越小在网络上传播的速度就相对会更快一点
- 序列化反序列化直接对应程序中的数据类，不需要解析后在进行映射，其实除了可读性差之外，pb 的使用方式跟 json 基本都差不多了
- 支持向前兼容和向后兼容，升级比较简单
- 支持多语言

### 典型的 gRPC 实现

典型的 gRPC 实现有 3 个部分，分别是

- 服务定义，使用 protobuf 的语法
- server 端实现，可以使用任意支持的语言
- client 端实现，可以使用任意支持的语言

这里我们简单演示一下如何使用 python 实现简单的 grpc server 和 client

服务定义

```bash
// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
  // Sends another greeting
  rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}

```

server 端实现

```python
class Greeter(helloworld_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

  def SayHelloAgain(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)
...
```

client 端实现

```python
def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
```

### 测试 gRPC 的 server

其实跟接口测试的概念差不多，使用 client stub 去调用 server，然后进行断言就好了。简而言之就是写代码去调用 server 端提供的函数，然后做断言

### 测试 client

这一部分对大家来说可能不太好想象，有一种做法是 mock client，实现 client 的一系列调用 server 的 mock 方法，然后把 client 代入正常的业务逻辑，最后做逻辑或流程正确与否的判断。

举个例子，比如有个微服务使用 client 调用了 a 和 b 两个函数，那么就 mock 掉 a 和 b 的 client 端实现，最后在正常的业务逻辑结束之后，断言 client 先调用了 a 再调用了 b。这种 mock 的方式之前在做单元测试的时候非常的普遍，一般是用来 mock 掉网络请求或者是数据库连接，用在 rpc 的 client 测试上就显得比较有意思了。

### 性能测试

推荐使用 ghz。

[ghz · gRPC benchmarking and load testing tool](https://ghz.sh)

### 监控

一般可以使用下面的两种方案

- OpenCensus
- Prometheus

### Tracing

因为微服务之前的调用链路很复杂，所以需要使用 tracing 来进行调用链的跟踪。这里可以简单的使用 OpenCensus Jaeger exporter 来实现。

### grpc gateway

在测试和调式的时候，每次写 client 去调用 server 其实是一件比较麻烦的事情，grpc gateway 提供了一种简单的方式把 grpc 转成 restful 形式的接口，这样就可以直接使用 postman 等工具进行调试和测试了。
