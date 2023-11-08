"""Script with shared test cases"""

# pylint: disable=wrong-import-position
from great_expectations.core.expectation_suite import ExpectationConfiguration  # noqa:E402,E501
# pylint: enable=wrong-import-position


NAME_NOTNULL_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Name"
    },
)

ARTIST_NOT_NULL_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Artist"
    },
)

ENERGY_NOTNULL_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Energy"
    },
)

LIVENESS_NOTNULL_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Liveness"
    },
)

LOUDNESS_NOTNULL_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Loudness"
    },
)

NAME_STRING_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Name",
        "type_": "str"
    },
)

ARTIST_STRING_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Artist",
        "type_": "str"
    },
)

ENERGY_FLOAT_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Energy",
        "type_": "float"
    },
)

LIVENESS_FLOAT_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Liveness",
        "type_": "float"
    },
)

LOUDNESS_FLOAT_CONFIG = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Loudness",
        "type_": "float"
    },
)
