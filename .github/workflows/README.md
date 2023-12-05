# Github Actions

**GitHub Actions** is a tool integrated with GitHub for **continuous integration and delivery (CI/CD)**.
It allows to **automate tasks** like testing and checking the quality of the code **directly within a GitHub repository**.

## Our Actions

We defined **three different actions**, each activated under certain conditions:

1. [Quality Assessment (QA)](QA.yml)
   - **Trigger**: On changes to the src folder
   - **Actions**: Runs Pylint in the src folder
   - **Criteria**: Fails if the Pylint quality score is below 8
2. [API and Scripts Testing](test_scripts_api.yml):

   - **Trigger**: On changes to specific src sub-folders (_api, tests, data, features, models_)
   - **Actions**: Runs Pytest tests to verify proper functionality
   - **Purpose**: Ensures everything works correctly in the specified sub-folders

3. [Model Testing](model_testing.yml):
   - **Trigger**: On changes to specific src sub-folders (_data, features, models_)
   - **Actions**: Executes main pipeline steps to validate system integrity post-changes
   - **Purpose**: Confirm that the system doesn't fail after changes

DVC has been utilized to retrieve the required data within the [API and Scripts Testing](test_scripts_api.yml) and [Model Testing](model_testing.yml) actions.

Within each action different jobs can be defined. Those are run in parallel allowing us to check different things at the same time. For example, in the [API and Scripts Testing](test_scripts_api.yml) we check that the tests for our API and the ones for our Python scripts still work thanks to two different jobs named, respectively, _api-testing_ and _scripts-testing_.
