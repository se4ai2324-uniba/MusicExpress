"""Script containing methods for file management"""

import conf
import os
import time
import pandas as pd
import spotipyUtilities as spUt


# Method that checks whether a file has already been stored or not
def checkFileExists(playlist_id):

    currentPlaylist = spUt.clearPlaylistName(spUt.getPlaylistName(playlist_id))

    file_name = str(currentPlaylist) + ".csv"
    file_path = conf.PREPRO_DATA_DIR + file_name

    if os.path.isfile(file_path):
        print(f'The playlist {currentPlaylist} was already stored.')
        print("Checking for differences...")
        return True
    
    return False


# Method that reads a stored file
def readPlaylistDF(playlist_id):

    file_name = str(playlist_id) + ".csv"
    file_path = conf.DATA_DIR + file_name

    if os.path.isfile(file_path):
        dataframe = pd.read_csv(file_path)
        print("Playlist has been successfully loaded!")
        return dataframe
    
    print("File does not exist. Unable to load playlist.")
    return None


# Method that creates the Dataframe for a Playlist and stores it
def createPlaylistDF(playlist_id):

    tracks = spUt.trackIDsFromPlaylist("ivanrinaldi_", playlist_id)
    print(f'{len(tracks)} tracks have been found in the given playlist!')
    print("Extracting features of each track...")

    tracksFeatures = []

    for id in tracks:
        time.sleep(.20)
        tracksFeatures.append(spUt.getTrackFeatures(id))

    print(f'Feature for all {len(tracks)} songs have been extracted.')
    print("Creating dataframe..")

    tracksDF = pd.DataFrame(tracksFeatures, columns=conf.DATAFRAMECOLUMNS)
    print("The dataframe has been successfully created!")
    storePlaylistDataframe(playlist_id, tracksDF)
    return tracksDF


# Method that stores the Dataframe of a Playlist
def storePlaylistDataframe(playlist_id, dataframe):
    playlistName = spUt.getPlaylistName(playlist_id)
    file_name = playlistName + ".csv"
    file_path = conf.DATA_DIR + file_name
    dataframe.to_csv(file_path, index=False)
    print("Playlist has been successfully saved!")
    print(f' - Playlist\'s Name: {str(spUt.getPlaylistName(playlist_id))}.')
