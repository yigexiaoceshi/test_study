#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
递归函数：在函数内部不调用其他的函数，而是自己本身

遵循：
1、要有出口，即终止条件
2、每递归一次向出口靠近
3、一般入口是传入的参数
"""

# 函数内部调用其他函数
# def a():
#     print("---------a----------")
#     b()


# 递归函数：函数内部调用自身（此处死循环）
# def b():
#     print("---------b----------")
#     b()
#
#
# b()

print("*" * 25, "示例1：使用递归函数打印1-10的数字", "*" * 25)


def one_to_ten(n):
    if n >= 10:  # 走该分支不再循环调用函数本身，即终止递归条件
        print(n)
    else:  # 走该分支会一直调用函数本身，一直递归
        print(n)
        n += 1
        one_to_ten(n)


one_to_ten(1)

print("*" * 25, "示例2：使用递归函数打印1-10的数字累加和", "*" * 25)
sum1 = 0


def one_to_ten_sum(n):
    global sum1
    if n >= 10:
        sum1 += n
        print("n为{}时，sum1等于：{}".format(n, sum1))
    else:
        sum1 += n
        print("n为{}时，sum1等于：{}".format(n, sum1))
        n += 1
        one_to_ten_sum(n)


one_to_ten_sum(1)

print("*" * 25, "示例2：使用递归函数打印1-10的数字累加和，第二种写法", "*" * 25)


def a1(i):
    if i == 10:
        return 10
    else:
        return i + a1(i + 1)  # return里包含其他调用或者待运算表达式时，都会先执行调用或者计算，得出最终确定结果之后才会执行return


r = a1(1)
print(r)

print("*" * 25, "示例3：使用递归函数实现斐波那契数列，1-100", "*" * 25)


def b(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return b(k - 1) + b(k - 2)


bbb = b(3)
print("bbb为：", bbb)

# print("\n", "*" * 25, "示例3：斐波那契数列，while循环实现", "*" * 25)
# # 获取用户输入数据
# nterms = int(input("你需要几项？"))
#
# # 第一和第二项
# n1 = 0
# n2 = 1
# count = 2
#
# # 判断输入的值是否合法
# if nterms <= 0:
#     print("请输入一个正整数。")
# elif nterms == 1:
#     print("斐波那契数列：")
#     print(n1)
# else:
#     print("斐波那契数列：")
#     print(n1, ",", n2, end=" , ")
#     while count < nterms:
#         nth = n1 + n2
#         print(nth, end=" , ")
#         # 更新值
#         n1 = n2
#         n2 = nth
#         count += 1

print("\n", "*" * 25, "示例3：斐波那契数列", "*" * 25)
a = 0
b = 1
while b < 1000:
    a, b = b, a + b
    print("b的值为：", b)

print("\n", "*" * 25, "示例3：递归函数实现斐波那契数列", "*" * 25)
list = []


def fb(n):  # 传入的参数n定义了需要几个数
    for i in range(n):  # 根据传入的参数n定义n次循环
        if i == 0:  # 第一次循环，第一个数定义为0
            list.append(0)
        elif i == 1:  # 第二次循环，第二个数定义为1
            list.append(1)
        else:
            list.append(list[i - 1] + list[i - 2])
    return list


result_fb = fb(3)
print(result_fb)
