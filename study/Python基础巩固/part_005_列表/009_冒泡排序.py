#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random

print("*" * 20, "生成列表，元素为8位1-100内的随机数字", "*" * 20)
list = []
for aaa in range(8):
    list.append(random.randint(1, 100))
print(list)

print("*" * 20, "遍历列表：while循环", "*" * 20)
n = 0
while n < len(list):
    print(list[n], end='  ')
    n += 1

print("\n", "*" * 20, "遍历列表：for循环", "*" * 20)
for i in list:
    print(i, end='  ')

print("\n", "*" * 20, "交换变量的值", "*" * 20)
a = 1
b = 2
a, b = b, a
print(a, b)

print("\n", "*" * 20, "例题1：冒泡排序，从小到大排序", "*" * 20)
# 随机生成8位1-100内的整数，放入列表list1
list1 = []
for aaa in range(8):
    list1.append(random.randint(1, 100))
# 冒泡排序，升序排列
for i in range(len(list1) - 1):
    for j in range(len(list1) - 1 - i):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
        else:
            pass
print(list1)

print("\n", "*" * 20, "例题1：冒泡排序，从大到小排序", "*" * 20)
# 随机生成8位1-100内的整数，放入列表list2
list2 = []
for aaa in range(8):
    list2.append(random.randint(1, 100))
# 冒泡排序，降序排列
for h in range(len(list2) - 1):
    for k in range(len(list2) - h - 1):
        if list2[k] < list2[k + 1]:
            list2[k], list2[k + 1] = list2[k + 1], list2[k]
        else:
            pass
print(list2)
