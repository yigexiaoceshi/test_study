#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = []
list2 = ["A", "B"]

print("*" * 20, "列表添加元素：list.append('a')，在列表的末尾添加元素a", "*" * 20)
list1.append("aa")  # 返回None，所以不能进行赋值操作
list1.append("bb")  # list.append(a),a可以是列表支持的一切数据类型，作为单个元素添加在末尾
print(list1)

print("*" * 20, "指定索引位置添加元素：list.insert(index,'a')", "*" * 20)
list1.insert(2, 8)  # 索引2的位置插入元素8，原来索引为2的元素往后移动
print(list1)

print("*" * 20, "列表的合并1：list_a + list_b", "*" * 20)
"""数值可以用+(数学符号，相加)，字符串可以+(字符串拼接)，列表可以+(列表合并)"""
list3 = list1 + list2
print(list3)

print("*" * 20, "列表的合并2：list_a.extend(list_b)，在列表list_a的末尾添加所有list_b的元素", "*" * 20)
list1.extend(list2)  # 把list2里的元素依次加入到list1的末尾
print(list1)

print("*" * 20, '示例1：添加多个商品，储存所有商品信息', "*" * 20)
container = []
flag = True
while flag:
    name = input("请输入商品名称：")
    price = input("请输入商品价格：")
    number = input("请输入商品数量：")
    goods = [name, price, number]
    container.append(goods)
    ask = input("是否继续添加商品，输入'q'或者'Q'退出添加，其他任意键继续添加：")
    if ask.upper() == "Q":
        flag = False  # 退出循环
price_all = 0.0
number_all = 0
for i in container:
    print(i)
    print(i[0], i[1], i[2])
    print("{}\t{}\t{}".format(i[0], float(i[1]), int(i[2])))
    price_all += (float(i[1]) * int(i[2]))
    number_all += int(i[2])
print("商品的总价为{}元".format(price_all))
print("商品的总数量为{}个".format(number_all))
