# Jewish
# 2021/4/18 14:47
from time import sleep

from selenium.webdriver.common.by import By
from Homework4_Wechat_Department.Test_web_wechat.page import BasePage
from Homework4_Wechat_Department.Test_web_wechat.page import ContactPage


class AddDepartPage(BasePage):

    ele_name = (By.NAME, "name")

    def add_department(self, name):
        self.driver.find_element(*self.ele_name).send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        #self.driver.find_element(By.CSS_SELECTOR, "js_parent_party_name").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.ww_dialog_body .jstree-anchor').click()
        self.driver.find_element(By.LINK_TEXT, '确定').click()
        # 页面的return
        # 1.其他页面的事例
        # 2.用例所需的断言
        return ContactPage(self.driver)

    def add_department_fail(self, name):
        self.driver.find_element(*self.ele_name).send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        #self.driver.find_element(By.CSS_SELECTOR, "js_parent_party_name").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.ww_dialog_body .jstree-anchor').click()
        self.driver.find_element(By.LINK_TEXT, '确定').click()

        element = self.driver.find_elements(By.ID, 'js_tips')
        error_list = []
        #遍历元素列表，通过元素列表的text属性提取文字信息
        for ele in element:
            error_list.append(ele.text)
        return error_list
        # 页面的return
        # 1.其他页面的事例
        # 2.用例所需的断言

