import os
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# Folder in which playlists (our data) are stored
data_dir = "data/raw/"
prepro_data_dir = "data/interim/"
pro_data_dir = "data/processed/"
output_dir = "data/output/"

# Columns' Labels needed when creating Dataframes of the Playlists later in the code
dataframeColumns = ['Name','Energy', 'Liveness', 'Loudness']

# Features to be used for clustering
features = ['Energy', 'Liveness', 'Loudness']

# List of Playlists IDs:
# "3fSsw9Mp5Mi2DDiweZggtP" # Keep grinding || Training Set
# "2YRe7HRKNRvXdJBp9nXFza" # Spotify Most Played All Time 500Mil+  || Test Set
playlists = [ "3fSsw9Mp5Mi2DDiweZggtP", "2YRe7HRKNRvXdJBp9nXFza"]

# ID and Secret of My Spotify App on Developer Spotify
spotifyClientId = "978d7e659f4440609a2399c869cc3e27"
spotifyClientSecret = "1b160cf5acf94d44922b14c3cc5b295a"

# Instances of the main elements needed from the Spotipy library in order to work with playlists and tracks
authManager = SpotifyClientCredentials(client_id = spotifyClientId, client_secret = spotifyClientSecret)
sp = spotipy.Spotify(auth_manager = authManager)

# Number of clusters to compute
no_cluster = 5

# K-Medoids Random State
rnd_state = 42

# Number of recommendations to provide
no_recommendations = 5

train_set_csv_path = os.path.join(prepro_data_dir, 'keep grinding..csv')
test_set_csv_path = os.path.join(prepro_data_dir, 'Spotify\'s Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+.csv')
feedbackUser1_path = os.path.join(prepro_data_dir, 'feedbackUser1.csv')
feedbackUser2_path = os.path.join(prepro_data_dir, 'feedbackUser2.csv')

pro_train_set_path = os.path.join(pro_data_dir, 'trainSet.csv')
pro_test_set_path = os.path.join(pro_data_dir, 'testSet.csv')

cluster_train_set_path = os.path.join(output_dir, 'clustertrainSet.csv')
cluster_test_set_path = os.path.join(output_dir, 'clustertestSet.csv')

recommendations_path = os.path.join(output_dir, 'recommendations.csv')

# Path to store the K-Medoids model (needed for MLFlow Model Registry)
model_file_path = "models/model.pkl"

