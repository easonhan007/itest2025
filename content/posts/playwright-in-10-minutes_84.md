---
weight: 1
title: "10分钟玩转playwright"
date: 2023-03-01T09:03:40+08:00
lastmod: 2023-03-01T09:03:40+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "playwright初体验"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/1/work-station-straight-on-view.jpg?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

playwright 是微软推出的一款自动化测试工具，据说开发小组的核心人员来自 google 的 puppeteer 团队，真是一出生就有了个好爹而且好爹的亲爹也是爹中的战斗机，这就让人非常期待了。

### 下载与安装

playwright 应该是使用 JavaScript 进行开发的，不过考虑到大部分的测试同学可能对 python 更为熟悉，这里的安装就以 python 版本为例。

在命令行中输入`pip install pytest-playwright`，等 playwright 安装成功之后再输入命令`playwright install`，这条命令的作用是安装测试所需要的各种浏览器支持，相比较 selenium 需要先安装浏览器再安装相应版本的 driver，playwright 的初始化工作就显得轻松了很多。

### 第一个用例

接下来按照官方文档里的例子我们来跑第一个 playwright 用例。

新建一个名为 test_my_app.py 的文件，然后把文档中的例子一字不差的进行拷贝粘贴。

```python
import re
from playwright.sync_api import Page, expect

def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.locator("text=Get Started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))
```

然后在命令行里输入 pytest，视网速而定，等待个 10 秒钟左右，就可以看运行结果了。

```python
collected 1 item

test_my_application.py .                                                                                                                       [100%]

================================================================= 1 passed in 7.08s ==================================================================
```

上面的用例去到了 playwright 的官网，定位并点击了名为 Get Started 的链接，最后断言页面上的 url 里含有 intro 这个字符串。

1 passed 表示运行了 1 个用例并且用例成功通过。另外默认情况下 playwright 是以 headless 的模式运行的，这表示运行的过程中浏览器在后台打开和工作，所以看不到浏览器界面是常规操作，不需要紧张和疑惑。

如果遇到了网络超时的情况，可以试试用下面的用例去替换。

```python
import re
from playwright.sync_api import Page, expect

def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(
    page: Page
):
    page.goto("http://www.itest.info/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("重定向科技")

    # create a locator
    plan = page.locator("css=.navbar-nav li >> nth=1 >> a")

    # Expect an attribute "to be strictly equal" to the value.
    expect(plan).to_have_attribute("href", "/plans")

    # Click the get started link.
    plan.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*plans"))
```

### 脚本录制

playwright 支持通过录制的方式生成部分的脚本。

### 作为爬虫使用
