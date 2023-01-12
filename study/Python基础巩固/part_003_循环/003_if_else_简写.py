#!/usr/bin/python3
# -*- coding:utf-8 -*-
a = 1
b = 2
# if a < b:
#     c = a
# else:
#     c = b
# 下面简写方式解读：c = 后面是一个条件判断，如果a<b成立，c=if前面的a，如果不成立，c=if后面的b
c = a if a < b else b
# 解读：如果if条件成立，执行if前面的语句，否则执行if后面的语句
print("if成立打印这句") if a < b else print("if条件不成立执行这句")
print(a, b, c)

# Python中，转换成bool值为False时，0,'',"",None,{},(),[]，其他都是True
if "":  # 返回False
    print("if条件不成立，不输出")
else:
    print("执行这句")

if "1":  # 1不为空，返回True，该条件恒成立
    print("111")
else:
    print("这里永远不会进来")