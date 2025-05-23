import pytest
from If_else_conditions_4.task_1 import find_positive_nums_count


@pytest.mark.parametrize(
    ("fn", "sn", "tn", "expected"),
    [
        (1, 0, 0, 1),
        (0, 0, 0, 0),
        (3, 2, 3, 3),
        (9, 99, 0, 2),
        (-77, 1, -3, 1),
        ("1", "1", "-3", 2)
    ]
)
def test_find_positive_nums_count_valid_input(fn, sn, tn, expected):
    assert find_positive_nums_count(fn, sn, tn) == expected



@pytest.mark.parametrize(
    ("fn", "sn", "tn"),
    [
        ("вфвф", 0, 0),
        (0, "антончик", 0),
        (0, 0, "вфвфвууу"),
        ("0", "llolo", "dadadads"),
    ]
)
def test_find_positive_nums_count_type_error(fn, sn, tn):
    with pytest.raises(ValueError):
        find_positive_nums_count(fn, sn, tn)