---
weight: 1
title: Android测试（一）：在Android中测试App
date: '2017-12-20T14:55:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---



原文：https://developer.android.com/training/testing/index.html

__测试你的App是开发过程中的重要组成部分。通过对应用程序持续的运行测试，你可以验证程序的正确性、功能和可用在发布之前。__

测试还提供了以下优点：

* 快速反馈失败。
* 开发周期的早期问题检测。
* 安全地重构代码，让你优化代码而不用担心回归。
* 稳定开发速度，帮助你减少技术债务。

这里的特指测试通过代码实现的“单元”测试。所以，它可以更早、更快的帮我们发现问题，使我们的代码重构更有信心；单元测试虽然前期编写会比较耗时，但是它可以有效的代码的质量，不会导致项目后期代码充满坏味道，严重拖慢开发进度；所以，减少你技术债务。

### 资源
---

在Android测试库、Android平台和开源社区都提供了帮助你编写Android应用测试的工具：


![](http://img.testclass.net/android_testing_app.png)


#### Espesso
---
Espresso是android应用开发自带测试库。他是一款白盒风格的UI测试工具。UI测试就都是黑盒的么？为什么会是白盒风格。

说白盒是因为，通过Espresso编写测试调用Android控件的方式和 Android开发中是一样的。
来看一段Android开发中，Activity中编写的代码。

```java
/** Called when the user clicks the Send button */
public void sendMessage(View view) {
    // Do something in response to button
    Intent intent = new Intent(this, DisplayMessageActivity.class);
    EditText editText = (EditText) findViewById(R.id.edit_message);
    String message = editText.getText().toString();
    intent.putExtra(EXTRA_MESSAGE, message);
    startActivity(intent);
}
```

通过 `R.id.edit_message` 调用布局文件中输入框中的内容，并转交到另外一个Activity处理。

再来看一段 Espesso 的测试代码：

```java
@Test
public void InputEditCase() throws InterruptedException{

    onView(withId(R.id.edit_message)).perform(typeText(STRING_TO_BE_TYPED));
    onView(withId(R.id.send_button)).perform(click());

    onView(withId(R.id.display_message)).check(matches(isDisplayed()));
    onView(withId(R.id.display_message)).check(matches(withText("hello," +STRING_TO_BE_TYPED)));
}
```

同样使用的是 `R.id.edit_message`  的定位方式来查找控件，是不是白盒？我们通常的黑盒UI自动化测试是通过UI属性查看工具（如：UIAutomatorViewer）确定元素的属性来进行定位的。Espesso不需要，你看代码就好了，准确点是看Android的布局文件的控件定义。

但是，Espesso的运行是基于 SDK 的，所以，要想运行一条用例必须在Android模拟器（或真机）上安装App，启动App，然后基于UI的操作来运行测试用例。


#### Robolectric
---

Robolectric是一款第三方的开源的Android单元测试框架。运行在JVM上，所以它运行速度上会比 Espesso快上很多。

```java
@RunWith(RobolectricTestRunner.class)
public class MyActivityTest {

    @Test
    public void clickingButton_shouldChangeResultsViewText() throws Exception {
        MyActivity activity = Robolectric.setupActivity(MyActivity.class);

        Button button = (Button) activity.findViewById(R.id.button);
        TextView results = (TextView) activity.findViewById(R.id.results);

        button.performClick();
        assertThat(results.getText().toString()).isEqualTo("Robolectric Rocks!");
    }
}
```

来一段官方Demo，robolectric的做法是通过实现一套JVM能运行的Android代码，然后在单元测试运行的时候去截取android相关的代码调用，然后转到他们的他们实现的代码去执行这个调用的过程。

你不明白原理也没关系，反正知道Robolectric的运行不需要你真正的打开App去执行测试，就像运行一段普通的Java代码一样。所以速度上当然就很快了。

#### AndroidJUnitRunner
---

AndroidJUnitRunner本质上不算是个测试工具，它只是Google基于Junit针对Anroid封装的一个测试用例运行器而已。至于它用来运行Espesso还是Uiautomator的用例都是可以的。那Robolectric呢？没看到上面的例子中Robolectric有自己的运行器叫RobolectricTestRunner

```java
@RunWith(AndroidJUnit4.class)
public class MainActiveTest{

   ……

｝
```

如果看到测试类是用 `AndroidJUnit4` 注释的，说明用的就是AndroidJUnitRunner运行器的。

#### 测试应用
---

最后，更好的编写测试用例的平台，当然是Google家的亲儿子了。器大活好不粘人！（现在才发现不是去幼儿园的车，晚了，把车门给我捍死，一个都不准下车。）

Android Studio 以简化测试为设计宗旨。 您只需完成几次点击，便可建立一个在本地 JVM 上运行的 JUnit 测试，或建立一个在设备上运行的仪器测试。

当然，您也可以通过集成测试框架来扩展测试能力，例如可以集成 Mockito 在本地单元测试中测试 Android API 调用，以及集成 Espresso 或 UI Automator 在仪器测试中演练用户交互。
您可以利用 Espresso 测试记录器自动生成 Espresso 测试。




原始封面

![课程图片](https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?w=300)

