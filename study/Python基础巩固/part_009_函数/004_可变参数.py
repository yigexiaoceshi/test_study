#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
*args：传过来的一组变量或一个变量args，前面加个*表示元组解包，args支持字符串，元组，列表，集合
**kwargs：传过来的字典解包，调用函数时，传入的时候必须是关键字参数
注意：调用函数时，出现关键字参数时要看传参是否出现**kwargs，如果出现，则会将关键字参数装入字典，如果不是，则是常规的关键字
传参(如果参数有默认值，则会替换默认值)。

装包：多个元素放入args时，会塞到一个元组里
解包：函数调用时，args前面加个*号，会将元组/列表/集合/字符串进行解包，按照一个元素一个变量值进行传入

参数类型多样时，顺序如下：位置参数、*args、默认参数/关键字参数、**kwargs，如'def sum_num(a,*args,b=22,c=33,**kwargs)'
"""
# 元组和列表的拆包
print("*" * 20, "字符串、列表、元组、集合的解包：变量前面加一个*号", "*" * 20)
str_a = "123a"
print("变量前面加*号表示解包：", *str_a)
tuple_a = (1, 2, 3, "a")
print("变量前面加*号表示解包：", *tuple_a)
list_a = [1, 2, 3, "a"]
print("变量前面加*号表示解包：", *list_a)
set_a = {1, 2, 3, "a"}
print("变量前面加*号表示解包：", *set_a)
print("*" * 20, "字典解包，加两个**号", "*" * 20)
dict_a = {1: "a", 2: "b", 3: "c"}

# 赋值
a, *b, c = 1, 2, 3, 4, 5  # 打包过程，将a,c赋值后，剩下的打包给b
print(a, b, c)
*a, b, c = 1, 2, 3, 4, 5  # 打包过程，将b,c赋值后，剩下的打包给a
print(a, b, c)
# *a,*b,*c = 1,2,3,4,5,6  # 这样就会报错
# print(a,b,c)

print("*" * 20, "求n个数之和", "*" * 20)


# 参数的个数不确定
def get_sum(*args):
    print(args)  # 可以看到，传入的是一个元组，*表示对元组解包，相当于传入多个参数
    print(*args)
    sum_number = 0
    for i in args:
        sum_number += i
    print(sum_number)


get_sum(1)
get_sum(1, 2, 3)
get_sum(1, 2, 3, 4, 5)

list_a = [23, 54, 25, 56, 98]
get_sum(*list_a)  # 解包过程

print("*" * 20, "可变参数：**kwargs", "*" * 20)


# **kwargs：key-word表明需要关键字传参
def show_books(**kwargs):
    print(kwargs)  # {}
    # print(**kwargs)
    for k, v in kwargs.items():
        print(k, v)


show_books()
show_books(book_name="西游记")  # 必须传递关键字参数，才可以装包到kwargs里（作为一个字典）
show_books(book_name="西游记", author="吴承恩")
books = {"book_name": "红楼梦", "author": "曹雪芹"}
show_books(**books)

print("*" * 20, "可变参数：*args和**kwargs同时存在", "*" * 20)


def show_bookss(*args, **kwargs):
    print(args)  # ()
    print(kwargs)  # {}
    # for i in args:
    #     print(i)
    print(f"{args[0]}和{args[1]}都想看{kwargs['book_name']}这本书！")


name = ["小红", "小明", "小花"]
bookss = {"book_name": "python入门到精通", "author": "老李"}
show_bookss("小红", "小明", **bookss)
print("*****************************************************")
show_bookss(*name, **bookss)

print("*****************************************************")
print("{}{}{}".format("aa", "bb", "cc", "dd"))  # 支持*arge
print("{name}{age}{sex}".format(name="老李", age=18, sex="男"))  # 也支持**kwargs
