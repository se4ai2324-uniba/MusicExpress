# Locust

**Locust** is a Python library for **performance testing** and **load testing** of web applications. It allows users to define user behaviour, simulate virtual users (locusts), and generate load on a target system to assess its performance under various conditions.

## How to run Locust

First, install the Locust library by running the following command:

```bash
pip install locust
```

Once the library is installed, create a Python script and import the necessary elements from Locust:

- **HttpUser**: virtual user for load testing web applications;
- **task**: decorator to define tasks that a virtual user performs during a test;
- **tag**: decorator to categorize tasks with metadata for better result analysis;
- **between**: function to set a random wait time between tasks, simulating user think time.

You can easily import those elements with the following command:

```bash
from locust import HttpUser, task, between, tag
```

The following snippet of code is taken directly from our [locusfile.py](locustfile.py) and serves as an example of the usage of those elements:

```bash
DEFAULT_PLAYLIST_PAYLOAD = {"id_playlist_train": "", "id_playlist_test": ""}

@tag('default_scenario', 'default_user')
@task(2)
def extract_data_default(self):
    """Extract default data behaviour"""
    self.client.post("/extract", json=DEFAULT_PLAYLIST_PAYLOAD)
    time.sleep(5)
```

When Locust is run, the task in the code snippet sends requests to the _/extract_ endpoint using default data.

You can easily run Locust by running the following command in the directory in which your locustfile.py is located:

```bash
locust
```

After executing this command, a UI will be accessible at the following URL: **http://localhost:8089**.

Within this UI, you need to specify the number of users, the time required to spawn users, and the host to be monitored.

![plot](/figures/locust_settings_ui.png?raw=true)

Here's an example of a Locust run, along with charts displaying the corresponding results.

![plot](/figures/locust_ui_example.png?raw=true)
![plot](/figures/locust_run_example.png?raw=true)

## Conducted Tests

We conducted tests to assess the scalability of our [website](https://stagingmusicexpress.azurewebsites.net) and encountered a limitation related to the maximum number of requests allowed by Spotify's API.

> [!CAUTION]
> As outlined in the [Spotify for Developer - Rate Limits webpage](https://developer.spotify.com/documentation/web-api/concepts/rate-limits):
> _Spotify's API rate limit is calculated based on the number of calls that your app makes to Spotify in a rolling 30 second window. If your app exceeds the rate limit for your app then you'll begin to see 429 error responses from Spotify's Web API, and you may hear from users about unexpected behavior that they have noticed while using your app. The limit varies depending on whether your app is in development mode or extended quota mode._

Unfortunately, we are unable to request the **_extended quota mode_** for university projects, and we were only able to perform 2 out of the 3 tests we designed:

![plot](/figures/locust_tests_table.png?raw=true)

During the last test (the one in the table that has the orange background), we consistently got blocked from Spotify after some time elapsed, preventing us from obtaining additional results.

We stored the Locust reports for the initial two tests in the **reports/locust/** folder, and the links to access them are provided below:

- **[Base Scenario Report](../../reports/locust/base_scenario_report.html)**
- **[Moderate Scenario Report](../../reports/locust/moderate_scenario_report.html)**
