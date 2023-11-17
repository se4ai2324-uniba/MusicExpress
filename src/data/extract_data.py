"""Script to extract the data"""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import zipfile as zf  # noqa:E402
import files_utilities as flUt  # noqa:E402
import spotipy_utilities as spUt  # noqa:E402
import conf  # noqa:E402
# pylint: enable=wrong-import-position


def extract_data():
    """ Method to extract data
    """
    with zf.ZipFile(conf.DATA_DIR + 'dataset.zip', 'r') as zip_ref:
        zip_ref.extractall(conf.PREPRO_DATA_DIR)

    print("The default playlists are:\n")
    for p in conf.PLAYLISTS:
        print(f"Playlist's ID: {p} || Name: {spUt.get_playlist_name(p)}")

    print("===================================================")
    print("Checking if the playlist is stored, "
          "otherwise the data will be extracted.")

    # List of the playlists names
    # needed to store them and avoid repeatedly retrieving them
    playlist_names = []

    for playlist_id in conf.PLAYLISTS:

        playlist_name = spUt.clear_playlist_name(spUt.get_playlist_name(playlist_id))  # noqa:E501

        playlist_names.append(playlist_name)

        if flUt.check_file_exists(playlist_id):
            print(f"{spUt.get_playlist_name(playlist_id)} is "
                  "stored and ready to be used.")
        else:
            print(f"{spUt.get_playlist_name(playlist_id)} isn't stored. "
                  f"Creating dataframe...")

            tracks_df = flUt.create_playlist_df(playlist_id)  # noqa:F841

        print("===================================================")

    print("All playlists have been stored!")

    print("Here is a list of all the stored playlists:")
    for x, playlist_name in enumerate(playlist_names):
        print(f"{str(x + 1)}. Playlist: {playlist_name}")
    print("===================================================")


extract_data()
