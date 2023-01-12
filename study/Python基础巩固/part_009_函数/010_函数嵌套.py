#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
函数嵌套：
1、执行代码碰到变量或函数，直接定义的话，出现重名时优先去内层函数找，其次外层函数，然后是全局变量，最后找系统builtins内置模块，都没有会报错
    L(local，本身局部变量)，E(encloseing，外层嵌套函数局部变量)，G(global，全局变量)，B(built-in，Python所有内置模块)
2、如果没有同名的全局变量，使用global定义会报错；同理，如果外层函数没有同名的局部变量，使用nonlocal定义会报错
3、使用global或nonlocal定义变量时，不能再关键字前面先进行定义，不然会因为冲突而报错
"""

#  示例1
print("***示例1***")


def outer():  # 函数理解为一个变量，指向一个存放了代码块的内存空间
    a = 100
    print(a)

    def inner():
        b = 200
        # b += a  # 内部函数可使用外部函数的变量
        nonlocal a  # 修改外层函数变量a，不建议使用global，加上nonlocal，表明引用外层函数变量a
        a += b
        print(b)
        print("我是内部函数变量", b)
        print("我是外部函数变量", a)

    result = locals()  # locals()查看函数中所有的局部变量，返回一个字典
    print(result)
    inner()


print(globals())  # globals()函数查看当前模块所有全局变量(包括系统默认加载的模块里的变量或方法)
outer()

# #  示例2
print("***示例2***")
# aa = 100
#
#
# def out_test():
#     aa = 200
#
#     def in_test():
#         aa = 300
#         print("内部函数aa：", aa)
#         aa -= 50
#
#     print(aa)
#     in_test()
#
#
# out_test()
# print(aa)


#  示例3
print("***示例3***")
aa = 100


def out_test():
    aa = 200

    def in_test():
        # aa = 300  # global是定义全局变量，不能再global之前定义
        nonlocal aa  # 用global改变的是全局变量初始值为100那个aa，用nonlocal改变的是外部函数初始值为200那个aa
        aa -= 40
        print("内部函数aa：", aa)

    print(aa)
    in_test()


out_test()
print(aa)

#  示例4
print("***示例4***")
bb = 100


def outer_test():
    bb = 200

    def inner_test():
        bb = 300
        print(bb)  # 变量同名时：优先找函数内部，其次找外部，最后找全局

    # print(bb)
    inner_test()


outer_test()
# print(bb)
