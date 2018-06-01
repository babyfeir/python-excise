# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：
get_digits(12345) ==> [1,2,3,4,5]
def get_digits(n):
    count = len(str(n)) - 1
    lists = []

    while count >= 0:
        num = n // 10**count
        n %= 10**count
        count -= 1
        lists.append(num)
    return lists

print(get_digits(1268733))
'''
result = []
def get_digits(n):
    if n > 0:
        result.insert(0, n%10)
        get_digits(n//10)

get_digits(1268733)
print(result)

