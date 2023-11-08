"""Script to process the extracted data"""

import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import pandas as pd  # noqa:E402
import conf  # noqa:E402


# =============================== Preprocessing ===============================

# Method that removes rows that contain null values in the field "Name"
def remove_null_values_df(df):

    df.isnull().sum()
    preLen = len(df)

    df = df.dropna(subset=['Name'])
    post_len = len(df)
    print(f"{preLen-post_len} rows have been removed!")

    return df


# Normalize specific dataframe columns using min-max
def min_max_normalization(data, columns):

    min_vals = data[columns].min()
    max_vals = data[columns].max()
    range_vals = max_vals - min_vals

    normalized_data = data.copy()
    normalized_data[columns] = (data[columns] - min_vals) / range_vals

    return normalized_data


# Normalize Tempo and Loudness columns in the dataframe.
def normalize_columns(df):
    cols_to_normalize = ['Loudness']
    df = min_max_normalization(df, cols_to_normalize)
    return df


# Preprocesses a dataframe by removing null rows and normalizing two columns.
def preprocess_data(df):
    df = remove_null_values_df(df)
    df = normalize_columns(df)
    return df


# Method to print the min and max value of a column in a dataframe
def print_column_min_max(df, column):
    min = df[column].min()
    max = df[column].max()
    print("For the column %s the min val. is %s and the max val. is %s"
          % (column, str(min), str(max)))


train_tracks_df = pd.read_csv(conf.TRAIN_SET_CSV_PATH)
test_tracks_df = pd.read_csv(conf.TEST_SET_CSV_PATH)

print("===================================================")
print("Preprocessing train set..\nRemoving rows with null values...")
train_tracks_df = remove_null_values_df(train_tracks_df)
print("Normalizing the values in the column Loudness."
      "Pre-Normalization min and max values:")
print_column_min_max(train_tracks_df, "Loudness")
train_tracks_df = normalize_columns(train_tracks_df)
print("Post-Normalization min and max values:")
print_column_min_max(train_tracks_df, "Loudness")
print("The train set has been preprocessed!")

print("===================================================")

print("Moving onto the test set. Removing rows with null values...")
test_tracks_df = remove_null_values_df(test_tracks_df)
print("Normalizing the values in the column Loudness."
      "Pre-Normalization min and max values:")
print_column_min_max(test_tracks_df, "Loudness")
test_tracks_df = normalize_columns(test_tracks_df)
print("The test set has been preprocessed!")
print("Pre-Normalization min and max values:")
print_column_min_max(test_tracks_df, "Loudness")
print("===================================================")

OUTPUT_TRAIN_FILE = conf.PRO_DATA_DIR + 'trainSet.csv'
OUTPUT_TEST_FILE = conf.PRO_DATA_DIR + 'testSet.csv'

print("Storing the preprocessed files in the folder preprocessed_data.")
train_tracks_df.to_csv(OUTPUT_TRAIN_FILE, index=False)
test_tracks_df.to_csv(OUTPUT_TEST_FILE, index=False)
print("The data has been stored!")
print("===================================================")
