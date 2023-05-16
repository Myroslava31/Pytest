from homework_19.api_collections.base_api import BaseApi


class UsersApi(BaseApi):
    def __init__(self, env):
        super().__init__(env)
        self.__people_url = '/users'

    def get_user(self, user_id, headers=None):
        response = self.get(url=f'{self.__people_url}/{user_id}', headers=None)
        return response

    def post_user(self, body, headers=None):
        response = self.post(url=f'{self.__people_url}', body=body, headers=None)
        return response

    def put_user(self, user_id, body, headers=None):
        response = self.put(url=f'{self.__people_url}/{user_id}', body=body, headers=None)
        return response
