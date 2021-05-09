# Jewish
# 2021/5/8 10:38
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from Homework6_AppWeChat.page.base_page import BasePage
from Homework6_AppWeChat.page.contactlist_page import ContactListPage


class MainPage(BasePage):
    contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        # click通讯录
        self.find(*self.contact_element).click()
        return ContactListPage(self.driver)
