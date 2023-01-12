#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
关系运算符：True,False
> : 大于
< : 小于
== : 等于
!= : 不等于
>= : 大于或等于
<= : 小于或等于
is : 比较的是内存地址，可以使用id()函数查看
is not :
in :
not in :
"""
a = 1
b = 2
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a == b)

aa = (1, 2, 3)
bb = 1
print(bb in aa)
print(bb not in aa)
print(aa is str)  # aa属于列表，不属于str，返回False
print(aa is not str)  # 返回True
print("aa是一个列表吗：", aa is tuple)  # 不能用这种写法，返回False

aaa = "abc"
bbb = "abd"
ccc = "bca"
print(aaa > bbb)  # 字符串比较大小的机制：参考ASCII码表，按照相同索引一个个值从左至右比较，直到分出大小
print(aaa == ccc)  # 比较索引为0时a和b的值不相同，只要已经得出结果，所以后面就不会再比较了

# is运算符比较内存地址，a,b,c内存地址一致
a = "hello"
b = a
c = "hello"
print(a is b)
print(a is c)
print(b is c)
