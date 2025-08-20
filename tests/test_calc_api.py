from calcweb import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_heathcheck_route():
    response = client.get("/heath")
    assert response.status_code == 200
    assert "Healthy!!" in str(response.content)


@pytest.mark.parametrize("command, result", [("3 + 5", 8), ("2 + 4", 6), ("6 * 9", 54), ("23", 23), ("", 0)])
def test_execute_route(command, result):
    response = client.post("/execute", json={"command": command})
    data = response.json()
    assert response.status_code == 200
    assert data["command"] == command
    assert data["result"] == result


@pytest.mark.parametrize("command", ["3 / ", "2 + "])
def test_execute_route_with_bad_request(command):
    response = client.post("/execute", json={"command": command})
    assert response.status_code == 400
