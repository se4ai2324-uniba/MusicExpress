import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "OK",
        "status-code": 200,
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs` if you want to use our system!"}
    }
    assert response.request.method == 'GET'


def test_extract_data():
    payload = {"id_playlist_train": "playlist_train", "id_playlist_test": "playlist_test"}
    response = client.post("/data/raw", json=payload)
    assert response.status_code == 200
    assert response.json()["status-code"] == 200
    assert response.request.method == 'POST'


def test_preprocess_data():
    payload = {"id_playlist_train": "playlist_train", "id_playlist_test": "playlist_test"}
    response = client.post("/data/processed", json=payload)
    assert response.status_code == 200
    assert response.json()["status-code"] == 200
    assert response.request.method == 'POST'


def test_cluster_data():
    response = client.post("/data/output")
    assert response.status_code == 200
    assert response.json()["status-code"] == 200
    assert response.request.method == 'POST'


def test_recommended_songs():
    response = client.get("/data/output")
    assert response.status_code == 200
    assert response.json()["status-code"] == 200
    assert response.request.method == 'GET'
