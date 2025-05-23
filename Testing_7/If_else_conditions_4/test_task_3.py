import pytest
from If_else_conditions_4.task_3 import print_maxmin_nums



@pytest.mark.parametrize(
    ("fn", "sn", "expected"),
    [
        (1, 0, (1, 0)),
        (0, 0, (0, 0)),
        (3, -2, (3, -2)),
        (9, 99, (99, 9)),
        (-77, 1, (1, -77)),
        ("1", "17", (17, 1))
    ]
)
def test_valid_input(fn, sn, expected):
    max_n, next_n = print_maxmin_nums(fn, sn)
    assert (max_n, next_n) == expected



@pytest.mark.parametrize(
    ("fn", "sn"),
    [
        ("вфвф", 0),
        (0, "антончик"),
        ("0", "llolo"),
    ]
)
def test_type_error(fn, sn):
    with pytest.raises(ValueError):
        print_maxmin_nums(fn, sn)