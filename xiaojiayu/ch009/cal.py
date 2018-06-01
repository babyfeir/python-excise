# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"
"""
编写一个程序，求 100~999 之间的所有水仙花数。
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数.
"""

for data in range(100,1000):
    d1 = data // 100%10
    d2 = data // 10%10
    d3 = data // 1%10
    sum = d1**3 + d2**3 + d3**3
    if data == sum:
        print(data)

    """
    lens = len(str(data))
    count = 0
    temp = 0
    sum = 0
    while count < lens:
        temp = data // (10**count) %10
        sum = sum + temp**3
        count += 1
    if data == sum:
        print(data)
    """