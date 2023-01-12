# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
装饰器带参数：多定义一层
"""


def outer_check(time):  # 第一层：接收装饰器的参数
    def check_time(action):  # 第二层：接收原函数
        def do_action():  # 第三层：接收原函数的参数
            if time < 22:
                return action()
            else:
                return "对不起，您不具备该权限！"

        return do_action  # 返回第三层

    return check_time  # 返回第二层


@outer_check(21)
def play_game():
    return "玩游戏"


print(play_game())

"""
装饰器应用场景
"""
is_login = False


def login():
    username = input("请输入登录用户名：")
    password = input("请输入登录密码：")
    if username == "admin" and password == "1234":
        return True
    else:
        return False


def login_required(func):
    def wrapper(*args, **kwargs):
        global is_login
        if is_login:  # 引用全局变量，无需global
            func(*args, **kwargs)
        else:
            print("请先登录")
            is_login = login()  # 改变全局变量的值，必须global
            print("登录结果为：", is_login)

    return wrapper


@login_required
def pay(money):
    print("---开始付款---")
    print("---正在付款---")
    print(f"---成功付款{money}元---")


pay(999)
pay(888)
