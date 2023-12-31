# Model Card

The K-Medoids model for Music Recommendation was introduced in the paper “Music Recommendation using Different Clustering Models”.

For our experiment, the Model was trained on 610 instances which are songs taken from a Spotify playlist. The model’s goal is to suggest five or more songs that align with a user’s musical preferences.

- **Authors:** Rinaldi Ivan, de Benedictis Salvatore, Sibilla Antonio, Laraspata Lucrezia
- **Model date:** 08/07/2023
- **Model version:** v1.0
- **Model type:** Music Recommendation using the K-Medoids Clustering Model
- **Useful papers:** [Music Recommendation using Different Clustering Models](https://unibari-my.sharepoint.com/:b:/g/personal/i_rinaldi4_studenti_uniba_it/EbaQjVz8KL9ClaJCLRMkJokB_fJo5hgBttinp57gU1IzIw?e=wZnMPdf)
- **License:** MIT License

## Model Description

**K-medoids**, also known as Partitioning Around Medoids (PAM), is one of the most widely used clustering algorithms. It is a variation of K-means that uses actual data points as cluster representatives or medoids. With respect to the K-Means, it is robust to outliers and works well with non-Euclidean distance metrics.

By utilizing playlists available on Spotify, song clusters are created using the K-Medoids clustering model.
For our experiment, we used the playlist «[keep grinding.](https://open.spotify.com/playlist/3fSsw9Mp5Mi2DDiweZggtP?si=151ba94cd4ca4cbb)» as the training set, and the playlist «[Spotify Most Played All Time 500Mil+](https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza#:~:text=Blinding%20Lights%20by%20The%20Weekend,at%20least%20500%20million%20streams.URL)» as the test set.

More information about the data used can be found in the [Data Card](../data/README.md) along with details about the performed Feature Selection.

The choice of the number of clusters (denoted by **k**) was made by evaluating the **Silhouette Score and two criteria**, which led us to select 5 as the optimal value for k in our experiment.

The criteria used to determine the optimal number of clusters are as follows:

- For a given **k**, all clusters should have a silhouette score higher than the average score of the dataset (represented by the red dotted line in each plot).

- Additionally, there should not be wide fluctuations in the size of the clusters (the width of the clusters in the plot represents their size).

![plot](/figures/silhouetteVisualizer.png?raw=true)

In our experiment, with k = 5, K-Medoids computed the following clusters.

Here, we can observe the clusters of the training dataset.

![plot](/figures/TrainSet_Clusters_3D.png?raw=true)

Here, instead, we can observe the clusters of the test dataset.

![plot](/figures/TestSet_Clusters_3D.png?raw=true)

Using the computed clusters, and randomly picking a song from the training set, the system suggests the 5 most similar songs from the test set, based on their features. The Euclidean Distance has been used to compute the most similar songs.

Here's an example of song suggestions provided by our model.

![plot](/figures/euclidean_distance_suggestions.png?raw=true)

## Intended use

**Primary intended uses**:

- The user can augment their playlist selection by inputting the ID of playlists they or other users have created on Spotify. Playlists created by Spotify cannot be utilized for this purpose. The extracted playlists can then function as either the training or test set for the system.

- The user selects a Spotify playlist which contains the user’s preferred songs (train set), then the model computes the clusters and suggests 5 songs picked from a selected test playlist, which are the closest in terms of song’s features to a random song previously picked from the train set. Both the train set and test set can be either default playlists or playlists extracted by the user.

**Primary intended users**:

- The model is intended to be used from whoever wants song suggestions based on their preferences.

## Metrics

We conducted user testing involving users to gather their **feedback**: each user was asked to provide feedback on the system's performance, particularly regarding song recommendations, indicating if the song suggested is liked or not.

### Experiment - User Feedback Results

Moreover, in our experiment, we solicited the opinions of only 10 users to rate the suggested songs as "Liked" or "Not Liked" based on the song used for the suggestions. Following the computed cluster and the results of this initial test.

![plot](/figures/euclideanDistanceResults.png?raw=true)

### Carbon Footprint

As suggested in the [Carbon emissions Section in Hugging Face's Model Card webpage](https://huggingface.co/docs/hub/model-cards-co2), we offer insights into our model's carbon footprint. Tracking and reporting emissions are crucial for understanding the environmental impact of our field.

We used [Code Carbon](https://github.com/mlco2/codecarbon) to track our emissions. This tool allows us to assess the environmental impact of code by estimating its carbon footprint.

```bibtex
co2_eq_emissions:
  emissions: 2.4699354187091408e-05 (in grams of CO2)
  source: Code Carbon
  geographical_location: Apulia, Italy
  hardware_used: 12th Gen Intel(R) Core(TM) i7-12650H and NVIDIA GeForce RTX 3050 6GB Laptop GPU
```

To clarify the very small value for the emissions, we reported the emissions value for a test scenario using our default dataset.

We also report the efficiency card computed on the [Energy Label website](https://energy-label.streamlit.app/Efficency_Label).

![plot](/figures/efficiency_card.jpg?raw=true)

Use the following command to access to the Code Carbon Dashboard:

```bash
carbonboard --filepath="reports\codecarbon\emissions.csv" --port=port_number
```

![plot](/figures/codecarbon_dashboard.png?raw=true)
![plot](/figures/codecarbon_dashboard_tables.png?raw=true)
