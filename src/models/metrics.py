"""Script for computing accuracy and storing the experiment."""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import pandas as pd  # noqa:E402
import mlflow  # noqa:E402
import mlflow.sklearn  # noqa:E402
import dagshub  # noqa:E402
from joblib import load  # noqa:E402
import conf  # noqa:E402
# pylint: enable=wrong-import-position


def metrics():
    """Method to compute accuracy metric"""
    rec_songs_pred = pd.read_csv(conf.RECOMMENDATIONS_PATH)
    rec_songs_pred['Feedback'] = 1

    print("These are the systems recommendations:")
    print(rec_songs_pred)
    print("Comparison with user-liked songs in the test set")

    # pylint: disable=unused-variable
    fdbk_1 = pd.read_csv(conf.FEEDBACKUSER1_PATH)  # noqa:F841
    fdbk_2 = pd.read_csv(conf.FEEDBACKUSER2_PATH)  # noqa:F841
    # pylint: enable=unused-variable

    correct_predictions = 0

    for _, row_pred in rec_songs_pred.iterrows():
        song_name = row_pred['Name']
        artist_name = row_pred['Artist']
        label = row_pred['Feedback']

        for _, row_fbk in fdbk_1.iterrows():
            song_name_fb = row_fbk['Name']
            artist_name_fb = row_fbk['Artist']
            label_fb = row_fbk['Feedback']

            if song_name == song_name_fb and artist_name == artist_name_fb:
                if label == label_fb:
                    correct_predictions += 1

    accuracy = float(correct_predictions / conf.NO_RECOMMENDATIONS)
    print(f"Accuracy: {accuracy:.2f}")
    return accuracy


def log_experiments(accuracy):
    """Method to log the experiments on mlflow"""
    kmedoids = load(conf.MODEL_FILE_PATH)

    dagshub.init("MusicExpress", "se4ai2324-uniba", mlflow=True)

    mlflow.start_run()

    mlflow.sklearn.log_model(kmedoids, "kmedoids-model")
    mlflow.log_params({
        "no_cluster": conf.NO_CLUSTER,
        "rnd_state": conf.RND_STATE,
        'no_recommendations': conf.NO_RECOMMENDATIONS
        })
    mlflow.log_metric("Accuracy", accuracy)

    mlflow.end_run()


if __name__ == "__main__":
    model_accuracy = metrics()
    log_experiments(model_accuracy)
