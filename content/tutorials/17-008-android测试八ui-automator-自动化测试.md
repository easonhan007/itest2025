---
weight: 8
title: Android测试（八）：UI Automator 自动化测试
date: '2017-12-20T14:20:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1703669020950-280d316e72aa?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---



原文：https://developer.android.com/training/testing/ui-testing/uiautomator-testing.html

涉及跨多个应用程序的用户交互的用户界面（UI）测试可以验证应用程序在用户流量跨越其他应用程序或进入系统UI时的行为。 这种用户流程的一个例子是一个消息应用程序，它允许用户输入文本消息，启动Android联系人选择器，以便用户可以选择收件人发送消息，然后将控制权返回给用户的原始应用程序并提交消息。

这一小节介绍如何使用Android测试支持库提供的UI Automator测试框架编写此类UI测试。 UI Automator API可让你与设备上的可见元素进行交互，而不管哪个Activity处于焦点。你的测试可以使用方便的描述符（如该组件中显示的文本或其内容描述）查找UI组件。 UI Automator测试可以在运行Android 4.3（API级别18）或更高版本的设备上运行。

UI Automator测试框架是基于 instrumentation的API，并与AndroidJUnitRunner测试运行器一起使用。

### 设置UI Automator
---

在使用UI Automator构建UI测试之前，请确保配置测试源代码位置和项目依赖关系，如前面章节中所述。

在Android应用程序模块的build.gradle文件中，必须设置对UI Automator库的依赖关系引用：

```java
dependencies {
    ...
    androidTestCompile 'com.android.support.test.uiautomator:uiautomator-v18:2.1.1'
}
```

为了优化您的UI Automator测试，您应该首先检查目标应用程序的UI组件，并确保它们可以访问。 这些优化技巧将在下面两节中介绍。

#### 查看设备上的UI


在设计您的测试之前，检查设备上可见的UI组件。 为确保您的UI Automator测试可以访问这些组件，请检查这些组件是否具有可见的文本标签、`android:contentDescription` 值。

uiautomatorviewer工具提供了一个方便的可视化界面来检查布局层次结构，并查看设备前台中可见的UI组件的属性。这个信息可以让你使用UI Automator创建更细致的测试。例如，可以创建一个匹配特定可见属性的UI选择器。

启动uiautomatorviewer工具：

1.在物理设备上启动目标应用程序。

2.将设备连接到你的开发机器。

3.打开终端窗口并导航到`<android-sdk> / tools /`目录。

4.使用以下命令运行该工具：

```
$ uiautomatorviewer
```

要查看您的应用程序的UI属性：

1.在uiautomatorviewer界面中，点击 __Device Screensho__ 按钮。

2.将鼠标悬停在左侧面板中的快照上，查看由uiautomatorviewer工具标识的UI组件。 属性列在右下方的面板中，右上方的布局层次中列出。

3.或者，单击 __Toggle NAF Nodes__ 按钮以查看UI Automator无法访问的UI组件。 这些组件只有有限的信息可用。


#### 确保你的Activity是可访问的

UI Automator测试框架对已实施Android辅助功能的应用程序执行得更好。当你使用View类型的UI元素或SDK或Support Library中的View的子类时，不需要实现可访问性支持，因为这些类已经为你完成了。

但是，有些应用程序使用自定义UI元素来提供更丰富的用户体验。 这些元素不会提供自动的可访问性支持。如果你的应用程序包含不是来自SDK或支持库的View子类的实例，请确保通过完成以下步骤将可访问性功能添加到这些元素：

1.创建一个扩展`ExploreByTouchHelper`的具体类。

2.通过调用`setAccessibilityDelegate（）`将新类的实例与特定的自定义UI元素相关联。

有关将辅助功能添加到自定义视图元素的其他指导，请参阅构建可访问自定义视图要详细了解Android上可访问性的一般最佳实践，请参阅使应用程序更易于访问。

### 创建一个UI Automator测试类
---

UI Automator测试类应该像JUnit 4测试类一样编写。 要了解有关创建JUnit 4测试类和使用JUnit 4断言和注释的更多信息，请参阅创建测试单元测试类。

在测试类定义的开始处添加`@RunWith（AndroidJUnit4.class）`注释。 还需要将Android测试支持库中提供的AndroidJUnitRunner类指定为您的默认测试运行器。 在设备或模拟器上运行UI Automator测试中将更详细地描述此步骤。

在UI Automator测试类中实现以下编程模型：

1.通过调用`getInstance（）`方法并传递一个Instrumentation对象作为参数，获取一个`UiDevice`对象来访问要测试的设备。

2.通过调用`findObject（）`方法，获取`UiObject`对象以访问设备上显示的UI组件（例如前景中的当前视图）。

3.通过调用`UiObject`方法来模拟特定的用户交互以在该UI组件上执行; 例如，调用`performMultiPointerGesture（）`来模拟多点触摸手势，`setText（）`来编辑文本字段。你可以根据需要重复调用步骤2和3中的API，以测试涉及多个UI组件或用户操作序列的更复杂的用户交互。

4.在执行这些用户交互之后，检查UI是否反映了预期的状态或行为。

以下各节将详细介绍这些步骤。

##### 访问UI组件

UiDevice对象是访问和操作设备状态的主要方式。在测试中调用`UiDevice`方法来检查各种属性的状态，例如当前方向或显示大小。 可以使用`UiDevice`对象执行设备级别的操作，例如强制设备进入特定的旋转状态，按下D-pad硬件按钮，然后按Home（主页）和Menu（菜单）按钮。

从设备的主屏幕开始测试是一种很好的做法。从主屏幕（或在设备中选择的其他位置），你可以调用UI Automator API提供的方法来选择特定的UI元素并与之交互。

下面的代码片段显示了测试如何得到一个`UiDevice`的实例，并模拟按下一个主页按钮：

```java
import org.junit.Before;
import android.support.test.runner.AndroidJUnit4;
import android.support.test.uiautomator.UiDevice;
import android.support.test.uiautomator.By;
import android.support.test.uiautomator.Until;
...

@RunWith(AndroidJUnit4.class)
@SdkSuppress(minSdkVersion = 18)
public class ChangeTextBehaviorTest {

    private static final String BASIC_SAMPLE_PACKAGE
            = "com.example.android.testing.uiautomator.BasicSample";
    private static final int LAUNCH_TIMEOUT = 5000;
    private static final String STRING_TO_BE_TYPED = "UiAutomator";
    private UiDevice mDevice;

    @Before
    public void startMainActivityFromHomeScreen() {
        // Initialize UiDevice instance
        mDevice = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());

        // Start from the home screen
        mDevice.pressHome();

        // Wait for launcher
        final String launcherPackage = mDevice.getLauncherPackageName();
        assertThat(launcherPackage, notNullValue());
        mDevice.wait(Until.hasObject(By.pkg(launcherPackage).depth(0)),
                LAUNCH_TIMEOUT);

        // Launch the app
        Context context = InstrumentationRegistry.getContext();
        final Intent intent = context.getPackageManager()
                .getLaunchIntentForPackage(BASIC_SAMPLE_PACKAGE);
        // Clear out any previous instances
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
        context.startActivity(intent);

        // Wait for the app to appear
        mDevice.wait(Until.hasObject(By.pkg(BASIC_SAMPLE_PACKAGE).depth(0)),
                LAUNCH_TIMEOUT);
    }
}
```

在示例中，`@SdkSuppress（minSdkVersion = 18）`语句有助于确保测试只能在Android 4.3（API级别18）或更高级别的设备上运行，正如UI Automator框架所要求的那样。

使用`findObject（）`方法来检索一个`UiObject`，它表示一个匹配给定选择器条件的视图。根据需要重复使用在应用程序测试的其他部分创建的`UIObject`实例。 请注意，每次测试使用UiObject实例单击UI元素或查询属性时，UI Automator测试框架都会在当前显示中搜索匹配项。

以下片段显示了测试如何构建表示应用程序中的“取消”按钮和“确定”按钮的`UIObject`实例。

```java
UiObject cancelButton = mDevice.findObject(new UiSelector()
        .text("Cancel"))
        .className("android.widget.Button"));
UiObject okButton = mDevice.findObject(new UiSelector()
        .text("OK"))
        .className("android.widget.Button"));

// Simulate a user-click on the OK button, if found.
if(okButton.exists() && okButton.isEnabled()) {
    okButton.click();
}
```

##### 指定选择器

如果要访问应用程序中的特定UI组件，请使用`UiSelector`类。 这个类表示对当前显示的UI中特定元素的查询。

如果找到多个匹配元素，则层次结构中的第一个匹配元素将作为目标`UiObject`返回。 构建`UiSelector`时，可以将多个属性链接在一起以优化搜索。 如果找不到匹配的UI元素，则抛出`UiAutomatorObjectNotFoundException`。

你可以使用`childSelector（）`方法来嵌套多个`UiSelector`实例。 例如，下面的代码示例显示如何测试搜索以在当前显示的UI中查找第一个`ListView`，然后在该`ListView`内搜索以查找具有文本属性Apps的UI元素。

```java
UiObject appItem = new UiObject(new UiSelector()
        .className("android.widget.ListView")
        .instance(0)
        .childSelector(new UiSelector()
        .text("Apps")));
```

最佳做法是，在指定选择器时，应使用资源ID（如果将其分配给UI元素）而不是文本元素或内容描述符。并非所有元素都有文本元素（例如，工具栏中的图标）。文本选择器很脆弱，如果UI发生细微的变化，可能会导致测试失败。他们也可能不能跨越不同的语言; 您的文本选择器可能不匹配翻译的字符串。

在选择器条件中指定对象状态可能很有用。例如，如果要选择所有选中的元素的列表，以便取消选中它们，请使用参数设置为true的`checked（）`方法。

##### 执行操作

一旦你的测试获得了一个`UIObject`对象，可以调用`UIObject`类中的方法在该对象表示的UI组件上执行用户交互。指定如下操作：

* click（）：单击UI元素的可见边界的中心。

* dragTo（）：将此对象拖动到任意坐标。

* setText（）：清除字段内容后，设置可编辑字段中的文本。 相反，clearTextField（）方法会清除可编辑字段中的现有文本。

* swipeUp（）：对UiObject执行滑动操作。 同样，swipeDown（），swipeLeft（）和swipeRight（）方法也会执行相应的操作。

UI Automator测试框架允许您通过`getContext（）`获取Context对象来发送Intent或启动一个Activity，而无需使用shell命令。

以下片段显示了测试如何使用Intent来启动测试中的应用程序。 这种方法是有用的，当你只是在测试计算器应用程序感兴趣，并不关心发射器。

```java
public void setUp() {
    ...

    // Launch a simple calculator app
    Context context = getInstrumentation().getContext();
    Intent intent = context.getPackageManager()
            .getLaunchIntentForPackage(CALC_PACKAGE);
    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
            // Clear out any previous instances
    context.startActivity(intent);
    mDevice.wait(Until.hasObject(By.pkg(CALC_PACKAGE).depth(0)), TIMEOUT);
}
```

##### 对集合执行操作

如果要模拟项目集合（例如，音乐相册中的歌曲或收件箱中的电子邮件列表）上的用户交互，请使用`UiCollection`类。要创建`UiCollection`对象，请指定一个`UiSelector`，用于搜索UI容器或其他子UI元素的包装器，例如包含子UI元素的布局视图。

以下代码片段显示了测试如何构建`UiCollection`来表示在`FrameLayout`中显示的视频专辑：

```java
UiCollection videos = new UiCollection(new UiSelector()
        .className("android.widget.FrameLayout"));

// Retrieve the number of videos in this collection:
int count = videos.getChildCount(new UiSelector()
        .className("android.widget.LinearLayout"));

// Find a specific video and simulate a user-click on it
UiObject video = videos.getChildByText(new UiSelector()
        .className("android.widget.LinearLayout"), "Cute Baby Laughing");
video.click();

// Simulate selecting a checkbox that is associated with the video
UiObject checkBox = video.getChild(new UiSelector()
        .className("android.widget.Checkbox"));
if(!checkBox.isSelected()) checkbox.click();
```

##### 在可滚动视图上执行操作

使用`UiScrollable`类模拟垂直或水平滚动显示。 当UI元素位于屏幕外并且需要滚动以将其显示在视图中时，此技术很有用。

以下代码片段显示了如何模拟向下滚动“Settings ”菜单并点击“About tablet option”：

```java
UiScrollable settingsItem = new UiScrollable(new UiSelector()
        .className("android.widget.ListView"));
UiObject about = settingsItem.getChildByText(new UiSelector()
        .className("android.widget.LinearLayout"), "About tablet");
about.click();
```

##### 验证结果

InstrumentationTestCase扩展了TestCase，因此你可以使用标准的JUnit  `Assert`方法来测试应用程序中的UI组件，以返回预期的结果。

以下片段显示了如何在计算器应用程序中找到几个按钮，然后按顺序点击它们，然后验证是否显示了正确的结果。

```java
private static final String CALC_PACKAGE = "com.myexample.calc";

public void testTwoPlusThreeEqualsFive() {
    // Enter an equation: 2 + 3 = ?
    mDevice.findObject(new UiSelector()
            .packageName(CALC_PACKAGE).resourceId("two")).click();
    mDevice.findObject(new UiSelector()
            .packageName(CALC_PACKAGE).resourceId("plus")).click();
    mDevice.findObject(new UiSelector()
            .packageName(CALC_PACKAGE).resourceId("three")).click();
    mDevice.findObject(new UiSelector()
            .packageName(CALC_PACKAGE).resourceId("equals")).click();

    // Verify the result = 5
    UiObject result = mDevice.findObject(By.res(CALC_PACKAGE, "result"));
    assertEquals("5", result.getText());
}
```

### 在设备或模拟器上运行UI Automator测试
---

你可以从Android Studio或从命令行运行UI Automator测试。 确保将AndroidJUnitRunner指定为项目中的默认检测工具。

要运行UI Automator测试，请按照前面章节中所述的步骤来运行测试。




原始封面

![课程图片](https://images.unsplash.com/photo-1703669020950-280d316e72aa?w=300)

