from clients.products_client import ProductsClient
import requests
def test_get_brands_list(products_client):
    response = products_client.get_brands_list()

    assert response.status_code == 200
    data = response.json()
    assert 'brands' in data
    assert len(data['brands']) > 0
    