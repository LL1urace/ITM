# Тест на случайные правильные значения
import pytest
from Data_structures_1.part_3.task_9 import in_nums_are_uneven  # адаптируй путь
from faker import Faker

faker = Faker()

# --- Валидные случаи: одно или оба числа нечётные ---
@pytest.mark.parametrize("a, b", [
    (1, 2),     # первое нечётное
    (2, 3),     # второе нечётное
    (5, 7),     # оба нечётные
    (3.0, 4.0), # float с нечётным int значением
])
def test_in_nums_are_uneven_some_odd(a, b):
    expected = (int(a) % 2 != 0 or int(b) % 2 != 0)
    assert in_nums_are_uneven(a, b) is expected


# --- Валидные случаи: оба чётные ---
@pytest.mark.parametrize("a, b", [
    (2, 4),
    (0, 6),
    (100, 200),
    (8.0, 12.0),  # float с чётными значениями
])
def test_in_nums_are_uneven_both_even(a, b):
    expected = (int(a) % 2 != 0 or int(b) % 2 != 0)
    assert in_nums_are_uneven(a, b) is expected


# --- Граничные случаи ---
@pytest.mark.parametrize("a, b", [
    (0, 1),        # ноль и нечётное
    (0, 0),        # оба ноль — чётные
    (-1, 2),       # отрицательное нечётное
    (-2, -4),      # оба чётные и отрицательные
])
def test_in_nums_are_uneven_edge_cases(a, b):
    expected = (int(a) % 2 != 0 or int(b) % 2 != 0)
    assert in_nums_are_uneven(a, b) == expected


# --- Исключения: невалидные типы ---
@pytest.mark.parametrize("a, b", [
    ("a", "b"),
    ([], []),
    (None, None),
    ({}, {}),
    ("3ы", 2),     # строка-число — вызовет ValueError
])
def test_in_nums_are_uneven_invalid_types(a, b):
    with pytest.raises((TypeError, ValueError)):
        in_nums_are_uneven(a, b)