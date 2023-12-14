"""Script for data clustering processed data"""

# pylint: disable=wrong-import-position
import sys                                          # noqa:E402
sys.path.append('src')                              # noqa:E402
import time                                         # noqa:E402
from locust import HttpUser, task, between, tag     # noqa:E402
# pylint: enable=wrong-import-position


DEFAULT_PLAYLIST_PAYLOAD = {"id_playlist_train": "",
                            "id_playlist_test": ""}

USER_PLAYLIST_PAYLOAD = {"id_playlist_train": "2zBDRrXmYP3FDJ6NSVUFHT",
                         "id_playlist_test": "0M30TrJrlMHl8kjECKYPg0"}


class DefaultUser(HttpUser):
    """Class to run default users' behaviours"""
    wait_time = between(1, 5)

    @tag('index', 'default_user')
    @task(1)
    def root_endpoint(self):
        """Root endpoint behaviour"""
        self.client.get("/")

    @tag('default_scenario', 'default_user')
    @task(2)
    def extract_data_default(self):
        """Extract default data behaviour"""
        self.client.post("/extract", json=DEFAULT_PLAYLIST_PAYLOAD)
        time.sleep(5)

    @tag('default_scenario', 'default_user')
    @task(3)
    def get_recommendations_default(self):
        """Get recommendations using default data behaviour"""
        self.client.post("/recommendation", json=DEFAULT_PLAYLIST_PAYLOAD)
        time.sleep(5)


class PersonalizedUser(HttpUser):
    """Class to run personalized users' behaviours"""
    wait_time = between(1, 5)

    @tag('index', 'personalized_user')
    @task(1)
    def root_endpoint(self):
        """Root endpoint behaviour"""
        self.client.get("/")

    @tag('user_scenario', 'personalized_user')
    @task(3)
    def extract_data(self):
        """Extract user data behaviour"""
        self.client.post("/extract", json=USER_PLAYLIST_PAYLOAD)
        time.sleep(5)

    @tag('user_scenario', 'personalized_user')
    @task(4)
    def get_recommendations(self):
        """Get recommendations using user data behaviour"""
        self.client.post("/recommendation", json=USER_PLAYLIST_PAYLOAD)
        time.sleep(5)
