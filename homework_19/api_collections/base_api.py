import requests

class BaseApi:
    def __init__(self, env):
        self.__requests = requests
        self.__base_url = env.base_api_url
        self.__headers = {'Accept': "*/*"}

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.post(f'{self.__base_url}{url}', data=body, headers=headers)
        return response

    def put(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.put(f'{self.__base_url}{url}', data=body, headers=headers)
        return response