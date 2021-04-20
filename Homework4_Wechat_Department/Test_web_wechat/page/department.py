# Jewish
# 2021/4/18 14:47
from time import sleep

from selenium.webdriver.common.by import By

from Homework4_Wechat_Department.Test_web_wechat.page import BasePage


class ContactPage(BasePage):

    def get_department_list(self):
        sleep(2)
        ele_list = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        #print(ele_list)
        department_list = []
        #遍历元素列表，通过元素列表的text属性提取文字信息
        for ele in ele_list:
            department_list.append(ele.text)
        #print(department_list)
        return department_list
