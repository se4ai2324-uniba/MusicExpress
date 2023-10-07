# Model Card

The K-Medoids model for Music Recommendation was introduced in the paper “Music Recommendation using Different Clustering Models”.

The Model was trained on 610 instances which are songs taken from a Spotify playlist. The model’s goal is to suggest five or more songs that align with a user’s musical preferences.

- **Authors:** Rinaldi Ivan, de Benedictis Salvatore, Sibilla Antonio, Laraspata Lucrezia
- **Model date:** 08/07/2023
- **Model version:** v1.0
- **Model type:** Music Recommendation using Different Clustering Models
- **Useful papers:** [Music Recommendation using Different Clustering Models](https://unibari-my.sharepoint.com/:b:/g/personal/i_rinaldi4_studenti_uniba_it/EbaQjVz8KL9ClaJCLRMkJokB_fJo5hgBttinp57gU1IzIw?e=wZnMPdf)
- **License:** MIT License

## Model Description

**K-medoids**, also known as Partitioning Around Medoids (PAM), is one of the most widely used clustering algorithms. It is a variation of K-means that uses actual data points as cluster representatives or medoids. With respect to the K-Means, it is robust to outliers and works well with non-Euclidean distance metrics.

By utilizing playlists available on Spotify, song clusters are created using the K-Medoids clustering model.

The choice of the number of clusters (denoted by **k**) was performed evaluating the Silhouette Score, which led to choose 5 as the optimal value for k.

This value has been chosen given the following criteria:

- For a given **k**, all clusters should have a silhouette score higher than the average score of the dataset (represented by the red dotted line in each plot).

- Additionally, there should not be wide fluctuations in the size of the clusters (the width of the clusters in the plot represents their size).

![plot](./figures/silhouetteVisualizer.png?raw=true)

Using the computed clusters, and randomly picking a song from the training set, the system suggests the 5 (or more) most similar songs from the test set, based on their features.

## Intended use

**Primary intended uses**:

- The user selects a Spotify playlist which contains the user’s preferred songs (train set), then the model computes the clusters and suggests k songs picked from the test playlist, which are the closest in terms of song’s features to a random song previously picked from the train set.

- The user selects two Spotify playlist. The first playlist contains the user’s preferred songs (train set), the second playlist (test set) contains the songs from which the model must suggest k songs.

**Primary intended users**:

- The model is intended to be used from whoever wants song suggestions based on their preferences.

## Metrics

We conducted user testing involving users to gather their **feedback**: each user was asked to provide feedback on the system's performance, particularly regarding song recommendations, indicating if the song suggested is liked or not.
