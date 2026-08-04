import requests
from config import BASE_URL

class ProductsClient:
    def get_products_list(self):
        return requests.get(f"{BASE_URL}/productsList")

    def post_product_list(self):
        return requests.post(f"{BASE_URL}/productsList")

    def get_brands_list(self):
        return requests.get(f"{BASE_URL}/brandsList")

    def put_brand_list(self):
        return requests.put(f"{BASE_URL}/brandsList")