# Reports

## Code Quality

To ensure code quality, we utilized three essential code analysis tools:

-**flake8**

-**pylint**

-**pynblint**

We chose to utilize these libraries to achieve comprehensive coverage of potential code issues.

### Flake8

---

A linting tool that checks Python code for adherence to coding standards, potential bugs, and style consistency. It ensures clean and consistent code, enhancing maintainability. More information about this tool can be found [here](https://github.com/PyCQA/flake8).

The following command will generate a Flake8 report, indicating code quality assessments for all scripts in the **src** directory.

```bash
flake8 src\ --format=html --htmldir=reports\flake8\
```

Here an example of the genertaed HTML report, before and after fixing the identifies issues.

![plot](/figures/flake8_before.png?raw=true)

![plot](/figures/flake8_after.png?raw=true)

If you want to check issues for a single script, use the following command (replace the folders and script names accordingly).

```bash
flake8 folder\script_to_examine.py --format=html --htmldir=dir_to_store_html_file\
```

Additionally, when executing the command in the terminal, a summary of all the identified issues is printed. Here's an example:

![plot](/figures/flake8_example_vscode.png?raw=true)

### Pylint

---

A versatile code analysis tool that assesses Python code for adherence to coding standards, potential errors, and offers in-depth code quality assessments. It aids in maintaining code reliability and readability. More information about this tool can be found [here](https://github.com/pylint-dev/pylint).

To generate the report for a single script, use the following command (replace the folders and script names accordingly).

```bash
pylint --output-format=json:folder\name_of_your_report.json,colorized script_folder\script_to_examine.py
```

To keep a historical record of our reports, we've established the following naming conventions:

Naming Convention for Individual Script Reports:

```bash
report_script_name_yyyymmdd.json
```

Naming Convention for Folder Reports:

```bash
report_yyyymmdd_version_number.json
```

Here's an illustrative report, conforming to one of the previously explained naming conventions, accompanied by a screenshot spotlighting some of the detected code issues:

```bash
report_20231108_v1.json
```

![plot](/figures/pylint_example.png?raw=true)

Finally, a code quality rating is assigned after issue detection. We've achieved a rating of 10/10 for our code. Here's a terminal screenshot as proof:

![plot](/figures/pylint_example_rating_vscode.png?raw=true)

### Pynblint

---

A static analysis tool for Jupyter notebooks written in Python. It reveals potential notebook defects and recommends corrective actions. More information about this tool can be found [here](https://github.com/collab-uniba/pynblint).

If you're using a Windows distribution and encountering notebook encoding issues, we recommend using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

You can easily run the analysis on a notebook with the following command:

```bash
pynblint path\to\notebook.ipynb
```

We run the Pynblint analysis on the [test_deepchecks notebook](../src/tests/test_deepchecks.ipynb) and we show a snippet of the analysis' results at first:

![plot](/figures/pynblint_before_fix.png?raw=true)

After fixing all the listed issues, the analysis' results should be as follows:

![plot](/figures/pynblint_after_fix.png?raw=true)
