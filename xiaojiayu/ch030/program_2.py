# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件名
是否存在。如遇到文件夹，则进入文件夹继续搜索。
'''
import os


def search_file(search_path, target):
	os.chdir(search_path)

	lists = os.listdir(os.curdir)

	for each in lists:
		if each == target:
			path = os.path.join(os.path.abspath(os.curdir), each)
			print(path)
			# print(os.getcwd() + os.sep + each)

		if os.path.isdir(each):
			search_file(each, target)
			os.chdir(os.pardir)   # 返回上一级目录


if __name__ == '__main__':
	init_path = input('请输入待查找的初始目录：')
	target = input('请输入需要查找的目标文件：')
	search_file(init_path, target)
