# pytest -v -s Test_cases/Test_login.py  cls
# >pytest -v -s --html=Reports\report.html Test_cases/Test_login.py

import pytest
from selenium import webdriver
from Page_objects.Login_page import login
path="C:/Users/Hugo-Tech-1775/Downloads/Compressed/chromedriver_win32_2/chromedriver.exe"
import Configurations.constants as const
from Utilities1.Custom_logger import LogGen

class Test_001_login:
    base_url=const.base_url
    username=const.username
    password=const.password
    logger=LogGen.loggen()

    def test_homepage(self):
        self.logger.info("************  test_homepage   *****")
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get(self.base_url)
        self.homepage_title=self.driver.title
        if self.homepage_title=="Your store. Login":
            assert True
            # self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homepage.png")
            assert False
            self.driver.close()



    def test_login(self):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.implicitly_wait(20)
        # self.driver.get(self.base_url)
        loginpage=login(self.driver)
        loginpage.set_username(self.username)
        loginpage.set_password (self.password)
        loginpage.click_login()
        if self.driver.title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homepage.png")
            assert False
            self.driver.close()



