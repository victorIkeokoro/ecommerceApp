# pytest -v -s Test_cases/Test_login.py  cls
# >pytest -v -s --html=Reports\report.html Test_cases/Test_login.py
import pytest
from selenium import webdriver
from Page_objects.Login_page import login
import Configurations.constants as const
path=const.path

from Utilities1.Custom_logger import LogGen
driver = webdriver.Chrome(executable_path=path)
class Test_001_login:
    base_url=const.base_url
    username=const.username
    password=const.password
    logger=LogGen.loggen()

    def test_homepage(self):
        self.logger.info("************  test_homepage   *****")
        # driver = webdriver.Chrome(executable_path=path)
        driver.get(self.base_url)
        self.homepage_title=driver.title
        if self.homepage_title=="Your store. Login":
            assert True
            # driver.close()
        else:
            driver.save_screenshot(".\\Screenshots\\test_homepage.png")
            assert False
            driver.close()



    def test_login(self):
        # driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(20)
        # driver.get(self.base_url)
        loginpage=login(driver)
        loginpage.set_username(self.username)
        loginpage.set_password (self.password)
        loginpage.click_login()
        if driver.title=="Dashboard / nopCommerce administration":
            assert True
            driver.close()

        else:
            driver.save_screenshot(".\\Screenshots\\test_homepage.png")
            assert False
            driver.close()


