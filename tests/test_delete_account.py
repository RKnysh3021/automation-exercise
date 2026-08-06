import pytest

@pytest.mark.delete
def test_delete_account_valid(user_client, valid_user_data):
    # сначала создаём пользователя, которого будем удалять
    create_response = user_client.post_create_account(**valid_user_data)
    assert create_response.json()['responseCode'] == 201

    # теперь удаляем именно его
    response = user_client.delete_user_account(
        valid_user_data['email'],
        valid_user_data['password']
    )

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 200
    assert data['message'] == 'Account deleted!'

@pytest.mark.delete
def test_delete_account_not_found(user_client):
    response = user_client.delete_user_account(
        'definitely_does_not_exist_9999999@example.com',
        'anypassword'
    )

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 404
    assert data['message'] == 'Account not found!'


@pytest.mark.delete
def test_delete_account_missing_email(user_client):
    response = user_client.delete_user_account(email=None, password='TestPass123')

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email parameter is missing in DELETE request.'


@pytest.mark.delete
def test_delete_account_missing_password(user_client, valid_user_data):
    user_client.post_create_account(**valid_user_data)

    response = user_client.delete_user_account(email=valid_user_data['email'], password=None)

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, password parameter is missing in DELETE request.'


@pytest.mark.delete
def test_delete_account_wrong_password(user_client, valid_user_data):
    user_client.post_create_account(**valid_user_data)

    response = user_client.delete_user_account(valid_user_data['email'], 'WrongPassword999')

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 404
    assert data['message'] == 'Account not found!'