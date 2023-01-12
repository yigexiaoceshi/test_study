#!/usr/bin/python3
# -*- coding:utf-8 -*-
import allure
import pytest
import yaml


def get_data():
    with open("../testdata/calc_test_data.yaml") as file:
        datas = yaml.safe_load(file)
        data_intdata = datas.get("add").get("int").get("intdata")
        data_intids = datas.get("add").get("int").get("intids")
        data_floatdata = datas.get("add").get("float").get("floatdata")
        data_floatids = datas.get("add").get("float").get("floatids")
        data_divrightdata = datas.get("div").get("right").get("rightdata")
        data_divrightids = datas.get("div").get("right").get("rightids")
        data_diverrordata = datas.get("div").get("error").get("errordata")
        data_diverrorids = datas.get("div").get("error").get("errorids")
        return (data_intdata, data_intids, data_floatdata, data_floatids, data_divrightdata, data_divrightids,
                data_diverrordata, data_diverrorids)


# 通过fixture获取加法整型参数及用例别名
@pytest.fixture(params=get_data()[0], ids=get_data()[1])
def get_add_data_int_byfixture(request):
    print(f"使用fixture中的request获取到的加法整型数据为：{request.param}")
    return request.param


# 通过fixture获取加法浮点型参数及用例别名
@pytest.fixture(params=get_data()[2], ids=get_data()[3])
def get_add_data_float_byfixture(request):
    print(f"使用fixture中的request获取到的加法浮点型数据为：{request.param}")
    return request.param


# 通过fixture获取除法正确参数及用例别名
@pytest.fixture(params=get_data()[4], ids=get_data()[5])
def get_div_data_right_byfixture(request):
    print(f"使用fixture中的request获取到的除法正确数据为：{request.param}")
    return request.param


# 通过fixture获取除法错误参数及用例别名
@pytest.fixture(params=get_data()[6], ids=get_data()[7])
def get_div_data_error_byfixture(request):
    print(f"使用fixture中的request获取到的除法错误数据为：{request.param}")
    return request.param


# 定义一个测试类
@allure.feature("计算器")
class TestCalculate:
    # 测试加法：整数相加
    @allure.story("加法，整数相加")
    @pytest.mark.run(order=4)
    def test_add_int(self, get_calc, get_add_data_int_byfixture, test_text):
        result = get_calc.add(get_add_data_int_byfixture[0], get_add_data_int_byfixture[1])
        assert result == get_add_data_int_byfixture[2]

    # 测试加法：小数相加
    @allure.story("加法，小数相加")
    @pytest.mark.run(order=3)
    def test_add_float(self, get_calc, get_add_data_float_byfixture, test_text):
        result = get_calc.add(get_add_data_float_byfixture[0], get_add_data_float_byfixture[1])
        assert result == get_add_data_float_byfixture[2]

    # 测试除法：数据正确
    @allure.story("除法，数据正确")
    @pytest.mark.run(order=2)
    def test_div_right(self, get_calc, get_div_data_right_byfixture, test_picture):
        result = get_calc.div(get_div_data_right_byfixture[0], get_div_data_right_byfixture[1])
        assert result == get_div_data_right_byfixture[2]

    # 测试除法：输入数据不正确
    @allure.story("除法，数据不正确")
    @pytest.mark.run(order=1)
    def test_div_error(self, get_calc, get_div_data_error_byfixture, test_picture):
        result = get_calc.div(get_div_data_error_byfixture[0], get_div_data_error_byfixture[1])
        assert result == get_div_data_error_byfixture[2]


"""
命令行执行：
pytest test_calculate.py --alluredir=../result  -vs --clean-alluredir
allure serve ../result/
allure generate ../result  --clean -o 指定目录
"""
