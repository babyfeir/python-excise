# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
定义普通函数实现阶乘
def factor(num):
	sum = 1
	for i in range(1,num+1):
		sum *= i
	return sum

number = int(input('请输入一个整数：'))
result = factor(number)
print('%d的阶乘等于:%d' %(number,result))
'''

'''
用递归方法来实现阶乘
'''
def factor(n):
    if n==1:
        return 1
    else:
        return n*factor(n-1)

number = int(input('请输入一个整数：'))
result = factor(number)
print('%d的阶乘等于:%d' %(number,result))
