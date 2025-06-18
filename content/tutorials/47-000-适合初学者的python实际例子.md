---
weight: 0
title: 适合初学者的python实际例子
date: '2018-05-10T12:55:59+08:00'
lastmod: '2025-06-17T17:29:15+08:00'
draft: false
author: 乙醇
authorLink: https://github.com/easonhan007
images: []
resources:
- name: featured-image
  src: https://images.unsplash.com/photo-1444090542259-0af8fa96557e?w=300
tags: []
categories:
- 博客合集
lightgallery: true
toc:
  auto: false
---



最近在github上发现了一个有意思的项目，很适合初学者学习python代码。

学习一门语言刚开始的时候是很枯燥的，各种概念语法以及无聊的打印都会让人失去更进一步学习的动力。

很多同学在学习了一段时间之后甚至会怀疑学习语言的用处，因为总是写不出东西，只会写一些简单的打印代码。

这个叫做[geekcomputers/Python](https://github.com/geekcomputers/Python)的项目很好的回答了一个问题，就是学习python可以做什么。

仔细观察里面的例子，我们可以发现写一些简单的python代码就可以做很多有意思的事情，比如

* 批量修改文件的后缀名
* 显示文件的一些信息
* 测试某个文件夹是否存在，不存在就自动创建
* 搜索所有目录下的log文件，并自动压缩归档
* 把所有创建时间超过240天的文件移动到某个文件夹
* 自动发twitter
* 下载最新的漫画
* 下载视频网站的视频
* ......

这些例子的代码都很简单，推荐大家这样学习

* 首先照着这些代码敲一遍
* 让代码可以正确运行
* 为每一行代码写上注释
* 只保留注释，去掉具体代码，看看自己能不能写出来

相信经过一段时间的努力，你应该可以熟练使用python去实现一些简单有趣的功能了。

最后附上例子的链接。

- [batch_file_rename.py](https://github.com/geekcomputers/Python/blob/master/batch_file_rename.py) - This batch renames a group of files in a given directory, once you pass the current and the new extensions.

- [create_dir_if_not_there.py](https://github.com/geekcomputers/Python/blob/master/create_dir_if_not_there.py) - Checks to see if a directory exists in the users home directory, if not then create it.

- [Fast Youtube Downloader](https://github.com/geekcomputers/Python/blob/master/youtube-downloader%20fast.py) - Downloads youtube videos quickly with parallel threads using aria2c

- [Google Image Downloader](https://github.com/geekcomputers/Python/tree/master/Google%20Image%20Downloader) - Query the specific term and retrieve images from the google image database.

- [dir_test.py](https://github.com/geekcomputers/Python/blob/master/dir_test.py) - Tests to see if the directory `testdir` exists, if not it will create the directory for you.

- [env_check.py](https://github.com/geekcomputers/Python/blob/master/env_check.py) - This script will check to see if all of the environment variables required are set.

- [fileinfo.py](https://github.com/geekcomputers/Python/blob/master/fileinfo.py) - Shows file information for a given file.

- [folder_size.py](https://github.com/geekcomputers/Python/blob/master/folder_size.py) - Scans the current directory and all subdirectories and displays the size.

- [logs.py](https://github.com/geekcomputers/Python/blob/master/logs.py) - This script will search for all `*.log` files in the given directory, zip them using the program you specify, and then date stamp them.

- [move_files_over_x_days.py](https://github.com/geekcomputers/Python/blob/master/move_files_over_x_days.py) - Moves all files over 240 days old from the source directory to the destination directory.

- [nslookup_check.py](https://github.com/geekcomputers/Python/blob/master/nslookup_check.py) - This simple script opens the file `server_list.txt` and then does an nslookup for each one to check the DNS entry.

- [osinfo.py](https://github.com/geekcomputers/Python/blob/master/osinfo.py) - Displays some information about the OS on which you are running this script.

- [ping_servers.py](https://github.com/geekcomputers/Python/blob/master/ping_servers.py) - This script, depending on the arguments supplied, will ping the servers associated with that application group.

- [ping_subnet.py](https://github.com/geekcomputers/Python/blob/master/ping_subnet.py) - After supplying the first 3 octets this file scans the final range for available addresses.

- [powerdown_startup.py](https://github.com/geekcomputers/Python/blob/master/powerdown_startup.py) - This file goes through the server list and pings the machine, if it is up it will load the putty session, if it is not it will notify you.

- [puttylogs.py](https://github.com/geekcomputers/Python/blob/master/puttylogs.py) -  This file zips up all the logs in the given directory.

- [script_count.py](https://github.com/geekcomputers/Python/blob/master/script_count.py) - This file scans the scripts directory and gives a count of the different types of scripts.

- [script_listing.py](https://github.com/geekcomputers/Python/blob/master/script_listing.py) - This file will list all the files in the given directory, and go through all the subdirectories as well.

- [testlines.py](https://github.com/geekcomputers/Python/blob/master/testlines.py) - This simple script opens a file and prints out 100 lines of whatever is the set for the line variable.

- [tweeter.py](https://github.com/geekcomputers/Python/blob/master/tweeter.py) - This script allows you to tweet text or a picture from the terminal.

- [serial_scanner.py](https://github.com/geekcomputers/Python/blob/master/serial_scanner.py) contains a method called ListAvailablePorts which returns a list with the names of the serial ports that are in use in the computer, this method works only on Linux and Windows (can be extended for mac osx). If no port is found, an empty list is returned.

- [get_youtube_view.py](https://github.com/geekcomputers/Python/blob/master/get_youtube_view.py) - This is very simple python script to get more views for your youtube videos. Useful for repeating songs on youtube.

- [CountMillionCharacter.py](https://github.com/geekcomputers/Python/blob/master/CountMillionCharacter.py) And [CountMillionCharacter2.0](https://github.com/geekcomputers/Python/blob/master/CountMillionCharacters-2.0.py).py - Counts character scripts, or how much characters are present on any text based file.

- [xkcd_downloader.py](https://github.com/geekcomputers/Python/blob/master/xkcd_downloader.py) - Downloads the latest XKCD comic and places them in a new folder called "comics".

- [timymodule.py](https://github.com/geekcomputers/Python/blob/master/timymodule.py) - A great alternative to Pythons 'timeit' module and easier to use.

- [calculator.py](https://github.com/geekcomputers/Python/blob/master/calculator.py) - Uses Python's eval() function to implement a calculator.

- [Google_News.py](https://github.com/geekcomputers/Python/blob/master/Google_News.py) - Uses BeautifulSoup to provide Latest News Headline along with news link.

- [cricket_live_score](https://github.com/geekcomputers/Python/blob/master/Cricket_score.py) - Uses BeautifulSoup to provide live cricket score.

- [youtube.py](https://github.com/geekcomputers/Python/blob/master/youtube.py) - Takes a song name as input and fetches the youtube url of the best matching song and plays it.  




原始封面

![课程图片](https://images.unsplash.com/photo-1444090542259-0af8fa96557e?w=300)

