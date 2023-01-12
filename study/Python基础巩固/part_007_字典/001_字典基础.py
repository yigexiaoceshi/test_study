#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
字典（dictionary）：
1、花括号里头是键值对
2、键(key)不可重复：如果重复，则后定义的value会替换之前的value，即键不可修改，只能添加或删除，只能修改value
3、根据第2点，所以只有数字/字符串/元组等不可变数据类型可以做key，列表/集合等则不可以做key
4、当字典中仅有一个元素(即只有一个键值对)时，不需要加逗号(,)
5、字典无序
"""
print("*" * 20, "字典的定义", "*" * 20)
dict1 = {}
dict2 = {"name": "老李", }
print(type(dict1))
print(type(dict2))

print("*" * 20, "字典新增元素：dict[key] = value，key不存在时为新增", "*" * 20)
dict1["age"] = 19
dict1["sex"] = "男"
print(dict1)

print("*" * 20, "字典编辑value：dict[key] = value，key存在时为修改value", "*" * 20)
dict1["age"] = 20
print(dict1)

"""
例题：
1、定义一个book字典，里头存放书名/价格/作者/出版社名称
2、做活动，价格打了八折
"""
book = {}
book["书名"] = "《三体》"
book["价格"] = 20
book["作者"] = "刘慈欣"
book["出版社"] = "XXX出版社"
print(book)
book["价格"] *= 0.8
print(book)

dict3 = {"name": "老李", "age": 17, "sex": "男"}
if "name" in dict3:  # 使用in dict语法时，字典会取出所有的key进行比较，相当于in dict.keys()
    print("'name'在字典dict3里！")
elif "老李" in dict3:
    print("'老李'在字典dict3里！")
else:
    print("'name'和'老李'都不在字典dict3里！")
