# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，实现“全部替换”功能
'''

def replace_words(file_name, original, destination):
    f1 = open(file_name, 'r')

    list = []
    count = 0

    for each in f1:
        if original in each:
            count = each.count(original)
            each = each.replace(original, destination)
        list.append(each)

    print('文件 %s 中共有%d个【%s】' %(file_name, count, original))
    print('您确定要把所有的【%s】替换为【%s】吗？'%(original, destination))
    confirm = input('【YES/NO】：')

    if confirm in ['yes','YES', 'Yes']:
        f2 = open(file_name, 'w')
        f2.writelines(list)
        f2.close()
    else:
        print('文件不做修改！')

    f1.close()

if __name__ == '__main__':
    file_name = input('请输入文件名：')
    original = input('请输入需要替换的单词或字符：')
    destination = input('请输入新的单词或字符：')

    replace_words(file_name, original, destination)

