#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
图书馆图书管理系统：
1、库存library，一共7本书
2、借书：根据书名book_name和作者author查询，二选其一，库存number是否足够，借书成功，库存减少
3、还书：库存增多
4、查询书：根据书名book_name和作者author查询，二选其一
5、查询库存所有书
6、退出管理系统
"""
from time import sleep

library = [{"book_name": "红楼梦", "author": "曹雪芹", "price": 100, "number": 40},
           {"book_name": "红楼梦", "author": "无名氏", "price": 100, "number": 40},
           {"book_name": "西游记", "author": "吴承恩", "price": 100, "number": 40},
           {"book_name": "水浒传", "author": "施耐庵", "price": 100, "number": 40},
           {"book_name": "三国演义", "author": "罗贯中", "price": 100, "number": 40},
           {"book_name": "天龙八部", "author": "金庸", "price": 100, "number": 40},
           {"book_name": "神雕侠侣", "author": "金庸", "price": 100, "number": 40}]

print('~~~~~~~~~~~~~~~~~~欢迎来到图书管理系统~~~~~~~~~~~~~~~~~~')
flag = True
while flag:
    choice = input("请选择功能：\n1.借书\n2.还书\n3.查询书\n4.查询所有库存\n5.退出系统\n")
    if choice == "1":
        print("欢迎使用借书功能！")
        bbbb = True
        while bbbb:
            borrow_book_name = input("请输入要借的书名：")
            book_names = []
            for j in library:
                book_names.append(j["book_name"])
            if borrow_book_name in book_names:
                print(f"您查找的书名'{borrow_book_name}'在库存里存在，书籍信息如下：")
                borrow_books = []
                for k in library:
                    if borrow_book_name == k["book_name"]:
                        for a, b in k.items():
                            print(str(a).ljust(10), str(b).ljust(10), end="")
                        print("")
                        borrow_books.append(k)
                print("符合书名的书籍信息为：", borrow_books)
                borrow_author = input("请输入书籍的作者：")
                success_book = []
                borrow_authors = []
                for aa in borrow_books:
                    if aa["author"] == borrow_author:
                        borrow_authors.append(aa["author"])
                        if borrow_author in borrow_authors:
                            print("名字为{}的书中找到了作者为{}的书。".format(borrow_book_name, borrow_author))
                            for e, f in aa.items():
                                print(str(e).ljust(10), str(f).ljust(10), end="")
                            success_book.append(aa)
                            print()
                            aaaa = True
                            while aaaa:
                                borrow_number = input("请输入要借的数量：")
                                for bb in success_book:
                                    if borrow_number.isdigit():
                                        if int(borrow_number) <= bb["number"]:
                                            print("借阅数量不大于库存数量，支持借阅")
                                            answer = input("是否借阅？(输入y或Y确定，其他任意键退出！)")
                                            if answer.upper() == "Y":
                                                print("借书成功！")
                                                for cc in library:
                                                    if cc["book_name"] == borrow_book_name and cc["author"] == borrow_author:
                                                        cc["number"] -= int(borrow_number)
                                                aaaa = False
                                                bbbb = False
                                            else:
                                                aaaa = False
                                                bbbb = False
                                        else:
                                            print("库存不足，请重新输入")
                                    else:
                                        print("数量输入有误，请重新输入")
                            break
                        else:
                            print("名字为'{}'的书中未找到作者为'{}'的书。请重新输入！".format(borrow_book_name, borrow_author))
                    else:
                        pass
            else:
                print("您输入的书名不在图书馆库存中，请重新输入！")
    elif choice == "2":
        return_book_name = input("请输入要归还的书名：")
        return_book_author = input("请输入要归还的书籍的作者：")
        return_book_number = input("请输入要归还的数量：")
        for i in library:
            if i["book_name"] == return_book_name and i["author"] == return_book_author:
                i["number"] += int(return_book_number)
        while True:
            ask = input("是否继续还书？(输入y/Y继续还书，输入其他任意键退出)")
            if ask.upper() == "Y":
                pass
            else:
                print("您选择了不再还书，即将退出还书功能！")
                break
    elif choice == "3":
        print("欢迎使用图书查询功能！")
        while True:
            find = input("请输入需要查找的书名(book_name)或作者(author):")
            book_names = []
            authors = []
            for j in library:
                book_names.append(j["book_name"])
                authors.append(j["author"])
            if find in book_names:
                print(f"您查找的书名'{find}'在库存里存在，书籍信息如下：")
                for k in library:
                    if find == k["book_name"]:
                        for a, b in k.items():
                            print(str(a).ljust(10), str(b).ljust(10), end="")
                        print()
                ask = input("是否继续查询(输入y或Y继续查，其他任意键退出)：")
                if ask.upper() == "Y":
                    pass
                else:
                    break
            elif find in authors:
                print(f"您查找的作者'{find}'在库存里存在，书籍信息如下：")
                for h in library:
                    if find == h["author"]:
                        for c, d in h.items():
                            print(str(c).ljust(10), str(d).ljust(10), end="")
                        print()
                ask = input("是否继续查询(输入y或Y继续查，其他任意键退出)：")
                if ask.upper() == "Y":
                    pass
                else:
                    break
            else:
                ask = input("您输入的书名或作者未找到任何记录，是否继续查询(输入y或Y继续查，其他任意键退出)：")
                if ask.upper() == "Y":
                    pass
                else:
                    break
    elif choice == "4":
        print("欢迎使用查询库存功能，实时库存如下：")
        for i in library:
            for k, v in i.items():
                print(str(k).ljust(10), str(v).ljust(10), end="")
            print()
    elif choice == "5":
        print("正在退出图书管理系统，请稍后...")
        sleep(1)
        print("退出成功，欢迎再次使用！")
        flag = False
    else:
        print("输入有误，请重新选择！")
