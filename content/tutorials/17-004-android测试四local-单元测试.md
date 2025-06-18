---
weight: 4
title: Android测试（四）：Local 单元测试
date: '2017-12-20T14:40:12+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1553356084-58ef4a67b2a7?w=300
tags: []
categories:
- Android测试基础教程
lightgallery: true
toc:
  auto: false
---



原文：https://developer.android.com/training/testing/unit-testing/local-unit-tests.html

如果你的单元测试没有依赖或者只有简单的Android依赖，则应该在本地开发机器上运行测试。这种测试方法非常高效，因为它可以帮助你避免每次运行测试时将目标应用程序和单元测试代码加载到真机或模拟器上的开销。因此，运行单元测试的执行时间大大减少了。通过这种方法，你通常使用mock框架（如Mockito）来完成任何依赖关系。

#### 设置测试环境
---
在你的Android Studio项目中，必须将本地单元测试的源文件存储在module-name/src/test/java/ 目录中。在创建新项目时，该目录已经存在。

你还需要配置项目的测试依赖，以使用JUnit 4框架提供的标准API。如果你的测试需要与Android依赖关系进行交互，请包含Mockito库以简化本地单元测试。要了解有关在本地单元测试中使用模拟对象的更多信息，请参阅模拟Android依赖关系。

在你的App程序的目录下找到build.gradle文件中，将这些库指定为依赖项：

```java
dependencies {
    // Required -- JUnit 4 framework
    testCompile 'junit:junit:4.12'
    // Optional -- Mockito framework
    testCompile 'org.mockito:mockito-core:1.10.19'
}
```

#### 创建本地单元测试类
---

你的本地单元测试类应该写成一个JUnit 4测试类。 JUnit是Java最流行和广泛使用的单元测试框架。这个框架的最新版本，JUnit 4，允许你用比前一版本更清晰，更灵活的方式编写测试。与以前的基于JUnit 3的Android单元测试方法（使用JUnit 4）不同，你不需要扩展junit.framework.TestCase类。也不需要在测试方法名称前加上“test”关键字，或者使用junit.framework或junit.extensions包中的任何类。

要创建基本的JUnit 4测试类，请创建一个包含一个或多个测试方法的Java类。 测试方法从`@Test`注释开始，包含代码来练习和验证要测试的组件中的单个功能。

以下示例显示了如何实现本地单元测试类。 测试方法`emailValidator_CorrectEmailSimple_ReturnsTrue`验证被测试的应用程序中的`isValidEmail()`方法是否返回正确的结果。

```Java
import org.junit.Test;
import java.util.regex.Pattern;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class EmailValidatorTest {

    @Test
    public void emailValidator_CorrectEmailSimple_ReturnsTrue() {
        assertThat(EmailValidator.isValidEmail("name@email.com"), is(true));
    }
    ...
}
```
要测试应用程序中的组件是否会返回预期的结果，请使用junit.Assert方法执行验证检查（或断言），以便将待测组件的状态与某个预期值进行比较。 为了使测试更具可读性，可以使用Hamcrest匹配器（如is（）和equalTo（）方法）将返回的结果与期望的结果进行匹配。


#### Mock Android依赖
---
默认情况下，针对Gradle的Android插件将针对android.jar库的修改版本执行本地单元测试，该库不包含任何实际的代码。 相反，从你的单元测试方法调用Android类抛出一个异常。 这是为了确保只测试你的代码，而不依赖于Android平台的任何特定行为（你没有明确地mock）。

你可以使用mock框架在代码中删除外部依赖项，以便以预期的方式轻松测试组件与依赖项的交互。 通过用mock对象代替Android依赖关系，可以将单元测试与Android系统的其余部分分离，同时验证这些依赖关系中正确的方法被调用。Java的Mockito模拟框架（版本1.9.5及更高版本）提供了与Android单元测试的兼容性。借助Mockito可以配置模拟对象以在调用时返回某个特定的值。

要使用此框架将mock对象添加到本地单元测试中，请遵循以下编程模型：

1、在你的 build.gradle 文件中包含Mockito库依赖项，如设置上面的测试环境中所述。

2、在单元测试类定义的开始处，添加 `@RunWith（MockitoJUnitRunner.class）`注释。 这个注释告诉Mockito测试运行器验证你对框架的使用是否正确，并且简化了你的模拟对象的初始化。

3、要为Android依赖项创建一个模拟对象，请在字段声明之前添加@Mock注释。

4、为了Stub依赖的行为，可以通过使用`when（）`和`return（）`方法来满足条件时，可以指定一个条件和返回值。

以下示例显示如何创建使用模拟Context对象的单元测试。

```Java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.*;
import static org.mockito.Mockito.*;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;
import android.content.SharedPreferences;

@RunWith(MockitoJUnitRunner.class)
public class UnitTestSample {

    private static final String FAKE_STRING = "HELLO WORLD";

    @Mock
    Context mMockContext;

    @Test
    public void readStringFromContext_LocalizedString() {
        // Given a mocked Context injected into the object under test...
        when(mMockContext.getString(R.string.hello_word))
                .thenReturn(FAKE_STRING);
        ClassUnderTest myObjectUnderTest = new ClassUnderTest(mMockContext);

        // ...when the string is returned from the object under test...
        String result = myObjectUnderTest.getHelloWorldString();

        // ...then the result should be the expected one.
        assertThat(result, is(FAKE_STRING));
    }
}
```
要了解有关使用Mockito框架的更多信息，请参阅[示例代码](https://github.com/googlesamples/android-testing/tree/master/unit/BasicSample)中的Mockito API参考和SharedPreferencesHelperTest类。




#### Error: "Method ... not mocked"
----
如果您运行测试，从Android SDK调用API，你不会使用mock，可能会收到一个错误，说这种方法没有被模拟。 这是因为用于运行单元测试的android.jar文件不包含任何当前代码（这些API仅由设备上的Android系统映像提供）。

相反，所有方法默认都会抛出异常。 这是为了确保你的单元测试你的代码，而不是依赖于Android平台的任何特定的行为（你没有明确地mock，如Mockito）。

如果抛出的异常说你的测试有问题，可以更改行为，以便通过在项目的顶级build.gradle文件中添加以下配置来返回null或零：

```java
android {
  ...
  testOptions {
    unitTests.returnDefaultValues = true
  }
}
```

> 注意：将returnDefaultValues属性设置为true应该小心。 null / zero返回值可以在测试中引入回归，这些回调很难调试，并且可能允许失败的测试通过。只能用它作为最后的手段。


#### 运行本地单元测试
---

要运行您的本地单元测试，请按照下列步骤操作：

1、通过单击工具栏中的“ Sync Project”，确保您的项目与Gradle同步。

2、以下列其中一种方式运行测试：

* 要运行单个测试，请打开“Project”窗口，然后右键单击以进行测试，然后单击“Run”。
* 要测试类中的所有方法，请右键单击测试文件中的类或方法，然后单击“Run”。
* 要在目录中运行所有测试，请右键单击该目录并选择“Run Tests”。




原始封面

![课程图片](https://images.unsplash.com/photo-1553356084-58ef4a67b2a7?w=300)

