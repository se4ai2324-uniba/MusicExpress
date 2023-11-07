"""Script for data clustering"""

import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import conf  # noqa:E402
import pandas as pd  # noqa:E402
from sklearn_extra.cluster import KMedoids  # noqa:E402
from joblib import dump  # noqa:E402


# ================================ Clustering ================================

print("Starting to cluster out the data...")
trainTracksDF = pd.read_csv(conf.PRO_TRAIN_SET_PATH)
testTracksDF = pd.read_csv(conf.PRO_TEST_SET_PATH)

trainSet = trainTracksDF[conf.FEATURES]
testSet = testTracksDF[conf.FEATURES]

# Clustering train set (user's preferences playlist)
kmedoids = KMedoids(n_clusters=conf.NO_CLUSTER,
                    random_state=conf.RND_STATE)

clusters = kmedoids.fit_predict(trainSet)
trainTracksDF['Cluster'] = clusters

# Cluster the test set using the trained model for song suggestions.
test_clusters = kmedoids.predict(testSet)
testTracksDF['Cluster'] = test_clusters

print("Clustering completed!")

print("===================================================")
outputTrainFile = conf.OUTPUT_DIR + 'clustertrainSet.csv'
outputTestFile = conf.OUTPUT_DIR + 'clustertestSet.csv'

print("Storing the processed files in the folder processed_data.")
trainTracksDF.to_csv(outputTrainFile, index=False)
testTracksDF.to_csv(outputTestFile, index=False)
print("The data has been stored!")
print("===================================================")

print("First 5 rows of the train set:")
print(trainTracksDF.head())

print("First 5 rows of the test set:")
print(testTracksDF.head())

# Save the model to the file
dump(kmedoids, conf.MODEL_FILE_PATH)
