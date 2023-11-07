"""Script to process the extracted data"""

import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import pandas as pd  # noqa:E402
import conf  # noqa:E402


# =============================== Preprocessing ===============================

# Method that removes rows that contain null values in the field "Name"
def removeNullValuesDF(df):

    df.isnull().sum()
    preLen = len(df)

    df = df.dropna(subset=['Name'])
    postLen = len(df)
    print("%d rows have been removed!" % (preLen-postLen))

    return df


# Normalize specific dataframe columns using min-max
def minMaxNormalization(data, columns):

    minVals = data[columns].min()
    maxVals = data[columns].max()
    rangeVals = maxVals - minVals

    normalized_data = data.copy()
    normalized_data[columns] = (data[columns] - minVals) / rangeVals

    return normalized_data


# Normalize Tempo and Loudness columns in the dataframe.
def normalizeColumns(df):
    colsToNormalize = ['Loudness']
    df = minMaxNormalization(df, colsToNormalize)
    return df


# Preprocesses a dataframe by removing null rows and normalizing two columns.
def preprocessData(df):
    df = removeNullValuesDF(df)
    df = normalizeColumns(df)
    return df


# Method to print the min and max value of a column in a dataframe
def printColumnMinMax(df, column):
    min = df[column].min()
    max = df[column].max()
    print("For the column %s the min val. is %s and the max val. is %s"
          % (column, str(min), str(max)))


trainTracksDF = pd.read_csv(conf.TRAIN_SET_CSV_PATH)
testTracksDF = pd.read_csv(conf.TEST_SET_CSV_PATH)

print("===================================================")
print("Preprocessing train set..\nRemoving rows with null values...")
trainTracksDF = removeNullValuesDF(trainTracksDF)
print("Normalizing the values in the column Loudness."
      "Pre-Normalization min and max values:")
printColumnMinMax(trainTracksDF, "Loudness")
trainTracksDF = normalizeColumns(trainTracksDF)
print("Post-Normalization min and max values:")
printColumnMinMax(trainTracksDF, "Loudness")
print("The train set has been preprocessed!")

print("===================================================")

print("Moving onto the test set. Removing rows with null values...")
testTracksDF = removeNullValuesDF(testTracksDF)
print("Normalizing the values in the column Loudness."
      "Pre-Normalization min and max values:")
printColumnMinMax(testTracksDF, "Loudness")
testTracksDF = normalizeColumns(testTracksDF)
print("The test set has been preprocessed!")
print("Pre-Normalization min and max values:")
printColumnMinMax(testTracksDF, "Loudness")
print("===================================================")

OUTPUT_TRAIN_FILE = conf.PRO_DATA_DIR + 'trainSet.csv'
OUTPUT_TEST_FILE = conf.PRO_DATA_DIR + 'testSet.csv'

print("Storing the preprocessed files in the folder preprocessed_data.")
trainTracksDF.to_csv(OUTPUT_TRAIN_FILE, index=False)
testTracksDF.to_csv(OUTPUT_TEST_FILE, index=False)
print("The data has been stored!")
print("===================================================")
