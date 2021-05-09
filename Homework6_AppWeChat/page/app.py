# Jewish
# 2021/5/8 10:34
#app.py 用于放置app相关的操作，启动、关闭、重启
from appium import webdriver
from faker import Faker

from Homework6_AppWeChat.page.base_page import BasePage
from Homework6_AppWeChat.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            self.faker = Faker('zh-CN')
            desire_cap = {}
            desire_cap['platformName'] = 'android'
            desire_cap['platformVersion'] = '6.0'
            desire_cap['deviceName'] = '127.0.0.1:7555'
            desire_cap["appPackage"] = "com.tencent.wework"
            desire_cap["appActivity"] = ".launch.WwMainActivity"
            desire_cap['noReset'] = 'true'
            desire_cap['skipDeviceInitialization'] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(5)
        else:
            # 否则复用driver
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        #入口
        return MainPage(self.driver)