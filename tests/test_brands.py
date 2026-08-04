from clients.products_client import ProductsClient
import requests
def test_get_brands_list(products_client):
    response = products_client.get_brands_list()

    assert response.status_code == 200
    data = response.json()
    assert 'brands' in data
    assert len(data['brands']) > 0

def check_brand_structure(brand):
    required_fields = ['id', 'brand']

    for field in required_fields:
        assert field in brand, f"Поле '{field}' отсутствует в бренде: {brand}"

    assert isinstance(brand['id'], int)
    assert isinstance(brand['brand'], str)

def test_all_brands_have_correct_structure(products_client):
    response = products_client.get_brands_list()
    brands = response.json()['brands']
    for brand in brands():
        check_brand_structure(brand)

def test_put_brands_list_not_allowed(products_client):
    response = products_client.put_brand_list()

    answer = response.json()

    assert answer['responseCode'] == 405
    assert answer['message'] == "This request method is not supported."