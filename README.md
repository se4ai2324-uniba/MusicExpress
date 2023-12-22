# MusicExpress

[![python](https://img.shields.io/badge/Python-3.11.5-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11.6-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
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

- Python 3.11.5 ([Download here](https://python.domainunion.de/downloads/release/python-3115/)) or even 3.11.6 (on VS Code select the correct Python Kernel) since there might be some problems with the _scikit-learn-extra_ library when using Python 3.12.0

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

## Integrated Tools

In this project, we've seamlessly integrated a variety of tools, each designed for specific tasks. For detailed information about each tool, please refer to the following list:

- **[Testing](src/tests/README.md)**: GreatExpectations, Deepchecks and Pytest
- **[Quality Assessment (QA)](reports/README.md)**: Pylint, Pynblint and Flake8
- **[API](src/api/README.md)**: FastAPI
- **[Automated Workflows](.github/workflows/README.md)**: Github Actions
- **[Containerization](docker/README.md)**: Docker
- **[GreenAI](models/README.md)**: Code Carbon (details are in the last section of the linked README)
- **[Performance & Load Testing](src/locust/README.md)**: Locust
- **[Resource & Performance Monitoring](src/api/README.md)**: Prometheus and Grafana (details are in the last section of the linked README)
- **[Data Drifts Monitoring](src/tests/DataDrift/README.md)**: Deepchecks

## Cloud Deployment

We selected Azure as cloud provider to deploy our services, available [here](musicexpress.azurewebsites.net).

## Uptime Monitoring

We use **Better Uptime** to monitor the status of our website. Check the current status at [our status page](https://musicexpress.betteruptime.com/).

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
    │   │
    │   └── workflows      <- Github actions
    │
    ├── data
    │   │
    │   ├── external       <- Data from third party sources
    │   ├── interim        <- Data before processing
    │   ├── output         <- Data after clustering and song recommendations
    │   ├── processed      <- Processed data, ready for clustering
    │   └── raw            <- The original, immutable data dump
    │
    ├── docker             <- Docker files
    │   │
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
    │   │
    │   ├── codecarbon     <- Codecarbon emission report
    │   ├── deepchecks     <- Deepchecks HTML pages for data integrity
    │   ├── figures        <- Generated graphics and figures to be used in reporting
    │   ├── flake8         <- Flake8 HTML page for quality assessment (QA)
    │   ├── pylint         <- Pylint reports for quality assessment (QA)
    │   └── pynblint       <- Pynblint reports for quality assessment (QA)
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    ├
    ├── src                <- Project's source code
    │   │
    │   ├── api            <- Scripts related to API
    │   │   │
    │   │   ├── main.py         <- API endpoints
    │   │   ├── monitoring.py   <- Additional Prometheus metrics
    │   │   └── schemas.py      <- API utilities
    │   │
    │   ├── data           <- Scripts to download or extract data
    │   │   │
    │   │   └── extract_data.py
    │   │
    │   ├── features       <- Scripts to process raw data
    │   │   │
    │   │   └── preprocessing.py
    │   │
    │   ├── locust         <- Scripts to run Locust performance and load tests
    │   │   │
    │   │   └── locustfile.py
    │   │
    │   ├── models         <- Scripts to train the model, make suggestions, and compute metrics
    │   │   │
    │   │   ├── clustering.py   <- Scrip to cluster data
    │   │   ├── recommend.py    <- Scrip to compute song recommendations
    │   │   └── metrics.py      <- Scrip to compute metrics
    │   │
    │   ├── tests          <- Test scripts
    │   │   │
    │   │   ├── datadrift
    │   │   │   │
    │   │   │   └── deepchecks_datadrift.ipynb  <- Deepchecks data drift monitoring
    │   │   │
    │   │   ├── pytest
    │   │   │   │
    │   │   │   ├── test_api.py
    │   │   │   ├── test_files_utilities.py
    │   │   │   ├── test_preprocessing.py
    │   │   │   ├── test_recommend.py
    │   │   │   └── test_spotipy_utilities.py
    │   │   │
    │   │   ├── test_deepchecks.ipynb           <- Deepchecks data inspection tests
    │   │   ├── test_extract_data.py            <- GreatExpectations test on extract_data.py
    │   │   └── test_preprocessed_data.py       <- GreatExpectations test on preprocessed_data.py
    │   │
    │   │── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │
    │   │── conf.py                             <- Variables used in all the other scripts
    │   │── files_utilities.py                  <- Methods for file operations
    │   │── great_expectations_utilities.py     <- Methods for file operations
    │   └── spotipy_utilities.py                <- Methods that make use of Spotipy features
    │
    ├── compose.yaml       <- Docker-compose file
    ├── prometheus.yaml    <- Prometheus config file
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
