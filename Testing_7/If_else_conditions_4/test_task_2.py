import pytest
from If_else_conditions_4.task_2 import max_num



@pytest.mark.parametrize(
    ("fn", "sn", "expected"),
    [
        (1, 0, 1),
        (0, 0, None),
        (3, -2, 3),
        (9, 99, 99),
        (-77, 1, 1),
        ("1", "17", 17)
    ]
)
def test_valid_input(fn, sn, expected):
    assert max_num(fn, sn) == expected



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
        max_num(fn, sn)