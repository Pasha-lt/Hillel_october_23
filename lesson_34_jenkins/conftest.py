import pytest
import requests

from setting import url
# https://api.chucknorris.io/

@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url=f"{url}jokes/random")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code