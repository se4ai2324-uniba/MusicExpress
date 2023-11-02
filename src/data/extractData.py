# ================================ Playlist Retrival ================================
import sys
sys.path.append('src')
import conf
import filesUtilities as flUt
import spotipyUtilities as spUt
import pandas as pd
import zipfile as zf

with zf.ZipFile(conf.data_dir +'dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(conf.prepro_data_dir)

print("The default playlists are:\n")
for p in conf.playlists:
    print("Playlist's ID: %s || Name: %s" % (p, spUt.getPlaylistName(p)))

print("===================================================")
print("Checking if the playlist is stored, otherwise the data will be extracted.")

# List of the playlists names, needed to store them and avoid repeatedly retrieving them
playlistsNames = []

for playlistID in conf.playlists:

  playlistName = spUt.clearPlaylistName(spUt.getPlaylistName(playlistID))

  playlistsNames.append(playlistName)

  if(flUt.checkFileExists(playlistID)):
    print("The file of the playlist \"%s\" is stored and ready to be used." % spUt.getPlaylistName(playlistID))
  else:
    print("The file of the playlist \"%s\" isn't stored. Creating dataframe..." % spUt.getPlaylistName(playlistID))
    tracksDF = flUt.createPlaylistDF(playlistID)

  print("===================================================")


print("All playlists have been stored! Here a list of all the stored playlists:")
for x in range(len(playlistsNames)):
  print(str(x+1) + ". Playlist: " + playlistsNames[x])
print("===================================================")