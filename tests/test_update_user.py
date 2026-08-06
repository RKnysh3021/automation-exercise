import pytest

@pytest.mark.update
def test_update_account_valid(user_client, valid_user_data):
    # сначала создаём пользователя
    create_response = user_client.post_create_account(**valid_user_data)
    assert create_response.json()['responseCode'] == 201


    updated_data = valid_user_data.copy()
    updated_data['name'] = 'RomaUpdated'
    updated_data['firstname'] = 'RomaNew'
    updated_data['city'] = 'Saint Petersburg'

    response = user_client.put_update_account(**updated_data)

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 200
    assert data['message'] == 'User updated!'


@pytest.mark.update
def test_update_account_and_verify_changes(user_client, valid_user_data):

    user_client.post_create_account(**valid_user_data)


    updated_data = valid_user_data.copy()
    updated_data['name'] = 'RomaUpdated'
    updated_data['city'] = 'Saint Petersburg'
    user_client.put_update_account(**updated_data)

    check_response = user_client.get_user_by_email(valid_user_data['email'])
    user_info = check_response.json()['user']

    assert user_info['name'] == 'RomaUpdated'
    assert user_info['city'] == 'Saint Petersburg'

@pytest.mark.update
def test_update_account_nonexistent_user(user_client, valid_user_data):
    response = user_client.put_update_account(**valid_user_data)

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 404
    assert data['message'] == 'Account not found!'


@pytest.mark.update
def test_update_account_missing_email(user_client, valid_user_data):
    invalid_data = valid_user_data.copy()
    del invalid_data['email']

    response = user_client.put_update_account(**invalid_data)

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email parameter is missing in PUT request.'


@pytest.mark.update
def test_update_account_wrong_password(user_client, valid_user_data):
    user_client.post_create_account(**valid_user_data)

    invalid_data = valid_user_data.copy()
    invalid_data['password'] = 'WrongPassword999'

    response = user_client.put_update_account(**invalid_data)

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 404
    assert data['message'] == 'Account not found!'