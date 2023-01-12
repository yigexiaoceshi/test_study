#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = ["兔子", "老虎", "狮子", "狮子", "熊猫", "豹子", "狮子"]
print(list1)

print("*" * 20, "根据索引删除列表元素：list.pop(-2)，不添加索引参数，默认删除最后一个，即默认参数为-1", "*" * 20)
list1.pop(-2)  # 索引为-2，删除元素"豹子"，索引不能超出list的范围，否则报错(index out of range)
print(list1)

print("*" * 20, "根据元素名删除指定元素：list.remove('元素名')，多个同名元素，从左至右默认仅删除第一个", "*" * 20)
if "狮子" in list1:  # 元素不存在会报错，一般结合条件语句使用，先查询是否存在
    list1.remove("狮子")  # 删除从左至右匹配到的第一个"狮子"，不能传不存在的元素名，否则报(元素 not in list)
    print(list1)
else:
    print("该元素不存在列表list1里面！")

print("*" * 20, "del list[index]：根据索引删除指定元素", "*" * 20)
del list1[1]  # 此时索引为1的元素是"老虎"
print(list1)
print(id(list1))
# del list1  # 直接删除该列表的内存地址，list.clear()只是清空列表元素，并未删除该列表的内存地址
# print(id(list1))

print("*" * 20, "使用list.remove()方法删除所有重复元素", "*" * 20)
# 见(004_列表元素_删除重复元素.py)


print("*" * 20, "list.clear()方法：清空列表里所有元素，无需传参", "*" * 20)
list1.clear()
print(list1)
