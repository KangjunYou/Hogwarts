# Jewish
# 2021/5/8 21:47
from appium.webdriver.common.mobileby import MobileBy

from Homework6_AppWeChat.page.base_page import BasePage
from Homework6_AppWeChat.page.confirm_page import ConfirmPage


class MumberInfoPage(BasePage):
    def deletemember(self):
        self.swipe_find('删除成员').click()
        return ConfirmPage(self.driver)
