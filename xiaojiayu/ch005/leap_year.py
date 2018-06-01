# !/usr/bin/env python
# -*- coding: UTF-8 -*-

temp = input('请输入一个年份：')
while not temp.isdigit():
    print('请输入数字，谢谢合作！！')
    temp = input('请输入一个年份：')
year = int(temp)
if year%4 == 0 or year%400 == 0:
    print('恭喜您，您输入的{0}年是闰年！'.format(year))
else:
    print('很抱歉，您输入的{0}年不是闰年！'.format(year))
