from pages.base_api import APIClient


class ProductsService(APIClient):
    def __init__(self):
        super().__init__("https://automationexercise.com/api")

    def get_all_products(self):
        return self.get("productsList")

    def search_products(self, query):
        return self.post("searchProduct", data={"search_product": query})

