#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
写法：
for i in n:   # n可以是range()函数，可以是列表，元组，字典，集合等，集合是随机取，取过的值会被抛弃不会重复取，字典的话仅取key值
    循环体子语句
else:
    循环体语句执行完成且未被中断(break或默认循环完成)过，则会执行else里的语句
"""
# 示例1
for i in [1, 2, 3]:
    print(i)
for j in (1, 2, 3):
    print(j)
for k in {"1", "abc", 3, (1, 2, 4)}:
    print(k)
for h in {"name": "老李", "age": 18}:
    print(h)

# 示例2：已知正确的用户名和密码(admin/1234)，用户输入正确则提示登录成功，输入错误则提示输入错误，连错三次提示账号被锁定
for L in range(3):
    username = input("请输入登录用户名：")
    password = input("请输入登录密码：")
    if username == "admin" and password == "1234":
        print("~~~登录成功啦~~~")
        break
    else:
        print("~~~账号密码输入错误~~~")
    L += 1
else:
    print("账号密码输入连续错误三次，账号已被锁定")