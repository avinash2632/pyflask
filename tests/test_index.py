import requests

def test_index():
    response = requests.get("http://18.236.144.81:5000/")
    assert response.status_code == 200
