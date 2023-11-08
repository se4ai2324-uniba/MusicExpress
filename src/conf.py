"""Script with shared constants for most scripts"""

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Folder in which playlists (our data) are stored
DATA_DIR = "data/raw/"
PREPRO_DATA_DIR = "data/interim/"
PRO_DATA_DIR = "data/processed/"
OUTPUT_DIR = "data/output/"

# Labels needed when creating Dataframes of the Playlists later in the code
DATAFRAMECOLUMNS = ['Name', 'Artist', 'Energy', 'Liveness', 'Loudness']

# Features to be used for clustering
FEATURES = ['Energy', 'Liveness', 'Loudness']

# List of Playlists IDs:
# "3fSsw9Mp5Mi2DDiweZggtP" # Keep grinding || Training Set
# "2YRe7HRKNRvXdJBp9nXFza" # Spotify Most Played All Time 500Mil+  || Test Set
PLAYLISTS = ["3fSsw9Mp5Mi2DDiweZggtP", "2YRe7HRKNRvXdJBp9nXFza"]

# ID and Secret of My Spotify App on Developer Spotify
SPOTIFYCLIENTID = "978d7e659f4440609a2399c869cc3e27"
SPOTIFYCLIENTSECRET = "1b160cf5acf94d44922b14c3cc5b295a"

# Instances of the main elements needed from the Spotipy library
# in order to work with playlists and tracks
AUTHMANAGER = SpotifyClientCredentials(client_id=SPOTIFYCLIENTID,
                                       client_secret=SPOTIFYCLIENTSECRET)

SP = spotipy.Spotify(auth_manager=AUTHMANAGER)

# Number of clusters to compute
NO_CLUSTER = 5

# K-Medoids Random State
RND_STATE = 42

# Number of recommendations to provide
NO_RECOMMENDATIONS = 5

TRAIN_SET_CSV_PATH = os.path.join(PREPRO_DATA_DIR, 'keep grinding..csv')
#pylint: disable=line-too-long
TEST_SET_CSV_PATH = os.path.join(PREPRO_DATA_DIR, 'Spotify\'s Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+.csv')  # noqa:E501
#pylint: enable=line-too-long
FEEDBACKUSER1_PATH = os.path.join(PREPRO_DATA_DIR, 'feedbackUser1.csv')
FEEDBACKUSER2_PATH = os.path.join(PREPRO_DATA_DIR, 'feedbackUser2.csv')

PRO_TRAIN_SET_PATH = os.path.join(PRO_DATA_DIR, 'trainSet.csv')
PRO_TEST_SET_PATH = os.path.join(PRO_DATA_DIR, 'testSet.csv')

CLUSTER_TRAIN_SET_PATH = os.path.join(OUTPUT_DIR, 'clustertrainSet.csv')
CLUSTER_TEST_SET_PATH = os.path.join(OUTPUT_DIR, 'clustertestSet.csv')

RECOMMENDATIONS_PATH = os.path.join(OUTPUT_DIR, 'recommendations.csv')

# Path to store the K-Medoids model (needed for MLFlow Model Registry)
MODEL_FILE_PATH = "models/model.pkl"
