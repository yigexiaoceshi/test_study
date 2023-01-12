#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
输入：input()
输出：print()
"""

a = input("请输入任意字符：")
print("a的类型为：", type(a), "'%s'的值为：" % a, a)  # 字面量使用，只要出现在字符串里面就行，包括字符串里再套一层引号
print("a的类型为：", type(a), "a的值为：", a)

b = "abc"
print("b的类型为：", type(b), "%s的值为：" % b, b)
print("b的类型为：", type(b), "b的值为：", b)
