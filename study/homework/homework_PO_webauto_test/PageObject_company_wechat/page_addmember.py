#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_base import PageBase
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_contact import PageContact


# 企业微信_添加成员页面，定义一个类
class PageAddMember(PageBase):

    # 添加成员页面，方法1：成功添加成员，跳转到通讯录页面
    def addmember_success(self, username, account, phone):
        self.br.find_element(By.ID, 'username').send_keys(username)
        self.br.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        self.br.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        self.br.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return PageContact(self.br)

    # 添加成员页面，方法2：点击【取消】按钮，返回通讯录页面
    def addmember_cancel(self):
        # 暂未完善
        return PageContact(self.br)

    # 添加成员页面，方法3：添加成员失败，停留在当前页面
    def addmember_fail(self, username, account, phone):
        self.br.find_element(By.ID, 'username').send_keys(username)
        self.br.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        self.br.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        error_message1 = self.br.find_element(By.XPATH, '//div[contains(text(), "该帐号已被")]').text
        self.br.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        error_message2 = self.br.find_element(By.XPATH, '//div[contains(text(), "该手机已被")]').text
        self.br.find_element(By.CSS_SELECTOR, '.js_btn_cancel').click()
        text_assert = error_message1 + "，" + error_message2
        return text_assert
