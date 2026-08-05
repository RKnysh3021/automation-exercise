VALID_EMAIL = 'rknysh@mail.ru'
VALID_PASSWORD = 'Olgaroman3021'

def test_verify_login_valid(user_client):
    response = user_client.post_verify_login(VALID_EMAIL, VALID_PASSWORD)

    assert response.status_code == 200
    data = response.json()

    assert data['responseCode'] == 200
    assert data['message'] == 'User exists!'

def test_verify_login_missing_email(user_client):
    response = user_client.post_verify_login(password=VALID_PASSWORD)

    assert response.status_code == 200

    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email or password parameter is missing in POST request.'

def test_verify_login_missing_password(user_client):
    response = user_client.post_verify_login(email=VALID_EMAIL)

    assert response.status_code == 200

    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email or password parameter is missing in POST request.'

def test_verify_login_missing_data(user_client):
    response = user_client.post_verify_login()

    assert response.status_code == 200

    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email or password parameter is missing in POST request.'

def test_verify_login_invalid_credentials(user_client):
    response = user_client.post_verify_login('unexpectedEmail@mail.com', 'unexpectedPassword')

    assert response.status_code == 200

    data = response.json()
    assert data['responseCode'] == 404
    assert data['message'] == 'User not found!'

def test_delete_verify_login_not_supported(user_client):
    response = user_client.delete_verify_login()
    assert response.status_code == 200
    data = response.json()
    assert data['message'] == 'This request method is not supported.'
    assert data['responseCode'] == 405