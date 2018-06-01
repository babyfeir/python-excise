# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
斐波那契数列，假设需要求出经历了20个月后，总共有多少对小兔崽子
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('输入错误！')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

result = fab(20)
if result != -1:
    print('总共有%d对小兔崽子诞生' %result)
'''
def fab(n):
    if n < 1:
        print('输入错误！')
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(20)
if result != -1:
    print('总共有%d对小兔崽子诞生' %result)
