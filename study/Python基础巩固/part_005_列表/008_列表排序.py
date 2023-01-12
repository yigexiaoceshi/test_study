#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random

print("*" * 20, "随机生成8个1-20之间的随机整数", "*" * 20)
list = []
for i in range(8):
    list.append(random.randint(1, 100))  # random.randint(1,100)，此处是前闭后闭区间：[1,100]
print("生成的随机列表为：", list)

print("*" * 20, "翻转列表(不涉及排序)：list.reverse()", "*" * 20)
list.reverse()
print('翻转后的列表为：', list)

print("*" * 20, "翻转列表：list.sort()，默认参数reverse=False，升序，由小到大", "*" * 20)
list.sort()
print('默认从小到大，升序：', list)

print("*" * 20, "翻转列表：list.sort(reverse=True)，参数reverse=True，降序，由大到小", "*" * 20)
list.sort(reverse=True)
print('从大到小，降序排列：', list)

print("*" * 20, "例题1", "*" * 20)
"""
1、从1-100的整数里随机产生8个数字，保存到列表，做升序或降序排列
2、键盘输入一个1-100的整数，插入到指定位置，使得原来的顺序不变
"""
number = []
for i in range(8):
    number.append(random.randint(1, 100))
number.sort()
print(number)
# 方法1：笨方法，依次判断列表每个数和输入数字的大小
# flag = True
# while flag:
#     person_number = input("请输入1-100之间的任意整数：")
#     if person_number.isdigit() and 1 <= int(person_number) <= 100:
#         for i in range(8):
#             if int(person_number) > number[i] and i != 7:
#                 pass
#             elif int(person_number) > number[i] and i == 7:
#                 number.append(int(person_number))
#             elif int(person_number) == number[i]:
#                 number.insert(i, int(person_number))
#                 break
#             elif int(person_number) < number[i]:
#                 number.insert(i, int(person_number))
#                 break
#             else:
#                 pass
#         flag = False
#     else:
#         print("输入有误，请重新输入")
# print(number)

# 方法2：输入的数字插入列表，重新排序依次
person_number = input("请输入1-100之间的任意整数：")
number.append(int(person_number))
number.sort()
print(number)