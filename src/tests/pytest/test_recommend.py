"""PyTest for recommend.py"""
# pylint: disable=wrong-import-position
import sys                      # noqa:E402
sys.path.append('src')          # noqa:E402
import pandas as pd             # noqa:E402
import conf                     # noqa:E402
import models.recommend as rec  # noqa:E402
# pylint: enable=wrong-import-position


def test_euclidean_distance():
    """Method to test euclidean distance computation"""
    train_tracks_df = pd.read_csv(conf.CLUSTER_TRAIN_SET_PATH)

    track_1 = train_tracks_df.iloc[0]
    track_2 = train_tracks_df.iloc[1]
    # pylint: disable=line-too-long
    assert rec.euclidean_distance(track_1, track_2, conf.FEATURES) > 0, "Euclidean distance cannot be negative"  # noqa:E501
    # pylint: enable=line-too-long


def test_five_recommended_songs():
    """Method to test if 5 songs are recommended"""
    train_tracks_df = pd.read_csv(conf.CLUSTER_TRAIN_SET_PATH)
    test_tracks_df = pd.read_csv(conf.CLUSTER_TEST_SET_PATH)

    sample_track = train_tracks_df.iloc[0]
    track_cluster = train_tracks_df[train_tracks_df['Name'] == sample_track['Name']]  # noqa:E501
    train_track_cluster = track_cluster['Cluster'].values[0]
    no_recommendatios = 5

    recommendations = rec.recommend_songs(test_tracks_df,
                                          sample_track, train_track_cluster,
                                          no_recommendatios, conf.FEATURES)

    assert len(recommendations) == 5, "Songs in the cluster are not enough"
