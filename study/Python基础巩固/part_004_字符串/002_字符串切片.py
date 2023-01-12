#!/usr/bin/python3
# -*- coding:utf-8 -*-
print("*" * 20, "检查下面三个变量内存地址是否一致", "*" * 20)
# 对于Python来说，变量也可以赋值给变量(如果右侧的变量已经被赋值过)
# 赋值的过程(比如：a = "abc")，先去内存中找是否存在(没有被释放)"abc"，如果找到，则将"abc"的地址给a，下面的c = "hello"同理；
# 如果没找到，则会先在申请一个和"abc"大小一致的内存空间存放这个"abc"，然后将内存地址给到a，形成一种指向关系;
# 此时a再赋值给b，b会查找变量a里是否有指向内存中的值，没有则会报错，如果有的话，会直接将a指向的地址拿过来使用(不管a以后是否发生变化，b不变)
# 1、内存中储存某个值可以复用；2、如果没有任何变量指针指向该值，则会回收该内存地址(也可以叫释放)
a = "hello"
b = a
c = "hello"
print(id(a))
print(id(b))
print(id(c))
print(a is b)

"""切片：str[start_index,end_index,step]"""
print("*" * 20, "切片:切取单个元素", "*" * 20)
# 左--->右：index(索引)从0到len(a)-1，或者-len(a)到-1，依次+1
# 右--->左：index(索引)从-1开始，依次-1,
d = "ABCDEFG哈喽"
print(len(a))  # 获取字符串长度
print("变量a的第一个元素是：", d[0])
print("变量a的第八个元素是：", d[7], d[-2])

print("*" * 20, "切片:切取多个元素", "*" * 20)
e = "ABCDEFG哈喽"
print("变量e中取CDE：", e[2:5])  # 前闭后开，相当于[2,5)
print("变量e中取前面四个元素：", e[:4])  # start_index为0时从头开始取
print("变量e中取后面三个元素：", e[-3:], e[-3:9])  # end_index为0时，一直取到末尾
print("变量e中取后面元素CE：", e[2:5:2], e[-7:-4:2])
print("变量e中取所有元素：", e[:], e[::1])  # 获取所有元素
print("变量e中取所有元素：", e[::])  # 默认step是1，可省略

"""
注意：当step为负数时，会从start_index开始往左边数(即index依次-1)，当不指定start_index和end_index时，可以使用-1翻转字符串；
因为此时都不指定的情况下，程序默认会解读为str[-1,0,-1]，start_index为最后一个元素，end_index为第一个元素；
如果指定start_index和end_index的情况下，一定要保证start_index在end_index的左侧才可以使用负数step，否则取不到任何值

start_index 到 end_index的方向，和step（正数-从左至右；负数-从右至左）的方向必须一致

"""
print("翻转字符串e：", e[::-1])  # step为正数，从左至右取值，step为负数，从右至左取值，所以注意start_index和end_index的位置
print("翻转字符串e：", e[0:-1:-1])  # 从0开始依次index-1，取不到值
