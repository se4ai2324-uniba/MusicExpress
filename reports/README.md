# Reports

Different tools used in this project generate reports upon execution. The listed tools include:

- **codecarbon**: Checks carbon emissions during recommendation computations
- **deepchecks**: Assesses data quality and detects data drift
- **flake8**: Evaluates code quality, specifically for Python scripts
- **locust**: Performs load testing
- **pylint**: Assesses code quality for Python scripts
- **pynblint**: Evaluates code quality for Jupyter notebooks

Insights for some tools are detailed in other README files, with links provided:

- **[codecarbon](../models/README.md#carbon-footprint)**
- **[deepchecks - Data Quality Tests](../src/tests/README.md#deepchecks)**
- **[deepchecks - Data Drift Detection](../src/tests/DataDrift/README.md)**
- **[locust](../src/locust/README.md)**

Additional insights for the remaining tools, employed for **Code Quality Assessment**, including **flake8**, **pylint**, and **pynblint**, are provided below.

## Code Quality

To ensure code quality, we utilized three essential code analysis tools:

-**flake8**

-**pylint**

-**pynblint**

We chose to utilize these libraries to achieve comprehensive coverage of potential code issues.

---

### Flake8

A linting tool that checks Python code for adherence to coding standards, potential bugs, and style consistency. It ensures clean and consistent code, enhancing maintainability.

The following command will generate a Flake8 report, indicating code quality assessments for all scripts in the **src** directory.

```bash
flake8 src\ --format=html --htmldir=reports\flake8\
```

Here an example of the generated HTML report, before and after fixing the identifies issues.

![plot](/figures/flake8_before.png?raw=true)

![plot](/figures/flake8_after.png?raw=true)

Additionally, when executing the command in the terminal, a summary of all the identified issues is printed. Here's an example:

![plot](/figures/flake8_example_vscode.png?raw=true)

If you want to check issues for a single script, use the following command (replace the folders and script names accordingly).

```bash
flake8 folder\script_to_examine.py --format=html --htmldir=dir_to_store_html_file\
```

More information about this tool can be found [here](https://github.com/PyCQA/flake8).

---

### Pylint

A versatile code analysis tool that assesses Python code for adherence to coding standards, potential errors, and offers in-depth code quality assessments. It aids in maintaining code reliability and readability.

To keep a historical record of our reports, we've established the following _naming convention_ for the generated reports:

```bash
report_yyyymmdd_version_number.json
```

Here's an illustrative report, conforming to one of the previously explained _naming convention_, accompanied by a screenshot spotlighting some of the detected code issues: **_report_20231108_v1.json_**.

![plot](/figures/pylint_example.png?raw=true)

Finally, a **code quality rating** is assigned after issue detection. A terminal screenshot is provided below, showcasing the output message.

![plot](/figures/pylint_example_rating_vscode.png?raw=true)

To generate the report for a single script, use the following command (replace the folders and script names accordingly).

```bash
pylint --output-format=json:folder\name_of_your_report.json,colorized script_folder\script_to_examine.py
```

More information about this tool can be found [here](https://github.com/pylint-dev/pylint).

---

### Pynblint

A static analysis tool for Jupyter notebooks written in Python. It reveals potential notebook defects and recommends corrective actions.

You can easily run the analysis on a notebook with the following command:

```bash
pynblint path\to\notebook.ipynb -qo path/to/save/report.json
```

For the [MusicExpress notebook](../notebooks/MusicExpress.ipynb) we had to address certain issues by marking them as unsolvable. To address these issues, the exclude tag is utilized in the following manner:

```bash
pynblint MusicExpress.ipynb --exclude '["notebook-too-long", "cell-too-long", "imports-beyond-first-cell"]'
```

We run the Pynblint analysis on the [test_deepchecks notebook](../src/tests/test_deepchecks.ipynb) and on the [MusicExpress notebook](../notebooks/MusicExpress.ipynb) we show a snippet of the analysis' results at first:

![plot](/figures/pynblint_before_fix.png?raw=true)

Following the analysis on the test_deepchecks notebook, after fixing all the listed issues:

![plot](/figures/pynblint_after_fix.png?raw=true)

Here for the MusicExpress notebook:

![plot](/figures/pynblint_MusicExpress.png?raw=true)

More information about this tool can be found [here](https://github.com/collab-uniba/pynblint).

> [!TIP]
> If you're encountering notebook encoding issues when using a Colab Notebook and you are on a Windows distribution, we recommend using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install).
