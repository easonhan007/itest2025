---
weight: 5
title: Android测试（五）：Instrumented 单元测试
date: '2017-12-20T14:35:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1487243528516-7fa712e910f4?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---



原文：https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html

Instrumented 单元测试是在真机和模拟器上运行的测试，它可以利用Android框架API和支持的API（如Android测试支持库）。如果你的测试需要访问工具信息（例如目标应用程序的`Context`），或者需要真正实现Android框架组件（如`Parcelable`或`SharedPreferences`对象），则应该创建Instrumented 单元测试。

使用Instrumented单元测试还有助于减少编写和维护mock代码所需的工作量。 如果你愿意，仍然可以自由地使用一个mock框架模拟任何依赖关系。

#### 设置测试环境
---
在你的Android Studio项目中，你必须将mock测试的源文件存储在module-name/src/androidTest/java/ 中。 创建新项目时该目录已经存在，并包含示例代码。

在开始之前，你应该下载Android测试支持库安装程序，该安装程序提供的API可让你快速构建和运行应用程序的检测代码。测试支持库包括用于功能性UI测试（Espresso和UI Automator）的JUnit 4测试运行器（AndroidJUnitRunner）和API。

还需要为项目配置Android测试依赖项，以使用测试运行程序和测试支持库提供的规则API。 为了简化测试开发，还应该包含Hamcrest库，它可以让你使用Hamcrest匹配器API创建更灵活的断言。

在你的App的顶级build.gradle文件中将这些库指定为依赖项：

```Java
dependencies {
    androidTestCompile 'com.android.support:support-annotations:24.0.0'
    androidTestCompile 'com.android.support.test:runner:0.5'
    androidTestCompile 'com.android.support.test:rules:0.5'
    // Optional -- Hamcrest library
    androidTestCompile 'org.hamcrest:hamcrest-library:1.3'
    // Optional -- UI testing with Espresso
    androidTestCompile 'com.android.support.test.espresso:espresso-core:2.2.2'
    // Optional -- UI testing with UI Automator
    androidTestCompile 'com.android.support.test.uiautomator:uiautomator-v18:2.1.2'
}
```

__警告：__ 如果构建配置包含support-annotations库的编译依赖项和espresso-core库的androidTestCompile依赖项，则由于依赖冲突，构建可能会失败。 请按照下面步骤更新对espresso-core的依赖关系：

```Java
androidTestCompile('com.android.support.test.espresso:espresso-core:2.2.2', {
    exclude group: 'com.android.support', module: 'support-annotations'
})
```

要使用JUnit 4测试类，请确保将AndroidJUnitRunner指定为项目中的默认测试工具运行器，方法是在应用程序的模块级build.gradle文件中包含以下设置：

```Java
android {
    defaultConfig {
        testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
    }
}
```

#### 创建一个Instrumented的单元测试类
---

你的Instrumented单元测试类应该写成JUnit 4测试类。要了解有关创建JUnit 4测试类和使用JUnit 4断言和注释的更多信息，请参阅创建本地单元测试类。

要创建一个Instrumented的JUnit 4测试类，在测试类定义的开头添加@RunWith（AndroidJUnit4.class）注释。 还需要将Android测试支持库中提供的AndroidJUnitRunner类指定为默认测试运行器。测试入门中对此步骤进行了更详细的介绍。

以下示例显示如何编写一个Instrumented单元测试，以确保LogHistory类正确实现了Parcelable接口：

```Java
import android.os.Parcel;
import android.support.test.runner.AndroidJUnit4;
import android.util.Pair;
import org.junit.Test;
import org.junit.runner.RunWith;
import java.util.List;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

@RunWith(AndroidJUnit4.class)
@SmallTest
public class LogHistoryAndroidUnitTest {

    public static final String TEST_STRING = "This is a string";
    public static final long TEST_LONG = 12345678L;
    private LogHistory mLogHistory;

    @Before
    public void createLogHistory() {
        mLogHistory = new LogHistory();
    }

    @Test
    public void logHistory_ParcelableWriteRead() {
        // Set up the Parcelable object to send and receive.
        mLogHistory.addEntry(TEST_STRING, TEST_LONG);

        // Write the data.
        Parcel parcel = Parcel.obtain();
        mLogHistory.writeToParcel(parcel, mLogHistory.describeContents());

        // After you're done with writing, you need to reset the parcel for reading.
        parcel.setDataPosition(0);

        // Read the data.
        LogHistory createdFromParcel = LogHistory.CREATOR.createFromParcel(parcel);
        List<Pair<String, Long>> createdFromParcelData = createdFromParcel.getData();

        // Verify that the received data is correct.
        assertThat(createdFromParcelData.size(), is(1));
        assertThat(createdFromParcelData.get(0).first, is(TEST_STRING));
        assertThat(createdFromParcelData.get(0).second, is(TEST_LONG));
    }
}
```

#### 创建一个测试套件
---

要组织测试单元测试的执行，可以将一组测试集合在一个测试套件类中，并将这些测试一起运行。测试套件可以嵌套; 测试套件可以将其他测试套件分组，并将所有组件测试类一起运行。

测试套件包含在测试包中，类似于主应用程序包。按照惯例，测试套件包名通常以`.suite`后缀结尾（例如，`com.example.android.testing.mysample.suite`）。

以下示例显示了如何实现名为`UnitTestSuite`的测试套件，该测试套件将`CalculatorInstrumentationTest`和`CalculatorAddParameterizedTest`测试类分组并运行在一起。

```
import com.example.android.testing.mysample.CalculatorAddParameterizedTest;
import com.example.android.testing.mysample.CalculatorInstrumentationTest;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

// Runs all unit tests.
@RunWith(Suite.class)
@Suite.SuiteClasses({CalculatorInstrumentationTest.class,
        CalculatorAddParameterizedTest.class})
public class UnitTestSuite {}

```

#### 运行Instrumented单元测试
---
要运行Instrumented测试，请遵循以下步骤:

1、通过单击工具栏中的“Sync Project”，确保您的项目与Gradle同步。。

2、以下列其中一种方式运行测试：

* 要运行单个测试请打开Project窗口，然后单击“Run”。
* 要测试类中的所有方法，请右键单击测试文件中的类或方法，然后单击“Run”。
* 要在目录中运行所有测试，请右键单击该目录并选择“Run Tests”。

Gradle的Android插件编译位于默认目录（src/androidTest/java/）中的测试代码，构建测试APK和生产APK，在连接的真机或模拟器上安装两个APK，并运行测试。Android Studio然后在“Run”窗口中显示测试执行结果。

> 注意:在运行或调试测试工具时，Android Studio不会为即时运行注入所需的额外方法，并关闭该特性。

#### 使用Firebase测试实验室运行测试
---
略....  

(请查看原文)


#### 额外的示例代码
---
要下载到示例应用程序，请参阅[Android ActivityInstrumentation Sample](https://github.com/googlesamples/android-ActivityInstrumentation/)。




原始封面

![课程图片](https://images.unsplash.com/photo-1487243528516-7fa712e910f4?w=300)

