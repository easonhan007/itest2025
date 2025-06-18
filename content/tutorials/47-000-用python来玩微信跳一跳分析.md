---
weight: 0
title: 用Python来玩微信《跳一跳》分析
date: '2018-01-22T01:10:24+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1445712525433-eba07da78bd2?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



上周无意中发现的一个《跳一跳》辅助的开源程序；现在已经12k的Star了。

https://github.com/wangshub/wechat_jump_game

今天要就来简单分析一下它的实现原理。当然，目的肯学是学习啦！

自动化的实现主要用到两个技术。


#### ADB
---

官方网站：http://adbshell.com/

Android Debug Bridge（ADB）是一种命令行工具，可以让PC与Android模拟器或连接的手机之间进行通信。

做Android开发的同学都懂，我们在PC上开发App，需要通过“adb shell install ”命令安装到Android模拟器或连接的手机上运行。当然，Android自动化测试也离不开它。

这里主要用它来截图，以便来计算跳跃的每个箱子之间的距离。还有最后执行对棋子的按压。

通过数据线将手机与PC之间连接，开启USB调试功能。通过“adb devices”命令检查是否可以连接调试设备。

```
> adb devices
List of devices attached
d552be87        device
```

打开微信，启动《跳一跳》小游戏，通过“adb shell screencap”命令截图。

```
D:\> adb shell screencap -p /sdcard/autojump.png
D:\> adb pull /sdcard/autojump.png
```

“adb pull”命令将保存在手机里的截图拉取到PC当前目录。所以，我在D盘执行该命令，那么图片就会保存到D盘根目录。如下：

![](http://img.testclass.net/wechat_jump_img.png)


#### python
---

首先，你需要有Python开发环境。

其次，将项目用Git克隆（或直接下载）到本地。

通过pip安装依赖库：

> pip install requirements.txt

python部分分手动版和自动版，手动版会每次将截图展示在PC端，手动点击下一个跳跃的箱子，不需要考虑按压时间；所以，想跳哪里就点哪里。

自动版就高级了，运行脚本后自动在手机上进行跳一跳游戏。接一来分析自动版实现（webchat_jump_auto.py）。作者在脚本里已经写得很清楚了。


<font color="blue">
__=== 思路 ===__

核心：每次落稳之后截图，根据截图算出棋子的坐标和下一个块顶面的中点坐标，根据两个点的距离乘以一个时间系数获得长按的时间。


识别棋子：靠棋子的颜色来识别位置，通过截图发现最下面一行大概是一条直线，就从上往下一行一行遍历，比较颜色（颜色用了一个区间来比较）找到最下面的那一行的所有点，然后求个中点，求好之后再让 Y 轴坐标减小棋子底盘的一半高度从而得到中心点的坐标。



识别棋盘：靠底色和方块的色差来做，从分数之下的位置开始，一行一行扫描，由于圆形的块最顶上是一条线，方形的上面大概是一个点，所以就用类似识别棋子的做法多识别了几个点求中点，这时候得到了块中点的 X 轴坐标，这时候假设现在棋子在当前块的中心，根据一个通过截图获取的固定的角度来推出中点的 Y 坐标。


最后：根据两点的坐标算距离乘以系数来获取长按时间（似乎可以直接用 X 轴距离）。</font>



关键点分析：



一个关键字是如何找到图片中的棋子和棋盘的坐标，find_piece_and_board()函数接收游戏截图。这里用到了Pillow库的两个方法有。size语句获取图片的宽高，主要限定像素遍历的范围，load()方法加载图片，找到它的像素。通过像素对比找到棋子的坐标和棋盘的坐标。


```python
def find_piece_and_board(im):
    """
    寻找关键坐标
    """
    w, h = im.size

    piece_x_sum = 0
    piece_x_c = 0
    piece_y_max = 0
    board_x = 0
    board_y = 0
    scan_x_border = int(w / 8)  # 扫描棋子时的左右边界
    scan_start_y = 0  # 扫描的起始 y 坐标
    im_pixel = im.load()
    # 以 50px 步长，尝试探测 scan_start_y
    for i in range(int(h / 3), int(h*2 / 3), 50):
        last_pixel = im_pixel[0, i]
        for j in range(1, w):
            pixel = im_pixel[j, i]
            # 不是纯色的线，则记录 scan_start_y 的值，准备跳出循环
            if pixel != last_pixel:
                scan_start_y = i - 50
                break
        if scan_start_y:
            break
    print('scan_start_y: {}'.format(scan_start_y))

    # 从 scan_start_y 开始往下扫描，棋子应位于屏幕上半部分，这里暂定不超过 2/3
    for i in range(scan_start_y, int(h * 2 / 3)):
        # 横坐标方面也减少了一部分扫描开销
        for j in range(scan_x_border, w - scan_x_border):
            pixel = im_pixel[j, i]
            # 根据棋子的最低行的颜色判断，找最后一行那些点的平均值，这个颜
            # 色这样应该 OK，暂时不提出来
            if (50 < pixel[0] < 60) \
                    and (53 < pixel[1] < 63) \
                    and (95 < pixel[2] < 110):
                piece_x_sum += j
                piece_x_c += 1
                piece_y_max = max(i, piece_y_max)

    if not all((piece_x_sum, piece_x_c)):
        return 0, 0, 0, 0
    piece_x = int(piece_x_sum / piece_x_c)
    piece_y = piece_y_max - piece_base_height_1_2  # 上移棋子底盘高度的一半

    # 限制棋盘扫描的横坐标，避免音符 bug
    if piece_x < w/2:
        board_x_start = piece_x
        board_x_end = w
    else:
        board_x_start = 0
        board_x_end = piece_x

    for i in range(int(h / 3), int(h * 2 / 3)):
        last_pixel = im_pixel[0, i]
        if board_x or board_y:
            break
        board_x_sum = 0
        board_x_c = 0

        for j in range(int(board_x_start), int(board_x_end)):
            pixel = im_pixel[j, i]
            # 修掉脑袋比下一个小格子还高的情况的 bug
            if abs(j - piece_x) < piece_body_width:
                continue

            # 修掉圆顶的时候一条线导致的小 bug，这个颜色判断应该 OK，暂时不提出来
            if abs(pixel[0] - last_pixel[0]) \
                    + abs(pixel[1] - last_pixel[1]) \
                    + abs(pixel[2] - last_pixel[2]) > 10:
                board_x_sum += j
                board_x_c += 1
        if board_x_sum:
            board_x = board_x_sum / board_x_c
    last_pixel = im_pixel[board_x, i]

    # 从上顶点往下 +274 的位置开始向上找颜色与上顶点一样的点，为下顶点
    # 该方法对所有纯色平面和部分非纯色平面有效，对高尔夫草坪面、木纹桌面、
    # 药瓶和非菱形的碟机（好像是）会判断错误
    for k in range(i+274, i, -1):  # 274 取开局时最大的方块的上下顶点距离
        pixel = im_pixel[board_x, k]
        if abs(pixel[0] - last_pixel[0]) \
                + abs(pixel[1] - last_pixel[1]) \
                + abs(pixel[2] - last_pixel[2]) < 10:
            break
    board_y = int((i+k) / 2)

    # 如果上一跳命中中间，则下个目标中心会出现 r245 g245 b245 的点，利用这个
    # 属性弥补上一段代码可能存在的判断错误
    # 若上一跳由于某种原因没有跳到正中间，而下一跳恰好有无法正确识别花纹，则有
    # 可能游戏失败，由于花纹面积通常比较大，失败概率较低
    for j in range(i, i+200):
        pixel = im_pixel[board_x, j]
        if abs(pixel[0] - 245) + abs(pixel[1] - 245) + abs(pixel[2] - 245) == 0:
            board_y = j + 10
            break

    if not all((board_x, board_y)):
        return 0, 0, 0, 0
    return piece_x, piece_y, board_x, board_y
```

另一个关键点就是如何测算距离与按压时间的关系（按得时间越长跳得越远），并执行不能时长的按压。在jump()函数中，press_coefficient 是一个时间与距离的系数，distance是距离，两者相乘得到一个按压时长。通过“adb shell input swipe”命令完成对棋子坐标的不同时长按压。

```python
def jump(distance):
    """
    跳跃一定的距离
    """
    press_time = distance * press_coefficient
    press_time = max(press_time, 200)   # 设置 200ms 是最小的按压时间
    press_time = int(press_time)
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=swipe_x1,
        y1=swipe_y1,
        x2=swipe_x2,
        y2=swipe_y2,
        duration=press_time
    )
    print(cmd)
    os.system(cmd)
    return press_time
```

其它部分的代码，这里就不一一分析，感兴趣的去分析源码。

最后，通过python来执行 wechat_jump_auto.py 文件。

```
>  python wechat_jump_auto.py

Load config file from D:\github\wechat_jump_game-master/config/1920x1080/config.json
请确保手机打开了 ADB 并连接了电脑，然后打开跳一跳并【开始游戏】后再用本程序，确定开始？ y/
n [y]: y
程序版本号：1.1.1
error: no devices/emulators found
**********
Screen: Physical size: 1080x1920
Density: Physical density: 480
Device: surabaya
Phone OS:
Host OS: win32
Python: 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]
**********
minLayer = 0, maxLayer = 4294967295
capture ok : w = 1080, h = 1920, s = 1088, f = 1, size = 8355840
/sdcard/autojump.png: 1 file pulled. 3.3 MB/s (58596 bytes in 0.017s)
采用方式 0 获取截图
……
```

附带效果视频：
<div id="mod_tenvideo_flash_player_1516593959610" class="tenvideo_player"><embed wmode="direct" flashvars="vid=m13326hvg65&amp;tpid=0&amp;showend=1&amp;showcfg=1&amp;searchbar=1&amp;pic=//shp.qpic.cn/qqvideo_ori/0/m13326hvg65_496_280/0&amp;skin=http://imgcache.qq.com/minivideo_v1/vd/res/skins/TencentPlayerMiniSkin.swf&amp;shownext=1&amp;list=2&amp;autoplay=0" src="https://imgcache.qq.com/tencentvideo_v1/player/TPout.swf?max_age=86400&amp;v=20140714" quality="high" name="tenvideo_flash_player_1516593959610" id="tenvideo_flash_player_1516593959610" bgcolor="#000000" width="670px" height="502px" align="middle" allowscriptaccess="always" allowfullscreen="true" type="application/x-shockwave-flash" pluginspage="http://get.adobe.com/cn/flashplayer/"></div>


总结：

帮你刷分不是本文目的，本文背后的思考是“如何自动化测试移动游戏”，昨天看InfoQ上百度公司‘“一框多用”Android通用脚本测试解决方案’的分享，其中就用涉及到了这方面的技术，值得大家学习。

http://www.infoq.com/cn/presentations/the-solution-of-android-general-script-test




原始封面

![课程图片](https://images.unsplash.com/photo-1445712525433-eba07da78bd2?w=300)

