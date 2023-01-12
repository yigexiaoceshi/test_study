#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
键盘输入以下内容并打印输出：
默认（admin,1234）
用户名：username
密码：password
是否记住密码is_remember为bool类型
判断：如果用户名和密码正确并且is_remember是True则表示记住密码，输出"已经记住密码啦"，否则打印：没有记住密码，需要下次继续输入"
"""
username = input("请输入用户名：\n")
password = input("请输入密码：\n")
is_remember = True
if username == "admin" and password == "1234":
    if is_remember:
        print("已经记住用户名%s密码啦" % username)
    else:
        print("没有记住密码，需要下次继续输入")
else:
    print("用户名密码输入有误")
