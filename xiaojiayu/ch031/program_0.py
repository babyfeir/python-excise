#!/usr/bin/env python
# encoding: utf-8
'''
@author: luohui
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: program_0.py
@time: 2018/5/31 15:25
@desc:
'''
'''
编写一个程序，这次要求使用pickle将文件record.txt里的对话按照以下要求腌制成不同文件：
小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼：”）
小客服的对话单独保存为girl_*.txt的文件（去掉“小客服：”）
文件中总共有三段对话，分别保存为boy_1.txt，girl_1.txt,boy_2.txt,girl_2.txt,
boy_3.txt,girl_3.txt共6个文件（提示：文件中不同的对话间已经使用“=======”分割）
'''
import pickle

def save_to_file(boy, girl, number):
    boy_filename = 'boy' + '_' + str(number) +'.txt'
    girl_filename = 'girl' + '_' + str(number) +'.txt'

    boy_file = open(boy_filename,'wb')
    girl_file = open(girl_filename,'wb')

    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)

    boy_file.close()
    girl_file.close()

def split_file(file):
    count = 1
    boy = []
    girl = []

    fp = open(file, 'r')
    for each_line in fp:
        if each_line[:6] != '======':
            if "小甲鱼：" in each_line:
                boy.append(each_line.split('：',1)[1])

            elif "小客服：" in each_line:
                girl.append(each_line.split('：',1)[1])
            else:
                continue
        else:
            save_to_file(boy, girl, count)
            count += 1
            boy = []
            girl = []

        save_to_file(boy, girl, count)

    fp.close()

if __name__ == '__main__':
    split_file('record.txt')




