"""Main script: it includes our API initialization and endpoints."""
# pylint: disable=wrong-import-position
import sys                            # noqa:E402
sys.path.append('src')                # noqa:E402
from datetime import datetime         # noqa:E402
from functools import wraps           # noqa:E402
from http import HTTPStatus           # noqa:E402
from pathlib import Path              # noqa:E402
from typing import List               # noqa:E402
from fastapi import FastAPI, Request  # noqa:E402
from schemas import PredictPayload    # noqa:E402
import models.recommend as rec        # noqa:E402
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



@app.get("/models/{type}", tags=["Prediction"])
@construct_response
def _get_recommended_songs(request: Request, type: str, payload: PredictPayload):
    """Return the lsit of recommended songs"""

    # TODO: 
    #   1. Extract data
    #   2. Preprocessing
    #   3. Clustering
    recommended_songs = rec.recommend()

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": recommended_songs,
    }

    return response
