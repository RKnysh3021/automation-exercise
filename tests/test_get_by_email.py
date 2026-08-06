import pytest

@pytest.mark.get_user
def test_get_user_detail_by_email_valid(user_client, valid_user_data):
    # сначала создаём пользователя, которого будем искать
    create_response = user_client.post_create_account(**valid_user_data)
    assert create_response.json()['responseCode'] == 201

    response = user_client.get_user_by_email(valid_user_data['email'])

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 200

    user_info = data['user']
    assert user_info['email'] == valid_user_data['email']
    assert user_info['name'] == valid_user_data['name']
    assert user_info['first_name'] == valid_user_data['firstname']
    assert user_info['last_name'] == valid_user_data['lastname']


@pytest.mark.get_user
def test_get_user_detail_missing_email(user_client):
    response = user_client.get_user_by_email(email=None)

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 400
    assert data['message'] == 'Bad request, email parameter is missing in GET request.'


@pytest.mark.get_user
def test_get_user_detail_empty_email(user_client):
    """
    Известная особенность API: пустой email не отклоняется как невалидный,
    а ищется как обычное значение — сервер возвращает первого пользователя
    с email == '' (если такой существует в базе). Это баг/недочёт валидации
    на стороне API, а не ожидаемое поведение.
    """
    response = user_client.get_user_by_email('')

    assert response.status_code == 200
    data = response.json()
    assert data['responseCode'] == 200
    assert 'user' in data
    assert data['user']['email'] == ''