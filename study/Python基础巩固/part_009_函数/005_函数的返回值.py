#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
函数：
1、有参数，有返回值
2、有参数，无返回值
3、无参数，有返回值
4、无参数，无返回值

参数可无，可有，可一个，可多个
返回值可无，可有，可一个，可多个

注：
1、一个代码分支里只能有一个有效return
2、出现return，停止执行后续代码，可以用来跳出循环并且 终止函数调用
"""


def get_sum(*args):
    totle = 0
    for i in args:
        totle += i
    return totle  # 返回值仅代表存在内存空间，所以函数体外一定要有变量去接收这个存放值的空间，这个值才可以给到外界使用


list1 = [i for i in range(1, 101)]
print(get_sum(*list1))
a = "1-100的和是"
b = a + str(get_sum(*list1))
print(b)

print("**********************", "求最大值和最小值", "***********************")


def get_maxnumber_and_minnumber(*args):
    list_args = list(args)
    print(args, list_args)
    print(len(list_args))
    print("排序前", list_args)
    # print(id(list_args))
    for i in range(len(list_args)):
        for j in range(0, len(list_args) - 1 - i):
            if list_args[j] > list_args[j + 1]:
                list_args[j], list_args[j + 1] = list_args[j + 1], list_args[j]
    print("排序后", list_args)  # 为什么打印结果会是None
    return list_args[0], list_args[-1]  # 返回值有多个时，返回一个元组


list_b = [32, 45, 16, 26, 81, 9]
print(get_maxnumber_and_minnumber(*list_b))  # 加*表示传进去的是解包后的所有元素

print("**********************************************************************")
# a, b = get_maxnumber_and_minnumber(*list_b)
# print(a, b)
