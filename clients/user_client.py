import requests
from config import BASE_URL

class UserClient:

    """ Логирование """
    def post_verify_login(self, email=None, password=None):
        data = {}
        if email is not None:
            data['email'] = email
        if password is not None:
            data['password'] = password
        return requests.post(f"{BASE_URL}/verifyLogin", data=data)

    def delete_verify_login(self):
        return requests.delete(f"{BASE_URL}/verifyLogin")

    """ Регистрация """
    def post_create_account(self, **kwargs):
        return requests.post(f"{BASE_URL}/createAccount", data=kwargs)

    """ Удаление аккаунта"""
    def delete_user_account(self, email=None, password=None):
        data = {}
        if email is not None:
            data['email'] = email
        if password is not None:
            data['password'] = password
        return requests.delete(f"{BASE_URL}/deleteAccount",data=data )

    """ Обновление аккаунта"""
    def put_update_account(self, **kwargs):
        return requests.put(f"{BASE_URL}/updateAccount", data=kwargs)

    """ Получение аккаунта по емаил"""
    def get_user_by_email(self, email=None):
        params = {}
        if email is not None:
            params['email'] = email
        return requests.get(f"{BASE_URL}/getUserDetailByEmail", params=params)