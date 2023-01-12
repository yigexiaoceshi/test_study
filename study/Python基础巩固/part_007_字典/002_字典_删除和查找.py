#!/usr/bin/python3
# -*- coding:utf-8 -*-
book = {'书名': '《三体》', '价格': 16.0, '作者': '刘慈欣', '出版社': 'XXX出版社'}

print("*" * 20, "获取字典所有的键:dict.keys()，返回一个key的列表", "*" * 20)
print(book.keys())

print("*" * 20, "获取字典所有的键对应的值：dict.values()，返回一个value的列表", "*" * 20)
print(book.values())

print("*" * 20, "获取字典指定键的值:dict.get(key)，根据key获取value值，返回value值，key不存在时返回None", "*" * 20)
c = book.get("书名")  # 可根据返回值是否None来判断key是否存在
print(c)
# 第二个参数为value，默认是None，找的到时返回对应的value，找不到时默认返回None，不管key是否存在也可以指定返回值
e = book.get("书名书名啊", "《西游记》")
print(e)
# 根据key找对应的value值也可以使用这种写法，不同点是key不存在时会报错
d = book["书名"]
print(d)

print("*" * 20, "字典删除键值对：dict.pop(key)，返回key对应的value值", "*" * 20)
a = book.pop("出版社")  # 根据key删除键值对，返回对应的value值"XXX出版社"
print(a)
print(book)

print("*" * 20, "字典删除键值对：dict.popitem()，默认删除最后一对键值对，作为2个元素返回一个元组", "*" * 20)
b = book.popitem()  # 删除最后一对键值对，作为一个元组返回，如果字段为空会报错
print(b)
print(book)

print("*" * 20, "字典删除键值对：del dict[key]，类似dict.pop(key),但是无返回值", "*" * 20)
del book["书名"]
print(book)

# print("*" * 20, "删除字典结构：del dict", "*" * 20)
# del book

# print("*"*20,"字典清空：dict.clear()", "*" * 20)
# book.clear()


print("*" * 50, "例题", "*" * 50)
"""
例题1：
1、两本书：[{'书名': '《三体》', '价格': 16.0},{'书名': '《三毛流浪记》', '价格': 26.0}]
2、删除每本书的价格
"""
books = [{'书名': '《三体》', '价格': 16.0}, {'书名': '《三毛流浪记》', '价格': 26.0}]
for i in books:
    if "价格" in i.keys():
        print("子元素字典中存在'价格'这个key！")
        result = i.pop("价格")
        print("'价格'删除成功，返回值为对应的value：", result)
    else:
        print("子元素字典中没有'价格'这个key！")
print(books)
