# Jewish
# 2021/5/8 21:39

from appium.webdriver.common.mobileby import MobileBy

from Homework6_AppWeChat.page.base_page import BasePage
from Homework6_AppWeChat.page.mumberinfo_page import MumberInfoPage


class EditInfoPage(BasePage):
    def editinfo(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return MumberInfoPage(self.driver)
