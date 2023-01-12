#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_addmember import PageAddMember
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_base import PageBase
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_contact import PageContact


# 企业微信_首页，定义一个类
class PageHome(PageBase):

    # 首页，方法1：点击【通讯录】跳转到通讯录页面
    def pagehome_go_to_pagecontact(self):
        self.br.find_element(By.ID, 'menu_contacts').click()
        return PageContact(self.br)

    # 首页，方法2：点击【添加成员】跳转添加成员页面
    def pagehome_go_to_addmember(self):
        self.br.find_element(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return PageAddMember(self.br)
