#!/usr/bin/python3
# -*- coding:utf-8 -*-
import allure


# 定义一个测试类
@allure.feature("添加成员")
class TestAddMember:

    # 测试用例1：添加成员正常流程
    @allure.story("添加成员成功")
    def test_add_member_success(self, setup_teardown, get_datas_byfixture):
        phone_list = setup_teardown.pagehome_go_to_addmember().addmember_success(get_datas_byfixture[0],
                                                                                 get_datas_byfixture[1],
                                                                                 get_datas_byfixture[2]).get_members(
            get_datas_byfixture[2])
        assert get_datas_byfixture[2] in phone_list

    # 测试用例2：添加成员失败
    @allure.story("添加成员失败")
    def test_add_member_fail(self, setup_teardown, get_datasfail_byfixture):
        text_assert = setup_teardown.pagehome_go_to_addmember().addmember_fail(get_datasfail_byfixture[0],
                                                                               get_datasfail_byfixture[1],
                                                                               get_datasfail_byfixture[2])
        assert get_datasfail_byfixture[3] in text_assert
