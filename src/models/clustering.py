"""Script for data clustering"""

#pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import pandas as pd  # noqa:E402
from sklearn_extra.cluster import KMedoids  # noqa:E402
from joblib import dump  # noqa:E402
import conf  # noqa:E402
#pylint: enable=wrong-import-position


print("Starting to cluster out the data...")
train_tracks_df = pd.read_csv(conf.PRO_TRAIN_SET_PATH)
test_tracks_df = pd.read_csv(conf.PRO_TEST_SET_PATH)

train_set = train_tracks_df[conf.FEATURES]
test_set = test_tracks_df[conf.FEATURES]

# Clustering train set (user's preferences playlist)
kmedoids = KMedoids(n_clusters=conf.NO_CLUSTER,
                    random_state=conf.RND_STATE)

clusters = kmedoids.fit_predict(train_set)
train_tracks_df['Cluster'] = clusters

# Cluster the test set using the trained model for song suggestions.
test_clusters = kmedoids.predict(test_set)
test_tracks_df['Cluster'] = test_clusters

print("Clustering completed!")

print("===================================================")
OUTPUT_TRAIN_FILE = conf.OUTPUT_DIR + 'clustertrainSet.csv'
OUTPUT_TEST_FILE = conf.OUTPUT_DIR + 'clustertestSet.csv'

print("Storing the processed files in the folder processed_data.")
train_tracks_df.to_csv(OUTPUT_TRAIN_FILE, index=False)
test_tracks_df.to_csv(OUTPUT_TEST_FILE, index=False)
print("The data has been stored!")
print("===================================================")

print("First 5 rows of the train set:")
print(train_tracks_df.head())

print("First 5 rows of the test set:")
print(test_tracks_df.head())

# Save the model to the file
dump(kmedoids, conf.MODEL_FILE_PATH)
