import pytest
from If_else_conditions_4.task_10 import num_description



def test_valid_input():
    assert num_description(100) == "Введенное число: сто"
    assert num_description(111) == "Введенное число: сто одиннадцать"
    assert num_description(120) == "Введенное число: сто двадцать"
    assert num_description(105) == "Введенное число: сто пять"
    assert num_description(123) == "Введенное число: сто двадцать три"
    assert num_description(999) == "Введенное число: девятьсот девяносто девять"
    assert num_description(99) == "Ошибка-ввода: число должно быть в диапазоне 100-999"
    assert num_description(1000) == "Ошибка-ввода: число должно быть в диапазоне 100-999"


def test_invalid_input():
    with pytest.raises((ValueError, TypeError)):
        num_description(None)
        num_description("fdada")