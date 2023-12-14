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
