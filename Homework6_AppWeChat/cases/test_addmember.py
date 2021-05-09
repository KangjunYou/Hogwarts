# Jewish
# 2021/5/8 20:50
from faker import Faker

from Homework6_AppWeChat.page.app import App


class TestAddMember:
    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        pass

    def setup_class(self):
        self.faker = Faker('zh-CN')
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def test_addmember(self):
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.main.goto_contactlist().goto_addmember().addmember_bymenual().edit_member(name,phonenum).find_toast()

    def test_deletemember(self):
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.main.goto_contactlist().goto_addmember().addmember_bymenual().edit_member(name,phonenum).find_toast()
        self.app.restart()
        self.main.goto_contactlist().goto_editmember(name).editinformation().editinfo().deletemember().confirminfo().is_member_in_list(name)

