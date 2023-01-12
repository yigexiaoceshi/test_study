#!/usr/bin/python3
# -*- coding:utf-8 -*-
book = {'书名': '《三体》', '价格': 16.0, '作者': '刘慈欣', '出版社': 'XXX出版社'}
print("*" * 20, "获取字典所有的key", "*" * 20)
for i in book:
    print(i)  # 直接遍历字典，取出来的是key
# 等同于：
for j in book.keys():
    print(j)
print(book.keys())
print(list(book.keys()))

print("*" * 20, "获取字典所有的value", "*" * 20)
for k in book.values():
    print(k)
print(book.values())
print(list(book.values()))

print("*" * 20, "获取字典所有的key/value对：dict.items()，每一对放在一个元组里，嵌套成一个列表返回", "*" * 20)
print(book.items())
print(list(book.items()))
for h in book.items():
    print(h)
# 也可以写成：
for x, y in book.items():
    print(x, y)

print("*" * 20, "dict.setdefault(key,value),key存在则默认值无效，key不存在则新增，仅做新增", "*" * 20)
book.setdefault('出版社', '人民教育出版社')
print(book)
book.setdefault("出版时间", 1990)
print(book)

print("*" * 20, "字典合并：dict.update(dict1)，将参数dict1里的键值对添加到dict里", "*" * 20)
dict1 = {"a": 10, "b": 20}
book.update(dict1)
print(book)

print("*" * 20, "字典新增：dict.fromkeys(a,b)，参数a必须是个可迭代对象，作为key，b作为value的默认值", "*" * 20)
xx = dict.fromkeys(["a", "b"], 10)
print(xx)
yy = dict.fromkeys(("a", "b"), ["fsfs", 3234, True])
print(yy)

print("*" * 20, "字典转列表：list(dict)，将dict里的键转为了列表", "*" * 20)
dict_person = {"name": "张三", "age": 19, "sex": "男"}
print(list(dict_person))

print("*" * 20, "字典转元组：tuple(dict)，将dict里的键转为了元组", "*" * 20)
print(tuple(dict_person))

print("*" * 20, "字典转集合：set(dict)，将dict里的键转为了集合", "*" * 20)
print(set(dict_person))

print("*" * 20, "列表转字典：dict(list)，特定的格式才可以转", "*" * 20)
# 列表或者元组转字典的时候，元素必须全部刚好是元组内放置2个元素，且每个子元素的第一个元素必须为不可变数据类型，比如
list_a = [["a", 10], ["b", 20], ["c", 30]]
list_b = [("a", 10), ("b", 20), ("c", 30)]
list_c = [{"a": 10}, {"b": 20}, {"c": 30}]  # 转为字典会报错，因为字典是一个整体，是一个元素
print(dict(list_a))  # 原因是？？？？？？？？？
print(dict(list_b))
# print(dict(list_c))  # 报错

print("*" * 20, "元组转字典：dict(tuple)，特定的格式才可以转", "*" * 20)
# 列表或者元组转字典的时候，元素必须全部刚好是元组内放置2个元素，且第一个元素必须为不可变数据类型，比如
tuple_a = (["a", 10], ["b", 20], ["c", 30])
tuple_b = (("a", 10), ("b", 20), ("c", 30))
tuple_c = ({"a": 10}, {"b": 20}, {"c": 30})  # 转为字典会报错，因为一个字典是一个整体，是一个元素
print(dict(tuple_a))  # 原因是？？？？？？？？？
print(dict(tuple_b))
# print(dict(tuple_c))  # 报错

print("*" * 20, "集合转字典：dict(set)，特定的格式才可以转", "*" * 20)
# 列表或者元组转字典的时候，元素必须全部刚好是元组内防止2个元素，且第一个元素必须为不可变数据类型，比如
set_b = {("a", 10), ("b", 20), ("c", 30)}
print(dict(set_b))

