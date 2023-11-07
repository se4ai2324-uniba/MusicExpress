# Reports

## Code Quality

To ensure quality in our code, **flake8** and **pylint** were employed.

### Flake8

By running the following command, the Flake8 report will be produced denoting a cost for all the scripts in the _src_ directory.

# Examine all the scripts within a folder

```bash
flake8 src\ --format=html --htmldir=reports\flake8\
```

If you need to check the problems for only one script, use the following command (replace the folders and the script names).

# Examine a single script

```bash
flake8 folder\script_to_examine.py --format=html --htmldir=dir_to_store_html_file\
```

```bash

```

### Pylint

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
