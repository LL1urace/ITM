import pytest
from Data_structures_1.part_4.task_5 import get_set_of_list  # Замените на актуальный путь



@pytest.mark.parametrize(
    ("list_to_set", "expected"),
    [
        ([1, 32, 23], {1, 32, 23}),
        ([1, 32, 23, 356, 123, 22, 99], {1, 32, 23, 356, 123, 22, 99}),
        (["x", "y", "y", "z"], {"x", "y", "z"}),
        ([1, 2, "3", "004"], {1, 2, "3", "004"}),
        (["hello123", "42world", "!", "!", "!", "@"], {"hello123", "42world", "!", "@"}),
        ([None, 1.5, "abc123", True, False, [], {}, "", "   "], TypeError),
        (["a", 5, "42", None, "b1", 3.14, "z", {}, []], TypeError),
        ([], set()),  # если функция выбрасывает ошибку на пустом списке
    ]
)
def test_get_set_of_list_input(list_to_set, expected):
    if expected == TypeError:
        with pytest.raises(TypeError):
            get_set_of_list(list_to_set)
    else:
        result = get_set_of_list(list_to_set)
        assert result == expected