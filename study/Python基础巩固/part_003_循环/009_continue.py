#!/usr/bin/python3
# -*- coding:utf-8 -*-
for i in range(1, 11):
    if i % 3 == 0:
        continue  # 跳出本轮循环之后的语句，直接进入下一轮循环
        print("这个语句不会打印")
    print(i, "  ", end='')

for j in range(1, 11):
    if j % 3 != 3:
        print(j, "  ")
