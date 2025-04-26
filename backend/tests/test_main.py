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
    assert "title" in first_title.keys()
    assert "type" in first_title.keys()
    assert "release_year" in first_title.keys()


def test_titles_multiple_returned():
    """Test the data has more than many titles
    ie using real data"""
    response = client.get("/titles")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)

    assert len(body) >= 100


def test_titles_title_filter():
    response = client.get("/titles?title=California Heist")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)

    assert len(body) == 1
    assert body[0]['title'] == "Water & Power: A California Heist"


def test_titles_director_filter():
    response = client.get("/titles?director=Leclercq")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)

    assert len(body) == 3
    assert body[0]['director'] == "Julien Leclercq"

def test_titles_combined_title_director_filters():
    response = client.get("/titles?director=Leclercq&title=angl")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)

    assert len(body) == 1
    assert body[0]['director'] == "Julien Leclercq"
    assert body[0]['title'] == "Ganglands"