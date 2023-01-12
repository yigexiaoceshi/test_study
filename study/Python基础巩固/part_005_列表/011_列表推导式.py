#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
得到列表的一种方式
格式1：[变量或表达式 for 变量 in 可迭代对象]，可迭代对象：str,list,tuple,set,dict
格式2：[表达式或变量 for 变量 in 可迭代对象 if 条件]，注意没有冒号
格式3：[语句甲/表达式或变量 if 条件甲 else 语句乙/表达式或变量 for 变量 in 可迭代对象]
格式4：[语句甲/表达式或变量 if 条件甲 else 语句乙/表达式或变量 if 条件乙 else 语句丙 for 变量 in 可迭代对象]
格式5：[(x,y) for x in 可迭代对象1 for y in 可迭代对象2]
"""
list_1 = [i for i in range(20)]
print(list_1)

list_2 = [i * 2 for i in [1, 2, 3]]
print(list_2)

list_3 = [i ** 2 for i in (1, 2, 3)]
print(list_3)

list_4 = [i + i for i in {1, 2, 3}]
print(list_4)

list_5 = [i + 2 for i in {1: 2, 3: "a"}]
print(list_5)

list_6 = [i + i for i in "ABCDEFG"]
print(list_6)

print("*" * 20, "1-100之内的偶数", "*" * 20)
list_7 = [i for i in range(0, 101) if i % 2 == 0]
print(list_7)

print("*" * 20, "求已知列表里的所有的英文单词", "*" * 20)
list_8 = ["62", "hello", "100", "world", "luck", "high", "88"]
list_9 = [i for i in list_8 if i.isalpha()]
print(list_9)

print("*" * 20, "求已知列表里的所有的英文单词,h开头的的单词，首字母大写，不是h开头的单词全部转大写", "*" * 20)
list_8 = ["62", "hello", "100", "world", "luck", "high", "88"]
list_10 = [i.title() if i.isalpha() and i.startswith("h") else i.upper() for i in list_8]
list_11 = []
print(list_10)

print("*" * 20, "1-100里，实现[[1,2,3],[4,5,6],[7,8,9]...]", "*" * 20)
# 写法1
list_12 = [[a, a + 1, a + 2] if a <= 98 else [a for a in range(a, 101)] for a in range(1, 101, 3)]
print("方法1的结果是：", list_12)

# 写法2
x = [i for i in range(1, 101)]
list_13 = [x[y:y + 3] for y in range(0, len(x), 3)]  # 该方法是从切片的起始值和终止值找规律
print(x)
print("方法2的结果是：", list_13)

# 写法3
list_14 = [[c for c in range(b, b + 3)] if b <= 98 else [c for c in range(b, 101)] for b in range(1, 101, 3)]
print("方法3的结果是：", list_14)
