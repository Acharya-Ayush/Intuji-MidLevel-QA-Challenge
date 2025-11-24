import pytest
import time
from setup.web_setup import *
from pages.web_pages.home_page import HomePage

def test_signup(web_driver):
     driver = web_driver("Signup Functionality")
     signup_page = HomePage(driver)
     signup_page.goto_signup_page()
     