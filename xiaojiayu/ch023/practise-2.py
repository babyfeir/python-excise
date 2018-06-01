# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
使用递归编程求解以下问题：
有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁，问第4个人岁数，他说比第3个人大2岁。问第三个人，
又说比第2个人大两岁。问第2个人，说比第一个人大两岁。最后瓿第一个人，他说是10岁。请问第五个人多大？
'''
def Age(age, count):
    if count == 1:
        return age
    else:
        return Age(age+2, count-1)

print(Age(10, 5))



