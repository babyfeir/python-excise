# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"
'''
编写一个函数findstr()，该函数统计一个长度为2的子字符吕在另一个字符串中出现的次数。
例如：假定输入的字符串为"You cannot improve your part, but you can improve your future.
Once time is wasted, life is wasted."，子字符串"im"，函数执行后打印”子字符串在目录字符串中共出现3次“.
'''
def findstr(strs, search_key):
    '''统计子字符串在原字符串中出现的次数'''
    count = 0
    target_len = len(strs)

    if search_key not in strs:
        print('在目标字符串中未找到字符串！')
    else:
        for num in range(target_len - 1):
            if strs[num] == search_key[0]:
                if strs[num+1] == search_key[1]:
                    count += 1

        print('子字符串在目标字符串中共出现 %d 次' % count)

desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串（两个字符）：')
findstr(desStr, subStr)





