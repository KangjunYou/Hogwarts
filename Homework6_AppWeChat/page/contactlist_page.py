# Jewish
# 2021/5/8 10:40
from appium.webdriver.common.mobileby import MobileBy
from Homework6_AppWeChat.page.addmember_page import AddMemberPage
from Homework6_AppWeChat.page.base_page import BasePage



class ContactListPage(BasePage):

    def goto_addmember(self):
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_editmember(self, name):
        self.swipe_find(f'{name}').click()
        from Homework6_AppWeChat.page.memberinf_page import MemberInfPage
        return MemberInfPage(self.driver)

    def is_member_in_list(self, name):
        try:
            self.find(MobileBy.XPATH, f"//*[@text='{name}']")
            return True
        except:
            return False
