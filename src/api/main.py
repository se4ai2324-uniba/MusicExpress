"""Main script: it includes our API initialization and endpoints."""
# pylint: disable=wrong-import-position,line-too-long,anomalous-backslash-in-string  # noqa:E501
import os                                                        # noqa:E402
import sys                                                       # noqa:E402
sys.path.append('\\'.join(os.getcwd().split('\\')[:-2])+'\src')  # noqa:E402,E501,W605
from functools import wraps                                      # noqa:E402
from http import HTTPStatus                                      # noqa:E402
from fastapi import FastAPI, Request, HTTPException              # noqa:E402
# pylint: disable=import-error
from api.schemas import UserPlaylistPayload                      # noqa:E402
# pylint: enable=import-error
import conf                                                      # noqa:E402
import spotipy_utilities as spUt                                 # noqa:E402
from data.extract_data import extract_data                       # noqa:E402
from features.preprocessing import preprocess                    # noqa:E402
from models.clustering import clustering                         # noqa:E402
from models.recommend import recommend                           # noqa:E402
# pylint: enable=wrong-import-position

# Folder Directory
BASE_PATH = conf.DIR_PATH

# Default Data Directories
DATASET_ZIP_DIR = os.path.join(BASE_PATH, conf.DATA_DIR + 'dataset.zip')
DEFAULT_TRAIN_DATA = os.path.join(BASE_PATH, conf.TRAIN_SET_CSV_PATH)
DEFAULT_TEST_DATA = os.path.join(BASE_PATH, conf.TEST_SET_CSV_PATH)

# Data Directories
PREPRO_DIR = os.path.join(BASE_PATH, "data\interim\\")  # noqa:W605
PRO_DIR = os.path.join(BASE_PATH, "data\processed\\")  # noqa:W605
OUT_DIR = os.path.join(BASE_PATH, "data\output\\")  # noqa:W605

# Directory containing models.pkl files
STORE_MODEL_DIR = os.path.join(BASE_PATH, "models\model.pkl")  # noqa:W605

# Define application
app = FastAPI(
    title="MusicExpress",
    description="Music Recommender System using the K-Medoids clustering method",   # noqa:E501
    version="v01",
)


def construct_response(f):
    """Construct a JSON response for an endpoint's results."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs):
        results = f(request, *args, **kwargs)

        # Construct response
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
        }

        # Additional data in the response
        if "target_song" in results:
            response["target_song"] = results["target_song"]

        if "data" in results:
            response["data"] = results["data"]

        if "authors" in results:
            response["authors"] = results["authors"]

        return response

    return wrap


# pylint: disable=unused-argument
@app.get("/", tags=["General"])
@construct_response
def _index(request: Request):
    """Root endpoint."""

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs` if you want to use our system!"},  # noqa:E501
        "authors": ['Rinaldi Ivan', 'Sibilla Antonio', 'de Benedictis Salvatore (Spiderman)', 'Laraspata Lucrezia'],  # noqa:E501
    }

    return response


@app.post('/extract', tags=["Data"])
@construct_response
def _extract_data(request: Request, user_payload: UserPlaylistPayload):

    if (user_payload is None or ((user_payload.id_playlist_train == '') and (user_payload.id_playlist_test == ''))):  # noqa:E501
        result = extract_data(zip_dir=DATASET_ZIP_DIR,
                              dir_to_store_data=PREPRO_DIR)
    else:
        user_playlists = [user_payload.id_playlist_train,
                          user_payload.id_playlist_test]
        result = extract_data(user_data=True, playlists=user_playlists,
                              zip_dir=DATASET_ZIP_DIR,
                              dir_to_store_data=PREPRO_DIR)

    response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "data": result
        }

    return response


@app.post('/preprocess', tags=["Preprocessing"])
@construct_response
def _preprocess_data(request: Request, user_payload: UserPlaylistPayload):

    if (user_payload is None or ((user_payload.id_playlist_train == '') and (user_payload.id_playlist_test == ''))):  # noqa:E501
        result = preprocess(raw_train_data=DEFAULT_TRAIN_DATA,
                            raw_test_data=DEFAULT_TEST_DATA,
                            dir_to_store_data=PRO_DIR)
    else:
        user_playlists = [user_payload.id_playlist_train,
                          user_payload.id_playlist_test]

        tmp_dir_train = PREPRO_DIR + spUt.get_playlist_name(user_playlists[0]) + ".csv"  # noqa:E501
        tmp_dir_test = PREPRO_DIR + spUt.get_playlist_name(user_playlists[1]) + ".csv"   # noqa:E501

        result = preprocess(tmp_dir_train, tmp_dir_test,
                            dir_to_store_data=PRO_DIR)

    if result:

        response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "data": 'Preprocessing completed!'
        }

        return response

    raise HTTPException(status_code=404, detail='Error: can\'t preprocess the data!')   # noqa:E501


@app.post('/cluster', tags=["Clustering"])
@construct_response
def _cluster_data(request: Request):

    tmp_dir_train = PRO_DIR + "trainSet.csv"
    tmp_dir_test = PRO_DIR + "testSet.csv"

    result = clustering(tmp_dir_train, tmp_dir_test,
                        dir_to_store_data=OUT_DIR,
                        dir_to_store_model=STORE_MODEL_DIR)

    if result:

        response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "data": 'Clustering completed!'
        }

        return response

    raise HTTPException(status_code=404, detail='Error: can\'t clusterize the data!')   # noqa:E501


@app.get("/recommendation", tags=["Recommendation"])
@construct_response
def _recommended_songs(request: Request):
    """Return the list of recommended songs"""

    tmp_dir_train = OUT_DIR + "clustertrainSet.csv"
    tmp_dir_test = OUT_DIR + "clustertestSet.csv"

    target_song, recommended_songs = recommend(clustered_train_data=tmp_dir_train,   # noqa:E501
                                               clustered_test_data=tmp_dir_test,   # noqa:E501
                                               dir_to_store_recommendation=PRO_DIR)   # noqa:E501
    if len(target_song) > 0:

        response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "target_song": target_song,
            "data": recommended_songs
        }

        return response

    raise HTTPException(status_code=404, detail='We are sorry, our system was not able to provide any recommendations.')   # noqa:E501

# pylint: enable=line-too-long,anomalous-backslash-in-string,unused-argument
