# Jewish
# 2021/4/16 20:46
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()


class TestWechat:
    def test_cookie(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        # 当前页面点击通讯录按钮
        self.driver.find_element(By.ID, "menu_contacts").click()
        # 获取cookie信息
        cookie = self.driver.get_cookies()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    def test_cookie_input(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        #self.driver.implicitly_wait(10)
        sleep(5)
        self.driver.find_element_by_link_text('添加成员').click()
        sleep(2)
        username = "徐行"
        anothername = "Lodge"
        id = "hanghang"
        phonenumber = "12345678901"
        try:
            assert len(phonenumber) == 11
        except ValueError:
            print("非法手机号，请重新输入！")
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("memberAdd_english_name").send_keys(anothername)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(id)
        self.driver.find_element_by_name("gender").click()
        self.driver.find_element_by_id("memberAdd_phone").send_keys(phonenumber)
        self.driver.find_element_by_link_text('保存').click()

