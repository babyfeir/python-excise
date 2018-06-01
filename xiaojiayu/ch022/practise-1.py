# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
使用递归编写一个函数,利用欧几里得算法求最大公约数,例如gcd(x,y)返回值为参数x和参数y的最大公约数.
'''

def gcd(x, y):
    if x % y:
        return gcd(y, x%y)
    else:
        return y

number1 = int(input('请输入一个整数:'))
number2 = int(input('请输入一个整数:'))
result = gcd(number1, number2)
print('%d和%d的最大公约数值为:%d' %(number1, number2, result))
