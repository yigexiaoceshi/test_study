#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
集合（set）：
1、无序：无索引概念，无法通过下标读取元素
2、元素不重复且必须可哈希：类似字典里的key，所以列表/集合/字典不可作为集合的元素，数值/字符串/元组则可以
3、符号：{}
4、花括号里非键值对且非空时，为集合
"""
print("*" * 20, "定义空集合：set()", "*" * 20)
# 注：a = {}，此时a是个字典，空集合用set()表示
set1 = set()
print("set1的类型为：{}，值为：{}".format(type(set1), set1))

print("*" * 20, "定义非空集合：set()", "*" * 20)
set2 = {1, "a", "你好", False}
print("set2的类型为：{}，值为：{}".format(type(set2), set2))

# 例题：列表元素去重，转为集合再转换回列表就去重了
lista = [1, 3, 3, 4, 5, 6, 5, 7, 8, 9, 9]
print(list(set(lista)))

print("*" * 20, "集合添加单个元素：set.add(元素)", "*" * 20)
set3 = set()
set3.add("西游记")
set3.add("红楼梦")
print(set3)

print("*" * 20, "集合合并：set.update(集合1)，将集合1的所有元素添加到set里", "*" * 20)
set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set5.update(set4)  # 将set4里的元素合并到set5，set4本身不变
print(set4)
print(set5)

print("*" * 20, "删除单个元素：set.remove(元素)，元素不存在会报错(KeyError)", "*" * 20)
set6 = {'NDFq', 'YV0D', 'otwy', 's23k', 'GadY'}
set6.remove('s23k')  # 要删除的元素不存在时会报错
print('set6:', set6)

print("*" * 20, "删除单个元素：set.discard(元素)，元素不存在不做任何操作，也不报错", "*" * 20)
set7 = {'NDFq', 'YV0D', 'otwy', 's23k', 'GadY'}
set7.discard('s23kKKKKKK')  # 要删除的元素不存在时不会报错
print('set7:', set7)

print("*" * 20, "清空整个集合：set.clear()，内存地址还在，未被释放", "*" * 20)
set8 = {'NDFq', 'YV0D', 'otwy', 's23k', 'GadY'}
set8.clear()
print('清空后的set8:', set8)
set8.add("重新添加元素")
print('set8:', set8)

print("*" * 20, "删除整个集合：del set，释放内存空间", "*" * 20)
# del用来操作删除元素，都是根据下标(有序数列)或者key(字典)来删除的，集合的特性无需且无key所以无法用del删除元素，只能删除整个集合
set9 = {1, 2, "ABC"}
del set9

print("*" * 20, "随机删除任意一个元素：set.pop()", "*" * 20)
set10 = {'NDFq', 'YV0D', 'otwy', 's23k', 'GadY'}
set10.pop()
print('set10:', set10)

print("*" * 20, "求交集：set.intersection(set1),set和set1相同的元素，也可以使用符号(&)", "*" * 20)
set11 = {1, 2, 3, 4, 5}
set12 = {3, 4, 5, 6, 7}
result_jiaoji = set11.intersection(set12)
print(result_jiaoji)
# 也可以使用符号(&)
print(set11 & set12)

print("*" * 20, "求并集：set.union(set1)，set和set1所有的元素，相同的去重，也可以使用符号(|)", "*" * 20)
set13 = {1, 2, 3, 4, 5}
set14 = {3, 4, 5, 6, 7}
result_bingji = set13.union(set14)
print(result_bingji)
# 也可以使用符号(|)：
print(set13 | set14)

print("*" * 20, "求差集：set.difference(set1)，set里存在，set1里不存在元素，也可以使用符号(-)", "*" * 20)
set15 = {1, 2, 3, 4, 5}
set16 = {3, 4, 5, 6, 7}
result_chaji = set15.difference(set16)  # set15里有，set16里没有的元素
print(result_chaji)
# 也可以使用符号(-)：
print(set15 - set16)

result_chaji1 = set16.difference(set15)  # set16里有，set15里没有的元素
print(result_chaji1)
# 也可以使用符号(-)：
print(set16 - set15)
