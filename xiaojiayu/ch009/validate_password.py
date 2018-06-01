# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"
"""
设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内
"""
password = 'python'
times = 3
while times > 0:
    input_pwd = input('请输入用户密码：')
    if input_pwd == password:
        print('恭喜您，登录成功！')
        break
    elif '*' in input_pwd:
        print('密码中不能含有*，请重新输入，您还有',times,'次机会重新输入次数。')
    else:
        print('密码输入错误，您还有',times-1,'次机会重新输入次数。')
        times -= 1
