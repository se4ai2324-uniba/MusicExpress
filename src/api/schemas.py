"""Definitions for the objects used by our resource endpoints."""
# pylint: disable=wrong-import-position
import sys                      # noqa:E402
sys.path.append('src')          # noqa:E402
import conf                     # noqa:E402
import string                   # noqa:E402
from pydantic import BaseModel  # noqa:E402
# pylint: enable=wrong-import-position


class PredictPayload(BaseModel):
    id_playlist_train: string
    id_playlist_test: string
    no_recommendations : int
   
    class Config:
        schema_extra = {
            "default": {
                "id_playlist_train": conf.PLAYLISTS[0],
                "id_playlist_test": conf.PLAYLISTS[1],
                "no_recommendations": conf.NO_RECOMMENDATIONS,
            }
        }
