# Jewish
# 2021/4/18 14:53
import pytest

from Homework4_Wechat_Department.Test_web_wechat.page import MainPage


class TestAddDepart:
    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("name", ['研发部'])
    def test_add_apartment(self, name):
        name_list = self.main_page.goto_add_department().add_department(name).get_department_list()
        assert name in name_list

    @pytest.mark.parametrize("name", ['研发部'])
    def test_add_apartment_fail(self, name):
        error_data = self.main_page.goto_add_department().add_department_fail(name)
        err = [i for i in error_data if i != ""]
        print(err)
