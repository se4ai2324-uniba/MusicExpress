"""Main script: it includes our API initialization and endpoints."""
# pylint: disable=wrong-import-position,line-too-long,anomalous-backslash-in-string  # noqa:E501
import os                                                        # noqa:E402
import sys                                                       # noqa:E402
from sys import platform                                         # noqa:E402
sys.path.append('\\'.join(os.getcwd().split('\\')[:-2])+'\src')  # noqa:E402,E501,W605
from functools import wraps                                      # noqa:E402
from http import HTTPStatus                                      # noqa:E402
from fastapi import FastAPI, Request, HTTPException              # noqa:E402
from fastapi.middleware.cors import CORSMiddleware               # noqa:E402
# pylint: disable=import-error
from api.schemas import UserPlaylistPayload                      # noqa:E402
from api.monitoring import instrumentator                        # noqa:E402
# pylint: enable=import-error
import conf                                                      # noqa:E402
import spotipy_utilities as spUt                                 # noqa:E402
import files_utilities as flUt                                   # noqa:E402
from data.extract_data import extract_data                       # noqa:E402
from features.preprocessing import preprocess                    # noqa:E402
from models.clustering import clustering                         # noqa:E402
from models.recommend import recommend                           # noqa:E402
# pylint: enable=wrong-import-position

# Folder Directory
BASE_PATH = conf.DIR_PATH

# Default Data Directories
DATASET_ZIP_DIR = os.path.join(BASE_PATH, conf.DATA_DIR, 'dataset.zip')
DEFAULT_TRAIN_DATA = os.path.join(BASE_PATH, conf.TRAIN_SET_CSV_PATH)
DEFAULT_TEST_DATA = os.path.join(BASE_PATH, conf.TEST_SET_CSV_PATH)

# Data Directories
PREPRO_DIR = os.path.join(BASE_PATH, "data", "interim")  # noqa:W605
PRO_DIR = os.path.join(BASE_PATH, "data", "processed")  # noqa:W605
OUT_DIR = os.path.join(BASE_PATH, "data", "output")  # noqa:W605

# Directory containing models.pkl files
STORE_MODEL_DIR = os.path.join(BASE_PATH, "models", "model.pkl")  # noqa:W605

PROCESSED_TRAIN_DIR = os.path.join(PRO_DIR, "trainSet.csv")
PROCESSED_TEST_DIR = os.path.join(PRO_DIR, "testSet.csv")
CLUSTER_TRAIN_DIR = os.path.join(OUT_DIR, "clustertrainSet.csv")
CLUSTER_TEST_DIR = os.path.join(OUT_DIR, "clustertestSet.csv")

TRAIN_SET_CSV_PATH = os.path.join(PREPRO_DIR, "keep grinding..csv")
TEST_SET_CSV_PATH = os.path.join(PREPRO_DIR, "Spotify's Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+.csv")  # noqa:E501

# Modify file paths based on the operating system
if platform == "win32":
    PREPRO_DIR = PREPRO_DIR.replace("/", "\\")
    PRO_DIR = PRO_DIR.replace("/", "\\")
    OUT_DIR = OUT_DIR.replace("/", "\\")
    STORE_MODEL_DIR = STORE_MODEL_DIR.replace("/", "\\")
    PROCESSED_TRAIN_DIR = PROCESSED_TRAIN_DIR.replace("/", "\\")
    PROCESSED_TEST_DIR = PROCESSED_TEST_DIR.replace("/", "\\")
    CLUSTER_TRAIN_DIR = CLUSTER_TRAIN_DIR.replace("/", "\\")
    CLUSTER_TEST_DIR = CLUSTER_TEST_DIR.replace("/", "\\")
    TRAIN_SET_CSV_PATH = TRAIN_SET_CSV_PATH.replace("/", "\\")
    TEST_SET_CSV_PATH = TEST_SET_CSV_PATH.replace("/", "\\")


# Additional details for each endpoint
tags_metadata = [
    {
        "name": "Root",
        "description": "Explore the root endpoint for essential details, including version, authors, and external links.",   # noqa:E501
    },
    {
        "name": "Data",
        "description": "Extract songs from users' playlists available on Spotify.",   # noqa:E501
    },
    {
        "name": "Recommendation",
        "description": "Get song recommendations given the IDs of two previously extracted playlists.",   # noqa:E501
    }
]

APP_DESCRIPTION_MESSAGE = (
    "Welcome! Explore our Music Recommender System API utilizing K-Medoids clustering for song recommendations. "   # noqa:E501
    "Feel free to test the API's endpoints with your playlists or the default ones!"   # noqa:E501
    )


# Define application
app = FastAPI(
    title="MusicExpress",
    description=APP_DESCRIPTION_MESSAGE,
    version="v01",
    openapi_tags=tags_metadata
)

# Expose app to compute Prometheus metrics
instrumentator.instrument(app).expose(app, include_in_schema=False, should_gzip=True)  # noqa:E501

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

        if "version" in results:
            response["version"] = results["version"]

        if "authors" in results:
            response["authors"] = results["authors"]

        if "github" in results:
            response["github"] = results["github"]

        if "dagshub" in results:
            response["dagshub"] = results["dagshub"]

        return response

    return wrap


# pylint: disable=unused-argument
@app.get("/", tags=["Root"])
@construct_response
def _index(request: Request):
    """Root endpoint.

    **Parameters**
    - No parameters needed

    **Output**
    - A **JSON object** containing the **HTTP message**,
    the **HTTP status code**, a **welcome message*
      and the **names of the system's authors**
    """

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs` if you want to use our system!"},  # noqa:E501
        "version": "Current: 1.0",
        "authors": ['Rinaldi Ivan', 'Sibilla Antonio', 'de Benedictis Salvatore', 'Laraspata Lucrezia'],  # noqa:E501
        'github': 'https://github.com/se4ai2324-uniba/MusicExpress',
        'dagshub': 'https://dagshub.com/se4ai2324-uniba/MusicExpress',
    }

    return response


@app.get("/available_playlists", tags=["Available_Playlists"])
@construct_response
def _get_available_playlists(request: Request):
    """
    Endpoint to **get all available playlists** for the current user.

    **Parameters**
    - None

    **Output**
    - If everything works out, a **JSON object** containing the
    **HTTP message**, the **HTTP status code**,
      and **a list of the names of all the available playlists**
    - Otherwise, an **exception** will be raised
    """

    available_playlists = flUt.retrieve_all_playlists(PREPRO_DIR)
    print(available_playlists)

    if len(available_playlists) > 0:

        response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "data": available_playlists
        }

        return response

    raise HTTPException(status_code=404, detail='We are sorry, our system was not able to retrieve any playlist.')   # noqa:E501


@app.post('/extract', tags=["Data"])
@construct_response
def _extract_data(request: Request, user_payload: UserPlaylistPayload):
    """
    Endpoint to **extract data** from two playlists available on Spotify.

    **Parameters**
    - **ID** of a **playlist** with **songs that you like**
    - **ID** of a **playlist** from which **recommendations
    have to be computed**
    - If **no IDs** are provided, two **default playlists** will be used

    The playlist's id can be found in the link provided by Spotify when
    sharing a user created playlist. Here's an example:
    open.spotify.com/playlist/**3fSsw9Mp5Mi2DDiweZggtP**?si=406250be812b4b0a.

    The IDs will be sent together within the endpoint's **Payload**.

    **Output**
    - If everything works out, a **JSON object**
    containing the **HTTP message**,
    the **HTTP status code** and the **playlists' names**
    - Otherwise, an **exception** will be raised
    """

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


@app.post("/recommendation", tags=["Recommendation"])
@construct_response
def _recommended_songs(request: Request, user_payload: UserPlaylistPayload):
    """
    Endpoint to **get song recommendations** given the IDs of
    two playlists previously extracted.

    **Parameters**
    - **ID** of an **extracted playlist** with **songs that you like**
    - **ID** of an **extracted playlist** from which **recommendations
    have to be computed**
    - If **no IDs** are provided, two **default playlists** will be used

    The playlist's id can be found in the link provided by Spotify
    when sharing a user created playlist. Here's an example:
    open.spotify.com/playlist/**3fSsw9Mp5Mi2DDiweZggtP**?si=406250be812b4b0a.

    The IDs will be sent together within the endpoint's **Payload**.

    **Output**
    - If everything works out, a **JSON object** containing the
    **HTTP message**, the **HTTP status code**,
      the **target song (song used to compute recommendations)**
      and the **song recommendations**
    - Otherwise, an **exception** will be raised
    """

    default_case = (user_payload is None or ((user_payload.id_playlist_train == '') and (user_payload.id_playlist_test == '')))  # noqa:E501

    # Check if the data has been extracted and then preprocess it
    if default_case:
        if not os.path.exists(TRAIN_SET_CSV_PATH) or not os.path.exists(TEST_SET_CSV_PATH):  # noqa:E501
            extract_data(zip_dir=DATASET_ZIP_DIR, dir_to_store_data=PREPRO_DIR)

        preprocess(raw_train_data=DEFAULT_TRAIN_DATA,
                   raw_test_data=DEFAULT_TEST_DATA, dir_to_store_data=PRO_DIR)

    else:
        user_playlists = [user_payload.id_playlist_train,
                          user_payload.id_playlist_test]

        train_playlist_name = spUt.get_playlist_name(user_playlists[0])
        test_playlist_name = spUt.get_playlist_name(user_playlists[1])

        tmp_dir_train = os.path.join(PREPRO_DIR, spUt.clear_playlist_name(train_playlist_name) + ".csv")  # noqa:E501
        tmp_dir_test = os.path.join(PREPRO_DIR, spUt.clear_playlist_name(test_playlist_name) + ".csv")  # noqa:E501

        if platform == "win32":
            tmp_dir_train = tmp_dir_train.replace("/", "\\")
            tmp_dir_test = tmp_dir_test.replace("/", "\\")

        if not os.path.exists(tmp_dir_train) or not os.path.exists(tmp_dir_test):  # noqa:E501
            extract_data(user_data=True, playlists=user_playlists,
                         zip_dir=DATASET_ZIP_DIR,
                         dir_to_store_data=PREPRO_DIR)

        preprocess(tmp_dir_train, tmp_dir_test, dir_to_store_data=PRO_DIR)

    clustering(PROCESSED_TRAIN_DIR, PROCESSED_TEST_DIR,
               dir_to_store_data=OUT_DIR,
               dir_to_store_model=STORE_MODEL_DIR)

    target_song, recommended_songs = recommend(clustered_train_data=CLUSTER_TRAIN_DIR,   # noqa:E501
                                               clustered_test_data=CLUSTER_TEST_DIR,   # noqa:E501
                                               dir_to_store_recommendation=OUT_DIR)   # noqa:E501
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
