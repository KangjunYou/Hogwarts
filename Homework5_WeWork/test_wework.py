# Jewish
# 2021/5/5 21:54
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        desire_cap = {}
        desire_cap['platformName'] = 'android'
        desire_cap['platformVersion'] = '6.0'
        desire_cap['deviceName'] = '127.0.0.1:7555'
        desire_cap["appPackage"] = "com.tencent.wework"
        desire_cap["appActivity"] = ".launch.WwMainActivity"
        desire_cap['noReset'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ays").send_keys('徐航宇')
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys('18368290918')
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac9").click()
        #print(self.driver.page_source)
        ele_toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert ele_toast == '添加成功'

