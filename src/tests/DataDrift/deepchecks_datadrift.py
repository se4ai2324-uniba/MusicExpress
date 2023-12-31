"""Script to check data drift using deepchecks library"""

# pylint: disable=wrong-import-position
import os                                                   # noqa:E402
import sys                                                  # noqa:E402
sys.path.append('src')                                      # noqa:E402
import pandas as pd                                         # noqa:E402
from deepchecks.tabular.checks import FeatureDrift          # noqa:E402
from deepchecks.tabular.checks import MultivariateDrift     # noqa:E402
from deepchecks.tabular import Dataset                      # noqa:E402
import conf                                                 # noqa:E402
# pylint: enable=wrong-import-position

# Define the report file path
report_file_path_univariate = os.path.join(
    conf.DEEPCHECKS_REPORT_DIR, 'Drift_Univariate_report.html'
    )
report_file_path_multivariate = os.path.join(
    conf.DEEPCHECKS_REPORT_DIR, 'Drift_Multivariate_report.html'
    )

# Import Data
train_data = pd.read_csv(conf.PRO_TRAIN_SET_PATH)
test_data = pd.read_csv(conf.PRO_TEST_SET_PATH)

# Drop columns not used for Drift Detection
train_data = train_data.drop(['Artist', 'Name'], axis=1)
test_data = test_data.drop(['Artist', 'Name'], axis=1)

train_data_ds = Dataset(train_data)
test_data_ds = Dataset(test_data)

# Run Univariate Drift
check = FeatureDrift()
uni_result = check.run(
    train_dataset=train_data_ds, test_dataset=test_data_ds
    )

# Remove reports if it exists
if os.path.exists(report_file_path_univariate):
    os.remove(report_file_path_univariate)

if os.path.exists(report_file_path_multivariate):
    os.remove(report_file_path_multivariate)

# Save the report
uni_result.save_as_html(
    conf.DEEPCHECKS_REPORT_DIR + 'Drift_Univariate_report.html'
    )
print('The Univariate Drift report has been saved in reports/deepchecks.')

# Run Multivariate Drift
check = MultivariateDrift()
multi_result = check.run(
    train_dataset=train_data_ds, test_dataset=test_data_ds
    )

# Save the report
multi_result.save_as_html(
    conf.DEEPCHECKS_REPORT_DIR + 'Drift_Multivariate_report.html'
    )
print('The Multivariate Drift report has been saved in reports/deepchecks.')
