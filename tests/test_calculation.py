import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_say_hello(client):
    response = client.get("/math/hello/user")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello user"}


def test_cal(client):
    option_type = 'sq'
    option_value = 2
    response = client.get(f"/math/?option={option_type}&value={option_value}")
    assert response.status_code == 200
    assert response.json() == 4
