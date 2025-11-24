from pages.base import BasePage
from setup.data_entry import base_url
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import TimeoutException

class Product_page(BasePage):
     # Locators
     # For Category
     women_section_expand = (By.XPATH, "(//span[@class='badge pull-right'])[1]")
     select_dress = (By.XPATH, "//a[@href='/category_products/1' and contains(text(),'Dress')]")
     men_section_expand = (By.XPATH, "(//span[@class='badge pull-right'])[2]")
     kids_section_expand = (By.XPATH, "(//span[@class='badge pull-right'])[3]")
     
     #For Brands
     H_and_M = (By.XPATH, "//a[text()='H&M']")
     
     def __init__(self, driver, wait_time=20):
          super().__init__(driver, wait_time)
          
     def filter_women_category_for_dress(self):
          print("Expand Women section.")
          self.click_element(self.women_section_expand)
          self.click_element(self.select_dress)
          print("Women Dress Filtered.")
          
          
     def filter_H_and_M_brand(self):
          print("Select Brand")
          self.click_element(self.H_and_M)
          print("Men Dress Filtered.")