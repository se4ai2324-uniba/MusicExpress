"""Script with tests for API endpoints"""
# pylint: disable=wrong-import-position
import sys                                                       # noqa:E402
sys.path.append('src')                                           # noqa:E402
from fastapi.testclient import TestClient                        # noqa:E402
from api.main import app                                         # noqa:E402
# pylint: enable=wrong-import-position

client = TestClient(app)


def test_index():
    """Method to test index endpoint"""
    response = client.get("/")
    assert response.json() == {
        "status-code": 200,
        "message": "OK",
        "method": "GET",
        # pylint: disable=line-too-long
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs` if you want to use our system!"},  # noqa:E501
        "version": "Current: 1.0",
        "authors": ['Rinaldi Ivan', 'Sibilla Antonio', 'de Benedictis Salvatore', 'Laraspata Lucrezia'],  # noqa:E501
        "github": 'https://github.com/se4ai2324-uniba/MusicExpress',
        "dagshub": 'https://dagshub.com/se4ai2324-uniba/MusicExpress'
        # pylint: enable=line-too-long
    }


def test_get_available_playlists():
    """Method to test index endpoint"""
    response = client.get("/available_playlists")
    assert response.json() == {
        "status-code": 200,
        "message": "OK",
        "method": "GET",
        # pylint: disable=line-too-long
        "data": ["chill & late night",
                 "keep grinding.",
                 "smth.",
                 "Spotify's Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+"],  # noqa:E501
        # pylint: enable=line-too-long
    }


def test_extract_data():
    """Method to test extract endpoint"""
    payload = {"id_playlist_train": "", "id_playlist_test": ""}
    response = client.post("/extract", json=payload)
    assert response.status_code == 200
    assert response.json()["status-code"] == 200
    assert response.request.method == 'POST'


def test_recommended_songs():
    """Method to test recommendation endpoint"""
    payload = {"id_playlist_train": "", "id_playlist_test": ""}
    response = client.post("/recommendation", json=payload)
    assert response.status_code == 200
    assert response.request.method == 'POST'
