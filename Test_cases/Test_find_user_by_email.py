# Test_find_user_by_email
import pytest
from selenium import webdriver
from Page_objects.Login_page import login
import Configurations.constants as const
from Page_objects.Add_customer_page import Add_customer
from Page_objects.Search_customerpage import Search_customer
path=const.path
import time

from Utilities1.Custom_logger import LogGen
driver = webdriver.Chrome(executable_path=path)
class Test_003():
    base_url = const.base_url
    username = const.username
    password = const.password

    def test_new_customer(self):
        driver.get(self.base_url)
        loginpage = login(driver)
        loginpage.set_username(self.username)
        loginpage.set_password(self.password)
        loginpage.click_login()
        add = Add_customer(driver)
        add.click_customer_tab1()
        add.click_customer_tab()
        search=Search_customer(driver)
        search.input_email("victoria_victoria@nopCommerce.com")
        search.click_search()
        time.sleep(4)
        if (search.compare_search("victoria_victoria@nopCommerce.com")):
            print("----------------Email Exist!--------------")
        else:
            print("--------------Not Found!------------")
