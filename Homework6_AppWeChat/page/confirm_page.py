# Jewish
# 2021/5/8 21:53
from appium.webdriver.common.mobileby import MobileBy

from Homework6_AppWeChat.page.base_page import BasePage
from Homework6_AppWeChat.page.contactlist_page import ContactListPage


class ConfirmPage(BasePage):
    confirm_button = (MobileBy.XPATH, "//*[@text='确定']")
    def confirminfo(self):
        self.find(*self.confirm_button).click()
        return ContactListPage(self.driver)
