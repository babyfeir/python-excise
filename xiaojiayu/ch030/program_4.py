# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有
含有该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个
字符）。
'''
import os

txt_list = []

def print_lines(path, keyword):
    print('在文件【%s】中找到关键字【%s】' %(path, keyword))

def search_files(dir_path):
    os.chdir(dir_path)
    # 查找所有.txt文件
    for each_file in os.listdir(os.curdir):
        if '.txt' in each_file:
            txt_list.append(os.getcwd() + os.sep + each_file)

        if os.path.isdir(each_file):
            search_files(each_file)
            os.chdir(os.pardir)

    return txt_list

def search_keyword(path, keyword):
    target_file =search_files(path)

    for each_file in target_file:
        row_count = 0

        fp = open(each_file, 'r')
        # 搜索单个txt文件中的内容是否包含关键字
        for each_line in fp:
            row_count += 1
            if keyword in each_line:
                print_lines(each_file, keyword)
                col_count = 0
                # 找出指定行中关键字的位置
                if each_line.count(keyword) > 1:
                    col_count = each_line.find(keyword, col_count) + 1
                else:
                    col_count = each_line.find(keyword, col_count)
                    # pos[row_count] = col_count
                    print('关键字出现在第 %d 行，第 [%d, %d]个位置。' %(row_count, row_count, col_count))
        fp.close()

if __name__ == '__main__':
    keyword = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
    choose = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：'%keyword)
    if choose == 'YES' or choose == 'yes' or choose == 'Yes':
        dir_path = os.getcwd()
        search_keyword(dir_path, keyword)

