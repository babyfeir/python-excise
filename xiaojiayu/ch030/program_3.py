# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求
查找mp4，rmvb，avi的格式即可），并把创建一个文件（vedioList.txt)存放所有找到的文件的路径。
'''
import os


def search_video(file_path):
    os.chdir(file_path)
    fp = open('E:\\study\\Python\\xiaojiayu\\ch030\\videoList.txt', '+a')

    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            if os.path.splitext(each_file)[1] in ('.mp4', '.rmvb', '.avi'):
                fp.write(os.getcwd() + each_file + '\n\n')

        if os.path.isdir(each_file):
            search_video(each_file)
            os.chdir(os.pardir)
    fp.close()

if __name__ == '__main__':
    search_path = input(r'请输入待查找的初始目录：')
    search_video(search_path)
