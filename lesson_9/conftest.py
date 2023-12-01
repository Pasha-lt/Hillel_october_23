import pytest
import requests


@pytest.fixture(scope="session")
def postman_request():
    # setup start  ---------------------
    print("Setup")
    url = "https://postman-rest-api-learner.glitch.me//info"
    payload = {"name": "Add your name in the body"}
    response = requests.request("POST", url, json=payload)
    # setup end ---------------------
    # func start -------------
    yield response
    # func end -------------
    # teardown start ------
    print("Teardown")
    # teardown end ------