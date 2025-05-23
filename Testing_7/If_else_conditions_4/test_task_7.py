import pytest
from If_else_conditions_4.task_7 import get_days_in_month



@pytest.mark.parametrize(
    "month_number, expected",
    [
        (1, "Кол-во дней в январе: 31"),
        (2, "Кол-во дней в феврале: 28"),
        (3, "Кол-во дней в марте: 31"),
        (4, "Кол-во дней в апреле: 30"),
        (5, "Кол-во дней в мае: 31"),
        (6, "Кол-во дней в июне: 30"),
        (7, "Кол-во дней в июле: 31"),
        (8, "Кол-во дней в августе: 31"),
        (9, "Кол-во дней в сентябре: 30"),
        (10, "Кол-во дней в октябре: 31"),
        (11, "Кол-во дней в ноябре: 30"),
        (12, "Кол-во дней в декабре: 31"),
        (13, "Ошибка-ввода: номер месяце не находится в диапазоне 1-12"),
        ("Слово", ValueError),
        (None, TypeError),
        ([1, 2], TypeError),
    ]
)
def test_get_days_in_month(month_number, expected):
    if expected is ValueError or expected is TypeError:
        with pytest.raises((ValueError, TypeError)):
            get_days_in_month(month_number)
    else:
        assert get_days_in_month(month_number) == expected