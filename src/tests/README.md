# Testing

To test our code, two libraries have been adopted:

- **GreatExpectations**: this library can be used to validate, document, and test data to ensure its quality and integrity throughout the data pipeline.

- **Deepchecks**: this library, on the other hand, is valuable for diagnosing and monitoring deep learning models through the various tools it offers, including those for inspecting, visualizing, and comprehending the behavior of neural networks.

## GreatExpectations

The Greatexpectations library is employed in the [test_extractData script](../tests/test_extractData.py) and [test_preprocessedData script](../tests/test_preprocessedData.py) to examine the data needed for suggesting songs to the user. To assess this data, two test suites were established:

- Test Suite: **extracted_data_expectations**

  - Involved tests:
    - **expect_column_values_to_not_be_null**
    - **expect_column_values_to_be_of_type**

- Test Suite: **preprocessed_data_expectations**
  - Involved tests:
    - **expect_column_values_to_not_be_null**
    - **expect_column_values_to_be_of_type**
    - **expect_column_values_to_be_between**

Following is a code snippet displaying the defined tests for a column in our dataset:

```
# Expectation on the values of a column to not be null
energy_notnull_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={
        "auto": True,
        "column": "Energy"
    },
)

# Expectation on the values of a column to be of a specific type
energy_float_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_of_type",
    kwargs={
        "column": "Energy",
        "type_": "float"
    },
)

# Expectation on the values of a column to be within a range of values
energy_inrange_config = ExpectationConfiguration(
    expectation_type="expect_column_values_to_be_between",
    kwargs={
        "column": "Energy",
        "max_value": 1,
        "min_value": 0,
    },
)
```

The two test suites are included in the DVC pipeline prior to the corresponding extract and preprocessing steps.

More information about this tool can be found [here](https://github.com/great-expectations/great_expectations).

## Deepchecks

The Deepchecks library is utilized in the [test_deepchecks notebook](../tests/test_deepchecks.ipynb) to evaluate the train and test data required for song recommendations. The **data_integrity** test suite was adjusted to retain only the most pertinent tests, which include:

- **Mixed Data Type**: test that checks for variations in data types within a dataset. It helps identify columns or fields that may contain a mix of different data types.

- **Mixed Nulls**: test that examines the presence of null or missing values in the dataset, specifically looking for columns where nulls are mixed with non-null values.

- **Data Duplicates**: test that assesses the dataset for duplicate records or rows. It identifies instances where identical data points appear more than once.

With the listed tests, we can better understand if our data presents issues or not and they also help us in making the data more reliable when used for song recommendations.

More information about this tool can be found [here](https://github.com/deepchecks/deepchecks/tree/main).
