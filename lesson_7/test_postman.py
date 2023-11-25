import requests

def test_status_code():
    url = "https://postman-rest-api-learner.glitch.me//info"
    payload = {"name": "Add your name in the body"}
    response = requests.request("POST", url, json=payload)
    assert response.status_code == 200
