#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 鼠标hover，显示builtins表明是内置函数，input()是一个阻塞性提示语句，运行完成之后必须操作输入才会执行完成
input("请输入数字：")  # 输入后敲击回车表明把输入的内容给input函数，所以一般输入的内容如果需要使用，需要用一个变量去接收输入的结果
# 程序运行的时候显示红色实心方块或者程序名前面图标出现绿色点点，表明程序未运行完成
age = input("请输入年龄：")
print(type(age))  # input()方法里，键盘输入的都默认是str类型，所以如果要操作加减乘除或者拼接，得注意数据类型
# 整型 转换为 字符串
print(age+str(1000))
# 字符串 转换为 整型
print(int(age)+1000)

a = 9.9
print(int(a))  # 浮点型可以直接转为整型，默认去掉小数位仅取整数位
a = '9.9'
# print(int(a))  # 字符串里内容为浮点型时，直接转为整型会报错

"""
小结：变量a
str --> int : int(a) 如果是int("9.9")会报错
str --> float ： float(a)

int --> str : str(a)
float --> str : str(a)

int --> float : float(a)
float --> int : int(a) 去除小数位，取整

bool --> int : int(a) True时等于1，False时等于0
boot --> float : float(a) True时等于1.0，False时等于0.0
bool --> str : str(a) True时等于"True"，False时，等于"False"

int --> bool : bool(a) 整数为0时bool类型为False，不为0时为True
float --> bool : bool(a)  浮点型为0.0或0.00等时bool类型为False，反之为True
str --> bool : bool(a)  字符串为空时bool类型为False，不为空时为True，其中None不属于任何数据类型，对应的布尔类型为False
"""
x = 0
print(bool(x))
x = 0.0
print(bool(x))
x = None
print(type(x))
print(bool(x))
x = ""  # 声明一个变量x，赋值空字符串
print(type(x))
print(bool(x))