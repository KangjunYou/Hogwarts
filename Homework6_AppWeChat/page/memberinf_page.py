# Jewish
# 2021/5/8 21:12
from appium.webdriver.common.mobileby import MobileBy

from Homework6_AppWeChat.page.base_page import BasePage
from Homework6_AppWeChat.page.editinfo_page import EditInfoPage


class MemberInfPage(BasePage):
    def editinformation(self):
        self.find(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout/android.widget.TextView").click()
        return EditInfoPage(self.driver)