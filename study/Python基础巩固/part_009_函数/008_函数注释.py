#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
函数的注释：
def 函数名([参数1，参数2，...]):
    基本注释 "注释内容"
    高级注释 """
            函数说明
            函数参数说明
            函数返回值说明
            """
'''


def login(username, password):
    '''
    校验是否登录成功的函数
    :param username: 登录用户名
    :param password: 登录密码
    :return: 登录成功返回True，登录失败返回False
    '''
    if username == "admin" and password == "1234":
        print("登录成功！")
        return True
    else:
        print("用户名或密码有误！")
        return False


print("*" * 20, "在函数调用时，鼠标hover在函数名上，会显示函数的注释", "*" * 20)
login("admin", "1234")

print("*" * 20, "也可以使用help(函数名)查看函数注释", "*" * 20)
help(login)
