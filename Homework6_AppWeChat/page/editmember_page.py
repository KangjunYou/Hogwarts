# Jewish
# 2021/5/8 10:45
from appium.webdriver.common.mobileby import MobileBy
from Homework6_AppWeChat.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self,name,phonenum):
        from Homework5_WeWork.page.addmember_page import AddMemberPage
        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return AddMemberPage(self.driver)