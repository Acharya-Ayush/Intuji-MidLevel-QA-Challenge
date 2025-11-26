import pytest
import time
from setup.web_setup import *
from pages.web_pages.home_page import HomePage
from setup.configtest import driver

@pytest.mark.usefixtures("driver")
class TestCredentials():
     @pytest.fixture(autouse=True)
     def setup(self, driver):
        # Make driver available as self.driver
        self.driver = driver
        
     @pytest.mark.parallel
     def test_signup(self):
          signup_page = HomePage(self.driver)
          signup_page.goto_signup_page_and_signup()

     @pytest.mark.parallel          
     def test_login(self):
          home_page = HomePage(self.driver)
          home_page.login()