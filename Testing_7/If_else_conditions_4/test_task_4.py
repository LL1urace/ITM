import pytest
from If_else_conditions_4.task_4 import min_num



@pytest.mark.parametrize(
    ("fn", "sn", "tn", "expected"),
    [
        (1, 0, 0, 0),
        (0, 0, 0, 0),
        (3, -2, 4, -2),
        (9, 99, 32, 9),
        (-77, 1, 21, -77),
        ("1", "17", 11.3, 1)
    ]
)
def test_valid_input(fn, sn, tn, expected):
    assert min_num(fn, sn, tn) == expected



@pytest.mark.parametrize(
    ("fn", "sn", "tn"),
    [
        ("вфвф", 0, 0),
        (0, "антончик", None),
        ("0", "llolo", 1),
    ]
)
def test_type_error(fn, sn, tn):
    with pytest.raises(ValueError):
        min_num(fn, sn, tn)