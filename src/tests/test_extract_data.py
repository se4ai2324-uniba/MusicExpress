"""Script to test the data after extraction"""

# pylint: disable=wrong-import-position
import sys  # noqa:E402
sys.path.append('src')              # noqa:E402
import great_expectations as gx  # noqa:E402
import conf                         # noqa:E402
import great_expectations_utilities as grExpUt  # noqa:E402
# pylint: enable=wrong-import-position

# Create the Data Context
context = gx.get_context()

# Create expectation suite valid for both train and test extracted data
# pylint: disable=line-too-long
suite_extract_data = context.add_expectation_suite(expectation_suite_name="extracted_data_expectations")  # noqa:E501
# pylint: enable=line-too-long

suite_extract_data.add_expectation(grExpUt.NAME_NOTNULL_CONFIG)
suite_extract_data.add_expectation(grExpUt.ARTIST_NOT_NULL_CONFIG)
suite_extract_data.add_expectation(grExpUt.ENERGY_NOTNULL_CONFIG)
suite_extract_data.add_expectation(grExpUt.LIVENESS_NOTNULL_CONFIG)
suite_extract_data.add_expectation(grExpUt.LOUDNESS_NOTNULL_CONFIG)

suite_extract_data.add_expectation(grExpUt.NAME_STRING_CONFIG)
suite_extract_data.add_expectation(grExpUt.ARTIST_STRING_CONFIG)
suite_extract_data.add_expectation(grExpUt.ENERGY_FLOAT_CONFIG)
suite_extract_data.add_expectation(grExpUt.LIVENESS_FLOAT_CONFIG)
suite_extract_data.add_expectation(grExpUt.LOUDNESS_FLOAT_CONFIG)

context.save_expectation_suite(expectation_suite=suite_extract_data)

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
