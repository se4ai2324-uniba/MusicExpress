"""Script to test the data after extraction"""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')              # noqa:E402
import great_expectations as gx  # noqa:E402
from great_expectations.core.expectation_suite import ExpectationConfiguration  # noqa:E402,E501
import conf                         # noqa:E402
# pylint: enable=wrong-import-position

# Create the Data Context
context = gx.get_context()

# Create expectation suite valid for both train and test extracted data
# pylint: disable=line-too-long
suite = context.add_expectation_suite(expectation_suite_name="extracted_data_expectations")  # noqa:E501
# pylint: enable=line-too-long

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

context.save_expectation_suite(expectation_suite=suite)

# Connect to train and test data
train_validator = context.sources.pandas_default.read_csv(conf.TRAIN_SET_CSV_PATH)  # noqa:E501
test_validator = context.sources.pandas_default.read_csv(conf.TEST_SET_CSV_PATH)  # noqa:E501

# Load the expectation suite
extracted_data_suite = context.get_expectation_suite("extracted_data_expectations")  # noqa:E501

# Validate train data
print(
    train_validator.validate(
        expectation_suite=extracted_data_suite,
        only_return_failures=True
    )
)

# Validate test data
print(
    test_validator.validate(
        expectation_suite=extracted_data_suite,
        only_return_failures=True
    )
)
