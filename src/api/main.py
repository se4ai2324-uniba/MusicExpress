"""Main script: it includes our API initialization and endpoints."""
# pylint: disable=wrong-import-position
import os                                                        # noqa:E402
import sys                                                       # noqa:E402
from sys import platform                                         # noqa:E402
sys.path.append('\\'.join(os.getcwd().split('\\')[:-2])+'\src')  # noqa:E402
from datetime import datetime                                    # noqa:E402
from functools import wraps                                      # noqa:E402
from http import HTTPStatus                                      # noqa:E402
from pathlib import Path                                         # noqa:E402
from typing import List                                          # noqa:E402
from joblib import load                                          # noqa:E402
from fastapi import FastAPI, Request                             # noqa:E402
import pandas as pd                                              # noqa:E402
import conf                                                      # noqa:E402
from schemas import PredictPayload,UserPlaylistPayload           # noqa:E402
from data.extract_data import extract_data                       # noqa:E402
from features.preprocessing import preprocess                    # noqa:E402
from models.clustering import clustering                         # noqa:E402
from models.recommend import recommend                           # noqa:E402
# pylint: enable=wrong-import-position

# Folder Directory
BASE_PATH = '\\'.join(os.getcwd().split('\\')[:-2]) + '\\' if platform == 'win32' else '/'.join(os.getcwd().split('/')[:-2]) + '/'

# Default Data Directories
DATASET_ZIP_DIR = os.path.join(BASE_PATH, conf.DATA_DIR + 'dataset.zip')
DEFAULT_TRAIN_DATA = os.path.join(BASE_PATH, conf.TRAIN_SET_CSV_PATH)
DEFAULT_TEST_DATA = os.path.join(BASE_PATH, conf.TEST_SET_CSV_PATH)

# Data Directories
PREPRO_DIR = os.path.join(BASE_PATH, "data\interim\\")
PRO_DIR = os.path.join(BASE_PATH, "data\processed\\")
OUT_DIR = os.path.join(BASE_PATH, "data\output\\")

# Directory containing models.pkl files
STORE_MODEL_DIR = os.path.join(BASE_PATH, "models\model.pkl")
MODELS_DIR = Path("models/")

# Models list
model_wrappers_list: List[dict] = []

# Define application
app = FastAPI(
    title="MusicExpress",
    description="Music Recommender System using the K-Medoids clustering method",
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
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }

        # Additional data in the response
        if "target_song" in results:
            response["target_song"] = results["target_song"]

        if "data" in results:
            response["data"] = results["data"]
        
        return response

    return wrap


@app.get("/", tags=["General"])
@construct_response
def _index(request: Request):
    """Root endpoint."""

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs` if you want to use our system!"},  # noqa:E501
    }
    return response


@app.post('/data/raw', tags=["Data"])
@construct_response
def _extract_data(request: Request, user_payload:UserPlaylistPayload):

    if(user_payload == None or ((user_payload.id_playlist_train == '') and (user_payload.id_playlist_test == ''))):
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

import spotipy_utilities as spUt
@app.post('/data/processed', tags=["Preprocessing"])
@construct_response
def _preprocess_data(request: Request, user_payload:UserPlaylistPayload):

    if(user_payload == None or ((user_payload.id_playlist_train == '') and (user_payload.id_playlist_test == ''))):
        result = preprocess(raw_train_data=DEFAULT_TRAIN_DATA,
                            raw_test_data=DEFAULT_TEST_DATA,
                            dir_to_store_data = PRO_DIR)
    else:
        user_playlists = [user_payload.id_playlist_train,
                           user_payload.id_playlist_test]
        
        tmp_dir_train = PREPRO_DIR + spUt.get_playlist_name(user_playlists[0]) + ".csv"
        tmp_dir_test = PREPRO_DIR + spUt.get_playlist_name(user_playlists[1]) + ".csv"

        result = preprocess(tmp_dir_train,tmp_dir_test, 
                            dir_to_store_data = PRO_DIR)
        
    response = {
            "message": HTTPStatus.OK.phrase if result else HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
            "status-code": HTTPStatus.OK if result else HTTPStatus.INTERNAL_SERVER_ERROR,
            "data": 'Preprocessing completed!'if result else "Error: can't preprocess the data!"
        }
    return response

@app.post('/data/output', tags=["Clustering"])
@construct_response
def _cluster_data(request: Request):

    # As of now, the processed playlist are called trainSet and testSet
    # We may change the naming, but this is not of our interest atm
    tmp_dir_train = PRO_DIR + "trainSet.csv"
    tmp_dir_test = PRO_DIR + "testSet.csv"

    result = clustering(tmp_dir_train,tmp_dir_test, 
                        dir_to_store_data = OUT_DIR,
                        dir_to_store_model = STORE_MODEL_DIR)
        
    response = {
            "message": HTTPStatus.OK.phrase if result else HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
            "status-code": HTTPStatus.OK if result else HTTPStatus.INTERNAL_SERVER_ERROR,
            "data": 'Clustering completed!'if result else "Error: can't clusterize the data!"
        }
    return response

@app.post("/models/default", tags=["Recommendation"])
@construct_response
def _get_recommended_songs(request: Request):
    """Return the list of recommended songs"""

    # As of now, the processed playlist are called trainSet and testSet
    # We may change the naming, but this is not of our interest atm
    tmp_dir_train = OUT_DIR + "clustertrainSet.csv"
    tmp_dir_test = OUT_DIR + "clustertestSet.csv"

    target_song, recommended_songs = recommend(clustered_train_data=tmp_dir_train,
                                  clustered_test_data=tmp_dir_test, 
                                  dir_to_store_recommendation = PRO_DIR)

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "target_song": target_song if len(target_song) > 0 else "Check below output message!",
        "data": recommended_songs if len(recommended_songs) > 0 else "We are sorry, our system was not able to provide any recommendations.",
    }

    return response


# @app.on_event("startup")
# def _load_models():
#     """Loads all models in `MODELS_DIR`"""

#     # TODO: 
#     #   1. Load default model(s)
#     #   2. Append models to path

#     model_paths = [
#         filename for filename in conf.MODEL_FILE_PATH.iterdir() if filename.suffix == ".pkl" # conf.MODEL_FILE_PATH Ã¨ una stringa e non una lista su cui fare iterdir()
#     ]
#     for path in model_paths:
#         with open(path, "rb") as file:
#             model_wrapper = load(file)
#             model_wrappers_list.append(model_wrapper)


# @app.get("/models", tags=["Prediction"])
# @construct_response
# def _get_models_list(request: Request):
#     """Return the lsit of available models"""

#     available_models = [
#         {
#             "type": model["type"],
#             "parameters": model["params"],
#             "accuracy": model["metrics"],
#         }
#         for model in model_wrappers_list
#     ]

#     response = {
#         "message": HTTPStatus.OK.phrase,
#         "status-code": HTTPStatus.OK,
#         "data": available_models,
#     }

#     return response

# @app.post("/models", tags=["Clustering"])
# @construct_response
# def _cluster_data(request: Request, type: str, payload: PredictPayload):
#     """Cluster out the data"""

#     # TODO: 
#     #   1. Load data
#     #   2. Clustering
#     tmp_train_data = "abc"
#     tmp_test_data = "abc"
#     clustering(tmp_train_data, tmp_test_data)

#     response = {
#         "message": HTTPStatus.OK.phrase,
#         "status-code": HTTPStatus.OK,
#         "data": {"message": "The data has been clustered! You can now get recommendations!"},
#     }

#     return response

# @app.get("/data/output", tags=["Recommendation"])
# @construct_response
# def _get_clustered_playlists(request: Request):
#     """Return the list of clustered playlists"""

#     available_playlists = [
#         playlist for playlist in conf.OUTPUT_DIR.iterdir() if playlist.suffix == ".csv"
#         ]

#     response = {
#         "message": HTTPStatus.OK.phrase,
#         "status-code": HTTPStatus.OK,
#         "data": available_playlists,
#     }

#     return response

# @app.get("/models/{type}", tags=["Recommendation"])
# @construct_response
# def _get_recommended_songs(request: Request, type: str, payload: PredictPayload):
#     """Return the list of recommended songs"""

#     # TODO: 
#     #   1. Extract data
#     #   2. Preprocessing
#     #   3. Clustering
#     #   BONUS. Load data
#     recommended_songs = recommend()

#     response = {
#         "message": HTTPStatus.OK.phrase,
#         "status-code": HTTPStatus.OK,
#         "data": recommended_songs,
#     }

#     return response


# @app.get('/data/raw', tags=["General"])
# @construct_response
# def _get_default_data(request: Request):
#     extract_data(zip_dir=DATASET_ZIP_DIR)  # default: user_data=False, playlists=conf.PLAYLISTS
#     train_data = pd.read_csv(DEFAULT_TRAIN_DATA)
#     test_data = pd.read_csv(DEFAULT_TEST_DATA)
#     result = [train_data,test_data]
#     response = {
#         "message": HTTPStatus.OK.phrase,
#         "status-code": HTTPStatus.OK,
#         "data": result
#     }
#     return response

