#!/usr/bin/python3
# -*- coding:utf-8 -*-
print("*" * 20, "str.replace(old,new,count)：字符串替换，count表示替换个数，默认全部替换", "*" * 20)
a = "小张，说小王打了小吴，小王还打了小陈"
print(a.replace("小王", "**"))
print(a.replace("小王", "**", 1))  # 仅替换一个

print("*" * 20, "把小张和小王都替换成**", "*" * 20)
# 方法1：正则表达式
# 方法2：for循环，

print("*" * 20, "字符串切割", "*" * 20)
print("*" * 20, "str.split('分隔符',maxsplit)左切割，str.rsplit('分隔符',maxsplit)右切割", "*" * 20)
b = "哈喽  你好 拜拜"
print(b.split("  "))  # 要搜索的分隔符，遇到该分隔符就切断一次，返回一个列表
print(b.rsplit("  "), 1)  # 仅分割一次

print("*" * 20, "str.splitlines()：按行切割", "*" * 20)
c = '''你好，吃饭吧，
你好，跳舞吧，
你好，唱歌吧
你好，玩去吧'''
print(c.splitlines())

print("*" * 20, "str.partition('分隔符')，返回一个元组(分隔符左边部分，分隔符，分隔符右边部分)", "*" * 20)
d = "哈喽  你好 拜拜"
print(d.partition("  "))  # 匹配到的分隔符仅分割一次，返回元组

print("*" * 20, "str.title()：每个单词首字母大写", "*" * 20)
e = "hello world"
print('每个单词首字母大写：', e.title())

print("*" * 20, "str.capitalize()：第一个单词首字母大写", "*" * 20)
f = "hello world"
print('第一个单词首字母大写：', f.capitalize())

print("*" * 20, "str.upper()：所有小写字母转大写；str.lower()：所有大写字母转小写", "*" * 20)
g = "helLO wORld"
print("所有小写字母转为大写：", g.upper())
print("所有大写字母转为小写：", g.lower())
