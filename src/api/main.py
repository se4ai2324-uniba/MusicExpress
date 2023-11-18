"""Main script: it includes our API initialization and endpoints."""
# pylint: disable=wrong-import-position
from datetime import datetime                       # noqa:E402
from functools import wraps                         # noqa:E402
from http import HTTPStatus                         # noqa:E402
from pathlib import Path                            # noqa:E402
from typing import List                             # noqa:E402
from joblib import load                             # noqa:E402
from fastapi import FastAPI, Request                # noqa:E402
import conf
from schemas import PredictPayload                  # noqa:E402
from models.recommend import recommend              # noqa:E402
from models.clustering import clustering            # noqa:E402
# pylint: enable=wrong-import-position


MODELS_DIR = Path("models/")
model_wrappers_list: List[dict] = []


# Define application
app = FastAPI(
    title="MusicExpress",
    description="Description of Music Express APP",
    version="version",
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

        # Add data
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
        "data": {"message": "Welcome to MusicExpress! Please, read the `/docs`!"},  # TODO: modifica messaggio
    }
    return response


@app.on_event("startup")
def _load_models():
    """Loads all models in `MODELS_DIR`"""

    # TODO: 
    #   1. Load default model(s)
    #   2. Append models to path

    model_paths = [
        filename for filename in conf.MODEL_FILE_PATH.iterdir() if filename.suffix == ".pkl"
        
    ]
    for path in model_paths:
        with open(path, "rb") as file:
            model_wrapper = load(file)
            model_wrappers_list.append(model_wrapper)


@app.get("/models", tags=["Prediction"])
@construct_response
def _get_models_list(request: Request):
    """Return the lsit of available models"""

    available_models = [
        {
            "type": model["type"],
            "parameters": model["params"],
            "accuracy": model["metrics"],
        }
        for model in model_wrappers_list
    ]

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": available_models,
    }

    return response

@app.post("/models", tags=["Clustering"])
@construct_response
def _cluster_data(request: Request, type: str, payload: PredictPayload):
    """Cluster out the data"""

    # TODO: 
    #   1. Load data
    #   2. Clustering
    tmp_train_data = "abc"
    tmp_test_data = "abc"
    clustering(tmp_train_data, tmp_test_data)

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"message": "The data has been clustered! You can now get recommendations!"},
    }

    return response

@app.get("/data/output", tags=["Recommendation"])
@construct_response
def _get_clustered_playlists(request: Request):
    """Return the list of clustered playlists"""

    available_playlists = [
        playlist for playlist in conf.OUTPUT_DIR.iterdir() if playlist.suffix == ".csv"
        ]

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": available_playlists,
    }

    return response

@app.get("/models/{type}", tags=["Recommendation"])
@construct_response
def _get_recommended_songs(request: Request, type: str, payload: PredictPayload):
    """Return the list of recommended songs"""

    # TODO: 
    #   1. Extract data
    #   2. Preprocessing
    #   3. Clustering
    #   BONUS. Load data
    recommended_songs = recommend()

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": recommended_songs,
    }

    return response
