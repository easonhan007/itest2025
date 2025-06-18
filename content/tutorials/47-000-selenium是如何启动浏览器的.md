---
weight: 0
title: selenium是如何启动浏览器的
date: '2018-05-17T05:39:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1503435980610-a51f3ddfee50?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



前几天有同学问到selenium是怎么样启动浏览器的(selenium启动浏览器的原理)，当时稍微讲解了一下，不过自我感觉不够具体，现在特地把启动原理通过代码和一系列操作给串联起来，希望可以帮助大家更好的理解。

以chrome浏览器为例，selenium启动chrome浏览器的代码如下：

[源码](https://github.com/SeleniumHQ/selenium/blob/1a99e2161f8b777672f15fda9b329ee8e89af94a/py/selenium/webdriver/chrome/webdriver.py#L33)

```python

def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None):
        """
        Creates a new instance of the chrome driver.
        Starts the service and then creates new instance of chrome driver.
        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - desired_capabilities: Dictionary object with non-browser specific
           capabilities only, such as "proxy" or "loggingPref".
         - options: this takes an instance of ChromeOptions
        """
        if chrome_options:
            warnings.warn('use options instead of chrome_options', DeprecationWarning)
            options = chrome_options

        if options is None:
            # desired_capabilities stays as passed in
            if desired_capabilities is None:
                desired_capabilities = self.create_options().to_capabilities()
        else:
            if desired_capabilities is None:
                desired_capabilities = options.to_capabilities()
            else:
                desired_capabilities.update(options.to_capabilities())

        self.service = Service(
            executable_path,
            port=port,
            service_args=service_args,
            log_path=service_log_path)
        self.service.start()

        try:
            RemoteWebDriver.__init__(
                self,
                command_executor=ChromeRemoteConnection(
                    remote_server_addr=self.service.service_url),
                desired_capabilities=desired_capabilities)
        except Exception:
            self.quit()
            raise
        self._is_remote = False

```

其中跟浏览器启动密切相关的是这几句

```python
self.service = Service(
    executable_path,
    port=port,
    service_args=service_args,
    log_path=service_log_path)
self.service.start()
```

通过查看跟[Service](https://github.com/SeleniumHQ/selenium/blob/1a99e2161f8b777672f15fda9b329ee8e89af94a/py/selenium/webdriver/common/service.py#L35)相关的代码复盘得到启动逻辑: 调用chromedriver可执行文件运行chromedirver。这也是为什么我们需要把chromedriver放到系统PATH里的原因。

所以selenium先启动了chromedriver。当然，我们可以手工启动chromedriver来模拟这个启动过程。

在命令行中运行下面的命令```chromedirver```

你应该可以看来类似的结果

```
Starting ChromeDriver 2.38.552518 (183d19265345f54ce39cbb94cf81ba5f15905011) on port 9515
Only local connections are allowed.
```

这样我们就手工启动了chromedriver。driver监听的端口是9515.

启动了driver之后，我们需要告诉driver打开浏览器。selenium的[源码](https://github.com/SeleniumHQ/selenium/blob/1a99e2161f8b777672f15fda9b329ee8e89af94a/py/selenium/webdriver/remote/webdriver.py#L224)里这一过程如下

```python

def start_session(self, capabilities, browser_profile=None):
        """
        Creates a new session with the desired capabilities.
        :Args:
         - browser_name - The name of the browser to request.
         - version - Which browser version to request.
         - platform - Which platform to request the browser on.
         - javascript_enabled - Whether the new session should support JavaScript.
         - browser_profile - A selenium.webdriver.firefox.firefox_profile.FirefoxProfile object. Only used if Firefox is requested.
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})
        w3c_caps = _make_w3c_caps(capabilities)
        parameters = {"capabilities": w3c_caps,
                      "desiredCapabilities": capabilities}
        response = self.execute(Command.NEW_SESSION, parameters)
        if 'sessionId' not in response:
            response = response['value']
        self.session_id = response['sessionId']
        self.capabilities = response.get('value')

        # if capabilities is none we are probably speaking to
        # a W3C endpoint
        if self.capabilities is None:
            self.capabilities = response.get('capabilities')

        # Double check to see if we have a W3C Compliant browser
        self.w3c = response.get('status') is None
        self.command_executor.w3c = self.w3c
```

这一过程的核心就是就是向```localhost:9515/session```发送1个POST请求，并发送1个json对象，默认情况下，这个对象应该是下面这个样子。

```
{
    "capabilities": {
        "alwaysMatch": {
            "browserName": "chrome",
            "goog:chromeOptions": {
                "args": [],
                "extensions": []
            },
            "platformName": "any"
        },
        "firstMatch": [
            {}
        ]
    },
    "desiredCapabilities": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": [],
            "extensions": []
        },
        "platform": "ANY",
        "version": ""
    }
}
```
简单理解就是告诉remote driver打开什么浏览器，上面的例子里我们打开的是chrome浏览器。

我们可以手工还原这个过程。

确保chromedriver是在运行中的，然后打开postman，构造1个POST请求，路径是localhost:9515/session。在Body里选择raw和JSON(application/json), 贴入上面的json字符串，如下图所示

![postman](http://img.testclass.net/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202018-05-17%20%E4%B8%8B%E5%8D%882.02.44.png)

点击send，几秒之后chrome浏览器应该可以正常启动，并且postman的response里会有大致如下的返回值

```
{
    "sessionId": "ad4407e133cfd5f3f49bff4c2f1f087a",
    "status": 0,
    "value": {
        "acceptInsecureCerts": false,
        "acceptSslCerts": false,
        "applicationCacheEnabled": false,
        "browserConnectionEnabled": false,
        "browserName": "chrome",
        "chrome": {
            "chromedriverVersion": "2.38.552518 (183d19265345f54ce39cbb94cf81ba5f15905011)",
            "userDataDir": "/var/folders/s6/f2_brc114wv2g8w0qggk_m2c0000gn/T/.org.chromium.Chromium.NMsAKJ"
        },
        "cssSelectorsEnabled": true,
        "databaseEnabled": false,
        "handlesAlerts": true,
        "hasTouchScreen": false,
        "javascriptEnabled": true,
        "locationContextEnabled": true,
        "mobileEmulationEnabled": false,
        "nativeEvents": true,
        "networkConnectionEnabled": false,
        "pageLoadStrategy": "normal",
        "platform": "Mac OS X",
        "rotatable": false,
        "setWindowRect": true,
        "takesHeapSnapshot": true,
        "takesScreenshot": true,
        "unexpectedAlertBehaviour": "",
        "version": "66.0.3359.181",
        "webStorageEnabled": true
    }
}
```

上面的返回里最重要的就是sessionId，因为后面所有跟浏览器的交互都是基于该id进行的。

### 总结

* selenium里，selenium client先打开chromedriver
* chromedirver创建session时打开了浏览器，所以浏览器的打开跟selenium无关，完全是chromedriver的能力

### 更多

其实上面的例子里我们手工调用了[webdriver协议](https://w3c.github.io/webdriver/)里的[new session](https://w3c.github.io/webdriver/#new-session)协议，创建了webdriver session。具体的细节大家可以参考协议了解更多。




原始封面

![课程图片](https://images.unsplash.com/photo-1503435980610-a51f3ddfee50?w=300)

