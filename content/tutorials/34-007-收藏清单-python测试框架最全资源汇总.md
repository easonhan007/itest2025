---
weight: 7
title: '收藏清单: python测试框架最全资源汇总'
date: '2017-10-20T08:19:06+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1534398079543-7ae6d016b86a?w=300
tags: []
categories:
- 测试工具合集
lightgallery: true
toc:
  auto: false
---



## xUnit frameworks(单元测试框架)

- frameworks 框架
    * [unittest](https://docs.python.org/library/unittest.html) - python自带的单元测试库，开箱即用
    * [unittest2](https://pypi.python.org/pypi/unittest2) - 加强版的单元测试框架，适用于Python 2.7以及后续版本
    * [pytest](http://pytest.org/) - 成熟且功能强大的单元测试框架
    * [plugincompat](http://plugincompat.herokuapp.com/) - pytest的执行及兼容性插件
    * [nosetests](https://nose.readthedocs.org/en/latest/) - 让python测试更容易一点
    * [slash](https://github.com/slash-testing/slash) - python实现的单元测试框架
- extensions 扩展
    * [proboscis](https://pythonhosted.org/proboscis/) - 仿TestNG扩展了unittest模块以及Nose的功能
    * [grail](https://github.com/wgnet/grail) - 可以让你一步一步编写测试用例的库
    * [testify](https://github.com/Yelp/Testify/) - 单元测试框架，提供了加强型fixture，用例切割并行运行，testrunner高亮及详尽的log和report功能 
    * [trial](http://twistedmatrix.com/trac/wiki/TwistedTrial) - unittest模块的扩展，提供了命令行的testrunner工具以及代码覆盖率的整合，跟nose差不多
    * [subunit](https://launchpad.net/subunit) - 提供了unittest在另一个进程执行用例并汇总测试数据的能力
    * [testresources](https://launchpad.net/testresources) - 提供了多用例间管理测试数据的机制，兼容unittest
    * [testtools](https://launchpad.net/testtools) - 为Twisted和Bazaar提供的unittest扩展
    * [Sancho](https://www.mems-exchange.org/software/DurusWorks/) - 运行用例，并为失败的用例提供报告，但仅限于此
    * [zope.testing](https://pypi.python.org/pypi/zope.testing) - testrunner，提供了不错的debuge能力，并且集成了代码覆盖率。可以跟zope项目使用，也可以用在非zope项目上
    * [pythoscope](http://pythoscope.org/) - 自动或半自动为遗留的python系统创建测试用例的工具
    * [testlib](http://www.logilab.org/project/logilab-common/) - 更强大的unittest，更多的断言，支持module级的setup/teardown，skip test等...
    * [dutest](https://pypi.python.org/pypi/dutest) - An object oriented interface to retrieve unittest test cases out of doctests. Hides initialization from doctests by allowing setUp and tearDown for each interactive example. Allows control over all the options provided by doctest. Specialized classes allow selective test discovery across a package hierarchy.
    * [green](https://github.com/CleanCut/green) - Green是一个简洁多彩的testrunner，跟nose很像
    * [ddt](https://github.com/txels/ddt) - 让unittest 支持 Data-Driven 
    * [pytractor](https://github.com/kpodl/pytractor)  Selenium python bindings的扩展. 目的是让angular项目的测试更简单

## TDD \ ATDD \ BDD

- BDD
    * [behave](https://pypi.python.org/pypi/behave) - BDD 框架
    * [lettuce](http://lettuce.it/) - 又一个BDD框架
        * [lettuce-tools](https://github.com/telefonicaid/lettuce-tools) - 一整套lettuce扩展，让BDD更加简单
    * [contexts](https://github.com/benjamin-hodgson/Contexts) - Python的描述性测试工具
    * [mamba](http://nestorsalceda.github.io/mamba/) - python的definitive testing 工具
    * [pyvows](http://heynemann.github.io/pyvows/) - 异步的行为驱动开发测试工具
    * [pytest-bdd](https://github.com/pytest-dev/pytest-bdd) - py.test runner的BDD库
    * [robotframework](http://robotframework.org/) - 最有名的acceptance test-driven development (ATDD)测试框架
        * [awesome-robotframework](https://github.com/fkromer/awesome-robotframework) - 各种rf的扩展库
    * [radish-bdd](https://github.com/radish-bdd/radish) - BDD框架，支持gherkin语言
- Assertions 断言
    * [pyshould](https://github.com/drslump/pyshould) - 基于pyhamcrest的Should style断言
    * [pyhamcrest](https://github.com/hamcrest/PyHamcrest) - python版的Hamcrest matchers
    * [sure](https://github.com/gabrielfalcao/sure) -python实现的测试库,提供了强大灵活的断言
    * [assertpy](https://github.com/ActivisionGameScience/assertpy) - 巨简单的python单元测试断言库，提供了优雅流利的API. 支持Python 2 和 3.
- Mocking
    * [mock](https://pypi.python.org/pypi/mock) - python实现的Mocking和Patching库
    * [Ludibrio](http://github.com/nsigustavo/ludibrio/) - 用python实现的优雅的test doubles框架(mocks, stubs, spy, and dummies).
    * [responses](https://github.com/dropbox/responses) - mock请求的 Python测试工具库
    * [doublex](https://pypi.python.org/pypi/doublex) - 强大的 test doubles 框架
    * [freezegun](https://github.com/spulec/freezegun) - 通过mocking datetime模块实现时光穿梭
    * [httpretty](http://falcao.it/HTTPretty/) - HTTP请求的mock工具
    * [httmock](https://github.com/patrys/httmock) - requests的mock工具，支持Python 2.6+ and 3.2+.
    * [pretenders](https://github.com/pretenders/pretenders) - 测试用的fake server
    * [mock-server](https://github.com/tomashanacek/mock-server) - 简单的mock sever，支持REST and XML-RPC API，还有基于tornado的管理界面
    * [VCR.py](https://github.com/kevin1024/vcrpy) - 自动 mock HTTP 交互 让测试更简单快速





原始封面

![课程图片](https://images.unsplash.com/photo-1534398079543-7ae6d016b86a?w=300)

