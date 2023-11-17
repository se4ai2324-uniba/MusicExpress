"""Script to process the extracted data"""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import pandas as pd  # noqa:E402
import conf  # noqa:E402
# pylint: enable=wrong-import-position

OUTPUT_TRAIN_FILE = conf.PRO_DATA_DIR + 'trainSet.csv'
OUTPUT_TEST_FILE = conf.PRO_DATA_DIR + 'testSet.csv'


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


def preprocess():
    """Method to preprocess raw data"""
    train_tracks_df = pd.read_csv(conf.TRAIN_SET_CSV_PATH)
    test_tracks_df = pd.read_csv(conf.TEST_SET_CSV_PATH)

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
    train_tracks_df.to_csv(OUTPUT_TRAIN_FILE, index=False)
    test_tracks_df.to_csv(OUTPUT_TEST_FILE, index=False)
    print("The data has been stored!")
    print("===================================================")


preprocess()
