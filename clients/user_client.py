import requests
from config import BASE_URL

class UserClient:
    def post_verify_login(self, email=None, password=None):
        data = {}
        if email is not None:
            data['email'] = email
        if password is not None:
            data['password'] = password
        return requests.post(f"{BASE_URL}/verifyLogin", data=data)

    def delete_verify_login(self):
        return requests.delete(f"{BASE_URL}/verifyLogin")