# !/usr/bin/env python
# -*- coding: UTF-8 -*-
def discoounts(price, rate):
    final_price = price * rate
    # print('这里试图打印局部变量old_price的值：', old_price)
    old_price = 50
    print('修改后old_price的值是：', old_price)
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discoounts(old_price, rate)
print('修改后old_price的值是：', old_price)
print('打折后的价格是：', new_price)

