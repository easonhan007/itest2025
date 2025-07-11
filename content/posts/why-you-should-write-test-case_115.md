---
weight: 1
title: "做一个没有感情的用例生成机器"
date: 2023-03-01T09:04:27+08:00
lastmod: 2023-03-01T09:04:27+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "如何用最低的成本去实现这些自动化用例呢？"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1453928582365-b6ad33cbcf64?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

最近我们准备把一些服务从一个二次开发的 k8s 平台迁移到另一个二次开发的 k8s 平台去，这时候我们遇到了一个比较棘手的问题：因为迁移是有损的，也就是说迁移的过程中伴随着一定量的代码修改和容器编排方式的适配，那么我们如何保证服务迁移以后的功能是正常可用的呢？

想了一些方法，这些办法其实比较常见：

- 增加监控指标和告警指标，迁移后如果服务有问题那么这些指标会让我们尽可能快的发现问题；
- 增加自动化的测试用例，通过用例尽可能的对现有服务功能进行覆盖；

那么问题就来了，如何用最低的成本去实现这些自动化用例呢？

首先我们应该选择合适类型的自动化用例，目前我们可以实现的用例有

- 单元测试用例，实现成本高，但是运行成本低，运行速度快，服务没有启动的情况下也能跑，如果有的选，那么单元测试用例是首选；
- 接口级的测试用例，实现成本相对较低，运行成本高，需要服务跑起来才能进行测试，运行速度相对单元测试是慢一些的；
- ui 自动化测试用例，实现成本高，运行成本也高，运行速度也慢；

最终我们选择增加一些核心的单元测试用例和 ui 自动化用例，然后尽可能多写接口测试用例。

我们的服务实现了一些微服务化，请求从最前面接入层进来之后会到 http 层，该层会调用更下层的 rpc 微服务层实现具体的业务逻辑，因此我们的接口就有两种，分别是

- http 接口，客户端直接调用
- rpc 接口，http 层以及微服务之间进行调用

因为业务逻辑往往需要多次的 rpc 调用才能实现，所以直接写 http 层的接口测试用例相对来说是一种比较经济的方式，因为一次的 http 接口调用会产生多次的 rpc 调用，从业务逻辑上和服务的触达性上来说都是令人满意的。

那么怎么去用尽可能最低的成本去实现这些 http 接口的用例呢？我之前有过使用 postman 把自己变成一个没有感情的用例生成机器的经历，在这里可以给大家分享一下。

举一个具体的例子，看这个接口。

```jsx
POST /api/users

请求
{
  "user":{
    "username": "Jacob",
    "email": "jake@jake.jake",
    "password": "jakejake"
  }
}

响应
{
  "user": {
    "email": "jake@jake.jake",
    "token": "jwt.token.here",
    "username": "jake",
    "bio": "I work at statefarm",
    "image": null
  }
}
```

这是一个用户注册的 POST 接口，需要向后端传 json 类型的数据，我们可以看成是传递一个 user 对象，这个对象有 username, email 和 password 属性，用 json 字符串的形式表达出来而已。

我们的目的是测试用户注册成功的情况。

使用 postman 去调用这个接口，不出意外的话服务端会返回一个已经创建的 user 对象，也是用 json 字符串的形式进行表达，跟请求传递的参数相比，多了一些属性，其中最重要的就是 token 属性，用这个 token 可以完成鉴权，也就是登录，是调用一些需要鉴权接口的必要条件。

接口调通之后，我们面临一个问题，目前传入的参数是固定的，这个接口再次运行的时候就会报错，因为用户已经注册过了，这是业务的要求，所以我们在做用例设计的时候需要去规避这个错误，因为我们的目的是测试用户注册成功。

所以我们要对请求体里的数据进行参数化，postman 实现参数化非常方便，可以这么做

```jsx
{
  "user":{
    "username": "{{$randomEmail}}",
    "email": "{{$randomEmail}}",
    "password": "{{$randomEmail}}"
  }
}
```

我们使用了 postman 自带的全局变量 randomEmail，这个变量会生成随机的 email 字符串，参数化的问题很容易就解决了。

最后是断言，我们再看一遍响应的内容。

```jsx
{
  "user": {
    "email": "jake@jake.jake",
    "token": "jwt.token.here",
    "username": "jake",
    "bio": "I work at statefarm",
    "image": null
  }
}
```

因为我们要快速的实现用例，所以我们可以采用有损验证，也就是说不需要特别精准的验证方式。

如果是精准验证，那么你需要检查

1. user 属性存在
2. 1 为 True 的时候，email 必须是请求中传递给后端的 email 字段，也就是说传进去的是a@itest.info，那么响应里也必须是a@itest.info
3. 1 为 True 的时候，token 存在
4. 1 为 True 的时候，username 逻辑同 2 中的 email 逻辑
5. 1 为 True 的时候，bio 存在
6. 1 为 True 的时候，image 存在

写起来不难，但是 2，4 这两个验证是需要费一点时间和精力的。

有损验证的时候，你可以轻松很多，因为你只需要判断

1. user 属性存在
2. 1 为 True 的时候 username, email, token , bio, image 字段都存在，有一点代码基础的同学都知道，这个实现起来要么是复制粘贴，要么就是一个循环搞定

有损验证特别适合逻辑不变的时候，系统架构进行重构或者升级的场景，因为这种场景下代码逻辑的更改是有限的，更多只是部署架构和配置发生了变更。

因此，作为一个没有感情的用例生成机器，我会这样实现断言，当然，这里的代码都是我从 postman 提供的代码片段中拷贝出来稍加修改的，分分钟就可以搞定。

```jsx
pm.test("Status code is 201", function () {
  pm.response.to.have.status(201);
});
pm.test("check response", function () {
  var jsonData = pm.response.json();
  pm.expect(jsonData).to.have.property("user");
  pm.expect(jsonData.user).to.have.property("email");
  pm.expect(jsonData.user).to.have.property("token");
  pm.expect(jsonData.user).to.have.property("username");
  pm.expect(jsonData.user).to.have.property("bio");
  pm.expect(jsonData.user).to.have.property("image");
});
```

思路对了，后面的用例实现起来就是毫无难度了，无非就是

- 把接口调通
- 做必要的参数化，往往这个是比较费时间的，不过熟练了就好了，postman 的界面是自带代码提示和补全的，基本也不需要太动脑筋
- 拷贝粘贴修改断言

因为说到底我们只进行了字段存在性的校验，而并没有对数据的准确性进行校验，所以用例不仅好写，而且维护成本也比较低，另外由于不依赖数据，所以用例可以在大部分环境，比如测试环境，正式环境愉快的运行，通用性也是非常不错的。

我相信有了这个技巧，大家也可以在非常短的时间内成长为用例生成机器。对了，这里的断言是 javascript 实现的，不会 js？没关系，反正断言都是相似的，都是复制粘贴，只要改几个字段和状态码就好了，不会 js 问题也不大，入门成本还是很低的。

需要在命令行里运行跟 ci/cd 结合起来？也没问题，用 postman 自带的解决方案就好了，可以搜索关键字 newman 去获取更多细节。

我上面分享的方式有点像是葵花宝典，练成之后确实很厉害，但终究还是缺了点什么，所以适用的场景是有限制的，大家可以根据实际情况灵活运用。

用最少的时间实现最多的用例，尽可能的对后端代码进行覆盖，我觉得应该是今后效能提升大背景下的一个趋势。

结合现在讨论度非常高的 github copilot，这是 AI 实现的自动代码生成工具，像这种无脑的用例生成场景确实非常适合用 ai 去帮我们完成大部分的工作。是的，你没看错，ai 已经会写用例了，可能今后测试人员的工作不是去尽可能多的实现用例，而是从 ai 写好的用例中挑选合适的用例的去执行。

智能化的用例生成应该是今后一个很有意思的领域，不过在这一天到来之前，把自己培养成一个没有感情的用例生成工具会让你更加高效，摆脱一些重复繁琐的验证工作。
