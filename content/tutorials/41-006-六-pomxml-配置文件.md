---
weight: 6
title: （六） pom.xml 配置文件
date: '2017-11-25T12:30:11+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 虫师
authorLink: https://github.com/defnngj
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=300
tags: []
categories:
- maven简明教程
lightgallery: true
toc:
  auto: false
---



用 Maven 来管理 Java 项目的第三方库，最主要是通过 __pom.xml__ 文件，这一小节将解释该文件的使用。

#### pom.xml 文件
---

以 [（四）通过 mvn 命令创建 Maven 项目](/maven/create_project/) 创建的项目为例。打开项目根目录下的 pom.xml 文件。

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.myapp.pro</groupId>
  <artifactId>myapp</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>

  <name>myapp</name>
  <url>http://maven.apache.org</url>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>

  </dependencies>

</project>
```

 * project：pom.xml文件中的顶层元素； 

 * modelVersion：指明POM使用的对象模型的版本。这个值很少改动。

 * groupId：指明创建项目的组织或者小组的唯一标识。GroupId是项目的关键标识，典型的，此标识以组织的完全限定名来定义。比如，org.apache.maven.plugins是所有Maven插件项目指定的groupId。 

 * artifactId：指明此项目产生的主要产品的基本名称。项目的主要产品通常为一个JAR文件。第二，象源代码包通常使用artifactId作为最后名称的一部分。典型的产品名称使用这个格式：
 <artifactId>- <version>. <extension>(比如：myapp-1.0.jar)。 

 * version：项目产品的版本号。Maven帮助你管理版本，可以经常看到SNAPSHOT这个版本，表明项目处于开发阶段。 

 * name：项目的显示名称，通常用于maven产生的文档中。 

 * url：指定项目站点，通常用于maven产生的文档中。 

 * description：描述此项目，通常用于maven产生的文档中。


#### 管理第三方库
---

对于一个第三方库的添加，下面的几个参数是我们需要关注的。

```
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>3.8.1</version>
<scope>test</scope>
```
<scope></scope>，它主要管理依赖的部署。目前<scope>可以使用5个值： 

* compile，缺省值，适用于所有阶段，会随着项目一起发布。 
* provided，类似compile，期望JDK、容器或使用者会提供这个依赖。如servlet.jar。 
* runtime，只在运行时使用，如JDBC驱动，适用运行和测试阶段。 
* test，只在测试时使用，用于编译和运行测试代码。不会随项目发布。 
* system，类似provided，需要显式提供包含依赖的jar，Maven不会在Repository中查找它。

通过查看pom.xml中Junit的配置，显然版本有些旧了，我们去下载最新的Junit4，但我们又不知道Maven中的具体的版本怎么办呢？我们可以到 Maven 的中央仓库去查询。

Maven仓库：http://mavenrepository.com/

通过该网站查询“Junit”, 找到 Junit4 最新版本的配置。

![](http://img.testclass.net/maven_repository.png)

修改 pom.xml 中的 Junit4 的配置。

```
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>4.12</version>
<scope>test</scope>
```

或者通过 Maven 命令（插件）更新项目的第三方库。

```
myapp > mvn clean

myapp > mvn idea:idea
```
关于 Maven 插件列表参考：
http://maven.apache.org/plugins/index.html




原始封面

![课程图片](https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=300)

