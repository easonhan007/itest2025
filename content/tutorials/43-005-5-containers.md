---
weight: 5
title: 5. Containers
date: '2017-10-25T06:55:26+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1515965885361-f1e0095517ea?w=300
tags: []
categories:
- webium简明教程
lightgallery: true
toc:
  auto: false
---



我们可以使用容器(containers)来限制定位范围，webium的containers特性可以让我们的定位代码更加干净容易理解，避免大规模的使用难懂晦涩的xpath。

考虑下面的页面结构，为了可以遍历每一个搜索结果，我们可以使用下面的代码

![](http://wgnet.github.io/webium/_images/containers.png)


```python
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds, BasePage

class Vacancy(WebElement):
    title = Find(by=By.CLASS_NAME, value='vacancy_title')
    profession = Find(by=By.CLASS_NAME, value='vacancy_profession')
    location = Find(by=By.CLASS_NAME, value='vacancy_location')
    apply_button = Find(by=By.CLASS_NAME, value='vacancy_apply_button')


class VacanciesPage(BasePage):
    vacancies_list = Finds(Vacancy, By.XPATH, '//div[@id="careers-vacancies"]/div[@data-id]')

    def __init__(self):
        super(VacanciesPage, self).__init__(url='http://wargaming.com/en/careers/vacancies/')


if __name__ == '__main__':
    page = VacanciesPage()
    page.open()
    for vacancy in page.vacancies_list:
        # search by CLASS_NAME='vacancy_title' is performed within one node
        print('Title: ' + vacancy.title.text)
```



原始封面

![课程图片](https://images.unsplash.com/photo-1515965885361-f1e0095517ea?w=300)

