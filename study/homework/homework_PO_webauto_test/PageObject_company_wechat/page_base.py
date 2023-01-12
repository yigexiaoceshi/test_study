#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


# 定义一个父类
class PageBase():

    # 实例化浏览器时，会调用该构造函数，子类没有定义会直接调用父类的
    def __init__(self, son_br: WebDriver = None):  # 默认值为None
        if son_br == None:
            self.br = webdriver.Chrome()
            self.br.maximize_window()
            self.br.implicitly_wait(10)
            self.br.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
            # 读取cookie.yaml文件，my_cookies得到一个列表
            my_cookies = yaml.safe_load(open("../get_cookie/cookie.yaml"))
            # 轮询列表，依次将列表所有元素尝试添加至浏览器
            for my_cookie in my_cookies:
                self.br.add_cookie(my_cookie)
            # 再次打开企业微信已登录页面，实现无需再次扫码登录成功
            self.br.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.br = son_br
