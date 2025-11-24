from pages.base import BasePage
from setup.data_entry import base_url
from selenium.webdriver.common.by import By

class HomePage(BasePage):
     #locators
     login_nav = (By.XPATH, "//text()[contains(.,'Signup / Login')]")
     
     def __init__(self, driver, wait_time=20):
        super().__init__(driver, wait_time)
        
     def goto_signup_page(self, ):
          print("Going into login page")
          self.click_element(self.login_nav)