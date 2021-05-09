# Jewish
# 2021/5/8 16:32
# base_page.py 基类，init操作
# 封装一些最基本的方法，便于后期维护
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)

class BasePage:
    def __init__(self, driver: WebDriver=None):
        # 初始化driver
        self.driver = driver

    def find(self, by, value):
        # 查找元素
        logging.info(by)
        logging.info(value)
        return self.driver.find_element(by, value)

    def swipe_find(self, text, num=3):
        # 默认查找次数
        # 进入滑动查找后，改变隐式等待时长，提高效率
        self.driver.implicitly_wait(2)
        # 滑动查找
        for i in range(0, num):
            # 如果达到num-1次没有找到，则抛出异常
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except NoSuchElementException:
                print("未找到，滑动一页")
                size = self.driver.get_window_size()
                start_x = size['width'] / 2
                start_y = size['height'] * 0.8
                end_x = size['width'] / 2
                end_y = size['height'] * 0.2
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

