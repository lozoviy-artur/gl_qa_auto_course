def test_check_math():
    assert 5 * 5 == 25


def test_remove_name(user):
    user.name = ""


def test_name(user):
    assert user.name == "Artur"


def test_second_name(user):
    assert user.second_name == "Lozovyi"
