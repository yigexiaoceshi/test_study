#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
逻辑运算符
or ： 或
and ： 并且（优先级高于or)
not :
"""
a = 1
b = 3
c = 0
# 两侧都是数字或字符串时时进行逻辑运算时
print(a and b)  # and两侧都为真，输出后面的值，仅一侧为真时，输出0
print(a and c)  # and两侧只要一侧出现0，输出0
print(a or c)  # or两侧出现一个0，输出True的值，两侧都是True时，输出第一个True(此时已经得出结果，不需要看or后面的是否真假)
print(a or b)  # or两侧都是True，输出第一个True的值

# 两侧进行关系运算得出True和False之后再进行逻辑运算时
print(a > c and a == b)  # and两侧都为真时，输出True，只要一侧为False，输出False
print(a > c or c > b)  # or只要有一侧为True,输入True，全为False时，输入False

print("#" * 10)  # 字符串的乘法相当于输出10个字符串

print(a or b and c)  # and优先级高于or，先计算b and c为False，False再 or a，返回True
print(a == 1 or b == 3 and c != 0)  # 同理，先计算and，得出的结果False再和 a == 1计算or，得出True

print(a == 1)  # 返回True
print(not a == 1)  # 返回False

print("*"*60)
print("" or 0)
print(type(0 and False))