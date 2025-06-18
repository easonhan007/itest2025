---
weight: 0
title: 使用python实现测试工具(五)
date: '2018-08-20T06:55:32+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1532274402911-5a369e4c4bb5?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



本系列教程使用的python版本是**3.6.3**。

### 背景

我们在进行测试的时候经常需要去生成一些测试数据，这就是所谓的造数据。

生成随机的用户真实姓名是非常常见的需求，这一节我们看一下如何使用python的来实现这个功能。

我们将实现随机生成英文名的功能。

英文名的生成规则是```first_name last_name```，也就是名在前，姓在后，中间空格分隔。

### 代码

```python

import random

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
    'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
    'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
    'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
    'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
    'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
    'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
    'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
    'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
    'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
    'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
    'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
    'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
    'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
    'Woolysocks')

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
    'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
    'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
    'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
    'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
    'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
    "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
    'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
    'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
    'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
    'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
    'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
    'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
    'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')


def random_full_name():
    return "{} {}".format(random.choice(first), random.choice(last))

print(random_full_name())

```

### 分析

代码很简单，定义2个原组，就是小括号括起来的那个像列表的东西，分别是```last```和```first```。

我们的生成算法就是随机从first和last里选1个first_name和last_name，然后拼成1个完整的英文名。

需要注意的1个小点

* ```random.choice(seq)```的用法。从seq里随机选1个元素；

### 源码地址

[github地址](https://github.com/easonhan007/simple_test_tools)




原始封面

![课程图片](https://images.unsplash.com/photo-1532274402911-5a369e4c4bb5?w=300)

