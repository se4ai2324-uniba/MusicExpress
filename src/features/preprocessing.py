"""Script to process the extracted data (default or user's playlists)"""

# pylint: disable=wrong-import-position
import os                                 # noqa:E402
import sys                                # noqa:E402
from sys import platform                  # noqa:E402
from pathlib import Path                  # noqa:E402
sys.path.append('src')                    # noqa:E402
import pandas as pd                       # noqa:E402
from codecarbon import EmissionsTracker   # noqa:E402
import conf                               # noqa:E402
# pylint: enable=wrong-import-position


tracker = EmissionsTracker(
        project_name="_PREPROCESSING_",
        output_file=conf.CODECARBON_REPORT_PATH,
        tracking_mode='process',
        on_csv_write='update'
        )


def remove_null_values_df(df):
    """Method that removes rows that
    contain null values in the field "Name\""""

    df.isnull().sum()
    pre_len = len(df)

    df = df.dropna(subset=['Name'])
    post_len = len(df)
    print(f"{pre_len-post_len} rows have been removed!")

    return df


def min_max_normalization(data, columns):
    """Normalize specific dataframe columns using min-max"""
    min_vals = data[columns].min()
    max_vals = data[columns].max()
    range_vals = max_vals - min_vals

    normalized_data = data.copy()
    normalized_data[columns] = (data[columns] - min_vals) / range_vals

    return normalized_data


def print_column_min_max(df, column):
    """Method to print the min and max value of a column in a dataframe"""
    column_min = df[column].min()
    column_max = df[column].max()

    print(f"For the column {column} the min val. is {str(column_min)} "
          f"and the max val. is {str(column_max)}")


def preprocess(raw_train_data=conf.TRAIN_SET_CSV_PATH,
               raw_test_data=conf.TEST_SET_CSV_PATH,
               dir_to_store_data=conf.PRO_DATA_DIR):
    """Method to preprocess raw data"""
    
    tracker.start()
    print("Path file: " + str(Path(__file__).resolve()))

    train_tracks_df = pd.read_csv(raw_train_data)
    test_tracks_df = pd.read_csv(raw_test_data)

    output_train_file = os.path.join(dir_to_store_data, 'trainSet.csv')
    output_test_file = os.path.join(dir_to_store_data, 'testSet.csv')

    # Modify file paths based on the operating system
    if platform == "win32":
        output_train_file = output_train_file.replace("/", "\\")
        output_test_file = output_test_file.replace("/", "\\")

    print("===================================================")
    print("Preprocessing train set..\nRemoving rows with null values...")
    train_tracks_df = remove_null_values_df(train_tracks_df)
    print("Normalizing the values in the column Loudness."
          "Pre-Normalization min and max values:")
    print_column_min_max(train_tracks_df, "Loudness")
    train_tracks_df = min_max_normalization(train_tracks_df, ['Loudness'])
    print("Post-Normalization min and max values:")
    print_column_min_max(train_tracks_df, "Loudness")
    print("The train set has been preprocessed!")

    print("===================================================")

    print("Moving onto the test set. Removing rows with null values...")
    test_tracks_df = remove_null_values_df(test_tracks_df)
    print("Normalizing the values in the column Loudness."
          "Pre-Normalization min and max values:")
    print_column_min_max(test_tracks_df, "Loudness")
    test_tracks_df = min_max_normalization(test_tracks_df, ['Loudness'])
    print("The test set has been preprocessed!")
    print("Pre-Normalization min and max values:")
    print_column_min_max(test_tracks_df, "Loudness")
    print("===================================================")

    print("Storing the preprocessed files in the folder preprocessed_data.")
    train_tracks_df.to_csv(output_train_file, index=False)
    test_tracks_df.to_csv(output_test_file, index=False)
    print("The data has been stored!")
    print("===================================================")

    tracker.stop()
    return bool(os.path.exists(output_train_file) and os.path.exists(output_test_file))  # noqa:E501


if __name__ == "__main__":
    preprocess()
