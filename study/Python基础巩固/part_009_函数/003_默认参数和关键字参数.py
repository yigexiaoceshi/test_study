#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
位置参数：无默认值，调用时必须传入，且调用时的顺序是固定的，定义时没有赋值的参数又叫形式上的参数，简称"形参"

默认值参数：在定义函数的时候，有一个或者多个参数已经赋值
1、定义
def 函数名(参数1，参数2，参数3=value3，参数4=value4)
    函数体
注意：
    a."默认参数"一定要放在"位置参数"后面
    b.传递的参数和位置参数是一一对应的
2、调用："默认参数"可传可不传(传入参数会覆盖默认参数，不传就使用默认参数)，"位置参数"必须传值

关键字参数：调用时使用"变量=value"的方式，关键字参数可以用于位置参数和默认参数
"实参"：调用时赋值的参数叫做实参
"""


def borrow_book(book_name, book_number=1, school_name="清华大学"):
    print("欢迎进入'{}'的借书系统。。。".format(school_name))
    print("您借阅的书名是：{}，借阅的数量是：{}".format(book_name, book_number))


borrow_book("天龙八部")  # 默认借阅一本
borrow_book("神雕侠侣", 5)  # 5覆盖默认值1
# 数量使用默认，改变学校名，使用"关键字参数":
borrow_book("天龙八部", 4, school_name="北京大学")

print("*" * 20, "删除所有小于50的元素", "*" * 20)
list_a = [33, 21, 56, 96, 63, 45, 3]


def remove_element(list_list):
    # 定义起始索引
    n = 0
    while n < len(list_list):
        if list_list[n] < 50:
            list_list.remove(list_list[n])
        else:
            n += 1
    print(list_list)


remove_element(list_a)  # list_list和list_a指向的是同一个内存地址，操作的是同一个列表
