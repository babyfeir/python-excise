# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
使用递归编写一个power()函数模拟内建函数pow(),即power(x,y)为计算并返回x的y次幂的值.
'''

def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y-1)

number1 = int(input('请输入一个整数:'))
number2 = int(input('请输入一个整数作幂:'))
result = power(number1, number2)
print('%d的%d次幂的值为:%d' %(number1, number2, result))
