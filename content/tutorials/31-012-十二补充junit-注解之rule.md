---
weight: 12
title: （十二）补充：JUnit 注解之Rule
date: '2017-11-13T12:15:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1580983218547-8333cb1d76b9?w=300
tags: []
categories:
- Junit测试框架实用教程
lightgallery: true
toc:
  auto: false
---



一个JUnit Rule就是一个实现了TestRule的类，这些类的作用类似于 `@Before`、`@After`，是用来在每个测试方法的执行前后执行一些代码的一个方法。
那为什么不直接用这些 `@Before`、`@After`呢？这是因为它们都只能作用于一个类，如果同一个setup需要在两个类里面同时使用，那么你就要在两个测试类里面定义相同的@Before方法，然后里面写相同的代码，这就造成了代码重复。

此外，JUnit Rule还能做一些 `@Before`、`@After`这些注解做不到的事情，那就是他们可以动态的获取将要运行的测试类、测试方法的信息。

#### 使用框架自带的Rule
---

除了增加Rule特性，新版JUnit还添加了很多核心Rule

* TemporaryFolder：测试可以创建文件与目录并且会在测试运行结束后将其删除。这对于那些与文件系统打交道且独立运行的测试来说很有用。
* ExternalResource：这是一种资源使用模式，它会提前建立好资源并且会在测试结束后将其销毁。这对于那些使用socket、嵌入式服务器等资源的测试来说很有用。
* ErrorCollector：可以让测试在失败后继续运行并在测试结束时报告所有错误。这对于那些需要验证大量独立条件的测试来说很有用（尽管这本身可能是个“test smell”）。
* ExpectedException：可以在测试中指定期望的异常类型与消息。
* Timeout：为类中的所有测试应用相同的超时时间。

例如，TimeOut这个Rule的使用。

```Java
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.Timeout;


public class RuleTestDemo {

    //使用Timeout这个Rule
    @Rule
    public Timeout timeout = new Timeout(1000);  

    @Test
    public void testMethod1() throws Exception {
        Thread.sleep(1001);
    }

    @Test
    public void testMethod2() throws Exception {
        Thread.sleep(999);
    }
}
```

使用JUnit所提供的Timeout类，该类用于控制测试用例的执行超时时间。这里设置为1秒，当用例执行超过1秒则失败。接下来分别在 testMethod1和testMethod2两个用例中使用sleep()方法来控制用例的执行时间，显然testMethod1超过1秒，则运行失败。

![](http://img.testclass.net/junit_rule_run_result1.png)


#### 自定义的Rule
---

除了可以使用JUnit框架自带的Rule，还可以根据自己的需求自定义Rule。简单来说，自定义一个Rule就是implement一个TestRule 接口，并实现apply()方法。该方法需要返回一个Statement对象。例子如下：

```Java
import org.junit.rules.TestRule;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;


public class MethodNameRule implements TestRule {

    public Statement apply(final Statement base, final Description description) {
        return new Statement() {
            @Override
            public void evaluate() throws Throwable {
                //在测试方法运行之前做一些事情，在base.evaluate()之前
                String className = description.getClassName();
                String methodName = description.getMethodName();

                base.evaluate();  //运行测试方法

                //在测试方法运行之后做一些事情，在base.evaluate()之后
                System.out.println("Class name:"+className+", method name: "+methodName);
            }
        };
    }
}
```

这里实现的功能是在每次测试用例运行之后，打印当前测试用例的类名和方法名。
在上面的例子中添加这里定义的MethodNameRule 。

```Java
……
public class RuleTestDemo {

    //使用Timeout这个Rule
    @Rule
    public Timeout timeout = new Timeout(1000);  

    //使用自定义Rule，
    @Rule
    public MethodNameRule methodNameRule = new MethodNameRule();

……
```

再次运行测试用例，执行结果如下：

![](http://img.testclass.net/junit_rule_run_result2.png)




原始封面

![课程图片](https://images.unsplash.com/photo-1580983218547-8333cb1d76b9?w=300)

