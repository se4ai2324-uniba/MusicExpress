"""Script to extract the data (default or user's playlists)"""

# pylint: disable=wrong-import-position
import sys                                   # noqa:E402
from sys import platform                     # noqa:E402
sys.path.append('src')                       # noqa:E402
import zipfile as zf                         # noqa:E402
from codecarbon import EmissionsTracker      # noqa:E402
import files_utilities as flUt               # noqa:E402
import spotipy_utilities as spUt             # noqa:E402
import conf                                  # noqa:E402
# pylint: enable=wrong-import-position


# Codecarbon tracker instance
tracker = EmissionsTracker(
        project_name="_DATA_EXTRACTION_",
        output_file=conf.CODECARBON_REPORT_PATH,
        tracking_mode='process',
        on_csv_write='update'
        )


def extract_data(user_data=False, playlists=None,
                 zip_dir=conf.DATA_DIR + 'dataset.zip',
                 dir_to_store_data=conf.PREPRO_DATA_DIR):
    """ Method to extract playlist's data"""
    # List of the playlists names
    tracker.start()
    playlist_names = []

    dir_to_store_data += "/"

    # Modify file path based on the operating system
    if platform == "win32":
        dir_to_store_data = dir_to_store_data.replace("/", "\\")

    if not user_data:

        # Default scenario
        with zf.ZipFile(zip_dir, 'r') as zip_ref:
            zip_ref.extractall(dir_to_store_data)

        print("The default playlists are:\n")
        for p in conf.PLAYLISTS_NAMES:
            print(f"Playlist's Name: {p}")
            playlist_names.append(p)

    else:
        # User playlists scenario
        playlist_names = []

        print("The provided playlists are:\n")
        for p in playlists:
            playlist_names.append(spUt.clear_playlist_name(spUt.get_playlist_name(p)))  # noqa:E501
            print(f"Playlist's ID: {p} || Name: {playlist_names[-1]}")

        print("===================================================")
        print("Checking if the playlists are stored, "
              "otherwise the data will be extracted.")

        for playlist_id in playlists:
            # pylint: disable=line-too-long
            playlist_name = spUt.clear_playlist_name(spUt.get_playlist_name(playlist_id))  # noqa:E501
            # pylint: enable=line-too-long

            playlist_names.append(playlist_name)

            if flUt.check_file_exists(playlist_id, dir_to_store_data):
                print(f"{spUt.get_playlist_name(playlist_id)} is "
                      f"stored and ready to be used.")
            else:
                print(f"{spUt.get_playlist_name(playlist_id)} isn't stored. "
                      f"Creating dataframe...")

                flUt.create_playlist_df(playlist_id, dir_to_store_data)  # noqa:E501,F841

            print("===================================================")

        print("All playlists have been stored!")

        print("Here is a list of all the stored playlists:")
        for x, playlist_name in enumerate(playlist_names):
            print(f"{str(x + 1)}. Playlist: {playlist_name}")
        print("===================================================")

    tracker.stop()
    return playlist_names


if __name__ == "__main__":
    extract_data()
