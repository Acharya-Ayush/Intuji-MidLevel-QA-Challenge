from pages.base import BasePage
from setup.data_entry import base_url
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import TimeoutException
import requests

class Product_page(BasePage):
     # Locators
     # For Category
     product_button_in_nav = (By.XPATH, "//a[@href = '/products']")
     visible_element_in_product_page = (By.XPATH, "//h2[text() = 'All Products']")
     women_section_expand = (By.XPATH, "(//span[@class='badge pull-right'])[1]")
     select_dress = (By.XPATH, "//a[@href='/category_products/1' and contains(text(),'Dress')]")
     men_section_expand = (By.XPATH, "(//span[@class='badge pull-right'])[2]")
     kids_section_expand = (By.XPATH, "(//span[@class='badge pull-right'])[3]")
     search_input_box = (By.XPATH, "//input[@id='search_product']")
     search_button = (By.XPATH, "//button[@id='submit_search']")
     searched_products = (By.XPATH, "//div[@class='productinfo text-center']/p")
     
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
     
     def apply_women_and_HM_filter(self):
          print("Filtering Women category with H&M brand")
          self.navigate_to(url = "https://automationexercise.com/")
          self.click_element(self.product_button_in_nav)
          self.wait_for_visibility(self.visible_element_in_product_page)
          print("Went into product page.")
          self.filter_women_category_for_dress()
          self.filter_H_and_M_brand()
     
     def search_products(self):
          print("Searching products from UI")
          self.navigate_to(url = "https://automationexercise.com/")
          self.click_element(self.product_button_in_nav)
          self.wait_for_visibility(self.visible_element_in_product_page)
          print("Went into product page.")
          # Further implementation for searching products can be added here
          self.insert_keys(self.search_input_box, "tshirt")
          self.click_element(self.search_button)
          print("Product search completed from UI.")
     def get_visible_products(self):
          print("Getting visible products from UI")
          product_elements = self.find_elements(self.searched_products)
          products = [elem.text for elem in product_elements]
          return products
          
          
          