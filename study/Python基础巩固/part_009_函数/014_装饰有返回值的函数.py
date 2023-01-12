#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
装饰器修饰有返回值的函数：
原函数有返回值，装饰器的内部函数也要有返回值
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print("原函数返回值，即预计装修费用是：{}".format(r))
        print("刷油漆")
        print("铺地板")
        print("买家具")
        print("精装修，可以入住了")
        return "实际装修费用：55555"

    return wrapper


@decorator
def house():
    print("我是一个毛坯房。。。")
    return 50000


rr = house()
print(rr)
