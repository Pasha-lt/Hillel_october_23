import pytest


import pytest
import requests


@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code

@pytest.fixture(scope="class")
def fixture_search_query_chuck(request):
    response = requests.request(method="GET", url=f"https://api.chucknorris.io/jokes/search?query=chuck")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code



@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    def test_check_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200

    def test_icon_url_not_empty(self):
        assert self.response.json()["icon_url"] == "https://assets.chucknorris.host/img/avatar/chuck-norris.png"

    def test_icon_url_image(self):
        assert ".png" in self.response.json()["icon_url"]

    def test_value_key_is_there(self):
        assert self.response.json()["value"]

    def test_value_key_with_text(self):
        assert "Chuck Norris" in self.response.json()["value"]


@pytest.mark.usefixtures("fixture_search_query_chuck")
class TestSearchJokeWord:
    def test_search_status_code(self):
        assert self.status_code == 200

    def test_search_word_chuk(self):
        assert self.response.json()["total"] == 9667

    def test_search_joke_value(self):
        assert self.response.json()["result"][550][
                   "value"] == "In Chuck Norris' world a Grand Slam is simply slamming your face into a large shiny piano."

    def test_search_joke_all_keys(self):
        assert list(self.response.json()["result"][100].keys()) == ['categories', 'created_at', 'icon_url', 'id',
                                                                    'updated_at', 'url', 'value']

    def test_search_joke_category(self):
        assert self.response.json()["result"][1]["categories"] == ['explicit']

    def test_search_joke_len_id(self):
        assert len(self.response.json()["result"][1]["id"]) == 22