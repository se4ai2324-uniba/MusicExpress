"""Script to test the data after being processed"""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')              # noqa:E402
import great_expectations as gx  # noqa:E402
from great_expectations.core.expectation_suite import ExpectationConfiguration  # noqa:E402,E501
import conf                         # noqa:E402
import great_expectations_utilities as grExpUt  # noqa:E402
# pylint: enable=wrong-import-position


# Create the Data Context
context = gx.get_context()

# Create expectation suite valid for both train and test preprocessed data
# pylint: disable=line-too-long
suite_preprocessed_data = context.add_expectation_suite(expectation_suite_name="preprocessed_data_expectations")  # noqa:E501
# pylint: enable=line-too-long

energy_inrange_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_between",
    kwargs={
        "column": "Energy",
        "max_value": 1,
        "min_value": 0,
    },
)

liveness_inrange_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_between",
    kwargs={
        "column": "Liveness",
        "max_value": 1,
        "min_value": 0,
    },
)

loudness_inrange_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_between",
    kwargs={
        "column": "Loudness",
        "max_value": 1,
        "min_value": 0,
    },
)

suite_preprocessed_data.add_expectation(grExpUt.NAME_NOTNULL_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.ARTIST_NOT_NULL_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.ENERGY_NOTNULL_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.LIVENESS_NOTNULL_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.LOUDNESS_NOTNULL_CONFIG)

suite_preprocessed_data.add_expectation(grExpUt.NAME_STRING_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.ARTIST_STRING_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.ENERGY_FLOAT_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.LIVENESS_FLOAT_CONFIG)
suite_preprocessed_data.add_expectation(grExpUt.LOUDNESS_FLOAT_CONFIG)

suite_preprocessed_data.add_expectation(energy_inrange_config)
suite_preprocessed_data.add_expectation(liveness_inrange_config)
suite_preprocessed_data.add_expectation(loudness_inrange_config)

context.save_expectation_suite(expectation_suite=suite_preprocessed_data)

# Connect to train and test data
train_validator = context.sources.pandas_default.read_csv(conf.PRO_TRAIN_SET_PATH)  # noqa:E501
test_validator = context.sources.pandas_default.read_csv(conf.PRO_TEST_SET_PATH)  # noqa:E501

# Load the expectation suite
# pylint: disable=line-too-long
preprocessed_data_suite = context.get_expectation_suite("preprocessed_data_expectations")  # noqa:E501
# pylint: enable=line-too-long

# Create validation checkpoints
train_checkpoint = context.add_or_update_checkpoint(
    name="preprocessed_train_checkpoint",
    expectation_suite_name="preprocessed_data_expectations",
    validator=train_validator
)

test_checkpoint = context.add_or_update_checkpoint(
    name="preprocessed_test_checkpoint",
    expectation_suite_name="preprocessed_data_expectations",
    validator=test_validator
)

# Validate train data
print(
    train_validator.validate(
        expectation_suite=preprocessed_data_suite,
        only_return_failures=True
    )
)

# Validate test data
print(
    test_validator.validate(
        expectation_suite=preprocessed_data_suite,
        only_return_failures=True
    )
)
