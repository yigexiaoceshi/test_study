#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
赋值运算符：
= : 是等号右侧的先进行计算，得出结果，然后赋值给左侧的变量，程序的执行顺序是从右侧到左侧
+= : 比如(a += b，a = a + b)，意思是变量本身加上右侧的值，然后赋值给本身，下面依此类推
-= :
*= :
/= :
//= :
**= :
%= :
"""
a = 1
b = 2
c = 3
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
c += b
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)