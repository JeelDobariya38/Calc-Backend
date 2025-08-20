from calcweb import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-type"]


def test_style_route():
    response = client.get("/style.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["Content-type"]


def test_script_route():
    response = client.get("/script.js")
    assert response.status_code == 200
    assert "text/javascript" in response.headers["Content-type"]
