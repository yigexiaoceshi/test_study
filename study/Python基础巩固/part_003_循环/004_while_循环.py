#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
while语句格式：
while 条件：
    子语句
解读：当while条件成立时，执行子语句，子语句执行完会重新判断while条件是否为True，直到条件为False跳出while循环不再执行子语句
注意：while容易造成死循环，必须在子语句里创造条件使得循环到某个次数时while条件不成立，不然跳不出该循环
"""
# 示例1：循环打印1-10的数据
import random

n = 1
while n <= 10:
    print("n的值是", n)
    n += 1

# 示例2：打印出1-50之间能被3整除的所有整数
m = 1
while m <= 50:
    if m % 3 == 0:
        print("1-50里能被3整除的数为", m)
        m += 1
    else:
        m += 1
# 或者这么写
mm = 1
while mm <= 50:
    if mm % 3 == 0:
        print("1-50里能被3整除的数有", mm)
    mm += 1
# 或者初始值定义为3，子语句里m += 3也可以
# 或者这么写
mmm = 1
while mmm <= 50:
    if (mmm // 3) * 3 == mmm:  # mmm//3，整除是得出的商取整数部分，只有整除仅有整数部分时，再乘以3才会等于mmm
        print("1-50里3的倍数是：", mmm)
    mmm += 1

# 示例3：打印1-10之间的数字累加之和
# 思路：优先找出应该定义的变量有2个，一个是数字的初始值，一个是累加之和的初始值，然后找出循环时两个变量之间的关系
h = 1
sum = 0
while h <= 10:
    sum += h
    print("第%s次循环之和为" % h, sum)
    h += 1
# 也可以这么写
hh = 1
sum1 = 0
"""注意：变量如果在循环体需要变化，必须声明在循环体外面，如果声明在循环体里面，相当于每次都重新声明这个变量，值会被重置"""
# 一般不知道循环次数时使用while True，然后在循环体里使用认为判断来break
while True:
    sum1 += hh
    hh += 1
    print(sum1)
    answer = input("当前累计相加了%d-1次，总和为%d,还要继续计算吗（输入Q退出购买，其他任意键表示继续购买）：" % (hh, sum1))
    if answer == "Q":
        break

"""
猜数字游戏：
1、猜数字，可猜多次，猜对了打印猜对了，猜大了打印猜大了，猜小了打印猜小了
2、统计猜对时总共猜的的次数
3、如果一次猜对，打印：赶快去买彩票吧，运气太好了
4、如果2-5次猜对，打印：猜对了，运气还可以啊
5、如果猜6次以上才对，打印：猜对了，运气一般啊
"""
computer_number = random.randint(1, 50)  # random.randint(n,m)为前闭后闭区间
print(computer_number)
guess_number = 1
while True:
    person_number = int(input("请输入一个数字："))
    if computer_number == person_number:
        if guess_number == 1:
            print("赶快去买彩票吧，运气太好了")
        elif 1 < guess_number < 5:
            print("猜对了，运气还可以啊")
        else:
            print("猜对了，运气一般啊")
        break  # break也可以放在嵌套的if或者elif或者else的分支里，都能跳出整个循环
    elif computer_number < person_number:
        print("猜大了，再大一点")
    elif computer_number > person_number:
        print("猜小了，再小一点")
    guess_number += 1

"""猜拳游戏"""
x = 1
computer_count = 0
person_count = 0
while x < 4:
    # 电脑猜数每次循环需要变化，此时放里面，因为random.randint()函数本就是随机产生数字，如果在循环外面，则三轮循环只产生一个数字
    c_num = random.randint(1, 3)
    print(c_num)
    p_num = int(input("请输入石头剪刀布(石头-1；剪刀-2；布-3):"))  # input()都为字符串，和数字做==计算会一直走到else语句
    if p_num == 1 and c_num == 2 or p_num == 2 and c_num == 3 or p_num == 3 and c_num == 1:
        print("~~~~~~~~~本轮我赢啦~~~~~~~~~``")
        person_count += 1
    elif c_num == 1 and p_num == 2 or c_num == 2 and p_num == 3 or c_num == 3 and p_num == 1:
        print("~~~~~~本轮电脑赢啦~~~~~~~~`")
        computer_count += 1
    else:
        print("本轮平局")
    x += 1
if computer_count < person_count:
    print("~~~最终我赢了~~~")
elif computer_count > person_count:
    print("~~~最终电脑赢了~~~")
else:
    print("~~~最终是平局哦~~~")
