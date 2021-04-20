# Jewish
# 2021/4/18 16:12
import yaml
from selenium import webdriver


class BasePage:
    # 将页面重复步骤抽离出来封装，例如driver实例化
    def __init__(self, base_driver=None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            with open("data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver
