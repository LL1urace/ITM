# Практика:
#
# 5. Перекройте тестами выше указанные задачи.
import pytest
from Parallelism_and_сoncurrency_8 import task_async_1



# Task №1 (get_divisors_in_range, get_collection_divisors, main)
# get_collection_divisors()
# Валидные и невалидные данные обработка
@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (17, [1, 17]),  # простое
        (10, [1, 2, 5, 10]),  # составное
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),  # квадрат
        (3600, [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30,
             36, 40, 45, 48, 50, 60, 72, 75, 80, 90, 100, 120, 144,
             150, 180, 200, 225, 240, 300, 360, 400, 450, 600, 720,
             900, 1200, 1800, 3600]),  # много делителей
        (1_000_000, None),  # граничный низ
        (20_000_000, None),  # граничный верх
        (0, []),  # пустой вывод
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]), # проверка сортировки + уникальности
        (None, TypeError),
        ("string", TypeError),
    ]
)
def test_get_collection_divisors(number, expected):
    if expected == TypeError:
        with pytest.raises(expected):
            task_async_1.get_collection_divisors(number)
    else:
        result = task_async_1.get_collection_divisors(number)
        if expected != None:
            assert sorted(result) == expected
        assert all(number % d == 0 for d in result)


# get_divisors_in_range
# Диапазон для валидных данных
@pytest.mark.parametrize(
    ("args", "expected"),
    [
        ((10, 1, 6), [1, 10, 2, 5]),  # делители 10 в диапазоне 1-5 включительно
        ((36, 1, 7), [1, 36, 2, 18, 3, 12, 4, 9, 6]),  # делители 36 в диапазоне 1-6 включительно
        ((17, 1, 9), [1, 17]),  # простое число 17, диапазон 1-8
        ((10, 5, 10), [5, 2]),  # диапазон 5-9 (5 и 2 — взаимодополняющие делители)
        ((10, 10, 11), [10, 1])  # диапазон 10-10, делители 10
    ]
)
def test_get_divisors_in_range(args, expected):
    result = task_async_1.get_divisors_in_range(args)
    assert sorted(list(set(result))) == sorted(expected)