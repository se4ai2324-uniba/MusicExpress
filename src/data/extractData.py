import sys
import conf
import filesUtilities as flUt
import spotipyUtilities as spUt
import zipfile as zf

# ======================= Playlist Retrival =======================
sys.path.append('src')

with zf.ZipFile(conf.data_dir + 'dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(conf.prepro_data_dir)

print("The default playlists are:\n")
for p in conf.playlists:
    print("Playlist's ID: %s || Name: %s" % (p, spUt.getPlaylistName(p)))

print("===================================================")
print("Checking if the playlist is stored, \
      otherwise the data will be extracted.")

# List of the playlists names
# needed to store them and avoid repeatedly retrieving them
playlistsNames = []

for playlistID in conf.playlists:

    playlistName = spUt.clearPlaylistName(spUt.getPlaylistName(playlistID))

    playlistsNames.append(playlistName)

    if (flUt.checkFileExists(playlistID)):
        print(f"The file of the playlist {spUt.getPlaylistName(playlistID)} 
              is stored and ready to be used.")
    else:
        print(f"The file of the playlist {spUt.getPlaylistName(playlistID)} \
               isn't stored. Creating dataframe...")
        tracksDF = flUt.createPlaylistDF(playlistID)

    print("===================================================")


print("All playlists have been stored!")
print("Here a list of all the stored playlists:")
for x in range(len(playlistsNames)):
    print(str(x+1) + ". Playlist: " + playlistsNames[x])
print("===================================================")
