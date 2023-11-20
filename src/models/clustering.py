"""Script for data clustering"""

# pylint: disable=wrong-import-position
import os                                   # noqa:E402
import sys                                  # noqa:E402
sys.path.append('src')                      # noqa:E402
import pandas as pd                         # noqa:E402
from sklearn_extra.cluster import KMedoids  # noqa:E402
from joblib import dump                     # noqa:E402
import conf                                 # noqa:E402
# pylint: enable=wrong-import-position


def clustering(processed_train_data=conf.PRO_TRAIN_SET_PATH,
               processed_test_data=conf.PRO_TEST_SET_PATH,
               dir_to_store_data=conf.OUTPUT_DIR,
               dir_to_store_model=conf.MODEL_FILE_PATH):
    """Method to generate data clusters"""
    print("Starting to cluster out the data...")
    train_tracks_df = pd.read_csv(processed_train_data)
    test_tracks_df = pd.read_csv(processed_test_data)

    output_train_file = dir_to_store_data + 'clustertrainSet.csv'
    output_test_file = dir_to_store_data + 'clustertestSet.csv'

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

    print("Storing the processed files in the folder processed_data.")
    train_tracks_df.to_csv(output_train_file, index=False)
    test_tracks_df.to_csv(output_test_file, index=False)
    print("The data has been stored!")
    print("===================================================")

    print("First 5 rows of the train set:")
    print(train_tracks_df.head())

    print("First 5 rows of the test set:")
    print(test_tracks_df.head())

# Save the model to the file
    dump(kmedoids, dir_to_store_model)

    return bool(os.path.exists(output_train_file) and os.path.exists(output_test_file))  # noqa:E501


if __name__ == "__main__":
    clustering()
