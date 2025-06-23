---
weight: 1
title: "使用openAI来分析自动化测试报告的错误信息"
date: 2024-03-09T09:03:44+08:00
lastmod: 2024-03-09T09:03:44+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "有可行性"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1463620695885-8a91d87c53d0?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

今天看到有人用 ai 去分析自动化测试报告里的错误，代码和概念都很简单，也很有意思，忍不住翻译了一下，供大家参考。

原文地址[https://labs.pineview.io/using-openai-platform-to-analyse-automated-test-failures](https://labs.pineview.io/using-openai-platform-to-analyse-automated-test-failures)

## 引言

当涉及到人工智能，尤其是 OpenAI 平台时，关于它将如何影响一切的内容并不缺乏。因此乍一看，本文可能似乎是另一篇过于热情和乐观的标题党文章，告诉你应该加入人工智能的行列，否则就会被落下。

顺便说一下，本文并非由人工智能撰写。我只是使用我最喜欢的文本编辑器应用程序，它以西方文学中最令人激动的小说之一的名字命名——尤利西斯。除了一些基本的自动完成功能外，没有来自外部的干扰（或推理）。本文没有人工智能生成的废话，尽管我不能保证文章完全没有废话。

但无论你对人工智能生成内容持何种立场，作为软件专业人士，我认为我们都可以达成共识：在自动化软件测试方面，调试和调查测试失败总是很繁琐。因此，我认为这可能是一个可以引入一些人工智能辅助的好领域，因为我们只是在扩展机器已经完成的工作。在这里，不存在冒充人类或“让人们误以为他们正在与真人互动”的风险，这正如哲学家丹尼尔·丹尼特在他最近在《大西洋月刊》上发表的文章中所提到的一个真正的文明风险。

## 什么是端到端测试？

如果你对端到端测试还不熟悉，它是一种通过模拟真实用户的操作来测试整个应用程序的自动化软件测试类型。

Nightwatch.js 是一个开源库，用于编写和执行网站和 Web 应用程序的自动化端到端测试。它于 2014 年发布，2021 年被转移到 BrowserStack 的开源计划办公室，目前正在进行开发。Nightwatch.js 是用 Node.js 编写的，它支持所有主要的 Web 浏览器，并且还可以在移动设备上运行测试。

本教程将介绍如何开发一个 Nightwatch.js 插件，将测试失败和相关错误发送到与 OpenAI 平台集成的服务，以分析错误并获得一些可操作的反馈。默认情况下，Nightwatch 的最新版本已经对测试失败提供了相当好的反馈，并提供了一定程度的可操作反馈，因此我们将尝试使用 GPT-4 模型扩展其功能，以在输出消息中增加一些亮点，提供稍微更好的上下文，并学习如何开发结合人工智能辅助的服务。

## 为什么选择 Nightwatch？

诚然，目前市场上还有一些其他备受炒作和流行的测试工具，但实际上 Nightwatch 是我们在 2014 年在 Pineview 创建的项目，现在正在 BrowserStack 的开源计划办公室进行开发。我也是那个团队的一员，Nightwatch 仍然是我在所有其他项目中用于测试的最喜欢的工具，当然。

此外，Nightwatch 作为一个库已经存在了相当长的时间，在这些年里享有不同程度的受欢迎程度。有大量的可用于机器学习模型训练的数据，因此 GPT-4 在编写 Nightwatch 测试和解释结果方面具有相当好的能力，这意味着我们已经有了一个强大的基础，可以构建一个辅助人工智能来解释我们的测试失败，并可能与我们对抗。

## 步骤 1 - 创建错误分析服务

我们的小练习主要由两个部分组成，都相对简单：

构建调用 OpenAI 服务的后端服务
编写 Nightwatch.js 插件，接收实际的测试失败并将其发送到后端服务进行分析
我们将从第 1 部分开始 - 构建错误分析服务。在当今时代，构建与人工智能相关的任何东西可能听起来非常奢侈和光鲜，但实际上这只是一个非常基本的任务，并没有太多特别之处。

分析服务只是一个基本的 express.js API 服务，它接受 POST 请求并使用 Node.js 的 SDK 向 OpenAI 平台发出特定的调用。

你需要从 OpenAI 这里获取一个开发者密钥，然后配置要使用的模型。为了本文的目的，我使用了 gpt-4-1106-preview，但那需要一个付费计划。如果你想在免费计划上尝试它，你可以使用 gpt-3.5-turbo。

### 1.1 项目结构

使用以下命令设置新项目：

```
mkdir nightwatch-openai-service
cd nightwatch-openai-service
touch index.js
npm init -y
```

接下来，编辑 package.json 文件并设置 type=module，例如：

```
{
  "name": "openai-nightwatch-service",
  "type": "module",
  ...
}
```

然后继续安装所需的依赖项：

```
npm i dotenv express openai
```

### 1.2 添加服务

在新创建的项目中，创建两个新文件：

.env - 包含 OpenAI API 密钥，例如：

```
OPENAI_API_KEY=xxxxxx
PORT=4001
```

index.js - 粘贴以下代码

```javascript
import dotenv from "dotenv";
import express from "express";
import { OpenAI } from "openai";

dotenv.config();
const app = express();
app.use(express.json());
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.post("/analyze-error", async (req, res) => {
  try {
    const { errorMessage, codeSnippet, additionalDetails } = req.body;

    const details = `Additional details: Nightwatch version: ${additionalDetails.nightwatchVersion}, config file: ${additionalDetails.configFile}, platform: ${additionalDetails.platform}, browser: ${additionalDetails.browser}, headless mode: ${additionalDetails.headless}.`;
    const messages = [
      {
        role: "system",
        content:
          "You are an expert in web development using Node.js, automated testing with Selenium WebDriver, and the Nightwatch.js framework.",
      },
      {
        role: "user",
        content: [
          {
            type: "text",
            text: `Investigate and explain why the tests failed. Error message: ${errorMessage}\n.Code snippet from test case where the error occurred: ${codeSnippet}. ${details}`,
          },
        ],
      },
    ];

    const response = await openai.chat.completions.create({
      model: "gpt-4-1106-preview",
      messages,
      max_tokens: 600,
    });

    res.json({ analyzedResult: response.choices[0].message.content });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

至此，服务部分就完成了。只需使用以下命令运行它：

```
node index.js
```

正如你所见，这里几乎没有涉及创造性的工作。我们将发送来自 Nightwatch 插件的错误消息，以及一个包含发生错误或断言失败的代码行的小代码片段。

唯一剩下的事情就是调整提示。在 OpenAI 文档中有一个名为"prompt engineering"的完整部分，介绍了如何编写更好的提示以改进结果，这正是我们现在所关注的产品创新方面。

代码可在 Github(https://github.com/pineviewlabs/openai-nightwatch-service)上找到。请继续fork它并在本地运行，我们将在教程的下一部分中需要它。

## 步骤 2 - 编写 Nightwatch.js 报告插件

除了默认包含的内置测试报告器（junit-xml、json、html）之外，Nightwatch 还支持加载自定义报告器的功能，这是我们接下来要开发的内容。

完整的代码可以在 Github 上找到，该包已经在 NPM 上发布为 nightwatch-openai-plugin，因此如果你愿意，你可以直接使用它并跳过第 3 步。

自定义报告插件的作用是将错误数据发送到我们在第 1 步中开发的 AI 辅助分析服务。为此，我们需要创建一个新的 Node.js 项目，遵循 Nightwatch 能够理解的特定结构。

### 2.1 项目结构

首先，使用以下命令设置新项目：

```
mkdir my-nightwatch-ai-reporter
cd my-nightwatch-ai-reporter
touch index.js
npm init -y
git init
```

基本上，插件需要被包装为一个 NPM 包，并导出一个如下所示的模块：

```javascript
// index.js

module.exports = {
  async reporter(results) {
    console.log("在这里进行一些报告...");
  },
};
```

我们还需要添加一个.env 文件，其中将填入我们的 AI 分析服务的 URL。

如果你按照本文第 1 步的说明运行服务，则.env 文件如下所示：

```
SERVICE_URL=http://localhost:4001/analyze-error
```

2.2 编写自定义报告器
现在，我们只需要在 index.js 文件的 reporter()函数中添加一些逻辑，将报告发送到第 1 步的分析服务，并显示结果。分析服务将使用我们定义的提示调用 OpenAI 平台。

当测试运行完成时，Nightwatch 将调用带有 results 参数的报告器函数，该参数包含失败的结果和其他相关错误。下面是具体的代码：

```javascript
module.exports = {
  async reporter(results) {
    const errors = getErrorMessages(results);

    if (!errors) {
      return;
    }

    const outputs = makeOutputs(errors);

    for (const output of outputs) {
      try {
        const response = sendErrorAnalysisRequest(output);
        const terminalOutput = marked.parse(response.data.analyzedResult);
        console.log("错误分析完成：", terminalOutput);
      } catch (err) {
        console.error("错误分析失败：", error.response?.data || error.message);
      }
    }
  },
};
```

sendErrorAnalysisRequest 函数将使用测试数据发起一个 POST 请求。

## 第 3 步 - 将所有内容整合在一起

现在，我们已经有了插件和服务，是时候将它们整合到一个测试项目中了。我们将构建一个小型的端到端测试项目，其中包含一个示例网站的一些非常基本的测试。该项目将使用 Nightwatch 来运行测试，并使用我们新创建的插件。

### 3.1 设置一个测试项目

首先，使用以下命令创建一个测试项目：

```
mkdir nightwatch-testing
cd nightwatch-testing
npm init -y
```

### 3.2 从 NPM 安装 Nightwatch

Nightwatch 可以通过以下命令从 NPM 安装，并且准备就绪：

```
npm i nightwatch
```

你可以使用以下命令验证 Nightwatch 是否已安装：

```
npx nightwatch --info
```

### 3.3 添加 Nightwatch 报告插件

现在，我们将在步骤 2 中开发的 AI 分析插件添加到我们的测试项目中，以便 Nightwatch 可以发现并使用它。

你可以直接从 NPM 安装该包，或者如果你已经完整地完成了步骤 2，也可以使用本地版本。

从 NPM 安装插件：

```
npm i nightwatch-openai-plugin
```

从本地文件夹安装（根据实际路径进行更新，相对路径也适用）：

```
npm i /path/to/my-nightwatch-ai-reporter
```

### 3.4 配置 Nightwatch 加载插件

为了使 Nightwatch 能够加载插件，我们需要在 nightwatch 配置文件（nightwatch.conf.js）中进行定义。

首先，让我们查看 package.json 文件。它应该在依赖项列表中包含插件。假设插件是从 NPM 安装的，它应该如下所示：

```json
{
  "name": "nightwatch-testing",
  ...
  "dependencies": {
    "nightwatch": "^3.3.1",
    "nightwatch-openai-plugin": "^0.1.0"
  }
}
```

现在打开 nightwatch.conf.js 文件，并将 nightwatch-openai-plugin 添加到插件数组中，如下所示：

```javascript
// nightwatch.conf.js

module.exports = {
  // ... 其他设置
  plugins: ["nightwatch-openai-plugin"],
  // ... 继续设置
};
```

你可以通过使用 Chrome 运行一个与库捆绑在一起的示例测试来验证 Nightwatch 是否已安装并正常工作：

```
npx nightwatch examples/tests/duckDuckGo.js --chrome
```

输出结果将如下所示：

```
ℹ Connected to ChromeDriver on port 9515 (1001ms).
Using: chrome (119.0.6045.123) on MAC.


  Running Search Nightwatch.js and check results:
───────────────────────────────────────────────────────────────
  ✔ Element <body> was visible after 15 milliseconds.
  ✔ Testing if element <input[name="q"]> is visible (17ms)
  ✔ Testing if element <button[type=submit]> is visible (14ms)
  ✔ Testing if element <.react-results--main> contains text 'Nightwatch.js' (1545ms)

  ✨ PASSED. 4 assertions. (2.534s)
```

你还可以根据你在计算机上安装的浏览器选择使用`--firefox`、`--safari`或`--edge`选项。

## 第 4 步 - 运行测试并检查分析报告

现在，我们已经安装并配置了 Nightwatch，并在第 1 步中使用插件开发了 AI 辅助分析服务，我们可以运行更多的端到端测试并看到它的运行情况。

如果你还没有完成第 1 步，或者想在开始之前先了解一下，我已经为你准备了一个示例项目，其中包括一个演示后端服务，可以直接运行，这样你就可以看到它的运行情况：

GitHub - pineviewlabs/nightwatch-ai-testproject
Contribute to pineviewlabs/nightwatch-ai-testproject development by creating an account on GitHub.
GitHubpineviewlabs

请随意 fork 它并在本地运行。请注意，分析服务仅以演示目的的有限容量运行，不应在实际测试场景中使用。

### 4.1 添加一些端到端测试

对于那些已经完成了前面步骤并深入其中的人，我们只需要添加一些基本的测试，以便我们可以在本地运行所有内容。

进入 nightwatch-testing 文件夹并创建一个新的 test 文件夹：

```
mkdir test
```

然后在 test 文件夹中添加以下两个测试：

1. homepage.js

```javascript
describe("Homepage End-to-end Test", () => {
  it("tests if homepage is loaded", (browser) => {
    browser
      .navigateTo("https://middlemarch.netlify.app/")
      .assert.visible("#app .new-arrivals-panel")
      .expect.elements("#app .new-arrivals-panel .col-md-6")
      .count.toEqual(4);
  });
});
```

2. addtocart.js

```javascript
describe("add to cart test", () => {
  before((browser) => browser.navigateTo("https://middlemarch.netlify.app/"));

  it('adds 2 volumes of "Rhinoceros and Other Plays" to cart', (browser) => {
    const addToCartEl = browser.element
      .findByText("Rhinoceros and Other Plays")
      .getParentElement()
      .find("button");
    addToCartEl.click();
    addToCartEl.click();

    browser.assert.textEquals(".shopping-cart .badge", "2");
  });

  after((browser) => browser.end());
});
```

这两个测试是针对一个示例书店应用程序编写的，是我之前关于 Vite 和 Vue 3 的教程的一部分。第一个测试只是打开网站并验证内容是否存在，而第二个测试将一本书添加到购物车并执行基本断言。

要运行这些测试，请使用以下命令，如果你不想在测试过程中看到浏览器弹出，请选择传递--headless 参数：

```
npx nightwatch test --chrome
```

或者根据你的计算机上可用的浏览器选择--firefox、--safari 或--edge 选项。

### 4.2 故意使测试失败

为了测试 AI 分析服务，我们需要故意使至少一个测试失败。然后插件报告器将生效，将测试失败发送到后端服务，然后打印结果。

幸运的是，有许多可用的方法来使测试失败。其中一种最简单的方法是重命名其中一个元素，然后等待测试失败并显示“元素未找到”的错误。

模拟“元素未找到”错误
编辑 test 文件夹中的 homepage.js 文件，将以.assert.visible 开头的行更改为以下内容：

```javascript
browser.navigateTo("https://middlemarch.netlify.app/").assert.visible("#xapp");
```

然后测试将以错误消息失败，指示无法找到选择器为#xapp 的元素，并打印类似于以下输出：

```
TEST FAILURE (12.844s):
 - 1 assertions failed; 1 passed

✖ 1) homepage

 – tests if homepage is loaded (7.903s)

 → ✖ NightwatchAssertError
 Testing if element <#xapp .new-arrivals-panel> is visible in 5000ms - expected "is visible" but got: "element could not be located" (5131ms)

    Error location:
    /Users/andrei/pineviewlabs/nightwatch-openai/test/homepage.js:6
    –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
     4 |     browser
     5 |       .navigateTo('https://middlemarch.netlify.app/')
     6 |       .assert.visible('#xapp .new-arrivals-panel')
     7 |       .expect.elements('#app .new-arrivals-panel .col-md-6').count.toEqual(4)
     8 |   });
    –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
```

然后我们实际上可以看到来自 AI 分析服务的报告：

```
错误分析完成：失败表明在5000ms（5秒）的时间范围内未找到具有CSS选择器#xapp .new-arrivals-panel的元素。以下是您可以用于调试的操作：

    1. 更新测试代码：

    .debug({selector: "#xapp .new-arrivals-panel"}) // 添加此行
    .browser.expect.element('#xapp .new-arrivals-panel').to.be.visible.before(5000);

    2. 使用调试标志运行Nightwatch：

    nightwatch --debug --devtools

这将打开Chrome开发者工具，您可以在其中检查页面和控制台。

导致错误的可能原因包括：

    * 元素在测试时不存在于页面上。
    * 由于页面尚未加载完成、存在网络延迟或显示元素的JavaScript运行较晚，该元素在5秒内不可见。
    * 选择器不正确或已更改。
    * 页面的JavaScript中存在错误，导致元素无法正确显示。
```

报告可能有点过长和过于通用，但现在只需要调整提示，使其生成所需的结果，这不是本文的任务。

### 4.3 配置分析后端服务

nightwatch-openai-plugin 使用默认的 HTTP API 服务与 OpenAI API 进行交互，该服务仅供演示目的使用。您可以通过克隆 openai-nightwatch-service 存储库并使用自己的 OpenAI API 密钥运行它来托管自己的服务。

在运行 openai-nightwatch-service 时，您需要定义 NIGHTWATCH_ANALYSIS_SERVICE_URL 环境变量，指向服务的 URL。您还可以使用.env 文件。

例如，假设您将服务运行在 http://localhost:4001 上，您可以在 Nightwatch 项目的根目录中创建一个.env 文件，内容如下：

```
NIGHTWATCH_ANALYSIS_SERVICE_URL=http://localhost:4001/analyze-error
```

## 结论

所以，我们已经成功构建（希望如此）一个用于 Nightwatch 测试的 AI 辅助分析插件，并且我们已经看到它的实际效果。您现在可以尝试模拟各种错误并查看响应。

请记住，这只是一个实验，该服务仅供演示目的使用。我尚未尝试不同类型的错误和测试失败，并且我没有花太多时间来调整提示，因此无法保证它能够适用于大量的测试集合，其中可能存在不同类型的失败。因此，您需要自行承担风险，但欢迎您进行自己的实验并报告您的发现。感谢阅读。
