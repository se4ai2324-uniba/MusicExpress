import spotipyUtilities as spUt
import conf

import os
import time
import pandas as pd

# Method that checks whether a file has already been stored or not
def checkFileExists(playlist_id):

  currentPlaylist = spUt.clearPlaylistName(spUt.getPlaylistName(playlist_id))

  file_name = str(currentPlaylist) + ".csv"
  file_path = conf.prepro_data_dir + file_name

  if os.path.isfile(file_path):
      print("The playlist %s was already stored.\nChecking for differences..." % currentPlaylist)
      return True
  else:
      return False

# Method that reads a stored file
def readPlaylistDF(playlist_id):

  file_name = str(playlist_id) + ".csv"
  file_path = conf.data_dir + file_name

  if os.path.isfile(file_path):
      dataframe = pd.read_csv(file_path)
      print("Playlist has been successfully loaded!")
      return dataframe
  else:
      print("File does not exist. Unable to load playlist.")
      return None

# Method that creates the Dataframe for a Playlist and stores it
def createPlaylistDF(playlist_id):

  tracks = spUt.trackIDsFromPlaylist("ivanrinaldi_", playlist_id)
  print("%d tracks have been found in the given playlist!\nExtracting features of each track..." % len(tracks))

  tracksFeatures = []

  for id in tracks:
    time.sleep(.20)
    tracksFeatures.append(spUt.getTrackFeatures(id))

  print("Feature for all %d songs have been extracted.\nCreating dataframe.." % len(tracks))

  tracksDF = pd.DataFrame(tracksFeatures, columns = conf.dataframeColumns)
  print("The dataframe has been successfully created!")
  storePlaylistDataframe(playlist_id, tracksDF)
  return tracksDF

# Method that stores the Dataframe of a Playlist
def storePlaylistDataframe(playlist_id, dataframe):
  playlistName = spUt.getPlaylistName(playlist_id)
  file_name = playlistName + ".csv"
  file_path = conf.data_dir + file_name
  dataframe.to_csv(file_path, index=False)
  print("Playlist has been successfully saved! - Playlist's Name: " + str(spUt.getPlaylistName(playlist_id)))