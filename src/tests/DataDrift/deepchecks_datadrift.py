"""Script to check data drift using deepchecks library"""
# pylint: disable=wrong-import-position
import os                                                   # noqa:E402
import sys                                                  # noqa:E402
import pandas as pd                                         # noqa:E402
from deepchecks.tabular.checks import FeatureDrift          # noqa:E402
from deepchecks.tabular.checks import MultivariateDrift     # noqa:E402
from deepchecks.tabular import Dataset                      # noqa:E402
current_dir = os.getcwd()
src = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, src)
import conf                                                 # noqa:E402
# pylint: enable=wrong-import-position

# Dataset
root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, root)
processed_train_data_directory = root + '/' + conf.PRO_DATA_DIR + 'trainSet.csv'    # noqa:E501
processed_test_data_directory = root + '/' + conf.PRO_DATA_DIR + 'testSet.csv'

# Selecton of Numerical Feature
df_processed_train = pd.read_csv(processed_train_data_directory)
df_processed_train = df_processed_train.drop(['Artist', 'Name'], axis=1)
df_processed_test = pd.read_csv(processed_test_data_directory)
df_processed_test = df_processed_test.drop(['Artist', 'Name'], axis=1)
ds_processed_train = Dataset(df_processed_train)
ds_processed_test = Dataset(df_processed_test)

# Univariate Drift
check = FeatureDrift()
uni_result = check.run(
    train_dataset=ds_processed_train, test_dataset=ds_processed_test
    )
report_path = root + '/reports/deepchecks/'
uni_result.save_as_html(report_path+'Drift_Univariate_report.html')
print('Univariate Drift report saved in reports/deepchecks folder')

# Multivariate Drift
check = MultivariateDrift()
multi_result = check.run(
    train_dataset=ds_processed_train, test_dataset=ds_processed_test
    )
multi_result.save_as_html(report_path+'Drift_Multivariate_report.html')
print('Multivariate Drift report saved in reports/deepchecks folder')
