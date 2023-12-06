"""Script for recommending songs to the user using clustered data"""
# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import random  # noqa:E402
import numpy as np  # noqa:E402
import pandas as pd  # noqa:E402
import conf  # noqa:E402
import spotipy_utilities as spUt  # noqa:E402
from codecarbon import EmissionsTracker     # noqa:E402
# pylint: enable=wrong-import-position


tracker = EmissionsTracker(
        project_name="_RECOMMENDATION_",
        output_file=conf.CODECARBON_REPORT_PATH,
        tracking_mode='process',
        on_csv_write='update'
        )


def euclidean_distance(track_1, track_2, features):
    """"Euclidean distance between two songs"""
    track_1_features = track_1[features].values
    track_2_features = track_2[features].values

    distance = np.linalg.norm(track_1_features - track_2_features)

    return distance


def recommend_songs(test_tracks_cluster, test_track,
                    cluster_label, num_recommendations, features):
    """Function to recommend songs based on cluster"""
    tracker.start()
    # pylint: disable=line-too-long
    cluster_tracks = test_tracks_cluster[test_tracks_cluster['Cluster'] == cluster_label]  # noqa:E501
    # pylint: enable=line-too-long

    # Calculate similarity with the test song
    similarity_scores = []

    for index, track in cluster_tracks.iterrows():
        # Avoids to compare between the test track and itself
        if track['Name'] != test_track['Name']:
            similarity = euclidean_distance(test_track, track, features)
            similarity_scores.append((index, similarity))

    # Sort songs by similarity in ascending order - Euclidean Distance
    similarity_scores.sort(key=lambda x: x[1])

    # Recommend top songs
    recommended_songs = []

    for i in range(min(num_recommendations, len(similarity_scores))):
        song_index = similarity_scores[i][0]
        recommended_songs.append(cluster_tracks.loc[song_index])

    return recommended_songs


def recommend(clustered_train_data=conf.CLUSTER_TRAIN_SET_PATH,
              clustered_test_data=conf.CLUSTER_TEST_SET_PATH,
              no_recommendations=conf.NO_RECOMMENDATIONS,
              dir_to_store_recommendation=conf.OUTPUT_DIR):
    """Method to recommend songs to the user"""
    train_tracks_df = pd.read_csv(clustered_train_data)
    test_tracks_df = pd.read_csv(clustered_test_data)
    recomm_path = dir_to_store_recommendation + "recommendations.csv"

    train_track = train_tracks_df.iloc[random.randint(0, len(train_tracks_df))]  # noqa:E501
    print("===================================================")
    print("Starting song recommendation phase...")
    print("===================================================")

    track_cluster = train_tracks_df[train_tracks_df['Name'] == train_track['Name']]  # noqa:E501

    print(f"The track from which suggestions will be computed is: "
          f"{track_cluster['Name'].values[0]} - "
          f"{track_cluster['Artist'].values[0]}")

    print("===================================================")

    recommendations = recommend_songs(test_tracks_df,
                                      train_track, track_cluster['Cluster'].values[0],  # noqa:E501
                                      no_recommendations, conf.FEATURES)
    recommendations_links = []

    for x, recommendation in enumerate(recommendations):
        recommendations_links.append(spUt.get_track_preview(
            recommendation['Name'], recommendation['Artist']))

    for x, recommendation in enumerate(recommendations):
        print(str(x+1) + "° Track: " + recommendation['Name'] +
              " - Artist: " + recommendation['Artist'])
        print("Preview: ", recommendations_links[x])
    print("===================================================")

    # pylint: disable=line-too-long
    recommendations_data = [{'Name': rec['Name'], 'Artist': rec['Artist']}
                            for rec in recommendations]
    # pylint: enable=line-too-long
    pd.DataFrame(recommendations_data).to_csv(recomm_path, index=False)

    # Build dict with recommended songs
    # pylint: disable=line-too-long
    result = [{'Name': rec['Name'], 'Artist': rec['Artist'],
               'Preview': recommendations_links[i]}
              for i, rec in enumerate(recommendations)]
    # pylint: enable=line-too-long

    tracker.stop()
    # pylint: disable=line-too-long
    return track_cluster['Name'].values[0] + " - " + track_cluster['Artist'].values[0], result  # noqa:E501
    # pylint: enable=line-too-long


if __name__ == "__main__":
    recommend()
