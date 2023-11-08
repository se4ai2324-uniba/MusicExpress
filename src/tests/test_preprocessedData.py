"""Script to test the data after being processed"""

import sys
sys.path.append('src')              # noqa:E402
import great_expectations as gx
from great_expectations.core.expectation_suite import ExpectationConfiguration
import conf                         # noqa:E402


# ================= Great Expectation - Preprocessed data =================

# Create the Data Context
context = gx.get_context()

# Create expectation suite valid for both train and test preprocessed data
suite = context.add_expectation_suite(expectation_suite_name="preprocessed_data_expectations")  # noqa:E501

name_notnull_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Name"
    },
)

artist_notnull_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Artist"
    },
)

energy_notnull_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Energy"
    },
)

liveness_notnull_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Liveness"
    },
)

loudness_notnull_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Loudness"
    },
)

name_string_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Name",
        "type_": "str"
    },
)

artist_string_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Artist",
        "type_": "str"
    },
)

energy_float_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Energy",
        "type_": "float"
    },
)

liveness_float_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Liveness",
        "type_": "float"
    },
)

loudness_float_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Loudness",
        "type_": "float"
    },
)

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

suite.add_expectation(name_notnull_config)
suite.add_expectation(artist_notnull_config)
suite.add_expectation(energy_notnull_config)
suite.add_expectation(liveness_notnull_config)
suite.add_expectation(loudness_notnull_config)

suite.add_expectation(name_string_config)
suite.add_expectation(artist_string_config)
suite.add_expectation(energy_float_config)
suite.add_expectation(liveness_float_config)
suite.add_expectation(loudness_float_config)

suite.add_expectation(energy_inrange_config)
suite.add_expectation(liveness_inrange_config)
suite.add_expectation(loudness_inrange_config)

context.save_expectation_suite(expectation_suite=suite)

# Connect to train and test data
train_validator = context.sources.pandas_default.read_csv(conf.PRO_TRAIN_SET_PATH)  # noqa:E501
test_validator = context.sources.pandas_default.read_csv(conf.PRO_TEST_SET_PATH)  # noqa:E501

# Load the expectation suite
preprocessed_data_suite = context.get_expectation_suite("preprocessed_data_expectations")  # noqa:E501

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
