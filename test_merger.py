import pytest
from merger import merge_lists

@pytest.fixture
def sample_lists():
    return [1, 2], ['a', 'b'], [3]

@pytest.fixture
def empty_lists():
    return [], [], []

def test_merge_normal(sample_lists):
    result = merge_lists(*sample_lists)
    assert result == [1, 2, 'a', 'b', 3]

def test_merge_empty(empty_lists):
    assert merge_lists(*empty_lists) == []

@pytest.mark.parametrize("input_lists, expected", [
    (([1], ['a'], []), [1, 'a']),
    (([], [], []), []),
    (([1, 2], [3], [4, 5]), [1, 2, 3, 4, 5])
])
def test_parametrized(input_lists, expected):
    assert merge_lists(*input_lists) == expected