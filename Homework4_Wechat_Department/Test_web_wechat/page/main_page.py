# Jewish
# 2021/4/18 14:47
from time import sleep
from selenium.webdriver.common.by import By
from Homework4_Wechat_Department.Test_web_wechat.page import AddDepartPage
from Homework4_Wechat_Department.Test_web_wechat.page import BasePage


class MainPage(BasePage):
    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        pass

    def goto_add_department(self):
        """
        跳转到添加成员页面
        :return:
        """
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@class="member_colLeft_top_addBtn"]').click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()
        return AddDepartPage(self.driver)
