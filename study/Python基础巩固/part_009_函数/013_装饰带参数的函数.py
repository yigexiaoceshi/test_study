#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
带参数的装饰器：
1、如果元函数有参数，则装饰器的内置函数也需要有参数
2、
"""


# 定义一个装饰器：不支持不同参数个数的多个原函数同时使用
# def decorator(func):
#     def wrapper(address, area):  # 后面调用的house是装饰后的house，就是wrapper，所以此处的参数和原函数要保持一致
#         func(address, area)  # 原house，必须要传参
#         print("刷油漆")
#         print("铺地板")
#         print("买家具")
#         print("精装修，可以入住了")
#
#     return wrapper
# 优化1：(支持不同参数个数的多个原函数同时使用，但不支持关键字参数)
# def decorator(func):
#     def wrapper(*args):  # 后面调用的house是装饰后的house，就是wrapper，所以此处的参数和原函数要保持一致
#         func(*args)  # 原house，必须要传参
#         print("刷油漆")
#         print("铺地板")
#         print("买家具")
#         print("精装修，可以入住了")
#
#     return wrapper
# 优化2：支持不同参数个数的多个原函数同时使用，也支持关键字参数
def decorator(func):
    def wrapper(*args, **kwargs):  # 后面调用的house是装饰后的house，就是wrapper，所以此处的参数和原函数要保持一致
        func(*args, **kwargs)  # 原house，必须要传参
        print(args)
        print(kwargs)
        print("刷油漆")
        print("铺地板")
        print("买家具")
        print("精装修，可以入住了")

    return wrapper


print("*" * 25, "原函数1：仅一个参数", "*" * 25)


@decorator
def house(address):
    print("这是我在{}的毛坯房".format(address))


house("西湖风景名胜区")

print("*" * 25, "原函数2：多个参数，使用可变参数(多个函数使用同一个装饰器，且当每个原函数参数个数不确定时)", "*" * 25)


@decorator
def changfang(address, area):
    print("这是我在{}的毛坯房，面积是{}".format(address, area))


changfang("云栖小镇", 1000)

print("*" * 25, "原函数3：包含关键字参数，可变参数后面加上**kwargs", "*" * 25)


@decorator
def hotel(address, name, area=40):
    print("位于{}的{}，每个房间的面积是{}".format(address, name, area))


hotel("西湖风景名胜区", "全季酒店", area=99)  # 使用了关键字参数传参，装饰器参数的内部参数必须加**kwargs参数
