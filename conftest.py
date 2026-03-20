import requests
import pytest

from urls import Endpoints
from generators import generate_fake_data

@pytest.fixture
def create_user_fixt():
    data = generate_fake_data()
    requests.post(Endpoints.REGISTER, json=data)
    log_response = requests.post(Endpoints.LOGIN, json=data)
    assert log_response.status_code == 200
    assert log_response.json()["success"] is True
    assert "accessToken" in log_response.json()
    access_token = log_response.json()["accessToken"]
    yield data, access_token
    headers = {"Authorization": access_token}
    requests.delete(Endpoints.DELETE_USER, headers=headers)