import pytest
from Data_structures_1.part_6.task_2 import bubble_sort


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
        ([1, 3, 5, 7, 9, 11, 13], [1, 3, 5, 7, 9, 11, 13]),
        ([3, 2, 1], [1, 2, 3]),
        ([], []),
        ([10], [10]),
        ([2, 2, 2], [2, 2, 2]),
        ([9, -1, 0], [-1, 0, 9]),
    ]
)
def test_binary_search(arr, expected):
    assert bubble_sort(arr) == expected