from homework_19.base_api import BaseApi


class UsersApi(BaseApi):
    def __init__(self, env):
        super().__init__(env)
        self.__people_url = '/users'

    def get_users(self, headers=None):
        response = self.get(url=f'{self.__people_url}', headers=None)
        return response
