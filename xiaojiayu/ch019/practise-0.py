# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，既可顺读，也可倒读。
例如：上海自来水来自海上
'''

def judgeWords(sentence):
    length = len(sentence)
    for i in range(length // 2):
        if sentence[i] == sentence[-(i + 1)]:
            continue
        else:
            print('不是回联文')  # 草草草草草草操
            break
    else:
        print('是回联文')

sen = input('请输入一句话：')
judgeWords(sen)
