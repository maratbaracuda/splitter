import pytest
from splitter import split_names_ages

@pytest.fixture
def sample_data():
    return [('Alice', 30), ('Bob', 25), ('Charlie', 40)]

@pytest.fixture
def empty_data():
    return []

def test_split_names_ages(sample_data):
    names, ages = split_names_ages(sample_data)
    assert names == ['Alice', 'Bob', 'Charlie']
    assert ages == [30, 25, 40]

def test_empty_list(empty_data):
    names, ages = split_names_ages(empty_data)
    assert names == []
    assert ages == []

@pytest.mark.parametrize("input_data, expected_names, expected_ages", [
    ([('Eve', 20)], ['Eve'], [20]),
    ([], [], []),
    ([('A', 1), ('B', 2)], ['A', 'B'], [1, 2])
])
def test_parametrized(input_data, expected_names, expected_ages):
    names, ages = split_names_ages(input_data)
    assert names == expected_names
    assert ages == expected_ages