#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random

print("*" * 20, "产生五组不重复的4位验证码，由字母和数字组成", "*" * 20)
# 写法1
# set1 = set()
# str = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
# n = 1
# while n < 6:
#     yanzhengma = ""
#     for j in range(4):
#         ele_index = random.randint(0, len(str) - 1)
#         yanzhengma += str[ele_index]
#     if yanzhengma in set1:
#         print("该验证码已存在")
#     else:
#         set1.add(yanzhengma)
#         print("验证码添加成功{}次".format(n))
#         n += 1
# print(set1)

# 写法2
set1 = set()
str = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
n = 1
while True:
    yanzhengma = ""
    for j in range(4):
        # ele_index = random.randint(0, len(str) - 1)
        # yanzhengma += str[ele_index]
        # 也可以使用random.choice(str)随机选一个，其实就是上面2行代码封装而成
        ele = random.choice(str)
        yanzhengma += ele
    set1.add(yanzhengma)
    print("验证码添加成功{}次".format(n))
    n += 1
    if len(set1) == 5:
        break
print(set1)