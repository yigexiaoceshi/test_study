#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、定义一个书架：books = [{},{},{}]
2、往里面循环添加三本书的信息，包括书名/作者/价格
3、书名不能重复
"""
# 写法1：
# books = []
# while True:
#     if len(books) >= 3:
#         break
#     while True:
#         value1 = input("请输入书名：")
#         for i in books:
#             if value1 in i.values():
#                 print("书名重复，请重新输入！")
#                 break  # 书名重复跳出for循环，重复执行while循环，重新输入书名
#         else:
#             break  # 书名不重复，跳出while循环
#     value2 = input("请输入作者：")
#     value3 = input("请输入价格：")
#     book = {"书名": value1, "作者": value2, "价格": value3}
#     books.append(book)
#     print(books)
# print(books)

# 写法2
# books = []
# flag = True
# while flag:
#     book = input("请输入'书名 作者 价格'(以一个空格隔开)：").split(" ")  # 以一个空格切割为三个元素的列表
#     for i in books:  # 第一次添加，books为空，不会执行直接进入对应的else进行添加，第二次books不为空，i为字典
#         if i["书名"] == book[0]:
#             print(f"'{book[0]}'已存在，请重新输入！")
#             break
#     else:
#         books.append({"书名": book[0], "作者": book[1], "价格": book[2]})
#         print(f"已成功将'{book[0]}'添加到书架！")
#     if len(books) >= 3:
#         flag = False
# print(books)

# 写法3：
"""
这里注意（踩坑了）：book定义在循环外面和循环里面的区别（声明一次和声明三次的区别）
（一）、book定义在循环外面时：
不管循环多少次，永远指向同一个内存空间，添加到books里的也一直是这个空间，循环第一次时，修改了book的value并添加到了
books这里正常，但是循环第二次时，再去更改book的value值，相当于在同一个内存空间上做修改，所以会同时修改掉books里的值，再做一次添加，会添加
2个相同的字典元素到books，第三次同理会添加三个相同的字典元素到books。
    理解：三次循环修改的是同一个book，然后再做添加，添加三个相同的字典。
（二）、book定义在循环里面时：每循环一次，都重新定义一个内存空间，第一次循环拿到第一个定义的book，并更改book的value值，放进books，第二次循环时，
book被重新定义，指向另一个不同的内存空间，此时修改book的value值不会影响到第一个book(就是已经添加到books里的book)，所以这时添加到books里
的book和第一个book不同，同理第三个book也和前两个book不同。
    理解：三次循环修改的是三个不同的book，然后再做添加，添加三个不同的字典。
（三）、小结：如果是可变数据类型，在循环时，数据发生改变，都在原来的内存空间修改数据，所以会修改已经循环并存放了的数据，所以需要在循环内部声明；
如果是不可变数据类型，在循环时，数据发生变化，会开辟一个新的内存空间去存放数据，不会修改原来的数据，所以可以声明在循环外面。这个坑需要注意的
就是必须把每次的值给到一个新的内存空间去操作，不影响原来的值，所以可以在循环内定义可变或不可变数据类型，可变数据类型每声明一次就给一个新的内存
空间，不可变数据类型每当数据发生变化，也会重新申请一个新的内存空间存放新的数据。
"""
books = []
n = 0
while n < 3:
    book = dict.fromkeys(["书名", "作者", "价格"])
    # 或者
    # book = {"书名": None, "作者": None, "价格": None}
    print("循环前book为：", book)
    book_name = input("请输入书名：")
    # if book_name == book["书名"]:  # 这个判断只能判断和上次是否一致，上次之前的无法判断，所以还是要从books里循环取值判断
    for i in books:
        if book_name == i["书名"]:  # 注：此处如果用book_name in i.values()的话，会判断其他元素的value不能重复，出现多判的情况
            print(f"{book_name}已存在，请重新输入")
            break
    else:
        book_person = input("请输入作者：")
        book_price = input("请输入价格：")
        book["书名"] = book_name
        book["作者"] = book_person
        book["价格"] = book_price
        print(id(book))
        print("循环后book的value更新：", book)
        print("添加book之前的books:",books)
        books.append(book)
        print("添加book之后的books为：", books)
        n += 1
print(books)
