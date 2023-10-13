# Data Card

The train dataset is a Spotify playlist named “keep grinding.” that consists of 610 songs.
Here is the link to this playlist: «[keep grinding.](https://open.spotify.com/playlist/3fSsw9Mp5Mi2DDiweZggtP?si=151ba94cd4ca4cbb)».

The test dataset “Spotify Most Played All Time 500Mil+” that consists of 721 songs.
Here is the link to this playlist: «[Spotify Most Played All Time 500Mil+](https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza#:~:text=Blinding%20Lights%20by%20The%20Weekend,at%20least%20500%20million%20streams.URL)».

With this data we want to provide the users with some personalized suggestions in a large space of possible options.

The Spotipy library ([Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)) is used to extract both the songs and their features from the Spotify playlists. Here is a brief description of each feature extracted using Spotipy:

| Feature          | Description                                                          |
| ---------------- | -------------------------------------------------------------------- |
| Acousticness     | Acoustic quality of a track                                          |
| Danceability     | Suitability of a track for dancing based on various musical elements |
| Energy           | Intensity and activity level of a track                              |
| Instrumentalness | Likelihood of a track being instrumental                             |
| Liveness         | Presence of a live audience in a track                               |
| Loudness         | Overall volume of a track in decibels (dB)                           |
| Speechiness      | Presence of spoken words in a track                                  |
| Tempo            | Overall speed or pace of a track measured in beats per minute (BPM)  |

## Dataset Example

Following an example of the data that has been used.

![plot](/figures/datasetExampleShort.png?raw=true)

## Feature Selection

The **Correlation Matrix**, used to examine relationships among features, helped us in determining significant correlations among them or if they were largely independent of each other.

The goal was to identify the two features with the highest correlation and select one additional feature with the strongest correlation to the other two among the remaining features.

![plot](/figures/corrMatrixExample.png?raw=true)

Most of the features are not significantly related to each other. Following the goal‘s criteria, a subset of only three features (**Loudness, Energy, Liveness**) was adopted due to a noticeable correlation between the Loudness and Energy features and a minor correlation between both the Loudness and Energy features with the Liveness feature.
