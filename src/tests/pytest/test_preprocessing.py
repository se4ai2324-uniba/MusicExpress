"""Script containing Pytest tests designed for preprocessing methods"""
# pylint: disable=wrong-import-position
import io
import sys  # noqa:E402
sys.path.append('src')  # noqa:E402
import pandas as pd  # noqa:E402
import features.preprocessing as prepro
# pylint: enable=wrong-import-position


def test_remove_null_values_df():
    # Test Case 1: No null values in the 'Name' column
    df1 = pd.DataFrame({'Name': ['John', 'Alice', 'Bob']})
    result_df1 = prepro.remove_null_values_df(df1)
    assert len(result_df1) == len(df1), "No rows should be removed"

    # Test Case 2: Null values in the 'Name' column
    df2 = pd.DataFrame({'Name': ['John', 'Alice', None, 'Bob', None]})
    result_df2 = prepro.remove_null_values_df(df2)
    assert len(result_df2) == 3, "Two rows with null values should be removed"

    # Test Case 3: Empty DataFrame
    df3 = pd.DataFrame({'Name': []})
    result_df3 = prepro.remove_null_values_df(df3)
    assert len(result_df3) == 0, "No rows to remove in an empty DataFrame"


def test_min_max_normalization():
    # Test Case 1: Normalization of a single column
    data1 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    columns1 = ['A']
    result_data1 = prepro.min_max_normalization(data1, columns1)
    assert result_data1['A'].min() == 0, "Min value should be 0 after normalization"
    assert result_data1['A'].max() == 1, "Max value should be 1 after normalization"

    # Test Case 2: Normalization of multiple columns
    data2 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    columns2 = ['A', 'B']
    result_data2 = prepro.min_max_normalization(data2, columns2)
    assert result_data2['A'].min() == 0, "Min value should be 0 after normalization for column 'A'"
    assert result_data2['A'].max() == 1, "Max value should be 1 after normalization for column 'A'"
    assert result_data2['B'].min() == 0, "Min value should be 0 after normalization for column 'B'"
    assert result_data2['B'].max() == 1, "Max value should be 1 after normalization for column 'B'"

    # Test Case 3: Normalization with negative values
    data3 = pd.DataFrame({'A': [-5, -3, 0, 2, 4]})
    columns3 = ['A']
    result_data3 = prepro.min_max_normalization(data3, columns3)
    assert result_data3['A'].min() == 0, "Min value should be 0 after normalization"
    assert result_data3['A'].max() == 1, "Max value should be 1 after normalization"
