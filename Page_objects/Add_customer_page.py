import selenium
from selenium import webdriver
import Configurations.constants as const
path=const.path
import random
from RandomWordGenerator import RandomWord
driver = webdriver.Chrome(executable_path=path)
class Add_customer():
    customer_tab_xpath1='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a'
    customer_tab_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a'
    add_new_customer_xpath='/html/body/div[3]/div[1]/form[1]/div/div/a'
    input_email_id="Email"
    input_pwd_id="Password"
    input_firstname_id="FirstName"
    input_lastname_id="LastName"
    radio_male_id="Gender_Male"
    radio_female_id="Gender_Female"
    input_DOB_month_id="DateOfBirth"
    input_companyname_id="Company"
    checkbox_tax_id="IsTaxExempt"
    input_newsletter_storename_xpath='//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[1]'
    input_newsletter_teststore_xpath='//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[2]'
    input_customer_role_xpath='//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    input_manager_role_id ="VendorId"
    checkbox_active_id = "Active"
    input_admincomment_id="AdminComment"
    button_submit_name="save"
    popup_success_xpath='/html/body/div[3]/div[1]/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def click_customer_tab1(self):
        self.driver.find_element_by_xpath(self.customer_tab_xpath1).click()
    def click_customer_tab(self):
        self.driver.find_element_by_xpath(self.customer_tab_xpath).click()
    def click_addnew_customer(self):
        self.driver.find_element_by_xpath(self.add_new_customer_xpath).click()


    def set_email(self):
        rw = RandomWord(max_word_size=7)
        random_email=rw.generate()+"@gamil.com"
        email=random_email
        self.driver.find_element_by_id(self.input_email_id).send_keys(email)

    def set_pwd(self, password):
        self.driver.find_element_by_id(self.input_pwd_id).send_keys(password)

    def set_first_name(self,name):
        self.driver.find_element_by_id(self.input_firstname_id).send_keys(name)

    def set_last_name(self,lname):
        self.driver.find_element_by_id(self.input_lastname_id).send_keys(lname)

    def set_gender(self,gender):
        if gender=="male":
            self.driver.find_element_by_id(self.radio_male_id).click()
        elif  gender=="female":
            self.driver.find_element_by_id(self.radio_female_id).click()

    def DOB(self,date):
        self.driver.find_element_by_id(self.input_DOB_month_id).send_keys(date)

    def set_company_name(self,name):
        self.driver.find_element_by_id(self.input_companyname_id).send_keys(name)

    def tick_checkbox_taxid(self):
        self.driver.find_element_by_id( self.checkbox_tax_id).click()

    def set_newsletter_storename(self):
        storename=self.driver.find_element_by_xpath(self.input_newsletter_storename_xpath)
        self.driver.execute_script("arguments[0].click();", storename)

    def set_newsletter_teststore(self):
        teststore = self.driver.find_element_by_xpath(self.input_newsletter_teststore_xpath)
        self.driver.execute_script("arguments[0].click();", teststore)

    def set_admin_comment (self,comment):
        self.driver.find_element_by_id(self.input_admincomment_id).send_keys(comment)

    def submit(self):
        self.driver.find_element_by_name(self.button_submit_name).click()

    def popup(self):
        popup=self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]').text
        return "The new customer has been added successfully." in popup




    









