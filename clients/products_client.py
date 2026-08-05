import requests
from config import BASE_URL

class ProductsClient:

    """ Продукты """
    def get_products_list(self):
        return requests.get(f"{BASE_URL}/productsList")

    def post_product_list(self):
        return requests.post(f"{BASE_URL}/productsList")

    """ Бренды """
    def get_brands_list(self):
        return requests.get(f"{BASE_URL}/brandsList")

    def put_brand_list(self):
        return requests.put(f"{BASE_URL}/brandsList")

    """ Поиск продукта """
    def post_search_product(self, search_product = None):
        if search_product is None:
            return requests.post(f"{BASE_URL}/searchProduct")
        return requests.post(f"{BASE_URL}/searchProduct", data = {"search_product":search_product})