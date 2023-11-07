# Reports

## Code Quality

To ensure code quality, we utilized three essential code analysis tools:

-**flake8**

-**pylint**

-**pynblint**

### Flake8

A linting tool that checks Python code for adherence to coding standards, potential bugs, and style consistency. It ensures clean and consistent code, enhancing maintainability. More information about this tool can be found [here](https://github.com/PyCQA/flake8).

Running the following command will generate a Flake8 report, indicating code quality assessments for all scripts in the **src** directory.

# Examine all the scripts within a folder

```bash
flake8 src\ --format=html --htmldir=reports\flake8\
```

If you want to check issues for a single script, use the following command (replace the folders and script names accordingly).

# Examine a single script

```bash
flake8 folder\script_to_examine.py --format=html --htmldir=dir_to_store_html_file\
```

### Pylint

A versatile code analysis tool that assesses Python code for adherence to coding standards, potential errors, and offers in-depth code quality assessments. It aids in maintaining code reliability and readability. More information about this tool can be found [here](https://github.com/pylint-dev/pylint).

To generate the report for a single script, use the following command (replace the folders and script names accordingly).

```bash
pylint --output-format=json:folder\name_of_your_report.json,colorized script_folder\script_to_examine.py
```

To maintain a historical record of our reports, we've adopted the following naming convention:

```bash
report_clustering_yyyymmdd.json
```

An example of a report that follows this naming convention is:

```bash
report_clustering_20231104.json
```

### Pynblint

A static analysis tool for Jupyter notebooks written in Python. It reveals potential notebook defects and recommends corrective actions. More information about this tool can be found [here](https://github.com/collab-uniba/pynblint).

We strongly recommend to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) if on a Windows distribution.
After initiazling the WSL bash with the **bash** command, you can easily run the analysis on the notebook as follows:

```bash
pynblint notebooks/MusicExpress.ipynb
```
