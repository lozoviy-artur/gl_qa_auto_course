import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get("http://api.github.com/zen")
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get("http://api.github.com/users/defunkt")
    print(f"Response body is {r.json()}")
    body = r.json()
    assert body['name'] == 'Chris Wanstrath'
    print(f"Response status code is {r.status_code}")
    assert r.status_code == 200
    print(f"Response Headers are {r.headers}")
    headers = r.headers
    assert headers['Server'] == 'GitHub.com'



