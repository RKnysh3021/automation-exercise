import pytest
import uuid
from clients.products_client import ProductsClient
from clients.user_client import UserClient

@pytest.fixture
def products_client():
    return ProductsClient()

@pytest.fixture
def user_client():
    return UserClient()

@pytest.fixture
def valid_user_data():
    return {
        'name': 'RomaTest',
        'email': f'roma_{uuid.uuid4().hex[:10]}@example.com',
        'password': 'TestPass123',
        'title': 'Mr',
        'birth_date': '15',
        'birth_month': '5',
        'birth_year': '2000',
        'firstname': 'Roma',
        'lastname': 'Testov',
        'company': 'QACorp',
        'address1': 'Lenina street 10',
        'address2': 'apt 5',
        'country': 'Russia',
        'zipcode': '123456',
        'state': 'Moscow region',
        'city': 'Moscow',
        'mobile_number': '79991234567',
    }