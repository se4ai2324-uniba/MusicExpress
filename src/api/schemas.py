"""Definitions for the objects used by our resource endpoints."""
# pylint: disable=wrong-import-position,anomalous-backslash-in-string, too-few-public-methods  # noqa:E501
import sys                                                       # noqa:E402
import os                                                        # noqa:E402
sys.path.append('\\'.join(os.getcwd().split('\\')[:-2])+'\src')  # noqa:E402,E501,W605
# pylint: disable=no-name-in-module
from pydantic import BaseModel                                   # noqa:E402
# pylint: enable=import-error
# pylint: enable=wrong-import-position,anomalous-backslash-in-string


class UserPlaylistPayload(BaseModel):
    '''User data payload'''
    id_playlist_train: str
    id_playlist_test: str
# pylint: enable=too-few-public-methods
