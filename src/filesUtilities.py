"""Script containing methods for file management"""

import os
import time
import pandas as pd
import conf
import spotipyUtilities as spUt


# Method that checks whether a file has already been stored or not
def check_file_exists(playlist_id):

    current_playlist = spUt.clear_playlist_name(spUt.get_playlist_name(playlist_id))

    file_name = str(current_playlist) + ".csv"
    file_path = conf.PREPRO_DATA_DIR + file_name

    if os.path.isfile(file_path):
        print(f"The playlist {current_playlist} was already stored.")
        print("Checking for differences...")
        return True

    return False


# Method that reads a stored file
def read_playlist_df(playlist_id):

    file_name = str(playlist_id) + ".csv"
    file_path = conf.DATA_DIR + file_name

    if os.path.isfile(file_path):
        dataframe = pd.read_csv(file_path)
        print("Playlist has been successfully loaded!")
        return dataframe

    print("File does not exist. Unable to load playlist.")
    return None


# Method that creates the Dataframe for a Playlist and stores it
def create_playlist_df(playlist_id):

    tracks = spUt.track_ids_from_playlist("ivanrinaldi_", playlist_id)
    print(f"{len(tracks)} tracks have been found in the given playlist!")
    print("Extracting features of each track...")

    tracks_features = []

    for id in tracks:
        time.sleep(.20)
        tracks_features.append(spUt.get_track_features(id))

    print(f"Feature for all {len(tracks)} songs have been extracted.")
    print("Creating dataframe..")

    tracks_df = pd.DataFrame(tracks_features, columns=conf.DATAFRAMECOLUMNS)
    print("The dataframe has been successfully created!")
    store_playlist_dataframe(playlist_id, tracks_df)
    return tracks_df


# Method that stores the Dataframe of a Playlist
def store_playlist_dataframe(playlist_id, dataframe):
    playlist_name = spUt.get_playlist_name(playlist_id)
    file_name = playlist_name + ".csv"
    file_path = conf.DATA_DIR + file_name
    dataframe.to_csv(file_path, index=False)
    print("Playlist has been successfully saved!")
    print(f" - Playlist\'s Name: {str(spUt.get_playlist_name(playlist_id))}.")
