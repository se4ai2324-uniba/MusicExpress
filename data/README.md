# Data Card

> [!NOTE]
> Reminder: The song count in the playlists may vary as they are updated daily.

The train dataset is a Spotify playlist named “keep grinding.” that consists of 610 songs.
Here is the link to this playlist: «[keep grinding.](https://open.spotify.com/playlist/3fSsw9Mp5Mi2DDiweZggtP?si=151ba94cd4ca4cbb)».

The test dataset “Spotify Most Played All Time 500Mil+” that consists of 721 songs.
Here is the link to this playlist: «[Spotify Most Played All Time 500Mil+](https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza#:~:text=Blinding%20Lights%20by%20The%20Weekend,at%20least%20500%20million%20streams.URL)».

With this data we want to provide the users with some personalized suggestions in a large space of possible options.

The Spotipy library ([Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)) is used to extract both the songs and their features from the Spotify playlists. Here is a brief description of each feature extracted using Spotipy:

| Feature  | Description                                |
| -------- | ------------------------------------------ |
| Energy   | Intensity and activity level of a track    |
| Liveness | Presence of a live audience in a track     |
| Loudness | Overall volume of a track in decibels (dB) |

Additional information on extracting various features is accessible in the [Spotify API documentation](https://developer.spotify.com/documentation/web-api/reference/get-audio-features).

## Dataset Before and After Processing & Clustering

We present screenshots to provide insight into the data used in the overall process.

1. **Raw Data (After Extraction)**:
   ![plot](/figures/rawDataExample.png?raw=true)

2. **Processed Data**:
   ![plot](/figures/processedDataExample.png?raw=true)

3. **Clustered Data (Used for Recommendations)**:
   ![plot](/figures/clusteredDataExample.png?raw=true)

## Feature Selection

The **Correlation Matrix**, used to examine relationships among features, helped us in determining significant correlations among them or if they were largely independent of each other.

The objective was to select the features with the strongest correlation, with the option to include an additional feature if it demonstrates a small correlation with the already identified high-correlation features.

![plot](/figures/corrMatrixExample.png?raw=true)

Following the goal‘s criteria, all the three features (**Loudness, Energy, Liveness**) were adopted due to a noticeable correlation between the Loudness and Energy features and a minor correlation between both the Loudness and Energy features with the Liveness feature.
