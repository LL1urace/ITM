import pytest
from If_else_conditions_4.task_11 import calculator



@pytest.mark.parametrize("f_num, s_num, operation, expected", [
    ("10", "5", "*", "Результат операции: 50.0"),
    ("10", "0", "/", "Ошибка-операции: ошибка деления на ноль"),
    ("10", "5", "/", "Результат операции: 2.0"),
    ("10", "5", "+", "Результат операции: 15.0"),
    ("10", "5", "-", "Результат операции: 5.0"),
    ("ten", "5", "+", "Ошибка-ввода: некорректные данные числовых значений"),
    ("10", "5", "x", "Ошибка-ввода: некорректные данные операции"),
])
def test_calculator(f_num, s_num, operation, expected):
    assert calculator(f_num, s_num, operation) == expected