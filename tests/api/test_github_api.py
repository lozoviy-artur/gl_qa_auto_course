import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii12323')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("qa_automation")
    number_of_qa_auto_accounts = (r['total_count'])
    assert number_of_qa_auto_accounts > 1000
    print("\ntotal qa_automation accounts:" + str(number_of_qa_auto_accounts))

def test_repo_not_exist(github_api):
    r = github_api.search_repo("abracadabra_just_account")
    total_accounts = (r['total_count'])
    assert total_accounts == 0
    print("\ntotal abracadabra_just_account accounts:" + str(total_accounts))





