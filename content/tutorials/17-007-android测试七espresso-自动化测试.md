---
weight: 7
title: Android测试（七）：Espresso 自动化测试
date: '2017-12-20T14:25:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1618927377242-d9640397483a?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---



原文：https://developer.android.com/training/testing/ui-testing/espresso-testing.html

在单个应用程序中测试用户交互有助于确保用户在与应用程序进行交互时不会遇到意外的结果，或遇到糟糕的体验。 如果需要验证应用的UI功能是否正常，则应该养成创建用户界面（UI）测试的习惯。

Espresso 测试框架，由Android测试支持库提供，用于编写UI测试的API来模拟单个应用程序内的用户交互。Espresso测试可以在运行Android 2.3.3（API等级10）及更高版本的设备上运行。 使用Espresso的一个关键好处是，它提供了测试操作与正在测试的应用程序的用户界面的自动同步。 Espresso检测主线程是否处于空闲状态，以便能够在适当的时候运行测试命令，从而提高测试的可靠性。此功能还可以减轻在测试代码中添加任何计时变通方法如`Thread.sleep（）` 的麻烦。

Espresso测试框架基于instrumentation的API，并通过AndroidJUnitRunner运行测试。

### 设置Espresso
----
在使用Espresso构建UI测试之前，请确保配置测试源代码位置和项目依赖关系，如“ [Getting Started with Testing](http://www.testclass.net/android/fundamentals/)”中所述。

在Android应用程序模块的build.gradle文件中，必须设置对Espresso库的依赖关系引用：

```Java
dependencies {
    // Other dependencies ...
    androidTestCompile 'com.android.support.test.espresso:espresso-core:2.2.2'
}
```

关闭测试设备上的动画 - 在测试设备中打开系统动画可能会导致意外的结果，或者可能导致测试失败。 通过打开“开发人员”选项关闭“设置”中的动画，并关闭以下所有选项：

* 窗口动画比例

* 过渡动画比例

* 动画师持续时间比例

如果你希望将项目设置为使用核心API提供的Espresso功能以外的功能，请参阅[此资源](https://developer.android.com/training/testing/espresso/index.html)


### 创建一个Espresso 测试
---

要创建Espresso测试，请创建遵循此编程模型的Java类：

1.找到想要在活动中测试的UI组件(例如，应用程序中的登录按钮)，调用onView()方法，或者调用AdapterView控件的onData()方法。

2.通过调用ViewInteraction.perform（）或DataInteraction.perform（）方法并传入用户操作（例如，单击登录按钮），模拟特定的用户交互以在该UI组件上执行。 要在同一UI组件上对多个操作进行排序，请使用方法参数中的逗号分隔列表链接它们。

3.根据需要重复上述步骤，模拟目标应用中多个活动的用户操作。

4.在执行这些用户交互之后，使用`ViewAssertions`方法来检查UI是否反映了期望的状态或行为。

以下各节将详细介绍这些步骤。

下面的代码片段显示了你的测试类可能如何调用这个基本的工作流程：

```java

onView(withId(R.id.my_view))            // withId(R.id.my_view) is a ViewMatcher
        .perform(click())               // click() is a ViewAction
        .check(matches(isDisplayed())); // matches(isDisplayed()) is a ViewAssertion

```

### 使用Espresso和ActivityTestRule
---

以下部分介绍如何使用JUnit 4样式创建新的Espresso测试，并使用ActivityTestRule来减少需要编写的样板代码的数量。 通过使用ActivityTestRule，测试框架在每个使用`@Test`注释的测试方法之前以及在使用`@Before`注释的方法之前启动被测活动。测试完成后，框架处理关闭活动，所有使用`@After`注释的方法都会运行。

```java
package com.example.android.testing.espresso.BasicSample;

import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;
...

@RunWith(AndroidJUnit4.class)
@LargeTest
public class ChangeTextBehaviorTest {

    private String mStringToBetyped;

    @Rule
    public ActivityTestRule<MainActivity> mActivityRule = new ActivityTestRule<>(
            MainActivity.class);

    @Before
    public void initValidString() {
        // Specify a valid string.
        mStringToBetyped = "Espresso";
    }

    @Test
    public void changeText_sameActivity() {
        // Type text and then press the button.
        onView(withId(R.id.editTextUserInput))
                .perform(typeText(mStringToBetyped), closeSoftKeyboard());
        onView(withId(R.id.changeTextBt)).perform(click());

        // Check that the text was changed.
        onView(withId(R.id.textToBeChanged))
                .check(matches(withText(mStringToBetyped)));
    }
}
```

### 访问UI组建
---
在Espresso可以与被测试的应用程序进行交互之前，必须先指定UI组件或视图。Espresso支持使用[Hamcrest 匹配器](http://hamcrest.org/)在应用程序中指定视图和适配器。

要查找视图，请调用`onView（）`方法并传递一个视图匹配器，该视图匹配器指定要定位的视图。 这在指定视图匹配器中有更详细的描述。 `onView（）`方法返回`ViewInteraction`对象，允许测试与视图进行交互。 但是，如果要在`RecyclerView`布局中查找视图，则调用`onView（）`方法可能不起作用。 在这种情况下，请按照在AdapterView中查找视图中的说明进行操作。

> 注意:onView()方法不检查你指定的视图是否有效。相反，Espresso只搜索当前的视图层次结构，使用matcher提供的视图。如果没有找到匹配，该方法将抛出一个NoMatchingViewException。

下面的代码片段展示了如何编写一个测试来访问EditText字段，输入一个文本字符串，关闭虚拟键盘，然后执行按钮单击。
```Java
public void testChangeText_sameActivity() {
    // Type text and then press the button.
    onView(withId(R.id.editTextUserInput))
            .perform(typeText(STRING_TO_BE_TYPED), closeSoftKeyboard());
    onView(withId(R.id.changeTextButton)).perform(click());

    // Check that the text was changed.
    ...
}
```

##### 指定一个视图匹配器
---
您可以使用以下方法指定视图匹配器：

* 在ViewMatchers类中调用方法。 例如，要查找显示的文本字符串来查找视图，可以调用如下所示的方法：

```java
onView(withText("Sign-in"));
```

也可以调用withId（）并提供视图的资源ID（R.id），如下例所示：
```java
onView(withId(R.id.button_signin));
```
Android资源ID不保证是唯一的。 如果测试尝试匹配多个视图使用的资源ID，则Espresso会引发AmbiguousViewMatcherException。

* 使用Hamcrest [Matchers](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matchers.html)类。可以使用`AllOf（）`方法来组合多个匹配器，例如`containsString（）`和`instanceOf（）`。 这种方法允许更窄地过滤匹配结果，如以下示例所示：

```java
onView(allOf(withId(R.id.button_signin), withText("Sign-in")));
```

但是，不能使用关键字来筛选不匹配匹配器的视图，如以下示例所示：

```java
onView(allOf(withId(R.id.button_signin), not(withText("Sign-out"))));
```

要在测试中使用这些方法，请导入`org.hamcrest.Matchers`包。 要了解有关Hamcrest匹配的更多信息，请参阅Hamcrest网站

要改善Espresso测试的性能，请指定查找目标视图所需的最低匹配信息。例如，如果某个视图可以通过其描述性文本唯一标识，则不需要指定它也可以从TextView实例分配。

##### 在AdapterView中查找视图

在AdapterView小部件中，视图在运行时动态填充子视图。 如果要测试的目标视图位于AdapterView中（如ListView，GridView或Spinner），则`onView（）`方法可能无法正常工作，因为只有视图的子集可能会加载到当前视图层次结构中。

相反，调用`onData（）`方法来获取DataInteraction对象来访问目标视图元素。 Espresso将目标视图元素加载到当前视图层次结构中。 Espresso还负责滚动目标元素，并将元素放在焦点上。

> 注意：onData（）方法不会检查你指定的项目是否与视图对应。Espresso只搜索当前的视图层次结构。如果找不到匹配，则该方法将引发NoMatchingViewException。

以下代码片段显示了如何使用`onData（）`方法和Hamcrest匹配一起搜索包含给定字符串的列表中的特定行。 在此示例中，LongListActivity类包含通过SimpleAdapter公开的字符串列表。
```java
onData(allOf(is(instanceOf(Map.class)),
        hasEntry(equalTo(LongListActivity.ROW_TEXT), is("test input")));
```

### 执行操作
---
调用 `ViewInteraction.perform（）` 或 `DataInteraction.perform（）` 方法来模拟UI组件上的用户交互。 您必须传入一个或多个ViewAction对象作为参数。 Espresso根据给定的顺序依次触发每个动作，并在主线程中执行它们。

ViewActions类提供了用于指定常用操作的帮助程序方法列表。 可以使用这些方法作为方便的快捷方式，而不是创建和配置单独的ViewAction对象。 你可以指定如下操作：

* ViewActions.click（）：点击视图。

* ViewActions.typeText（）：点击一个视图并输入一个指定的字符串。

* ViewActions.scrollTo（）：滚动到视图。 目标视图必须从ScrollView继承，其android：visibility属性的值必须是可见的。 对于扩展AdapterView的视图（例如，ListView），onData（）方法负责为您滚动。

* ViewActions.pressKey（）：使用指定的键码进行按键操作。

* ViewActions.clearText（）：清除目标视图中的文本。

如果目标视图位于ScrollView的内部，则先执行`ViewActions.scrollTo（）`操作，然后再执行其他操作。 如果已经显示视图，则`ViewActions.scrollTo（）`操作将不起作用。

### 用Espresso Intents隔离测试你的活动
---
Espresso Intents可以验证应用程序发送的意图的验证和存根。 通过Espresso Intents，可以通过拦截传出的意图，对结果进行存根并将其发送回被测组件来隔离测试应用程序，活动或服务。

```java
dependencies {
  // Other dependencies ...
  androidTestCompile 'com.android.support.test.espresso:espresso-intents:2.2.2'
}
```

为了测试一个intent，你需要创建一个IntentsTestRule类的实例，它与ActivityTestRule类非常相似。 IntentsTestRule类在每次测试之前初始化Espresso Intents，终止主活动，并在每次测试后释放Espresso Intents。

以下代码片段中显示的测试类为明确的意图提供了一个简单的测试。 它测试建立你的第一个应用程序教程中创建的活动和意图。

```Java
@Large
@RunWith(AndroidJUnit4.class)
public class SimpleIntentTest {

    private static final String MESSAGE = "This is a test";
    private static final String PACKAGE_NAME = "com.example.myfirstapp";

    /* Instantiate an IntentsTestRule object. */
    @Rule
    public IntentsTestRule≶MainActivity> mIntentsRule =
      new IntentsTestRule≶>(MainActivity.class);

    @Test
    public void verifyMessageSentToMessageActivity() {

        // Types a message into a EditText element.
        onView(withId(R.id.edit_message))
                .perform(typeText(MESSAGE), closeSoftKeyboard());

        // Clicks a button to send the message to another
        // activity through an explicit intent.
        onView(withId(R.id.send_message)).perform(click());

        // Verifies that the DisplayMessageActivity received an intent
        // with the correct package name and message.
        intended(allOf(
                hasComponent(hasShortClassName(".DisplayMessageActivity")),
                toPackage(PACKAGE_NAME),
                hasExtra(MainActivity.EXTRA_MESSAGE, MESSAGE)));

    }
}
```

有关 Espresso Intents的更多信息，请参阅Android测试支持库网站上的Espresso Intent文档。 您还可以下载IntentsBasicSample和IntentsAdvancedSample代码示例。

### 用Espresso Web测试WebViews
---
Espresso Web允许测试活动中包含的WebView组件。 它使用WebDriver API来检查和控制WebView的行为。

要开始使用Espresso Web进行测试，需要将以下行添加到应用程序的build.gradle文件中：

```java
dependencies {
  // Other dependencies ...
  androidTestCompile 'com.android.support.test.espresso:espresso-web:2.2.2'
}
```

使用Espresso Web创建测试时，需要在实例化ActivityTestRule对象以测试活动时在WebView上启用JavaScript。 在测试中，可以选择显示在WebView中的HTML元素，并模拟用户交互，例如在文本框中输入文本，然后单击按钮。在完成操作后，你可以验证网页上的结果是否符合预期结果。

在以下代码片段中，这个类测试一个WebView组件，该组件的id值“WebView”在被测试的活动中。 `verifyValidInputYieldsSuccesfulSubmission（）`测试选择网页上的`<input>`元素，输入一些文本，并检查出现在另一个元素中的文本。

```java
@LargeTest
@RunWith(AndroidJUnit4.class)
public class WebViewActivityTest {

    private static final String MACCHIATO = "Macchiato";
    private static final String DOPPIO = "Doppio";

    @Rule
    public ActivityTestRule mActivityRule =
        new ActivityTestRule(WebViewActivity.class,
            false /* Initial touch mode */, false /*  launch activity */) {

        @Override
        protected void afterActivityLaunched() {
            // Enable JavaScript.
            onWebView().forceJavascriptEnabled();
        }
    }

    @Test
    public void typeTextInInput_clickButton_SubmitsForm() {
       // Lazily launch the Activity with a custom start Intent per test
       mActivityRule.launchActivity(withWebFormIntent());

       // Selects the WebView in your layout.
       // If you have multiple WebViews you can also use a
       // matcher to select a given WebView, onWebView(withId(R.id.web_view)).
       onWebView()
           // Find the input element by ID
           .withElement(findElement(Locator.ID, "text_input"))
           // Clear previous input
           .perform(clearElement())
           // Enter text into the input element
           .perform(DriverAtoms.webKeys(MACCHIATO))
           // Find the submit button
           .withElement(findElement(Locator.ID, "submitBtn"))
           // Simulate a click via JavaScript
           .perform(webClick())
           // Find the response element by ID
           .withElement(findElement(Locator.ID, "response"))
           // Verify that the response page contains the entered text
           .check(webMatches(getText(), containsString(MACCHIATO)));
    }
}

```

有关Espresso Web的更多信息，请参阅Android测试支持库网站上的Espresso Web文档。您也可以将此代码段作为Espresso Web代码示例的一部分下载。

### 验证结果
---
调用`ViewInteraction.check（）`或`DataInteraction.check（）`方法来声明UI中的视图匹配某个预期的状态。 必须传递给ViewAssertion对象作为参数。如果断言失败，Espresso将抛出一个AssertionFailedError。

ViewAssertions类提供了用于指定公共断言的帮助器方法列表。 你可以使用的断言包括：

* doesNotExist：断言当前视图层次结构中没有与指定条件匹配的视图。

* matches：断言指定的视图存在于当前的视图层次结构中，并且其状态匹配给定的Hamcrest匹配器。

* selectedDescendentsMatch：声明指定的父视图的子视图存在，并且它们的状态匹配给定的Hamcrest匹配器。

以下代码片段显示如何检查用户界面中显示的文本与先前在EditText字段中输入的文本具有相同的值。

```java
public void testChangeText_sameActivity() {
    // Type text and then press the button.
    ...

    // Check that the text was changed.
    onView(withId(R.id.textToBeChanged))
            .check(matches(withText(STRING_TO_BE_TYPED)));
}
```

### 在设备或模拟器上运行Espresso测试 
---

你可以从Android Studio或从命令行运行Espresso测试。 确保将AndroidJUnitRunner指定为项目中的默认检测工具。

要运行Espresso测试，请按照前面章节介绍的步骤运行已测试的测试。




原始封面

![课程图片](https://images.unsplash.com/photo-1618927377242-d9640397483a?w=300)

