import pytest


def test_check_math():
    assert 5 * 5 == 25

@pytest.mark.change
def test_remove_name(user):
    user.name = ""

@pytest.mark.check
def test_name(user):
    assert user.name == "Artur"

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Lozovyi"

    