import pytest
from Data_structures_1.part_3.task_10 import one_num_is_uneven  # адаптируй путь
from faker import Faker

faker = Faker()

# --- Валидные: одно нечётное, другое чётное ---
@pytest.mark.parametrize("a, b", [
    ([1, 2, 3 ,4 ,5], ),        # нечётное, чётное
    (4, 3),        # чётное, нечётное
    (7.0, 8.0),    # float
    (-5, -6),      # отрицательные
])
def test_one_num_is_uneven_true_cases(a, b):
    expected = (int(a) % 2 != 0) ^ (int(b) % 2 != 0)
    assert one_num_is_uneven(a, b) is expected

# --- Валидные: оба нечётные или оба чётные ---
@pytest.mark.parametrize("a, b", [
    (1, 3),       # оба нечётные
    (2, 4),       # оба чётные
    (0, 8),       # оба чётные
    (-3, -5),     # оба нечётные отрицательные
])
def test_one_num_is_uneven_false_cases(a, b):
    expected = (int(a) % 2 != 0) ^ (int(b) % 2 != 0)
    assert one_num_is_uneven(a, b) is expected

# --- Граничные значения ---
@pytest.mark.parametrize("a, b", [
    (0, 1),         # чётное и нечётное
    (1, 0),
    (-1, 2),        # нечётное и чётное, включая отрицательные
    (2, -3),
])
def test_one_num_is_uneven_edge_cases(a, b):
    expected = (int(a) % 2 != 0) ^ (int(b) % 2 != 0)
    assert one_num_is_uneven(a, b) is expected

# --- Ошибки: невалидные типы ---
@pytest.mark.parametrize("a, b", [
    ("a", "b"),
    ([], []),
    (None, None),
    ({}, {}),
    ("3антон", 2),       # строка, которую нельзя интерпретировать напрямую
])
def test_one_num_is_uneven_invalid_types(a, b):
    with pytest.raises((TypeError, ValueError)):
        one_num_is_uneven(int(a), int(b))

# --- Большие числа ---
@pytest.mark.parametrize("a, b", [
    (10**12, 10**12 + 1),     # чётное и нечётное
    (10**12 + 1, 10**12 + 3), # оба нечётные
    (-10**10, -10**10 + 1),   # чётное и нечётное
])
def test_one_num_is_uneven_large_numbers(a, b):
    expected = (int(a) % 2 != 0) ^ (int(b) % 2 != 0)
    assert one_num_is_uneven(a, b) == expected
