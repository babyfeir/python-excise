# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
尝试利用字典的特性编写一个通讯程序
'''

print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料 ---|')
print('|--- 2:插入新的联系人 ---|')
print('|--- 3:删除已有联系人 ---|')
print('|--- 4:退出通讯录程序 ---|')

address_list = {}

while True:
    print('\n')
    try:
        code = int(input('请输入相关的指令代码:'))
        if code == 2:
            contact = input('请输入联系人姓名:')
            if contact in address_list:
                print('您输入的姓名在通讯录中已存在 --->> ' + contact + ' : ' + address_list[contact])
                confirm_flag = input('是否修改用户资料(YES/NO): ')
                if confirm_flag == 'YES':
                    phone = input('请输入用户联系电话:')
                    address_list[contact] = phone
            else:
                phone = input('请输入用户联系电话:')
                address_list.update({contact: phone})

        elif code == 1:
            contact = input('请输入联系人姓名:')
            if contact in address_list:
                print(contact + ' :' + address_list[contact])
            else:
                print('联系人: %s在通讯录中不存在!' %contact)

        elif code == 3:
            contact = input('请输入联系人姓名:')
            if contact in address_list:
                address_list.pop(contact)
                print('成功删除联系人:%s' %contact)
            else:
                print('联系人: %s在通讯录中不存在!' %contact)

        elif code == 4:
            print('|--- 感谢使用通讯录程序 ---|')
            break

    except ValueError :
        print('指令代码不正确,请重新输入')

