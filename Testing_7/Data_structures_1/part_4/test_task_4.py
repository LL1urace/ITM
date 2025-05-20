import pytest
from Data_structures_1.part_4.task_4 import del_last_and_reverse_list



@pytest.mark.parametrize(
    ("digits", "expected"),
    [
        ([1, 32, 23], [32, 1]),
        ([1, 32, 23, 356, 123, 22, 99], [22, 123, 356, 23, 32, 1]),
        (["x", "y", "z"], ValueError),
        ([1, 2, "3", "004"], ValueError),
        (["hello123", "42world", "!", "@", 99], ValueError),
        ([None, 1.5, "abc123", True, False, [], {}, "", "   "], ValueError),
        (["a", 5, "42", None, "b1", 3.14, "z", {}, []], ValueError),
        ([], []),  # если функция выбрасывает ошибку на пустом списке
    ]
)
def test_del_last_and_reverse_list_input(digits, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            del_last_and_reverse_list(digits)
    else:
        result = del_last_and_reverse_list(digits)
        assert result == expected