"""Script with shared constants for most scripts"""
# pylint: disable=wrong-import-position
import os
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# pylint: enable=wrong-import-position

# Directory in which the project is stored
DIR_PATH = Path(__file__).resolve().parent.parent

# Folder in which playlists (our data) are stored
DATA_DIR = "data/raw/"
PREPRO_DATA_DIR = "data/interim/"
PRO_DATA_DIR = "data/processed/"
OUTPUT_DIR = "data/output/"

# Root folder in which reports are stored
REPORT_DIR = "reports/"
DEEPCHECKS_REPORT_DIR = "reports/deepchecks/"

# Folder in which Code Carbon report is stored
CODECARBON_REPORT_PATH = str(DIR_PATH) + "/reports/codecarbon/emissions.csv"

# Labels needed when creating Dataframes of the Playlists later in the code
DATAFRAMECOLUMNS = ['Name', 'Artist', 'Energy', 'Liveness', 'Loudness']

# Features to be used for clustering
FEATURES = ['Energy', 'Liveness', 'Loudness']

# List of Playlists IDs:
# "3fSsw9Mp5Mi2DDiweZggtP" # Keep grinding || Training Set
# "2YRe7HRKNRvXdJBp9nXFza" # Spotify Most Played All Time 500Mil+  || Test Set
# pylint: disable=line-too-long
PLAYLISTS = ["3fSsw9Mp5Mi2DDiweZggtP", "2YRe7HRKNRvXdJBp9nXFza"]
PLAYLISTS_NAMES = ["keep grinding.", "Spotify's Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+"]  # noqa:E501
# pylint: enable=line-too-long

# ID and Secret of My Spotify App on Developer Spotify
SPOTIFYCLIENTID = "978d7e659f4440609a2399c869cc3e27"
SPOTIFYCLIENTSECRET = "1b160cf5acf94d44922b14c3cc5b295a"
SPOTIFYUSER = "ivanrinaldi_"

# SPOTIFYCLIENTID = "f8d07e9fe54f4f599c830d69a6cf8560"
# SPOTIFYCLIENTSECRET = "63e627330a5a447aa95f894b731ef61c"
# SPOTIFYUSER = "MusicExpress"

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
# pylint: disable=line-too-long
TEST_SET_CSV_PATH = os.path.join(PREPRO_DATA_DIR, 'Spotify\'s Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+.csv')  # noqa:E501
# pylint: enable=line-too-long
FEEDBACKUSER1_PATH = os.path.join(PREPRO_DATA_DIR, 'feedbackUser1.csv')
FEEDBACKUSER2_PATH = os.path.join(PREPRO_DATA_DIR, 'feedbackUser2.csv')

PRO_TRAIN_SET_PATH = os.path.join(PRO_DATA_DIR, 'trainSet.csv')
PRO_TEST_SET_PATH = os.path.join(PRO_DATA_DIR, 'testSet.csv')

CLUSTER_TRAIN_SET_PATH = os.path.join(OUTPUT_DIR, 'clustertrainSet.csv')
CLUSTER_TEST_SET_PATH = os.path.join(OUTPUT_DIR, 'clustertestSet.csv')

RECOMMENDATIONS_PATH = os.path.join(OUTPUT_DIR, 'recommendations.csv')

# Path to store the K-Medoids model (needed for MLFlow Model Registry)
MODEL_FILE_PATH = "models/model.pkl"
