import requests


def test_index():
    response = requests.get("http://52.34.46.190:5000/")
    assert response.status_code == 200
