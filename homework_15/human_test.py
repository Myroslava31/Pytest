import pytest


def test_change_age(create_human):
    human = create_human
    new_age = 100
    human.grow()
    assert human.age == new_age, "Age wasn't changed"


def test_age_limit_and_gender_change_for_dead(create_human):
    human = create_human
    new_age = 101
    human.grow()
    human.grow()
    assert human.age != new_age, "Age limit doesn't work"
    with pytest.raises(Exception):
        human.change_gender('female')


def test_check_age_setter(create_human):
    human = create_human
    with pytest.raises(AttributeError):
        human.age = 'aaa'


def test_change_gender(create_human):
    human = create_human
    new_gender = 'female'
    human.change_gender('female')
    assert human.gender == new_gender, 'Gender was not changed'


def test_set_non_correct_gender(create_human):
    human = create_human
    genders = ('cat', 123, 'male')
    for gender in genders:
        with pytest.raises(Exception):
            human.change_gender(gender)

@pytest.mark.xfail
def test_grow_for_human_with_negative_age(create_human_with_negative_age):
    human = create_human_with_negative_age
    new_age = -9
    human.grow()
    assert human.age != new_age, "Age can't be negative"

