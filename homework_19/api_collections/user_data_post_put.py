class UsersDataPostPut:
    def __init__(self, name, job):
        self.__name = name
        self.__job = job

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs.get('name'), kwargs.get('job'))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__



