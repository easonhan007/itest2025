---
weight: 2
title: 2. BasePage
date: '2017-10-28T06:55:26+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1508873699372-7aeab60b44ab?w=300
tags: []
categories:
- webium简明教程
lightgallery: true
toc:
  auto: false
---



页面类是Page Object设计模式的核心。在使用webium创建页面类的时候，必须继承```webium.base_page.BasePage```

```python
from webium import BasePage

class MyPage(BasePage):
    pass
```

### url

如果页面的url是固定的，那么可以在```__init__```方法中指定它，然后你就可以使用```open()```方法来跳转到该页面。

url也可以被定义成是类的静态属性。

```python
from webium import BasePage

class PageWithUrl(BasePage):
    def __init__(self):
        super(PageWithUrl, self).__init__(url='http://www.testclass.net/')

class AnotherPageWithUrl(BasePage):
    url = 'http://www.itest.info'

if __name__ == '__main__':
    page = PageWithUrl()
    page.open()

    itest = AnotherPageWithUrl()
    itest.open()
```

### driver

页面类必须持有```WebDriver```的实例以便操控浏览器。默认情况下，webium会使用```webium.settings.driver_class```来创建```WebDriver```实例。如果你需要获取driver的实例，你可以使用```webium.driver.get_driver()```来达到目的。

在实例化页面类时，我们也可以通过```driver```参数来显示传入```WebDriver```实例。

```python
from selenium.webdriver import Firefox
from webium import BasePage

class DriverHandlingPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(DriverHandlingPage, self).__init__(url='http://testclass.net/', *args, **kwargs)


if __name__ == '__main__':
    my_driver = Firefox()
    page = DriverHandlingPage(driver=my_driver)
    page.open()
    print('Page title: ' + my_driver.title)
    my_driver.quit()
```




原始封面

![课程图片](https://images.unsplash.com/photo-1508873699372-7aeab60b44ab?w=300)

