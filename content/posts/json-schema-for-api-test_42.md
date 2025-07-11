---
weight: 1
title: "接口测试进阶：在接口测试中框架中使用json schema"
date: 2024-03-08T09:02:36+08:00
lastmod: 2024-03-08T09:02:36+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "有规范就会容易不少"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1614793351079-11dd79b922ba?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

当今接口测试越来越重要，一般情况下我们总是会对接口的返回的 json 字符串进行验证，看返回是否跟我们的预期相符。不过很多情况下我们会遇到下面的问题

- 响应结果在测试中不停的发生变动，比如昨天还是 3 个字段，今天可能返回值里只有 2 个字段了，测试这边没有比较好的方式感受到后端的变化
- 我们需要对 json 的返回值进行一些校验，需要写很多的断言，大部分时候这些断言都是相似的，或者是重复的，比如说校验某个字段的长度必须小于 10 之类的

那如何解决呢？

- 与前后端沟通好返回值的字段，类型以及校验规则，最好有前后端+测试端统一一份合约，大家都按照合约来进行数据的处理
- 测试的时候通过合约里定义好的校验规则进行数据校验

这时候 json schema 就派上用场了。

### json schema

JSON Schema 是一种 JSON 媒体类型，用于定义 JSON 数据的结构。 JSON 模式旨在定义 JSON 数据的验证，可用于验证响应和请求 JSON。 在 JSON Schema 中，我们可以验证数据类型、字段是否为必填、最小长度或最大长度等。

### 举例

下面的数据代表了一个员工的信息

- id: `employeeId`
- 员工名称: `employeeName`
- 年龄: `employeeAge`
- 职称: `jobTitle`
- 爱好: `hobby`

```ruby
{
  "employeeId": 1,
  "employeeName": "Fulan",
  "employeeAge": 23,
  "jobTitle": "SDET",
  "hobby": [
    "watch movies",
    "play football"
  ]
}
```

上面的定义其实是有一些疑问的，比如

- id 是什么意思
- employeeName 的最大长度是多少
- employeeAge 的最小值是什么
- jobTitle 是必填吗
- hobby 可以填几个

我们可以通过生成 JSON schema 来回答上面的问题

```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "http://example.com/example.json",
  "type": "object",
  "title": "The root schema",
  "description": "The root schema comprises the entire JSON document.",
  "default": {},
  "examples": [
    {
      "employeeId": 1,
      "employeeName": "Fulan",
      "employeeAge": 23,
      "jobTitle": "SDET",
      "hobby": ["watch movie", "play football"]
    }
  ],
  "required": [
    "employeeId",
    "employeeName",
    "employeeAge",
    "jobTitle",
    "hobby"
  ],
  "properties": {
    "employeeId": {
      "$id": "#/properties/employeeId",
      "type": "integer",
      "title": "The employeeId schema",
      "description": "An explanation about the purpose of this instance.",
      "default": 0,
      "examples": [1]
    },
    "employeeName": {
      "$id": "#/properties/employeeName",
      "type": "string",
      "title": "The employeeName schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": ["Fulan"]
    },
    "employeeAge": {
      "$id": "#/properties/employeeAge",
      "type": "integer",
      "title": "The employeeAge schema",
      "description": "An explanation about the purpose of this instance.",
      "default": 0,
      "examples": [23]
    },
    "jobTitle": {
      "$id": "#/properties/jobTitle",
      "type": "string",
      "title": "The jobTitle schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": ["SDET"]
    },
    "hobby": {
      "$id": "#/properties/hobby",
      "type": "array",
      "title": "The hobby schema",
      "description": "An explanation about the purpose of this instance.",
      "default": [],
      "examples": [["watch movies", "play football"]],
      "additionalItems": true,
      "items": {
        "$id": "#/properties/hobby/items",
        "anyOf": [
          {
            "$id": "#/properties/hobby/items/anyOf/0",
            "type": "string",
            "title": "The first anyOf schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": ["watch movies", "play football"]
          }
        ]
      }
    }
  },
  "additionalProperties": true
}
```

看上去很多很乱对不对，别着急，我们慢慢看

- $schema 关键字表明此模式是根据标准的特定草案编写的，并且用于各种原因，主要是版本控制。
- $id 关键字定义模式的 URI 和模式中其他 URI 引用解析的基本 URI。
- title 和 description 注释关键字只是描述性的。 它们不会对正在验证的数据添加约束。 使用这两个关键字来说明模式的意图。
- type 关键字定义了我们的 JSON 数据的第一个约束，在这种情况下，它必须是一个 JSON 对象。

更具体一点

properties 里定义了各个字段的详情，我们可以在里面增加更多的约束

```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "http://example.com/example.json",
  "type": "object",
  "title": "The root schema",
  "description": "The root schema comprises the entire JSON document.",
  "default": {},
  "examples": [
    {
      "employeeId": 1,
      "employeeName": "Fulan",
      "employeeAge": 23,
      "jobTitle": "SDET",
      "hobby": ["watch movie", "play football"]
    }
  ],
  "required": [
    "employeeId",
    "employeeName",
    "employeeAge",
    "jobTitle",
    "hobby"
  ],
  "properties": {
    "employeeId": {
      "$id": "#/properties/employeeId",
      "type": "integer",
      "title": "The employeeId schema",
      "description": "An explanation about the purpose of this instance.",
      "default": 0,
      "examples": [1]
    },
    "employeeName": {
      "$id": "#/properties/employeeName",
      "type": "string",
      "title": "The employeeName schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": ["Fulan"]
    },
    "employeeAge": {
      "$id": "#/properties/employeeAge",
      "type": "integer",
      "title": "The employeeAge schema",
      "description": "An explanation about the purpose of this instance.",
      "default": 0,
      "exclusiveMinimum": 20,
      "examples": [23]
    },
    "jobTitle": {
      "$id": "#/properties/jobTitle",
      "type": "string",
      "title": "The jobTitle schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "minLength": 4,
      "examples": ["SDET"]
    },
    "hobby": {
      "$id": "#/properties/hobby",
      "type": "array",
      "title": "The hobby schema",
      "description": "An explanation about the purpose of this instance.",
      "default": [],
      "examples": [["watch movies", "play football"]],
      "additionalItems": true,
      "items": {
        "$id": "#/properties/hobby/items",
        "anyOf": [
          {
            "$id": "#/properties/hobby/items/anyOf/0",
            "type": "string",
            "title": "The first anyOf schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": ["watch movies", "play football"]
          }
        ]
      },
      "uniqueItems": true
    }
  },
  "additionalProperties": true
}
```

在上面的例子中我们规定

- employeeId 的默认值是 0
- employeeAge 最小值是 20
- jobTitle 的最小长度是 4
- hobbies 必须排重，所以 uniqueItems 的值是 true

json schema 合约可以尽可能的详细，这样模糊的点就会相对较少，验证的结果会更加的准确。

### 在测试框架中使用 json schema

这里以 java 为例，首先我们引入 json schema 的支持，然后定义断言工具，最后在用例中使用该断言。

引入 json schema 支持，这里用的是[https://github.com/everit-org/json-schema](https://github.com/everit-org/json-schema)，pom.xml 如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>json-schema</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>7.4.0</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.everit.json</groupId>
            <artifactId>org.everit.json.schema</artifactId>
            <version>1.3.0</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.12.4</version>
        </dependency>
        <dependency>
            <groupId>io.rest-assured</groupId>
            <artifactId>rest-assured</artifactId>
            <version>4.3.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

</project>
view raw
```

定义断言工具函数

```java
package utils;

import com.fasterxml.jackson.databind.ObjectMapper;
import functest.APITest;
import org.everit.json.schema.Schema;
import org.everit.json.schema.ValidationException;
import org.everit.json.schema.loader.SchemaLoader;
import org.json.JSONObject;
import org.json.JSONTokener;
import org.testng.Assert;

import java.util.logging.Logger;

public class JsonSchemaUtils {

    private static Logger LOGGER= Logger.getLogger(String.valueOf(JsonSchemaUtils.class));

    private ObjectMapper objMapper = new ObjectMapper();

    public void checkJsonSchema(String jsonSchemaPath, String jsonSubject) throws ValidationException {

        JSONObject retVal = new JSONObject();

        try {
            JSONObject jsonSchema = new JSONObject(new JSONTokener(APITest.class.getResourceAsStream(jsonSchemaPath)));
            Schema schema = SchemaLoader.load(jsonSchema);
            schema.validate(objMapper.convertValue(jsonSubject, JSONObject.class));
            retVal.put("errorMessage","");
        } catch (ValidationException ex) {
            ex.printStackTrace();
            LOGGER.info("JSON Schema Error Message: " + ex.getMessage());
            retVal.put("errorMessage",ex.getMessage());
            Assert.assertEquals(retVal.getString("errorMessage"), "");
        }
        Assert.assertEquals(retVal.getString("errorMessage"), "");
    }
}
```

在用例中使用

```java
package functest;

import io.restassured.RestAssured;
import org.json.JSONObject;
import org.testng.annotations.Test;
import io.restassured.response.Response;
import utils.JsonSchemaUtils;

public class APITest {

    private final static String JSON_SCHEMA_ACTIVITY_PATH = "/schema/apiTest-jsonSchema.response.json";

    JsonSchemaUtils jsonSchemaUtils = new JsonSchemaUtils();

    @Test
    public void getTest() {

        Response response = RestAssured.get("https://www.boredapi.com/api/activity/");
        JSONObject jsonObj = new JSONObject(response.getBody().asString());
        System.out.println(jsonObj.toString(4));
        jsonSchemaUtils.checkJsonSchema(JSON_SCHEMA_ACTIVITY_PATH,response.asString());

    }

}
```

### 最后

JSON schema 是一个多功能库，可以帮助我们执行 API 测试，使用 JSON 文件定义 schema 要求的能力显示了这个库的强大功能。 希望这些示例能让您了解如何在项目中使用模式验证。
