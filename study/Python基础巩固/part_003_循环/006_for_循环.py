#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
for循环结构：
for (...){
    循环体
}

for循环格式：range()是一个可迭代对象，只要是个可迭代对象都可以，比如字符串，列表，元祖，集合，字典等
for 变量名 in range(n):  # n可以是数字，可以是数组，可以是数字范围（前闭后开）等
    子语句
"""
# 示例1
# range(5)，相当于[0,4)，依次取值0，1，2，3，4，每循环一次给变量i赋值一个新的值，然后执行一次子语句，值取完时循环自动结束
for i in range(5):
    if i < 4:
        print(i, "  ", end='')
    else:
        print(i)  # 仅希望在最后一次循环结束时打印一个换行（默认带换行）

# 示例2
# range(1,5)，相当于[1,5)，依次取值1，2，3，4，每循环一次给变量j赋值一个新的值，然后执行一次子语句，值取完时循环自动结束
for j in range(1, 5):
    if j < 4:
        print(j, "  ", end='')
    else:
        print(j)  # 仅希望在最后一次循环结束时打印一个换行（默认带换行）

# 示例3
# 如果是直接打印函数range(n)，打印出来的是函数本身，因为没有变量接收函数的取值
print(range(5))
print(range(1, 5))

# 示例4
for k in range(1, 11, 2):
    print(k, "  ", end='')

# 示例5：1-100的累加和
sum_10 = 0
for x in range(1, 101):
    sum_10 += x
print("")  # 打印一个换行
print("1-100累加之和为：", sum_10)

# 示例6：1-100之间的奇数之和，写法1
sum_j = 0
for y in range(1, 101):
    if y % 2 == 1:
        sum_j += y
        # print(sum_j)
print("1-100之间所有奇数之和为：", sum_j)

# 示例6：写法2
sum_jj = 0
for z in range(1, 101, 2):
    sum_jj += z
print("1-100之间所有奇数之和为：", sum_jj)

# 示例6：写法3
sum_jjj = 0
for o in range(1, 101):
    if o & 1 == 1:  # 位运算符&，按位并，奇数的最右侧位肯定为1，XXX1，所以和1取并，即0001，一定等于1，反之一定等于0
        sum_jjj += o
print("1-100所有奇数之和：", sum_jjj)

# 示例7：1-100之间所有偶数之和，写法1
sum_o = 0
for p in range(1, 101):
    if p % 2 == 0:
        sum_o += p
print("1-100之间所有偶数之和为：", sum_o)

# 示例7：写法2
sum_oo = 0
for q in range(2, 101, 2):
    sum_oo += q
print("1-100之间所有偶数之和为：", sum_oo)

# 示例7：写法3
sum_ooo = 0
for o in range(1, 101):
    if o & 1 == 0:
        sum_ooo += o
print("1-100所有偶数之和：", sum_ooo)
