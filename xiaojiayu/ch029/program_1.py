# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置
'''
def compare_file(file_name1, file_name2):
    f1 = open(file_name1,'r')
    f2 = open(file_name2, 'r')

    differ = []
    list1 = []
    list2 = []
    rownum = 0

    for line1 in f1:
        list1.append(line1)

    for line2 in f2:
        list2.append(line2)

    for i in range(len(list1)):
        rownum += 1
        if list1[i] != list2[i]:
            differ.append(rownum)

    f1.close()
    f2.close()

    return differ

if __name__ == '__main__':
    file_name1 = input('请输入需要比较的头一个文件名：')
    file_name2 = input('请输入需要比较的另一个文件名：')
    differ_num = compare_file(file_name1, file_name2)

    if len(differ_num) == 0:
        print('两个文件完全一样！')
    else:
        print('两个文件有【%d】处不同：' %len(differ_num))
        for each in differ_num:
            print('第 %d 行不一样' %each)
