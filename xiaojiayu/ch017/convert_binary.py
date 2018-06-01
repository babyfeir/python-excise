# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"
'''
编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式
'''

def convert_binary(number):
    temp = []
    result = ''

    while number:
        remainder = number % 2
        number = number // 2
        temp.append(remainder)

    # 方法一：
    for i in range(len(temp)):
        result += str(temp.pop())

    return result

    # 方法二：
    # return ''.join(temp[::-1])

print(convert_binary(62))

