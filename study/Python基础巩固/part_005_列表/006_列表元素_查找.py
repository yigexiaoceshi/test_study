#!/usr/bin/python3
# -*- coding:utf-8 -*-
list1 = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']

print("*" * 20, "查找元素是否在列表内存在：元素 in list 或 元素 not in list，返回bool类型", "*" * 20)
if "兔子" in list1:
    print("元素'兔子'在列表list1里！")
else:
    print("元素'兔子'不在列表list1里！")


print("*" * 20, "查找列表中元素的索引：list.index('元素名')，返回索引值，元素不存在则会报错，一般结合if条件使用，避免报错", "*" * 20)
if "老虎" in list1:  # 先判断元素是否存在
    print(list1.index("老虎"))  # 存在再查找索引
    print("元素老虎的索引值是：{}".format(list1.index("老虎")))
else:
    print("元素'老虎'不在列表list1里面！")


print("*" * 20, "查找列表中指定元素的数量：list.count('元素名')，返回整数，不存在返回0", "*" * 20)
rabbit_count = list1.count('兔子')
print('元素"兔子"的数量为:{}'.format(rabbit_count))
# 返回0表示不存在该元素
if list1.count("小熊猫") == 0:
    print("元素'小熊猫'不在列表list1里")
else:
    print("元素'小熊猫'在列表list1里")