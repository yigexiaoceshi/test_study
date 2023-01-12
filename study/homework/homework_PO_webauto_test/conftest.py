#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List
import pytest
import yaml

from homework.homework_PO_webauto_test.PageObject_company_wechat.page_home import PageHome


def get_datas():
    with open(
            "/Users/liyong/Desktop/study/homework/homework_PO_webauto_test/test_company_wechat/member_list_data.yaml") as file:
        datas = yaml.safe_load(file)
        my_data = datas.get("datas").get("data")
        my_ids = datas.get("datas").get("ids")
        my_datafail = datas.get("datas").get("datafail")
        my_idsfail = datas.get("datas").get("idsfail")
        my_assertfail = datas.get("datas").get("assertfail")
        print(datas)
        print(my_data)  # 返回一个列表嵌套列表
        print(my_ids)  # 返回一个列表
        return (my_data, my_ids, my_datafail, my_idsfail, my_assertfail)


# 定义一个方法，获取成功的用例，使datas数组里的用例按照一组一组传入，params可以是列表，元组，字典，字符串等
@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_datas_byfixture(request):
    print(f"request.param：{request.param}")
    return request.param


# 定义一个方法，获取失败的用例
@pytest.fixture(params=get_datas()[2], ids=get_datas()[3])
def get_datasfail_byfixture(request):
    print(f"request.param：{request.param}")
    return request.param


@pytest.fixture()
def setup_teardown():
    print("测试开始")
    page_home = PageHome()
    yield page_home
    page_home.br.quit()
    print("测试结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:  # 遍历所有测试用例，定义编码格式
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
