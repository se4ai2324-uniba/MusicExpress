"""Script to extract the data"""

import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import conf  # noqa:E402
import filesUtilities as flUt  # noqa:E402
import spotipyUtilities as spUt  # noqa:E402
import zipfile as zf  # noqa:E402

# ======================= Playlist Retrival =======================


with zf.ZipFile(conf.DATA_DIR + 'dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(conf.PREPRO_DATA_DIR)

print("The default playlists are:\n")
for p in conf.PLAYLISTS:
    print(f'Playlist\'s ID: {p} || Name: {spUt.getPlaylistName(p)}')

print("===================================================")
print("Checking if the playlist is stored, \
      otherwise the data will be extracted.")

# List of the playlists names
# needed to store them and avoid repeatedly retrieving them
playlistsNames = []

for playlistID in conf.PLAYLISTS:

    playlistName = spUt.clearPlaylistName(spUt.getPlaylistName(playlistID))

    playlistsNames.append(playlistName)

    if (flUt.checkFileExists(playlistID)):
        print(f'{spUt.getPlaylistName(playlistID)} is stored and ready to be used.')
    else:
        print(f'{spUt.getPlaylistName(playlistID)} isn\'t stored. Creating dataframe...')

        tracksDF = flUt.createPlaylistDF(playlistID)

    print("===================================================")


print("All playlists have been stored!")
print("Here a list of all the stored playlists:")
for x in range(len(playlistsNames)):
    print(f'{str(x+1)}. Playlist: {playlistsNames[x]}')
print("===================================================")
