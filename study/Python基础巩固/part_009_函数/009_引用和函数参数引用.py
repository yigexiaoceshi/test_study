#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
引用：
1、普通变量的赋值，不是在函数中使用，可以通过sys.getrefcount(a)，查看指向对象a的指针数量(即引用次数)，注：当前函数也算作一次引用
    del 变量，表示删除了一个引用
2、函数参数的引用：
    分清楚传递的值的数据类型是否可变，如果不可变，函数体内的变化不会影响函数外的变量值，反之会同样改变函数外的变量值
"""
import sys

a = 1
b = a  # a将数据1在内存中的储存地址赋值给b，b就指向这块地址，不管a是否再发生改变
a = 2
print(b)
print(sys.getrefcount(a))

list1 = [1, 2, 3]
list2 = list1  # 赋值的只是个引用地址，指针指向该内存空间
list3 = list1
print(sys.getrefcount(list1))  # 返回对象首地址一共有多少个变量指针指向，list1/list2/list3，加上调用函数一共4个
del list3
print(sys.getrefcount(list1))  # 回收list3，少一个
del list1
print(sys.getrefcount(list2))  # 回收list1，list2的指针仍然指向数据[1,2,3]的指针空间
# Python垃圾回收机制，当一个空间没有任何指针指向它时，会回收
# 可以使用id()来查看变量是否指向同一个地址

print("*************不可变数据类型，函数内部不可改变全局变量的值**************")


def func1(n1):
    #  n1其实是函数的一个局部变量
    for i in range(n1):
        print(i, end="  ")
    n1 += 1


n = 9
func1(n)  # 相当于n=9,n1=n,即n1=9，n1+=1，n1指向了10，n仍然为9，且n1为函数的局部变量
print("\nn的值是：", n)

print("*************可变数据类型，函数内部可改变全局变量的值**************")


def func2(list1):
    if isinstance(list1, list):
        for i in list1:
            print(i, end="  ")
    else:
        print("list1不是列表类型。")
    list1.append(6)  # 可变数据类型，list1和list2指向的都是同一个地址，操作的也是同一个地址
    list1.insert(0, 100)  # 可变数据类型，list1和list2指向的都是同一个地址，操作的也是同一个地址
    print("\n函数内部的list1：", list1)


list2 = [1, 2, 3, 4, 5]
func2(list2)
print("函数外部的list2:", list2)
