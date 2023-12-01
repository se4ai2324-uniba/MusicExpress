"""Script containing Pytest tests designed for file_utilities methods"""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import os  # noqa:E402
import pandas as pd  # noqa:E402
import conf  # noqa:E402
import files_utilities as flUt  # noqa:E402
import spotipy_utilities as spUt  # noqa:E402
# pylint: enable=wrong-import-position

# Valid playlist id: 3fSsw9Mp5Mi2DDiweZggtP
STORED_PLAYLIST_ID = conf.PLAYLISTS[0]

# Playlist not stored in our folder
NOT_STORED_PLAYLIST_ID = "0THO1kZlbyWvlgAh8YUCSd"

# Empty dataframe used in test_store_playlist_dataframe
temp_df = pd.DataFrame(columns=conf.DATAFRAMECOLUMNS)


def test_check_file_not_exists():
    '''Test the method check_file_exists
    if the file does not exist'''
    method_result = flUt.check_file_exists(NOT_STORED_PLAYLIST_ID)
    assert method_result is False, "The file already exists!"


def test_check_file_exists():
    '''Test the method check_file_exists
    if the file exist'''
    method_result = flUt.check_file_exists(STORED_PLAYLIST_ID)
    assert method_result is True, "The file does not exists!"


def test_read_not_stored_playlist_df():
    '''Test method for the 
    method read_playlist_df'''
    method_result = flUt.read_playlist_df(NOT_STORED_PLAYLIST_ID)
    assert method_result is None, "The file is already stored!"


def test_read_stored_playlist_df():
    '''Test method for the method read_playlist_df'''
    playlist = spUt.get_playlist_name(STORED_PLAYLIST_ID)
    playlist = spUt.clear_playlist_name(playlist)
    method_result = flUt.read_playlist_df(playlist)
    assert len(method_result) > 0, "The file is not stored!"


def test_create_playlist_df():
    '''Test method for the method create_playlist_df.
    The invalid_playlist_id is used
    due to the playlist not being stored'''
    method_result = flUt.create_playlist_df(NOT_STORED_PLAYLIST_ID)
    assert method_result is not False, "The playlist was not created!"


def test_store_playlist_dataframe():
    '''Test method for the method store_playlist_dataframe'''
    tmp_dir = conf.PREPRO_DATA_DIR + "tempPlaylist.csv"
    flUt.store_playlist_dataframe(NOT_STORED_PLAYLIST_ID, temp_df)  # noqa:E501
    method_result = os.path.exists(tmp_dir)
    assert method_result is not False, "The playlist was not stored!"
    os.remove(tmp_dir)
