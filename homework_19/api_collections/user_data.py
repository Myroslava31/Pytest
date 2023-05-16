class UsersData:
    def __init__(self, data, support):
        self.__data = data
        self.__support = support

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs.get('data'), kwargs.get('support'))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

