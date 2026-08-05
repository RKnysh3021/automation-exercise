import pytest

@pytest.mark.skip
def test_get_products_list(products_client):
    response = products_client.get_products_list()
    data = response.json()

    assert data['responseCode'] == 200
    products = data['products']
    assert len(products) > 0

    first_product = products[0]

    # верхнеуровневые поля
    for field in ['id', 'name', 'price', 'brand', 'category']:
        assert field in first_product, f"Поле '{field}' отсутствует: {first_product}"

    # типы значений
    assert isinstance(first_product['id'], int)
    assert isinstance(first_product['name'], str)
    assert isinstance(first_product['price'], str) 
    assert isinstance(first_product['brand'], str)
    assert isinstance(first_product['category'], dict)

    #вложенная структура category
    category = first_product['category']
    assert 'category' in category
    assert 'usertype' in category
    assert 'usertype' in category['usertype']


def test_post_products_list(products_client):
    response = products_client.post_product_list()

    # ответ ошибочного поста
    response_data = response.json()
    assert response_data["responseCode"] == 405
    assert response_data["message"] == "This request method is not supported."