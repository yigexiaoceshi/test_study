#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
（一）装饰器：遵循开放(对原函数功能进行扩展)封闭(原函数不变)原则

（二）装饰器定义(遵循闭包规则，必须增加参数):
def xxx(func):
    def yyy(参数1，参数2...):
        前置代码块
        func()
        后置代码块
        return..
        ...
    return yyy

@装饰器名
def 原函数():    # 原函数 = 装饰函数(原函数)
    pass

（三）装饰器decorator可实现的功能(常见的实用场景)：
1、添加函数调用日志
2、函数执行时间统计
3、执行函数前预备处理
4、执行函数后清理功能
5、权限校验等场景
6、缓存
"""


# 定义装饰器
def decorator(func):  # 装饰器的原理就是个闭包函数，但是必须要传入一个参数(固定写法，要保证原函数的内容不变)
    def wrapper():
        func()  # 这里执行的是house()，输出"毛坯房"，目的是不改变原函数
        print("刷油漆")  # 这几行语句是在原函数功能上新增加的功能
        print("铺地板")
        print("买家具")
        print("精装修房子，可以入住")

    return wrapper  # 返回函数名，将原函数装饰后返回给house接收，称为装饰后的新的house，house = decorator(house)


@decorator  # 使用@decorator，会自动将house函数加载到内存，并且将house函数的地址传入函数，decorator
def house():
    print("毛坯房")


# 装饰的过程2个大步骤，第一个大步骤将初始的house传入装饰器函数，第二个步骤，将装饰器函数返回值赋值给house，此时的house是装饰过后的house
house()  # house接收的是decorator函数的返回值，即decorator的内置函数wrapper()：decorator.<locals>.wrapper
