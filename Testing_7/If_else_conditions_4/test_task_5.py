import pytest
from If_else_conditions_4.task_5 import get_point_quadrant



@pytest.mark.parametrize(
    ("coords", "expected"),
    [
        ([13, 2], 1),
        ([6, -3], 4),
        ([-71, 30], 2),
        ([1, 12], 1),
        (["1.2", "-32.0"], 4),
        ([0, 0], ValueError)
    ]
)
def test_valid_input(coords, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            get_point_quadrant(coords)
    else:
        assert get_point_quadrant(coords) == expected



@pytest.mark.parametrize(
    ("coords", "expected"),
    [
        ([13, "ывфв"], ValueError),
        ([6, 0], ValueError),
        ([0, 30], ValueError),
        ([1, None], ValueError),
        (["131ssssd.2", "-32.0"], TypeError),
        ([0, 0], ValueError)
    ]
)
def test_type_error(coords, expected):
    with pytest.raises((ValueError, TypeError)):
        get_point_quadrant(coords)