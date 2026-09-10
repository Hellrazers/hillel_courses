import os

import requests
from dotenv import load_dotenv

load_dotenv()


class ApiSession:
    def __init__(self):
        self.session = requests.Session()
        self.__token = None
        self.headers = {}

    def get_token(self):
        payload = {
            'email': os.getenv('USER_LOGIN'),
            'password': os.getenv('USER_PASSWORD')
        }
        resp_login = requests.post(
            url=f'{os.getenv('basic_url')}/api/auth/signin',
            data=payload
        )
        assert resp_login.status_code == 200
        if resp_login.json().get('token') is None:
            raise ConnectionError('Сервер не прислав нам токен')

        self.headers = resp_login.headers
        self.__token = resp_login.cookies.get('sid')

    def auth(self):
        if self.__token is None:
            self.get_token()
        self.session.cookies.update({'sid': self.__token}
                                    )
        self.headers.update(self.headers)

    def get(self, *args, **kwargs):
        self.auth()

        return self.session.get(*args, **kwargs)

# api = ApiSession()
# resp = api.get(
#     url=f'{os.getenv('basic_url')}/api/cars',
# )
# assert resp.status_code == 200
