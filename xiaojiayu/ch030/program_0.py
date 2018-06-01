# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
编写一个程序，统计当前目录下每个文件类型的文件数
'''
import os

dir_path = os.getcwd()
file_list = os.listdir()
txt_count, jpg_count, py_count, doc_count = 0, 0, 0, 0
html_count, xlsx_count, file_count = 0, 0, 0

for each_file in file_list:
	if '.txt' in each_file:
		txt_count += 1
	elif '.jpg' in each_file:
		jpg_count += 1
	elif '.py' in each_file:
		py_count += 1
	elif '.doc' in each_file:
		doc_count += 1
	elif '.html' in each_file:
		html_count += 1
	elif '.xlsx' in each_file:
		xlsx_count += 1
	elif os.path.isdir(each_file):
		file_count += 1

print('该文件夹下共有类型为【.txt】的文件 %d 个' %txt_count)
print('该文件夹下共有类型为【.jpg】的文件 %d 个' %jpg_count)
print('该文件夹下共有类型为【.py】的文件 %d 个' %py_count)
print('该文件夹下共有类型为【.doc】的文件 %d 个' %doc_count)
print('该文件夹下共有类型为【.html】的文件 %d 个' %html_count)
print('该文件夹下共有类型为【.xlsx】的文件 %d 个' %xlsx_count)
print('该文件夹下共有类型为文件夹的文件 %d 个' %file_count)
