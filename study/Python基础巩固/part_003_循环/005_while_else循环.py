#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 示例1
n = 1
while n <= 10:
    print(n,end='')
    n += 1
else:
    print("\n循环完成，且未被中断，就执行else")

# 示例2
m = 1
while m <= 10:
    if m == 5:
        break
    print(m,end='')
    m += 1
else:
    print("\n循环被中断，不再执行else")