#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
内置方法：
print():打印对象
input():输入对象（如果要用到，需要变量接收这个对象）
type():查看对象的数据类型
id():查看对象的内存地址
len():查看对象所占的内存长度
bin():转化为二进制
oct():转化为八进制
hex():转化为十六进制
chr():传入ASCII码值，求对应的字符
ord():传入字符，求对应的ASCII码
max():找出序列对象的最大值
min():找出序列对象的最小值
sum():序列对象求和
abs():求绝对值
sorted():系统排序方法，默认升序，返回一个新的列表
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(list1))
print(min(list1))
print(sum(list1))
print(abs(-1))

tuple1 = (1, 4, 5, 7, 4, 0, 3, 8, 2)  # 元组无sort()方法，仅列表有
print(sorted(tuple1))  # 返回一个新的列表
print(sorted(tuple1, reverse=True))  # 降序

print(chr(65))  # 传入ASCII码值，求对应的字符
print(ord("a"))  # 传入字符，求对应的ASCII码

"""
in : 字符串、列表、元组、字典(仅判断key)
not in : 字符串、列表、元组、字典(仅判断key)
is : 比较内存地址是否一致
is not
+ : 字符串、列表、元组
* : 字符串、列表、元组
& : 集合，求交集
| : 集合，求并集
- : 集合，求差集
"""
