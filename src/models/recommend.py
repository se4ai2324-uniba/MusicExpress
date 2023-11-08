"""Script for recommending songs to the user"""
#pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import random  # noqa:E402
import numpy as np  # noqa:E402
import pandas as pd  # noqa:E402
import conf  # noqa:E402
import spotipy_utilities as spUt  # noqa:E402
#pylint: enable=wrong-import-position

def euclidean_distance(track_1, track_2, features):
    """"Euclidean distance between two songs"""
    track_1_features = track_1[features].values
    track_2_features = track_2[features].values

    distance = np.linalg.norm(track_1_features - track_2_features)

    return distance


def recommend_songs(test_tracks_cluster, test_track,
                    cluster_label, num_recommendations, features):
    """Function to recommend songs based on cluster"""

    #pylint: disable=line-too-long
    cluster_tracks = test_tracks_cluster[test_tracks_cluster['Cluster'] == cluster_label]  # noqa:E501
    #pylint: enable=line-too-long

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


train_tracks_df = pd.read_csv(conf.CLUSTER_TRAIN_SET_PATH)
test_tracks_df = pd.read_csv(conf.CLUSTER_TEST_SET_PATH)

train_track_index = random.randint(0, len(train_tracks_df))
train_track = train_tracks_df.iloc[train_track_index]
print("===================================================")
print("Starting song recommendation phase...")
print("===================================================")

track_cluster = train_tracks_df[train_tracks_df['Name'] == train_track['Name']]

print(f"The track from which suggestions will be computed is: "
      f"Song: {track_cluster['Name'].values[0]} - " 
      f"Artist: {track_cluster['Artist'].values[0]}")

train_track_cluster = track_cluster['Cluster'].values[0]
print("===================================================")

recommendations = recommend_songs(test_tracks_df, train_track, train_track_cluster,
                                  conf.NO_RECOMMENDATIONS, conf.FEATURES)
recommendations_links = []

for x,recommendation in enumerate(recommendations):
    recommendations_links.append(spUt.get_track_preview(
        recommendation['Name'], recommendation['Artist']))

for x,recommendation in enumerate(recommendations):
    print(str(x+1) + "° Track: " + recommendation['Name'] +
          " - Artist: " + recommendation['Artist'])
    print("Preview: ", recommendations_links[x])
print("===================================================")

recommendations_data = []

for recommendation in recommendations:
    recommendation_dict = {
        'Name': recommendation['Name'],
        'Artist': recommendation['Artist']
    }
    recommendations_data.append(recommendation_dict)

recommendations_df = pd.DataFrame(recommendations_data)

RECOMM_PATH = conf.OUTPUT_DIR + "recommendations.csv"
recommendations_df.to_csv(RECOMM_PATH, index=False)
