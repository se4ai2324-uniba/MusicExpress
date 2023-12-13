# MusicExpress

[![python](https://img.shields.io/badge/Python-3.10.5-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![QA](https://github.com/se4ai2324-uniba/MusicExpress/actions/workflows/QA.yml/badge.svg)](https://github.com/se4ai2324-uniba/MusicExpress/actions/workflows/QA.yml)
[![Pytest](https://github.com/se4ai2324-uniba/MusicExpress/actions/workflows/test_scripts_api.yml/badge.svg)](https://github.com/se4ai2324-uniba/MusicExpress/actions/workflows/test_scripts_api.yml)
[![Pipeline](https://github.com/se4ai2324-uniba/MusicExpress/actions/workflows/Model_testing.yml/badge.svg)](https://github.com/se4ai2324-uniba/MusicExpress/actions/workflows/Model_testing.yml)

Within this repository, a Music Recommender System using the K-Medoids clustering method is presented. The goal of this system is to provide the user with personalized suggestions, taking into account their preferences in terms of songs. The number of suggestions can be decided by the users (e.g., 5 suggestions). Spotify playlists are used to compute the clusters and provide song suggestions to the user.
The user should provide a playlist with songs they like and may or may not provide a playlist from which suggestions should be made. To compute the best suggestions, a song is randomly picked from the user's preferences, and the Euclidean Distance measure is adopted to determine song recommendations, taking into account the songs' features.

The [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) library is used to extract both the songs and their features from the playlist or playlists provided by the user.

The Model and Data Cards are available here:

- [Model Card](models/README.md)
- [Data Card](data/README.md)

## Requirements

- Python 3.11.5 ([Download here](https://python.domainunion.de/downloads/release/python-3115/)) (on VS Code select the Python 3.11.5 Kernel) since there might be some problems with the scikit-learn-extra library when using Python 3.12.0

- The libraries **mlflow** and **dagshub** might be highlighted by Pylance (if installed) in the [metrics.py](src/models/metrics.py) script: this won't lead to issues when using the virtual environment to run the code

We suggest you to use a virtual environment in which you can download the requirements.

### Create a Virtual Environment

We report different ways to create a virtual environment so that if you have different versions of Python on your computer, you can easily create one without needing to look it up.

#### Standard creation

- Windows:

```bash
python -m venv your_venv_name
```

- Linux:

```bash
python3 -m venv your_venv_name
```

#### Specifc Python Version creation

```bash
path\to\the\python\version\exe\you\want\to\use -m venv your_venv_name
```

Example:

```bash
path\...\Python311\python.exe -m venv your_venv_name
```

### Activate the virtual environment

- Windows:

```bash
your_venv_name/Scripts/activate
```

```bash
your_venv_name/Scripts/activate.ps1
```

- Linux:

```bash
your_venv_name/bin/activate
```

### Installation of requirements.txt

We suggest to update pip before installing the requirements in the virtual environment. Copy the following code to update pip:

```bash
python.exe -m pip install --upgrade pip
```

After updating pip, you will need to install the requirements.txt in order for the model to work and also plot the results.
You can easily install them as follows:

```bash
pip install -r requirements.txt
```

### Reproduce DVC Pipeline

With the following instructions you will be able to run the DVC Pipeline that we developed:

```bash
# Retrieves the data needed in the pipeline from the remote storage
dvc pull -r myremote

# Runs the DVC Pipeline
dvc repro
```

## Testing

Testing is conducted within the DVC pipeline, and you can find more details about it [here](src/tests/README.md).

## Quality Assessment (QA)

Quality assessment tools have been integrated throughout the code, and you can discover further information [here](reports/README.md).

## API

API have been integrated, and you can discover further information [here](src/api/README.md).

## Github Actions

Github Actions has been integrated, and you can discover further information [here](.github/workflows/README.md).

## Docker

Docker has been integrated, and you can discover further information [here](docker/README.md).

## GreenAI - Code Carbon

Code Carbon has been integrated, and you can discover further information in the last section of our [Model Card](models/README.md).

## Citation

```bibtex
@misc{MusicRecommendationUsingClusters,
author = {Rinaldi Ivan and, de Benedictis Salvatore and, Sibilla Antonio and, Laraspata Lucrezia},
title = {Music Recommendation using the K-Medoids Clustering Model},
month = {October},
year = {2023},
url = {https://github.com/se4ai2324-uniba/MusicExpress}
}
```

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README of the repository
    │
    ├── .dvc               <- DVC files
    │
    ├── .github
    │   └── workflows      <- Github actions
    │
    ├── data
    │   ├── external       <- Data from third party sources
    │   ├── interim        <- Data before processing
    │   ├── output         <- Data after clustering and song recommendations
    │   ├── processed      <- Processed data, ready to be used for clustering
    │   └── raw            <- The original, immutable data dump
    │
    ├── docker             <- Docker files
    │   └── Dockerfile     <- Docker image of our system (interact with API)
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebook providing an overview of code and the Spotipy library
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc
    │   ├── codecarbo      <- Codecarbon generated emission report
    │   ├── deepchecks     <- Deepchecks generated HTML pages for data integrity
    │   ├── figures        <- Generated graphics and figures to be used in reporting
    │   ├── flake8         <- Flake8 generated HTML page for quality assessment (QA)
    │   ├── pylint         <- Pylint reports for quality assessment (QA)
    │   └── pynblint       <- Pynblint reports for quality assessment (QA)
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├
    ├── src                <- Source code for use in this project
    │   │
    │   ├── api            <- Scripts containing API endpoints
    │   │   └── main.py
    │   │   └── schemas.py
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── extract_data.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── preprocessing.py
    │   │
    │   ├── models         <- Scripts to train the model and then use the trained model to make
    │   │   │                 suggestions
    │   │   ├── clustering.py
    │   │   ├── recommend.py
    │   │   └── metrics.py
    │   │
    │   ├── tests          <- Test scripts
    │   │   ├── pytest
    │   │   │   │
    │   │   │   ├── test_api.ipynb
    │   │   │   ├── test_files_utilities.ipynb
    │   │   │   ├── test_preprocessing.ipynb
    │   │   │   ├── test_recommend.ipynb
    │   │   │   └── test_spotipy_utilities.ipynb
    │   │   │
    │   │   ├── test_deepchecks.ipynb
    │   │   ├── test_extract_data.py
    │   │   └── test_preprocessed_data.py
    │   │
    │   │── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │
    │   │── conf.py                             <- Variables used in all the other scripts
    │   │── files_utilities.py                  <- Methods for file operations
    │   │── great_expectations_utilities.py     <- Methods for file operations
    │   └── spotipy_utilities.py                <- Methods that make use of Spotipy features
    │
    ├── compose.yaml       <- Docker-compose file
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
