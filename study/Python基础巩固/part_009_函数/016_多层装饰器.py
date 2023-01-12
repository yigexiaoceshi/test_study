#!/usr/bin/python3
# -*- coding:utf-8 -*-

def decorate1(func):
    print("第一次装修，装水电咯----------")

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("水电装好了")

    return wrapper


def decorate2(func):
    print("第二次装修，铺地板-------")

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("地板铺好了")

    return wrapper


@decorate1
@decorate2
def house():
    print("毛坯房")


house()