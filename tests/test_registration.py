import pytest


def test_valid_registration(user_client, valid_user_data):
    response = user_client.post_create_account(**valid_user_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 201
    assert data['message'] == 'User created!'

def test_registration_without_email(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['email']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email parameter is missing in POST request.'


def test_registration_without_name(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['name']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, name parameter is missing in POST request.'

def test_registration_without_password(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['password']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, password parameter is missing in POST request.'

def test_registration_without_firstname(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['firstname']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, firstname parameter is missing in POST request.'


def test_registration_without_lastname(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['lastname']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, lastname parameter is missing in POST request.'

def test_registration_without_address1(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['address1']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, address1 parameter is missing in POST request.'

def test_registration_without_country(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['country']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, country parameter is missing in POST request.'

def test_registration_without_zipcode(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['zipcode']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, zipcode parameter is missing in POST request.'

def test_registration_without_state(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['state']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, state parameter is missing in POST request.'

def test_registration_without_mobile_number(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['mobile_number']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, mobile_number parameter is missing in POST request.'

def test_registration_without_city(user_client,valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['city']
    response = user_client.post_create_account(**invalid_data)

    assert response.status_code == 200

    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, city parameter is missing in POST request.'

def test_registration_user_exists(user_client, valid_user_data):
    # первая регистрация — должна пройти успешно
    first_response = user_client.post_create_account(**valid_user_data)
    assert first_response.status_code == 200
    assert first_response.json()['responseCode'] == 201

    # вторая регистрация с ТЕМИ ЖЕ данными  должна вернуть ошибку дубликата
    second_response = user_client.post_create_account(**valid_user_data)

    assert second_response.status_code == 200
    data = second_response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Email already exists!'

