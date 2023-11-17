"""Main script: it includes our API initialization and endpoints."""

import pickle
from datetime import datetime
from functools import wraps
from http import HTTPStatus
from pathlib import Path
from typing import Dict, List

from fastapi import FastAPI, Request

from app.schemas import IrisType, PredictPayload

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

