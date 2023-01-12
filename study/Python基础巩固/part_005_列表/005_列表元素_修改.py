#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = [1, 2, 3, "a", 4, 5, 6, "a"]
list1[0] = 8
print(list1)

print("*" * 20, "将列表中的元素a替换成b", "*" * 20)
a_index = list1.index("a")  # 找出元素a对应的索引位置，如果有多个元素a，则返回从左至右匹配到的第一个a元素的索引
print(type(a_index))  # 索引数据类型为int
print("a元素的索引下标是：", a_index)  # 仅返回第一个a的下标
list1[a_index] = "b"  # 完成元素替换(仅替换掉匹配到的第一个a元素)
print(list1)
