# Github Actions

**GitHub Actions** is a tool integrated with GitHub for **continuous integration and delivery (CI/CD)**.
It allows to **automate tasks** like testing and checking the quality of the code **directly within a GitHub repository**.

## Our Actions

We defined **five different actions**, each activated under certain conditions:

1. [Quality Assessment (QA)](QA.yml)

   - **Trigger**: On changes to the src folder
   - **Actions**: Runs Pylint in the src folder
   - **Criteria**: Fails if the Pylint quality score is below 8

2. [API and Scripts Testing](test_scripts_api.yml):

   - **Trigger**: On changes to specific src sub-folders (_api, tests, data, features, models_)
   - **Actions**: Runs Pytest tests to verify proper functionality
   - **Purpose**: Ensures everything works correctly in the specified sub-folders

3. [Model Testing](Model_testing.yml):

   - **Trigger**: On changes to specific src sub-folders (_data, features, models_)
   - **Actions**: Executes main pipeline steps to validate system integrity post-changes
   - **Purpose**: Confirm that the system doesn't fail after changes

4. [Production Deployment](azure_deploy_main.yml):

   - **Trigger**: On push onto _main_ branch
   - **Actions**: Builds a Docker image and deploys it on Azure
   - **Purpose**: Continous Deployment of the MusicExpress's production version

5. [Staging Deployment](azure_deploy_staging.yml):

   - **Trigger**: On push onto _staging_ branch
   - **Actions**: Builds a Docker image and deploys it on Azure
   - **Purpose**: Continous Deployment of the MusicExpress's staging version

6. [Data Drift Detection](datadrift_scan.yml):
   - **Trigger**: On push onto _src/tests/DataDrift/_ and _data/raw/_ folders
   - **Actions**: Checks for Data Drift in the default data and stores a report
   - **Purpose**: Check if there are differences among the two datasets

DVC has been utilized to retrieve the required data within the following actions:

- [API and Scripts Testing](test_scripts_api.yml)
- [Model Testing](Model_testing.yml)
- [Production Deployment](azure_deploy_main.yml)
- [Staging Deployment](azure_deploy_staging.yml)
- [Data Drift Detection](datadrift_scan.yml)

Within each action different jobs can be defined. Those are run in parallel allowing us to check different things at the same time. For example, in the [API and Scripts Testing](test_scripts_api.yml) we check that the tests for our API and the ones for our Python scripts still work thanks to two different jobs named, respectively, _api-testing_ and _scripts-testing_.
