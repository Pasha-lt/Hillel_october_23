import pytest
import requests


@pytest.mark.usefixtures("fixture_chuck_category")
class TestCategory:

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_jokes(self):
        pass
#
# def test_category():
#     URL = "https://api.chucknorris.io/jokes/categories"
#     response = requests.request(method="GET", url=URL)
#     print(response.json())
#
# @pytest.mark.parametrize("category",
#                          requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())
# def test_categories(category):
#     URL = f"https://api.chucknorris.io/jokes/random?category={category}"
#     response = requests.request(method="GET", url=URL)
#     assert len(response.json()["id"]) == 22
