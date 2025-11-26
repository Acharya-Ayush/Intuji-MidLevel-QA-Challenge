import pytest
import time
from setup.web_setup import *
from pages.web_pages.product_page import Product_page
from setup.configtest import driver 
from pages.request_handler.product_services import ProductsService

pytest.mark.usefixtures("driver")
class TestProductPage():
     @pytest.fixture(autouse=True)
     def setup(self, driver):
        # Make driver available as self.driver
        self.driver = driver
        self.product_page = Product_page(self.driver)
        self.api = ProductsService()
     
     @pytest.mark.parallel
     def test_filter_product(self):
          self.product_page.apply_women_and_HM_filter()
     
     @pytest.mark.parallel
     def test_compare_searched_products(self):
          # Search from UI
          self.product_page.search_products()
          time.sleep(2)  # Wait for results to load
          
          ui_products = self.product_page.get_visible_products()
          print(f"Products found in UI: {len(ui_products)}")
          
          # Search from API
          api_data = self.api.search_products("tshirt")
          assert api_data is not None
          assert "products" in api_data
          
          api_products = api_data["products"]
          print(f"Products found in API: {len(api_products)}")
          
          # Compare counts
          assert len(ui_products) == len(api_products), "Mismatch in product counts between UI and API"
          print("Product counts match between UI and API")