#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
发布一个贴：昨天晚会遇到一个漂亮的小姐姐，要不要表白呢？
输入用户名：小白
反复回复：
    1、回复内容不能为空
    2、回复内容不能存在"亲嘴"和"接吻"敏感词汇，都替换成"亲亲"
    3、最多评论20个字，剩余多少个字
    4、回复内容前后不能有空格
小白：抓紧表白
小黑：。。。
小花：。。。
"""
msg = input("请发布一个帖子：")
print("*" * 50)
print("以下为回复内容")
hello = True
while hello:
    name = input("请输入用户名：")
    if len(name.strip()) == 0:  # 用户名去除两端空格之后长度为0：用户名为空
        print("用户名不可为空！")
    else:
        print(name)
        while True:
            reply = input("请输入回复内容：")
            if len(reply.strip()) == 0:
                print("回复内容不可为空！")  # 回复内容为空，重新输入回复内容
            else:
                if len(reply.strip()) > 20:
                    print("回复内容不可超过20个字")  # 回复内容超过20字，重新输入回复内容
                else:
                    if ("亲嘴" in reply) or ("接吻" in reply):
                        for i in range(1, 3):
                            if i == 1:
                                reply = reply.strip().replace("亲嘴", "亲亲")  # 去除空格之后替换(去除空格后赋值给一个新变量也行)
                            else:
                                reply = reply.strip().replace("接吻", "亲亲")  # 去除空格之后替换
                        print("{}的评论'{}'发布成功".format(name, reply))
                        hello = False  # 评论成功，更改外层循环条件，相当于跳出外层循环，如果不跳出，则一直会输入用户名和回复，死循环
                    else:
                        print("{}的评论'{}'发布成功".format(name, reply))
                        hello = False  # 评论成功，更改外层循环条件，相当于跳出外层循环，如果不跳出，则一直会输入用户名和回复，死循环
                    break  # 评论成功跳出while循环
