#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']

# 方法1：元素被删除，影响的是从左至右的索引，从右至左的索引没变
# 这是list1的拷贝，所以删除元素该拷贝列表的索引不会发生变化
# for k in range(len(list1) - 1, -1, -1):  # 相当于range(5,-1,-1)，从5到-1，前开后闭，[5,-1)，即5，4，3，2，1，0
#     if list1[k] == "狮子":
#         list1.pop(k)
#     else:
#         pass
# print(list1)

# 等同于下面
for k in list1[::-1]:  # 列表的拷贝，相当于一直有6个元素的新列表
    if k == "狮子":
        list1.remove(k)
    else:
        pass
print('list1:', list1)

# 方法2：
list2 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
n = 0
while n < len(list2):  # 删除元素，索引自动前移
    if list2[n] == "狮子":
        list2.remove(list2[n])  # 只要删除了元素，索引不变
    else:
        n += 1  # 未删除元素，索引往后移
print('list2', list2)

# 方法3：
list3 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
list4 = []
for i in list3:
    if i != "狮子":
        list4.append(i)
print('list4', list4)

# 方法4：
list5 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
print(list5.count("狮子"))
for h in range(list5.count("狮子")):  # 遍历狮子出现的次数，而不是列表，所以删除元素带来的影响忽略
    list5.remove("狮子")
print('list5', list5)
