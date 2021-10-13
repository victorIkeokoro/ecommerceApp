import pytest
from selenium import webdriver
from Page_objects.Login_page import login
import Configurations.constants as const
from Page_objects.Add_customer_page import Add_customer
path=const.path
import time

from Utilities1.Custom_logger import LogGen
driver = webdriver.Chrome(executable_path=path)

class Test_002():
    base_url = const.base_url
    username = const.username
    password = const.password
    def test_new_customer(self):
        driver.get(self.base_url)
        loginpage = login(driver)
        loginpage.set_username(self.username)
        loginpage.set_password(self.password)
        loginpage.click_login()
        add=Add_customer(driver)
        add.click_customer_tab1()
        add.click_customer_tab()
        add.click_addnew_customer()
        add.set_email()
        add.set_pwd("123")
        add.set_first_name("Victor")
        add.set_last_name("Uche")
        add.set_gender("male")
        add.DOB("12/23/21")
        add.set_company_name("besters")
        add.tick_checkbox_taxid()
        add.set_newsletter_storename()
        add.set_newsletter_teststore()
        add.set_admin_comment("New user")
        time.sleep(10)
        add.submit()
        print(add.popup())






