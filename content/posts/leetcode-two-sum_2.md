---
weight: 1
title: "leetcode最有名的简单算法题：two sum"
date: 2024-03-08T09:01:36+08:00
lastmod: 2024-03-08T09:01:36+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "挺有意思"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1699838222616-5acc9fdaeced?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

应该还是有很多同学在刷题找工作吧，如果大家刷 leetcode 的话，推荐的做法是从简单到难，这样一来 two sum 是大家绕不过去的最著名的简单算法题了，废话不多说，先看题目的描述。

给定一个整数数组  `nums`  和一个整数目标值  `target`，请你在该数组中找出  **和为目标值** *`target`*  的那  **两个**  整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]

```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]

```

**提示：**

- `2 <= nums.length <= 104`
- `109 <= nums[i] <= 109`
- `109 <= target <= 109`
- **只会存在一个有效答案**

**进阶：**你可以想出一个时间复杂度小于  `O(n2)`  的算法吗？

### 最无脑的解法

看到题目之后我随手写了一个版本，大概 1 分钟就写完了

```python
for i, outer in enumerate(nums):
	for j, inner in enumerate(nums):
		if(i != j):
			tmp = outer + inner
			if tmp == target:
				return [i, j]
```

运行之后发现没啥问题，那就提交吧。

结果 leetcode 告诉我运行时间超出限制，可能是因为半夜脑子不行的关系，我百思不得其解，毕竟又不是不能用，能写出来就让我过得了。

### O(n\*n)的正确解法

后来稍微研究了一下题目，发现其实可以改进一点。

拿 [2,7,11,15]来说，其实代码运行的顺序可以是：

- 先拿 2，然后遍历剩下的[7, 11, 15]进行相加
- 再拿 7，遍历后面的[11,15]
- 再拿 11，遍历后面的[15]

也就是说每次遍历其实只要从后面剩下的部分开始，不需要再回到头部，毕竟正确结果只有 1 个，加过了的就不需要重复了。

知道了思路，改起来就方便了。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, outer in enumerate(nums):
            for j in range(i + 1, len(nums)):
                tmp = nums[j] + outer
                if tmp == target:
                    return [i, j]
```

提交之后发现没有问题，速度上击败了 18%的用户，看来还有更低算法复杂度的解法。

时间来到了半夜，还是睡觉先。

### O(n)的解法

时间来到了第 2 天。

题目的重点应该是只有 1 个有效的答案，而且因为给出的数组是没有顺序的，所有不用往 logn 的算法复杂度去思考，应该有 On 的解法。

应该可以用空间换时间。遍历数字把 target-num[i]的值作为 key 存在 dict 里，value 就是其 index，后面如果遇到 num[i]正好等与这个差值，那么返回 i 和对应的差值的 index 就好了。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [i, hash_table[nums[i]]]
            else:
                hash_table[target-nums[i]] = i
```

这里之遍历了一次，而且 dict 里判断元素是否存在的算法复杂度是 O(1)，因此整体来说复杂度还是 O(n)

### 总结

之所有去翻 two sum 这个题目是因为有次在某个群里看到有人说精通 two sum 的 4 种写法，很好奇，于是去写了一下，发现只写出了 2 种，自愧不如，不知道还有没有其他精妙的解决方案呢。
