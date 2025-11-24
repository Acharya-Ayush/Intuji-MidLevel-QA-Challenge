import pytest
import time
from setup.web_setup import *
from pages.web_pages.product_page import Product_page

def test_signup():
     driver = web_driver()
     product_page = Product_page(driver)
     product_page.filter_women_category_for_dress()
     product_page.filter_H_and_M_brand()
     driver.quit()