#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
用lambda关键词能创建小型匿名函数（一般功能非常简单）：
lambda 参数列表:运算表达式

参数列表，如果有多个，用逗号隔开，运算表达式是return的内容
"""
# sum1 = lambda a, b: a + b  # 此时的变量sum1就是匿名函数名
# print(sum1(10, 20))
#
#
# # 等同于：
# def sum1(a, b):
#     return a + b


"""
使用场合
1、作为参数使用，放在传参的位置
2、该函数仅在此处(指该函数内部)使用，其他地方用不到时
"""
print("*" * 25, "匿名函数使用场合：函数名作为其他函数的参数", "*" * 25)


def aaa():
    print("这是函数aaa")


def bbb(a, func):
    print("这是函数bbb的第一个参数a:", a)
    func()


bbb(5, aaa)

print("*" * 25, "匿名函数使用场合：函数名作为其他函数的参数", "*" * 25)


def ccc(a, func):
    print("这是函数bbb的第一个参数a:", a)
    r = func(9)
    print("------------", r)


ccc(6, lambda x: x ** 2)
ccc(9, lambda x: x if x % 2 == 0 else x + 2)
