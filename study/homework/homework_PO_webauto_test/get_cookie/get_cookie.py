#!/usr/bin/python3
# -*- coding:utf-8 -*-
import yaml
from selenium import webdriver
from time import sleep


# 定义一个类
class TestGetCookie:
    def setup(self):
        self.brower = webdriver.Chrome()

    def teardown(self):
        self.brower.quit()

    # 方法1：首次登录获取cookie，并存放到yaml文件
    def test_get_cookie(self):
        self.brower.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        self.brower.maximize_window()
        self.brower.implicitly_wait(3)
        # 等待10秒，人工进行扫码登录
        sleep(5)
        # 使用get_cookies()方法获取cookie
        cookies = self.brower.get_cookies()
        print(cookies)
        # with方法，文件不存在则创建，存在则打开，as为后续方便引用的别名
        with open("/Users/liyong/Desktop/study/homework/homework_PO_webauto_test/get_cookie/cookie.yaml",
                  "w") as cookies_file:
            # yaml.safe_dump(a,b)，参数a为需要写入的数据，参数b为接收数据写入的文件，至此，cookie被写入cookie.yaml
            yaml.safe_dump(cookies, cookies_file)

    # 方法2：从yaml文件里提取cookie，植入浏览器，实现无需扫码登录
    def test_add_cookie(self):
        # 打开企业微信扫码登录页面
        self.brower.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        # 读取cookie.yaml文件，my_cookies得到一个列表
        my_cookies = yaml.safe_load(
            open("/Users/liyong/Desktop/study/homework/homework_PO_webauto_test/get_cookie/cookie.yaml"))
        # 轮循列表，依次将列表所有元素尝试添加至浏览器
        for my_cookie in my_cookies:
            self.brower.add_cookie(my_cookie)
        # 再次打开企业微信已登录页面，实现无需再次扫码登录成功
        self.brower.get("https://work.weixin.qq.com/wework_admin/frame")
