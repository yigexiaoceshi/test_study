#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
无参函数：
def 函数名():
    pass

有参函数：使得函数可以实现灵活调用，适用更多不同的调用场景，没有给默认值的参数叫"位置参数"
def 函数名(参数1，参数2...):
    pass
"""
import random

print("*" * 20, "例题1：定义一个登录函数，生成一个大小写字母加数字的随机验证码", "*" * 20)


def generate_code(n):
    # 生成一个大小写字母加数字的随机四位验证码
    code = ''
    str_base = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(n):
        # 随机获取一个字母或数字
        number = random.choice(str_base)
        code += number
    print(code)


generate_code(4)
generate_code(6)

# print("*" * 20, "例题2：定义一个登录函数，验证是否登录成功，控制登录次数", "*" * 20)
# def login(n):
#     m = 1
#     while m <= n:
#         username = input("请输入用户名：")
#         password = input("请输入密码：")
#         if username == "admin" and password == "1234":
#             print("登录成功！")
#         else:
#             print("登录失败！")
#             m += 1
#     else:
#         print(f"错误次数超过{n}次，账号已被锁定")
# login(3)
# login(5)

print("*" * 20, "例题3：定义一个登录函数，求1-n的累加和", "*" * 20)


def number_sum(a):
    sum = 0
    for i in range(1, a + 1):
        sum += i
    print(sum)


number_sum(100)

print("*" * 20, "例题4：定义一个登录函数，结果为a和b相加", "*" * 20)


def get_sum(a, b):
    if isinstance(a, int) and isinstance(b, int):
        int_sum = a + b
        print("a和b相加的和为：", int_sum)
    elif isinstance(a, float) and isinstance(b, float):
        float_sum = a + b
        print("浮点数a和浮点数b相加的和为：%.2f" % float_sum)
    elif isinstance(a, str) and isinstance(b, str):
        str_sum = a + b
        print("字符串a和字符串b拼接后的字符串为：", str_sum)
    elif isinstance(a, list) and isinstance(b, list):
        list_sum = a + b
        print("列表a和列表b拼接后的列表为：", list_sum)
    elif isinstance(a, tuple) and isinstance(b, tuple):
        tuple_sum = a + b
        print("元组a和元组b拼接后的新元组为：", tuple_sum)
    else:
        print("输入类型错误或类型不一致！")


get_sum(3, 4)
get_sum(3.4, 4.3)
get_sum("a", "b")
get_sum([1, 2, 3], [4, 5, 6])  # 以变量的形式传入的话，传递的是列表的内存地址，使得2个变量有相同的内存指向
get_sum((1, 2, 3), (4, 5, 6))  # 以变量的形式传入的话，传递的是列表的内存地址，使得2个变量有相同的内存指向
get_sum(1, "a")
