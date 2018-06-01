# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，计算当前文件夹下所有文件的大小
'''
import os


def get_file_size(file_path):
    os.chdir(file_path)

    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            size = os.path.getsize(each_file)
            print(each_file + '【%dBytes】' % size)


if __name__ == '__main__':
    path = input(r'请输入要访问的文件夹路径：')
    get_file_size(path)
