#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
for i in range(n):   # 肯定有固定的循环次数
    pass

while 条件：  # 可以实现固定循环次数
    pass

while True:  # 可以实现不确定循环次数，添加人为判断break
    pass
"""
# 示例：掷骰子游戏
# 1、两个骰子：点数1-6
# 2、进入游戏必须有金币，否则无法进入游戏
# 3、得到金币：玩一局游戏赠送1个金币；充值获取金币（必须充值10的倍数，金币单价0.5元）
# 4、玩一局游戏消耗5金币
# 5、游戏过程：猜大小猜对额外赠送2个金币；猜错无奖励（两个骰子总数大于6定义为大，否则为小）
# 6、游戏结束：主动退出，金币不够退出
# 7、退出打印：剩余金币数多少，一共玩了几局
import random

money = 0
count = 0

if money < 5:
    print("金币数不足，请充值！")
    ask = input("请输入y/n，是否需要充值？")
    while True:   # 未知充值次数，用while，充值无条件，可以while True
        if ask == "y":
            cz_money = int(input("请输入充值金额："))
            if cz_money % 10 == 0:
                money += cz_money * 2
                print("充值成功，充值金额为%d，总金币为%d" % (cz_money, money))
                print("~~~~~~可以开始游戏了~~~~~~")
                ask_play = input("是否开始游戏？y/n")
                while money > 5:  # 未知的游戏次数，用while，游戏有条件，不可while True
                    if ask_play == "y":
                        money -= 5
                        money += 1
                        s1 = random.randint(1, 6)
                        s2 = random.randint(1, 6)
                        guess = input("猜大还是猜小")
                        if guess == "大" and s1 + s2 > 6 or guess == "小" and s1 + s2 <= 6:
                            money += 2
                            print("猜对了，奖励金币2个，此时总金币为%d" % money)
                        else:
                            print("很遗憾，猜错了，此时金币总额为%d" % money)
                        count += 1
                        ask_play = input("是否开始游戏？y/n")
                    else:
                        break  # 跳出当前while，并不会跳出上层while
                print("此时总金币为%d，一共玩了%d次" % (money, count))
            else:
                print("金额输入错误，充值失败~")
            ask = input("请输入y/n，是否继续充值？")
        else:
            print("游戏结束")
            break
