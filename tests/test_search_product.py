
def test_search_product_found(products_client):
    response = products_client.post_search_product('top')

    assert response.status_code == 200

    data = response.json()
    assert 'products' in data
    assert len(data['products']) > 0

    for product in data['products']:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product
        assert 'brand' in product
        assert 'category' in product

def test_search_product_without_parameter(products_client):
    response = products_client.post_search_product()

    data = response.json()
    assert response.status_code == 200
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, search_product parameter is missing in POST request.'

def test_search_products_not_found(products_client):
    response = products_client.post_search_product('asd')

    data = response.json()
    assert response.status_code == 200
    assert data['responseCode'] == 200
    assert len(data['products']) == 0