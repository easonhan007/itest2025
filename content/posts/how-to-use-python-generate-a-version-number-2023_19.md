---
weight: 1
title: "用python实现简单的版本号生成工具"
date: 2024-03-08T09:02:01+08:00
lastmod: 2024-03-08T09:02:01+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "如题"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1593491205049-7f032d28cf5c?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

我们发布比较频繁，每次发布都需要从 release 分支打 1 个 tag，不过可能是因为年纪大了的缘故吧，尽管借鉴了一些版本号的制定规则，不过每次我都记不太住，需要翻文档去重新复习，不如把这步自动化一下，为未来的自己节约一点时间，另外有了工具就好统一规则，后面所有相关的项目都可以用同一套规则来生成版本号，去掉了人工对齐的成本，变相提升了效率。

### 版本号规则

我们的版本号大概长这个样子

```bash
v1.00.0-hotfix-20221111-1
版本号   发布类型 发布时间  第几次发布

```

- 版本号规则: 大版本 1 位 + 小版本 2 位 + patch 版本号 1，比如 v1.00.0 表示大版本是 1，小版本是 0，patch 版本是 0
- 发布类型：普通发布/hotfix/adhoc(临时版本)

### 设计

首先不考虑写页面做系统，其实用 vue 随便写个单页应用是可以很快搞定的，不过没那个必要，用命令行工具就好了，简单快速，而且生成了版本号之后可以调用 githlab(我们公司用私有化部署的版本)api 来自动打 tag，在微服务化当道的今天，手动为每次发布的所有 repo 打版本号本身就不是一个很好的体验。命令行工具在这方面比单页应用更具优势一些。

另外交互式的命令行可以省去很多参数 validation 的工作量，这也应该是考虑的。随便搜索了一下，发现了 1 个名为 inquirer 的库可以很好的满足我的需求。

### 代码实现

```python
import inquirer
from datetime import datetime

STR_MAP = {
	'regular': '',
	'hotfix': '-hotfix',
	'adhoc': '-adhoc'
}

def build_version(options):
	release_type = STR_MAP[options['release_type'][0]]
	date = datetime.now().strftime('%Y%m%d')
	return f"v{options['version']}{release_type}-{date}-{options['seq']}"

if __name__ == "__main__":

	questions = [
		inquirer.Text("version", message="Please enter a version, for sample 1.00.0", default='2.00.0'),
		inquirer.Checkbox(
			"release_type",
			message="Please select a release type",
			choices=["regular", "hotfix", "adhoc"],
			default=['regular']
		),
		inquirer.Text("seq", message="please enter the sequence", default='1'),
		inquirer.Confirm(
			"correct",
			message="This will generate a tag name. Continue?",
			default=False,
		),
	]
	answers = inquirer.prompt(questions)

	if answers['correct']:
		tag_name = build_version(answers)
		print(tag_name)
	else:
		print('nothing to do')
```

整体流程非常的简单

- 提示用户输入版本号，也就是类似 1.00.0 这串，由于给了 default 值，所以只需要稍微修改一下就可以了
- 提示用户选择发布类型，默认是 regular，也就是正常发布
- 提示用户输入当天的发布次数，默认值给了 1，用户可以自行修改
- 提示用户确认
- 打印版本号

### 效果演示

```bash
➜  deploy python create_tag.py
[?] Please enter a version, for sample 1.00.0: 2.00.0
[?] Please select a release type:
 > X regular
   o hotfix
   o adhoc

[?] please enter the sequence: 1
[?] This will generate a tag name. Continue? (y/N): y

v2.00.0-20221118-1
```

### 后续

由于我打通了 gitlab 的 api，版本号生成之后我会提示用户选择项目并自动去 release 分支打 tag，如果 tag 创建成功的话，我就自动选择该 tag 进行发布。下面是一些示例代码。

```python
questions = [
		inquirer.Confirm(
			"create_tag",
			message=f"tag name is {tag_name}, do you want to create a tag on gitlab?",
			default=False,
		),
	]
	answers = inquirer.prompt(questions)

	if answers['create_tag']:
		questions = [
			inquirer.Checkbox(
				"project",
				message="Please select a project",
				choices=["project A", "project B", "Porject C"],
			),
		]
		answers = inquirer.prompt(questions)

		git = GitLabAPI(answers['project'])
		git.create_tag(tag_name)
	else:
		print('nothing to to. quit')
		exit()
```

### 总结

当一件事情需要周期性的手工做 n 次的时候，花一点点时间进行自动化是一件非常值得的事情的。既提升了工作效率，又提升了代码量，一举两得何乐不为呢？
