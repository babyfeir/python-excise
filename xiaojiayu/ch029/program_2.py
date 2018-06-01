# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上。
'''
def show_file(file_name, rownum):
    print('\n文件%s的前%d的内容如下：\n' %(file_name, rownum))
    f = open(file_name,'r')

    for each in range(1, rownum+1):
        print(f.readline())

    f.close()

if __name__ == '__main__':
    file_name = input(r'请输入要打开的文件（c:\\test.txt）：')
    rownum = int(input('请输入要显示该文件前几行：'))
    show_file(file_name, rownum)

