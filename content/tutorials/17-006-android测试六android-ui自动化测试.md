---
weight: 6
title: Android测试（六）：Android UI自动化测试
date: '2017-12-20T14:30:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1677727853667-86855f1ce0eb?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---




原文：https://developer.android.com/training/testing/ui-testing/index.html

用户界面（UI）测试可以确保你的应用程序满足其功能要求，并达到用户最可能成功采用的高质量标准。

UI测试的一种方法是简单地让人类测试人员在目标应用程序上执行一组用户操作，并验证其行为是否正确。 但是，这种手动方法可能耗时、乏味、且容易出错。更有效的方法是编写您的UI测试，以便用户操作以自动方式执行。 自动化方法使您能够以可重复的方式快速可靠地运行测试。

> 注意：强烈建议您使用Android Studio来构建测试应用程序，因为它提供了项目设置，包含库和包非常方便。 这个里假定你正在使用Android Studio。

要使用Android Studio自动执行UI测试，请在单独的Android测试文件夹`src/androidTest/java`中实现测试代码。针对Gradle的Android插件将根据你的测试代码构建测试应用程序，然后将测试应用程序加载到与目标应用程序相同的设备上。 在测试代码中，可以使用UI测试框架来模拟目标应用程序上的用户交互，以执行覆盖特定使用场景的测试任务。

为了测试Android应用程序，通常会创建这些类型的UI自动化测试：

__单个应用程序的UI测试：__ 这种类型的测试验证当用户执行特定操作或在其活动中输入特定内容时，目标验证应用程序的行为是否符合预期。它允许你检查目标应用程序是否返回正确的UI输出，以响应应用程序活动中的用户交互。像Espresso这样的UI测试框架允许以编程方式模拟用户操作并测试复杂的应用内用户交互。

__跨越多个应用程序的UI测试：__ 这种类型的测试验证不同用户应用程序之间或用户应用程序与系统应用程序之间交互的正确行为。例如，可能想要测试你的相机应用程序与第三方社交媒体应用程序或默认的Android照片应用程序正确共享图像。支持跨应用程序交互的UI测试框架（如UI Automator）允许你为这些方案创建测试。

本课的经验将告诉你如何使用Android测试支持库中的工具和API来构建这些类型的自动化测试。 在开始使用这些API构建测试之前，你必须安装Android测试支持库，如下载Android测试支持库中所述。


#### 课程
---

[Testing UI for a Single App](https://developer.android.com/training/testing/ui-testing/espresso-testing.html)（单个应用程序的UI测试）

* 了解如何使用Espresso测试框架在单个应用程序中测试UI。

[Testing UI for Multiple Apps](https://developer.android.com/training/testing/ui-testing/uiautomator-testing.html) （多个应用程序的UI测试）

* 了解如何使用UI Automator测试框架在多个应用程序中测试UI。




原始封面

![课程图片](https://images.unsplash.com/photo-1677727853667-86855f1ce0eb?w=300)

