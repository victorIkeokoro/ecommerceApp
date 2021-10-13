import selenium
from selenium import webdriver
import Configurations.constants as const
path=const.path
driver = webdriver.Chrome(executable_path=path)
class Search_customer():
    input_emailsearch_id="SearchEmail"
    button_search_id="search-customers"
    searchresult_xpath='//*[@id="customers-grid"]/tbody/tr/td[2]'


    def __init__(self,driver):
        self.driver=driver
    def input_email(self,email):
        self.driver.find_element_by_id(self.input_emailsearch_id).send_keys(email)
    def click_search(self):
        self.driver.find_element_by_id(self.button_search_id).click()
    def compare_search(self,email):
        result =self.driver.find_element_by_xpath(self.searchresult_xpath)
        return result.text==email
