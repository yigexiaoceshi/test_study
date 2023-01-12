#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
函数：主要解决代码复用的问题

函数的定义：def关键字
def 函数名([参数...])：  # 定义格式时使用[]表明可有可无
    代码块  # 封装重复的代码内容，注意缩进

函数名：类似变量名
1、单个单词(小写)：name()
2、多个单词(下划线隔开)：get_name()
"""
import random

print("*"*20,"例题1：定义一个登录函数，生成一个大小写字母加数字的随机四位验证码","*"*20)
def generate_code():
    # 生成一个大小写字母加数字的随机四位验证码
    code = ''
    str_base = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(4):
        # 随机获取一个字母或数字
        number = random.choice(str_base)
        code += number
    print(code)
# 打印函数名(相当于一个变量，指向这个地址)，可以看到该函数已经被加载到内存，代码运行到def关键字，就会把整个代码块加载到内存
print(generate_code)  # 相当于获取当前函数的内存地址

# 函数调用，函数名后面加()，表明开始执行函数中的代码
generate_code()
generate_code()

print("*"*20,"例题2：定义一个登录函数，验证是否登录成功","*"*20)
def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin" and password == "1234":
        print("登录成功！")
    else:
        print("登录失败！")

login()