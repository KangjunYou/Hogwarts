# Jewish
# 2021/5/8 10:42
from appium.webdriver.common.mobileby import MobileBy
from Homework6_AppWeChat.page.base_page import BasePage


class AddMemberPage(BasePage):
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    toast_element = (MobileBy.XPATH, "//*[@text='添加成功']")
    def addmember_bymenual(self):
        from Homework5_WeWork.page.editmember_page import EditMemberPage
        #self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find(*self.addmember_element).click()
        return EditMemberPage(self.driver)

    def find_toast(self):
        #self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        self.find(*self.toast_element)