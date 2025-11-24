import pytest
import time
from setup.web_setup import *
from pages.web_pages.home_page import HomePage

def test_signup():
     driver = web_driver()
     signup_page = HomePage(driver)
     signup_page.goto_signup_page()
     