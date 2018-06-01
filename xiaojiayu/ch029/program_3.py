# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。（如输入
13：21打印第13行到第21行，输入：21打印前21行，输入21：则打印从
第21行开始到文件结尾所有内容。
'''
def show_file(file_name, rownum):
    rownum = rownum.strip()

    start, end = rownum.split(':',1)

    if start == '':
        start = 1
    if end == '':
        end = -1

    if start == '1' and end == '-1':
        prompt = '的全文'
    if start == '1' and end != '-1':
        prompt = '从开始到第%s行'%end
    if start != '1' and end =='-1':
        prompt = '从第%s行到末尾'%start
    if start != '1' and end != '-1':
        prompt = '从第%s行到第%s行'%(start, end)

    print('\n文件%s%s的内容如下：\n' %(file_name, prompt))

    begin = int(start) - 1
    ending = int(end)
    lines = ending - begin

    f = open(file_name,'r')

    for i in range(begin):
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline())

    f.close()

if __name__ == '__main__':
    file_name = input(r'请输入要打开的文件（c:\\test.txt）：')
    rownum = input('请输入要显示的行数【格式如 13:21 或 :21 或 21:】：')

    show_file(file_name, rownum)

