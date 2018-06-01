# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"
'''
题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
编写一个程序，找出所有的水仙花数
'''
def find_flower():
    '''
    找到水仙花数
    '''
    for number in range(100,1000):
        num1 = number // 100
        num2 = (number % 100) // 10
        num3 = (number % 100) % 10
        sum = num1 **3 + num2 **3 + num3 **3
        if sum == number:
            print('数字%d是一个水仙花数' % number)
        else:
            continue

find_flower()
