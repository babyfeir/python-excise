# coding=utf-8
import random

secrect = random.randint(1,10)
print('secrect = %d' %secrect)
print('----------------小甲鱼C工作室----------------')
temp = input('不妨猜一下小甲鱼现在心里想的是哪个数字：')
if temp.isdigit():
    guess = int(temp)
    times = 1
    if guess == secrect:
        print('我去，你是小甲鱼心里的蛔虫吗？！')
        print('哼，猜中了也没有奖励！')
    else:
        while guess != secrect and times !=3:
            times += 1
            temp = input('哎呀，猜错了，请重新输入吧：')
            if temp.isdigit():
                guess = int(temp)
                if guess == secrect:
                    print('我去，你是小甲鱼心里的蛔虫吗？！')
                    print('哼，猜中了也没有奖励！')
                elif guess > secrect:
                    print('哥，大了大了~~')
                else:
                    print('嘿，小了！小了！')
            else:
                print('输入类型不对！！！')
    print('游戏结束，不玩啦^_^')
else:
    print('输入类型不对，请输入数字！！！')
