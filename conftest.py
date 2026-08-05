import pytest
from clients.products_client import ProductsClient
from clients.user_client import UserClient

@pytest.fixture
def products_client():
    return ProductsClient()

@pytest.fixture
def user_client():
    return UserClient()