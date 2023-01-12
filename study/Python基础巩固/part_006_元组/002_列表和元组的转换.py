#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
list(tuple)
tuple(list)
"""
# 定义元组
tuple_a = ("a", "b", 123, False)
print(tuple_a)
print(id(tuple_a))

# 元组转换为列表
list_a = list(tuple_a)
print(list_a)

# 列表里新增元素
list_a.append("a")
print(list_a)

# 列表重新转换为元组
tuple_a = tuple(list_a)
print(tuple_a)
print(id(tuple_a))  # 不是当初那个元组了，如果更改了值，内存地址也发生变化了，表明当前数据类型是不可变数据类型
