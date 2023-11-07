import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import conf  # noqa:E402
import spotipyUtilities as spUt  # noqa:E402
import numpy as np  # noqa:E402
import pandas as pd  # noqa:E402
import random  # noqa:E402


# ========================== Song Recommendations ===========================

# Euclidean distance between two songs
def euclideanDistance(track1, track2, features):

    track1Features = track1[features].values
    track2Features = track2[features].values

    distance = np.linalg.norm(track1Features - track2Features)

    return distance


# Function to recommend songs based on cluster
def recommend_songs(test_tracks_cluster, testTrack,
                    cluster_label, num_recommendations, features):

    clusterTracks = test_tracks_cluster[test_tracks_cluster['Cluster'] == cluster_label]  # noqa:E501

    # Calculate similarity with the test song
    similarity_scores = []

    for index, track in clusterTracks.iterrows():
        # Avoids to compare between the test track and itself
        if track['Name'] != testTrack['Name']:
            similarity = euclideanDistance(testTrack, track, features)
            similarity_scores.append((index, similarity))

    # Sort songs by similarity in ascending order - Euclidean Distance
    similarity_scores.sort(key=lambda x: x[1])

    # Recommend top songs
    recommended_songs = []

    for i in range(min(num_recommendations, len(similarity_scores))):
        song_index = similarity_scores[i][0]
        recommended_songs.append(clusterTracks.loc[song_index])

    return recommended_songs


trainTracksDF = pd.read_csv(conf.CLUSTER_TRAIN_SET_PATH)
testTracksDF = pd.read_csv(conf.CLUSTER_TEST_SET_PATH)

trainTrackIndex = random.randint(0, len(trainTracksDF))
trainTrack = trainTracksDF.iloc[trainTrackIndex]
print("===================================================")
print("Starting song recommendation phase...")
print("===================================================")

trackCluster = trainTracksDF[trainTracksDF['Name'] == trainTrack['Name']]
print("The track from which suggestions will be computed is: \"%s - %s\"."
      % (trackCluster['Name'].values[0], trackCluster['Artist'].values[0]))

trainTrackCluster = trackCluster['Cluster'].values[0]
print("===================================================")

recommendations = recommend_songs(testTracksDF, trainTrack, trainTrackCluster,
                                  conf.NO_RECOMMENDATIONS, conf.FEATURES)
recommendations_links = []

for x in range(len(recommendations)):
    recommendations_links.append(spUt.getTrackPreview(
        recommendations[x]['Name'], recommendations[x]['Artist']))

for x in range(len(recommendations)):
    print(str(x+1) + "° Track: " + recommendations[x]['Name'] +
          " - Artist: " + recommendations[x]['Artist'])
    print("Preview: ", recommendations_links[x])
print("===================================================")

recommendations_data = []

for recommendation in recommendations:
    recommendation_dict = {
        'Name': recommendation['Name'],
        'Artist': recommendation['Artist']
    }
    recommendations_data.append(recommendation_dict)

recommendationsDF = pd.DataFrame(recommendations_data)

recommPath = conf.OUTPUT_DIR + "recommendations.csv"
recommendationsDF.to_csv(recommPath, index=False)
