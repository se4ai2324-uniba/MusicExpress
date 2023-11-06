import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import conf  # noqa:E402
import pandas as pd  # noqa:E402
import mlflow  # noqa:E402
import mlflow.sklearn  # noqa:E402
import dagshub  # noqa:E402
from joblib import load  # noqa:E402

# ================================ Metrics ================================

recSongs_pred = pd.read_csv(conf.recommendations_path)
recSongs_pred['Feedback'] = 1

print("These are the systems recommendations:")
print(recSongs_pred)
print("Comparison with user-liked songs in the test set")

fdbk1 = pd.read_csv(conf.feedbackUser1_path)
fdbk2 = pd.read_csv(conf.feedbackUser2_path)

correct_predictions = 0

for _, row_pred in recSongs_pred.iterrows():

    song_name = row_pred['Name']
    artist_name = row_pred['Artist']
    label = row_pred['Feedback']

    for _, row_fbk in fdbk1.iterrows():

        song_name_fb = row_fbk['Name']
        artist_name_fb = row_fbk['Artist']
        label_fb = row_fbk['Feedback']

        if song_name == song_name_fb and artist_name == artist_name_fb:

            if label == label_fb:
                correct_predictions += 1

accuracy = float(correct_predictions / conf.no_recommendations)

print(f"Accuracy: {accuracy:.2f}")

kmedoids = load(conf.model_file_path)

dagshub.init("MusicExpress", "se4ai2324-uniba", mlflow=True)

mlflow.start_run()

mlflow.sklearn.log_model(kmedoids, "kmedoids-model")
mlflow.log_params({
    "no_cluster": conf.no_cluster,
    "rnd_state": conf.rnd_state,
    'no_recommendations': conf.no_recommendations
})
mlflow.log_metric("Accuracy", accuracy)

mlflow.end_run()
