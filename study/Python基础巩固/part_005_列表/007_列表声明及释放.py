#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
list3 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
#  获取列表内存地址
print("list1的内存地址是：", id(list1))
#  元素相同，列表地址不同（这点和字符串变量不一样）
print("list3的内存地址是：", id(list3))
#  获取列表首个元素的内存地址
print("list1的第一个元素的内存地址是：", id(list1[0]))
#  删除第一个元素
list1.pop(0)
#  删除元素后，列表地址不变
print("list1删除第一个元素后的内存地址是：", id(list1))

print("---*------*------*------*------*------*------*------*------*------*---")
# list1赋值给list2，2个列表指向同一个地址，能同时对该列表进行操作
list2 = list1
#  list2向列表添加一个元素，list1同样也会看到该元素
list2.append("大象")
print("list2的内存地址是：", id(list2))
print("list2添加元素，此时list1为：", list1)
print("list2为", list2)

print("---*------*------*------*------*------*------*------*------*------*---")
# 清空list1，list2也会清空
# list1.clear()
# print("清空后的list1为：", list1)
# print("清空list1后，list2为：", list2)

print("---*------*------*------*------*------*------*------*------*------*---")
# 使用del删除list1后，list1变量被释放，不再指向该列表的头部地址，即变为'未声明的变量'，被回收
del list2[-1]  # 删除最后一个元素
del list1
print("删除list1后，list2的指向仍然不变，list2为：", list2)
# print(list1)  # 报错

print("---*------*------*------*------*------*------*------*------*------*---")
# del也可以删除字符串变量，或某个元素
a = "hello world"
b = a
c = a
print(id(a))
print(id(b))
print(id(c))
d = a.replace(" world", "", 1)  # replace()方法返回一个新的字符串，不改变原字符串
print("d：", d)
print('操作元素替换之后的a:', a)
print('操作元素替换之后的b:', b)
print('操作元素替换之后的c:', c)
del a
print(b, c)
print(id(b))
print(id(c))
