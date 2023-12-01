
def test_status_code(postman_request):
    assert postman_request.status_code == 200

def test_message(postman_request):
    assert postman_request.json()["message"] == "You made a POST request with the following data!"

# evaluate = Alt + F8 on Windows/Linux or ⌥ + F8 on macOS.

