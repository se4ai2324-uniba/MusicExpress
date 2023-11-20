"""Definitions for the objects used by our resource endpoints."""
# pylint: disable=wrong-import-position,anomalous-backslash-in-string
import sys                                                       # noqa:E402
import os                                                        # noqa:E402
sys.path.append('\\'.join(os.getcwd().split('\\')[:-2])+'\src')  # noqa:E402,E501,W605
# pylint: disable=no-name-in-module
from pydantic import BaseModel                                   # noqa:E402
# pylint: enable=import-error
import conf                                                      # noqa:E402
# pylint: enable=wrong-import-position,anomalous-backslash-in-string


class PredictPayload(BaseModel):
    '''Default data payload'''
    id_playlist_train: str
    id_playlist_test: str
    no_recommendations: int

    class Config:
        '''Default data values'''
        schema_extra = {
            "default": {
                "id_playlist_train": conf.PLAYLISTS[0],
                "id_playlist_test": conf.PLAYLISTS[1],
                "no_recommendations": conf.NO_RECOMMENDATIONS,
            }
        }


class UserPlaylistPayload(BaseModel):
    '''User data payload'''
    id_playlist_train: str
    id_playlist_test: str
