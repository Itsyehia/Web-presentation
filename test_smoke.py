import requests

def test_smoke():
    url = "http://localhost:5000/"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response.text == "Hello, World!", "Response text doesn't match"
