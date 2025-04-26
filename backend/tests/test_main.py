from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_titles():
    response = client.get("/titles")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    first_title = body[0]
    assert isinstance(first_title, dict)
    assert 'title' in first_title.keys()
    assert 'type' in first_title.keys()
    assert 'release_year' in first_title.keys()
