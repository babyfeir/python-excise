# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
尝试利用字典的特性编写一个用户登录程序（这次尝试将功能封闭成函数）
'''

account_list = {}

def New_user():
    username = input('请输入用户名:')
    while True:
        if username in account_list:
            username = input('此用户名已经被使用，请重新输入:')
            continue
        else:
            break
    pwd = input('请输入密码:')
    account_list.update({username: pwd})
    print('注册成功，赶紧试试登录吧^_^')

def User_login():
    if len(account_list) == 0:
        print('目前没有注册用户，请先新建账号！')
        New_user()
    username = input('请输入用户名:')
    while True:
        if username not in account_list:
            username = input('您输入的用户名不存在，请重新输入：')
            continue
        else:
            break
    pwd = input('请输入密码:')
    if pwd == account_list[username]:
        print('欢迎进入XXOO系统，请点击右上角的X结束程序！')
    else:
        print('密码错误！')

def showmenu():
    while True:
        print('|--- 新建用户：N/n ---|')
        print('|--- 登录账号：E/e ---|')
        print('|--- 退出程序：Q/q ---|')
        code = input('请输入指令代码:')
        while True:
            if code not in 'NnEeQq':
                code = input('您输入的指令代码错误，请重新输入:')
            else:
                break

        if code == 'N' or code == 'n':
            New_user()

        elif code == 'E' or code == 'e':
            User_login()

        elif code == 'Q' or code == 'q':
            break

if __name__ == '__main__':
    showmenu()

