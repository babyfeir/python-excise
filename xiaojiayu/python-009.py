# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"

"""
# example1：
bingo = '小甲鱼是帅哥'
answer = input('请输入小甲鱼最想听的一句话：')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）：')

print('哎哟，帅哦~')
print('您真是小甲鱼肚子里的蛔虫啊！')
"""

# example2：
# 终止本轮循环，并开始下一轮循环，注意在开始下一轮循环前会测试一下循环条件，为真时才会开始下一轮循环，如果为假则退出循环
for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)
