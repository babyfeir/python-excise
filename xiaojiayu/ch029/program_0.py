# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，接受用户的输入并保存为新的文件
'''
def save_file(file_name):
    f = open(file_name,'w')

    print("请输入内容【单独输入':w'保存退出】：")
    while True:
        file_content = input()
        if file_content != ':w':
            f.write(file_content+'\n')
        else:
            break

    f.close()

if __name__ == '__main__':
    file_name = input('请输入文件名：')
    save_file(file_name)
