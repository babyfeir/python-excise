# coding=utf-8
"""
calc.py
要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”
"""

temp = input('请输入1-100之间的数字：')
number = int(temp)
if 1<= number <=100:
    print('你妹好漂亮')
else:
    print('你大爷好丑')