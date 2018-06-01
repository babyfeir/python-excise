# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"

score = int(input('请输入您的分数：'))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <90:
    print('B')
elif 60 <= score < 80:
    print('C')
elif 0 <= score < 60:
    print('D')
else:
    print('输入错误！')