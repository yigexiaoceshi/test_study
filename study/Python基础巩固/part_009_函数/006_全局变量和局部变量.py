#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
局部变量：声明在函数内部的变量，作用范围是函数范围内部，每次开始执行函数体内的代码句，变量都被重新声明，执行完成都会被回收，用来保存临时数据
全局变量：声明在函数体外部的变量，能在多个函数内部使用，全局变量必须声明在函数调用语句之前(注意代码执行顺序)

局部变量和全局变量同名：执行函数体的代码句时，优先找函数内部的变量，然后再找全局变量

global：函数内部需要修改全局变量的值时，不可变数据类型需要加global关键字，可变数据类型不需要添加，可以一次性声明多个全局变量'global aa,bb'
注：如果函数体中出现'global 全局变量名'，那么这个函数中即使出现和全局变量相同的变量名，如果出现'变量名=数据'，也是对全局变量进行修改

globals()：查看当前模块（包含系统默认加载模块）的所有全局变量，返回字典
locals()：查看当前方法所有局部变量，返回字典

函数可以视作一个变量，指向函数体内代码块存放的地址
"""
# 全局变量
a = 100


def func1():
    # 局部变量：作用范围仅限函数内部
    a = 0  # 先找函数体内是否有变量，如果有则覆盖全局变量的值直接使用，如果没有则到函数体外找全局变量并引用
    b = 8
    print("a=", a)
    print("b=", b)


func1()


def func2():
    b = 9
    print("a=", a)  # 此处使用的是全局变量
    print("b=", b)


func2()


def func3():
    # b = a - 10  # 仅拿全局变量做计算是可以的，只要不改变a的值
    global a  # 必须先声明全局变量，然后再赋值
    a += 11  # =号右侧a+11没有问题，但是赋值给a相当于要改变全局变量的值，所以必须加global
    b = a - 10
    print("改为全局变量后a：", a)
    print("b = ", b)


func3()

def func4():
    print("此时a的值是：", a)


func4()


def func5():
    list1 = [1, 2, 3]
    return list1


print(func5())

"""
定义函数1：is_login，参数username和password，函数体判断是否登录，登录返回True，未登录返回False
定义函数2:borrow_book，参数book_name，函数体 判断是否登录，登录可借，未登录不可借
"""
print("******************************************************")

login = False


def is_login(username, password):
    if username == "admin" and password == "1234":
        global login  # 改为全局变量，才会更改函数体外变量login的值
        login = True
    else:
        print("登录失败！")


def borrow_book(book_name):
    if login:
        print(f"{book_name}可以借阅！")
    else:
        print("用户未登录，不可借书！")
        username = input("请输入登录用户名：")
        password = input("请输入登录密码：")
        is_login(username, password)


borrow_book("红楼梦")
borrow_book("红楼梦")
