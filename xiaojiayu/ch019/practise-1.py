# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其他字符的个数。
'''

def count(*args):
    length = len(args)
    for i in range(length):
        sum1 = 0   # 统计空格数
        sum2 = 0   # 统计数字数
        sum3 = 0   # 统计英文字符数
        sum4 = 0   # 统计其他字符数
        for j in range(len(args[i])):
            if args[i][j].isdigit():
                sum2 += 1
            elif args[i][j].isalpha():
                sum3 += 1
            elif args[i][j].isspace():
                sum1 += 1
            else:
                sum4 += 1
        print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个' %(i+1, sum3, sum2, sum1, sum4))

count('I love fishc.com.', 'I love you, you love me.', 'bill, I love you too2!')






