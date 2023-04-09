import pytest

from homework_15.human import Human


@pytest.fixture()
def create_human():
    yield Human('Vasyl', 99, 'male')
    print('tear down')

@pytest.fixture()
def create_human_with_negative_age():
    yield Human('Vasyl', -10, 'male')
    print('tear down')
