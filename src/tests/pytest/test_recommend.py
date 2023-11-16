"""PyTest for recommend.py"""
# pylint: disable=wrong-import-position
import sys                      # noqa:E402
sys.path.append('src')          # noqa:E402
import pandas as pd             # noqa:E402
import conf                     # noqa:E402
import pytest                   # noqa:E402
import models.recommend as rec  # noqa:E402
# pylint: enable=wrong-import-position


def test_euclidean_distance() :
    train_tracks_df = pd.read_csv(conf.CLUSTER_TRAIN_SET_PATH)

    track_1 = train_tracks_df.iloc[0]
    track_2 = train_tracks_df.iloc[1]

    assert rec.euclidean_distance(track_1, track_2, conf.FEATURES) > 0, "Euclidean distance cannot be negative"    # noqa:E501


def test_five_recommended_songs() :
    train_tracks_df = pd.read_csv(conf.CLUSTER_TRAIN_SET_PATH)
    test_tracks_df = pd.read_csv(conf.CLUSTER_TEST_SET_PATH)

    sample_track = train_tracks_df.iloc[0]
    track_cluster = train_tracks_df[train_tracks_df['Name'] == sample_track['Name']]
    train_track_cluster = track_cluster['Cluster'].values[0]
    no_recommendatios = 5

    recommendations = rec.recommend_songs(test_tracks_df,
                                  sample_track, train_track_cluster,
                                  no_recommendatios, conf.FEATURES)

    assert len(recommendations) == 5, "Songs in the cluster are not enough"
