# Hogwarts_Homework
# Jewish
# 2021/4/8 22:23
import allure
import pytest
import yaml


def get_adddata():
    with open("adddata.yaml", encoding="utf-8") as f:
        adddatas = yaml.safe_load(f)
    return adddatas


def get_divdata():
    with open("divdata.yml", encoding="utf-8") as f:
        divdatas = yaml.safe_load(f)
    return divdatas


@pytest.fixture(params=get_adddata()['adddata'], ids=get_adddata()['ids'])
def get_adddata_cal(request):
    return request.param


@pytest.fixture(params=get_divdata()['divdata'], ids=get_divdata()['ids'])
def get_divdata_cal(request):
    return request.param

@allure.story("计算器测试")
class TestCal:

    @pytest.mark.run(order=2)
    @allure.feature("加法测试")
    def test_add(self, initcalc_class, get_adddata_cal):
        if type(get_adddata_cal[2]) == float:
            assert round(get_adddata_cal[2], 3) == round(initcalc_class.add(get_adddata_cal[0], get_adddata_cal[1]), 3)
        else:
            assert get_adddata_cal[2] == initcalc_class.add(get_adddata_cal[0], get_adddata_cal[1])
        print(get_adddata_cal[2])

    @pytest.mark.run(order=1)
    @allure.feature("除法测试")
    def test_div(self, initcalc_class, get_divdata_cal):
        try:
            assert get_divdata_cal[2] == initcalc_class.div(get_divdata_cal[0], get_divdata_cal[1])
        except ZeroDivisionError:
            print("除数为0")
        print(get_divdata_cal[2])
