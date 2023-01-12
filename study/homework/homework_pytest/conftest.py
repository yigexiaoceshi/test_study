#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List
import allure
import pytest
from homework.homework_pytest.calculate.calculate import Calculate


# 计算器每条用例都需要初始化被测类对象，使用fixture做优化，调用时，在调用函数中传入当前方法名称即可
@pytest.fixture()
def get_calc():
    print("测试开始执行，即将返回待测实例对象")
    calc = Calculate()
    yield calc
    print("本轮测试完成，即将开始下一轮测试")


# 定义一个插入文本方法
@pytest.fixture()
def test_text():
    allure.attach("这是我插入的测试报告文本", attachment_type=allure.attachment_type.TEXT)


# 定义一个插入图片的方法
@pytest.fixture()
def test_picture():
    allure.attach.file("/Users/liyong/Downloads/picture.jpg", attachment_type=allure.attachment_type.JPG)


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:  # 遍历所有测试用例，item就是测试用例
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
