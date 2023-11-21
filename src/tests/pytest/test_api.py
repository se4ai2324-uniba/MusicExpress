import sys                                                       # noqa:E402
sys.path.append('src')                                           # noqa:E402
import json                                                      # noqa:E402
from api.main import app
from fastapi.testclient import TestClient                        # noqa:E402

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.json() == {
        "status-code": 200,
        "message": "OK",
        "method":"GET",
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs` if you want to use our system!"},
        "authors": ['Rinaldi Ivan', 'Sibilla Antonio', 'de Benedictis Salvatore (Spiderman)', 'Laraspata Lucrezia'],
    }

def test_extract_data():
    payload = {"id_playlist_train": '', "id_playlist_test": ''}
    response = client.post("/data/raw", json=payload)
    assert response.status_code == 200
    assert response.json()["status-code"] == 200
    assert response.request.method == 'POST'

'''
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
'''