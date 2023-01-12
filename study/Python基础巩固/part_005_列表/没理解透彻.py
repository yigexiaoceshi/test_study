#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
for i in range(len(list1) - 1, -1, -1):  # 已经理解，range(5,-1,-1)，相当于从5开始，从右至左一直到-1(从右至左数时，-1在5左边)，即[5,-1)，即5,4,3,2,1,0
    print(i, end='')
print()  # 加个换行

for j in range(0, len(list1), 2):  # [0,1,2,3,4,5,6)
    print(j, end='')
print()  # 加个换行

for k in range(5, -1, -1):
    print(k, end="")
print()  # 加个换行
print(f"你好，你的名字是{'张三'}")
