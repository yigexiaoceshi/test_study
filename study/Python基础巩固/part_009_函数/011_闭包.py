#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
闭包(closure)：
1、嵌套函数
2、内层函数引用了外部函数的变量
3、返回值是内部函数
4、主要用于装饰器
"""


# 闭包示例
def outer(n):
    a = 10

    def inner():
        b = a + n
        print(b)

    return inner


result = outer(5)
print(result)
result()  # 调用内部函数


# 示例
def foo():
    print("打印的是：foo")


def func():
    print("打印的是：func")


foo = func  # 将func函数的地址赋值给foo，改变foo变量的内存空间地址指向
foo()  # 执行的事func()函数
foo = "123"
print(foo)
