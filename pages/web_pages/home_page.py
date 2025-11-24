from pages.base import BasePage
from setup.data_entry import base_url
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
   #locators
   #For signup
   login_nav = (By.XPATH, "//*[contains(normalize-space(), 'Signup / Login')]")
   name_input_box = (By.XPATH, "//input[@data-qa=\"signup-name\"]")
   email_input_box = (By.XPATH, "//input[@data-qa=\"signup-email\"]")
   signup_button = (By.XPATH, "//button[@data-qa=\"signup-button\"]")
   password_field = (By.XPATH, "//input[@data-qa=\"password\"]")
   day_of_birth = (By.XPATH, "//select[@data-qa=\"days\"]")
   month_of_birth = (By.XPATH, "//select[@data-qa=\"months\"]")
   year_of_birth = (By.XPATH, "//select[@data-qa=\"years\"]")
   first_name = (By.XPATH, "//input[@data-qa=\"first_name\"]")
   last_name = (By.XPATH, "//input[@data-qa=\"last_name\"]")
   company = (By.XPATH, "//input[@data-qa=\"company\"]")
   address = (By.XPATH, "//input[@data-qa=\"address\"]")
   country = (By.XPATH, "//select[@data-qa=\"country\"]")
   state = (By.XPATH, "//input[@data-qa=\"state\"]")
   city = (By.XPATH, "//input[@data-qa=\"city\"]")
   zipcode = (By.XPATH, "//input[@data-qa=\"zipcode\"]")
   mobile_number = (By.XPATH, "//input[@data-qa=\"mobile_number\"]")  
   create_account_btn = (By.XPATH, "//button[@data-qa=\"create-account\"]")
   verification_account_created = (By.XPATH, "//b[contains(text(),\"Account Created\")]")
   verification_for_taken_email = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")
   
   # For Login
   email_address = (By.XPATH, "//input[@data-qa=\"login-email\"]")
   password = (By.XPATH, "//input[@data-qa=\"login-password\"]")
   Login_btn =(By.XPATH, "//button[@data-qa=\"login-button\"]")
   
   
   #Visible element check after loading the URL.
   visible_element_in_signup_page = (By.XPATH, "//h2[contains(text(),\"New User Signup!\")]")
   visible_element_in_signup_page_after_clicking_signup_button = (By.XPATH, "//b[contains(text(),\"Enter Account Information\")]")     
   #load credentials from .env file
   load_dotenv()
   
   USERNAME = os.getenv("USERNAME")
   EMAIL = os.getenv("EMAIL")
   PASSWORD = os.getenv("PASSWORD")
   
   
   def __init__(self, driver, wait_time=20):
      super().__init__(driver, wait_time)
      
   def login(self):
      print("Logging In!!!")
      self.navigate_to("https://automationexercise.com/login")
      self.wait_for_visibility(self.visible_element_in_signup_page)
      self.insert_keys(self.email_address, text=self.EMAIL)
      self.insert_keys(self.password, text=self.PASSWORD)
      self.click_element(self.Login_btn)
      # Logging in will take time execution of the code is really fast so making it sleep for 2 second.
      time.sleep(3)
      print("Logged In")
        
   def goto_signup_page_and_signup(self):
      print("Going into login page")
      self.navigate_to(base_url)
      self.navigate_to(url = "https://automationexercise.com/login")
      self.wait_for_visibility(self.visible_element_in_signup_page)
      self.insert_keys(self.name_input_box, text=self.USERNAME)
      self.insert_keys(self.email_input_box, text=self.EMAIL)
      self.click_element(self.signup_button) 
      try:
         self.wait_for_visibility(self.verification_for_taken_email, wait_time=3)
         print("The account already exists.")
      except TimeoutException:   
         self.wait_for_visibility(self.visible_element_in_signup_page_after_clicking_signup_button)
         print("Went to Signup Page.")
         print("Filling PAssword.")
         self.insert_keys(self.password_field, text=self.PASSWORD)
         print("Filling birth date")
         self.select_from_dropdown(self.day_of_birth, text='5')
         print("Filling birth month")
         self.select_from_dropdown(self.month_of_birth, text='January')
         print("Filling birth year")
         self.select_from_dropdown(self.year_of_birth, text='1999')
         print("Filling name, last name, company, Address, Country, state, City, ZIP, and Mobile Number.")
         self.insert_keys(self.first_name, text = "TestUser2323")
         self.insert_keys(self.last_name, text="TestUser3232")
         self.insert_keys(self.company, text="INTUJI")
         self.insert_keys(self.address, text="123 Main Street, Los Angeles, CA 90011")
         self.select_from_dropdown(self.country, text="United States")
         self.insert_keys(self.state, text="California")
         self.insert_keys(self.city, text="Los Angeles")
         self.insert_keys(self.zipcode, text="90011")
         self.insert_keys(self.mobile_number, text="+19898767654")
         self.click_element(self.create_account_btn)
         # The code execution time is really fast so, need to implement break (This is not explicit wait.)
         time.sleep(2)
         self.wait_for_visibility(self.verification_account_created)
      print("SignUp process completed.")
         
         
         
         
         
         
          
          