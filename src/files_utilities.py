"""Script containing methods for file management"""

import os
import time
import pandas as pd
import conf
import spotipy_utilities as spUt


def check_file_exists(playlist_id, dir_to_check_data=conf.PREPRO_DATA_DIR):
    """Method that checks whether a file has already been stored or not"""
    current_playlist = spUt.clear_playlist_name(spUt.get_playlist_name(playlist_id))  # noqa:E501

    file_name = current_playlist + ".csv"
    file_path = dir_to_check_data + file_name

    if os.path.isfile(file_path):
        print(f"The playlist {current_playlist} was already stored.")
        print("Checking for differences...")
        return True

    return False


def read_playlist_df(playlist_id):
    """Method that reads a stored file"""
    file_name = str(playlist_id) + ".csv"
    file_path = conf.PREPRO_DATA_DIR + file_name

    if os.path.isfile(file_path):
        dataframe = pd.read_csv(file_path)
        print("Playlist has been successfully loaded!")
        return dataframe

    print("File does not exist. Unable to load playlist.")
    return None


def create_playlist_df(playlist_id, data_dir=conf.PREPRO_DATA_DIR):
    """Method that creates the Dataframe for a Playlist and stores it"""
    tracks = spUt.track_ids_from_playlist(conf.SPOTIFYUSER, playlist_id)
    print(f"{len(tracks)} tracks have been found in the given playlist!")
    print("Extracting features of each track...")

    tracks_features = []

    for id_track in tracks:
        time.sleep(.52)
        tracks_features.append(spUt.get_track_features(id_track))

    print(f"Feature for all {len(tracks)} songs have been extracted.")
    print("Creating dataframe..")

    tracks_df = pd.DataFrame(tracks_features, columns=conf.DATAFRAMECOLUMNS)
    print("The dataframe has been successfully created!")
    store_playlist_dataframe(playlist_id, tracks_df, data_dir)
    return tracks_df


def store_playlist_dataframe(playlist_id, dataframe,
                             data_dir_df=conf.PREPRO_DATA_DIR):
    """Method that stores the Dataframe of a Playlist"""
    playlist_name = spUt.get_playlist_name(playlist_id)
    file_name = playlist_name + ".csv"
    file_path = data_dir_df + file_name
    dataframe.to_csv(file_path, index=False)
    print("Playlist has been successfully saved!")
    print(f" - Playlist\'s Name: {str(spUt.get_playlist_name(playlist_id))}.")


def retrieve_all_playlists(playlist_dir=conf.PREPRO_DATA_DIR):
    """Method that retrieves the names of all the stored playlists"""
    default_ids = conf.PLAYLISTS
    default_names = conf.PLAYLISTS_NAMES

    available_playlists = []

    # Getting playlists available by default
    for playlist_id, playlist_name in zip(default_ids, default_names):
        available_playlists.append({"Id": playlist_id, "Name": playlist_name})

    # Getting other playlists that the user migth have extracted
    files_list = os.listdir(playlist_dir)
    # List of files that need to be removed if found in the folder
    files_to_remove = [".gitkeep", "feedbackUser1.csv", "feedbackUser2.csv"]   # noqa:E501

    for f in files_to_remove:
        if f in files_list:
            files_list.remove(f)

    files_list = [file[:-4] if file.endswith('.csv') else file for file in files_list]  # noqa:E501

    for playlist_name in files_list:
        if playlist_name not in default_names:
            playlist_id = spUt.get_playlist_id(playlist_name)

            if playlist_id is not None:
                available_playlists.append({"Id": playlist_id, "Name": playlist_name})  # noqa:E501

    print("Available playlists")
    print(available_playlists)

    return available_playlists
