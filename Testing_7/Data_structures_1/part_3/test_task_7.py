import pytest
from faker import Faker
from Data_structures_1.part_3.task_7 import check_inequalities  # обнови путь при необходимости

faker = Faker()



# --- Валидные: строго возрастающая или убывающая последовательность ---
@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),             # возрастающая
    (10, 5, 0),            # убывающая
    (-10, 0, 10),          # возрастающая с отрицательными
    (99999, 0, -99999),    # убывающая с экстремумами
])
def test_check_inequalities_valid_increasing_or_decreasing(a, b, c):
    assert check_inequalities(a, b, c) == (int(a) < int(b) < int(c) or int(a) > int(b) > int(c))


# --- Валидные: не монотонные или равные значения ---
@pytest.mark.parametrize("a, b, c", [
    (1, 2, 2),    # нестрого возрастающая
    (3, 3, 1),    # нестрого убывающая
    (1, 1, 1),    # все равны
    (1, 3, 2),    # перепутанный порядок
    (10, 0, 10),  # перепутанный порядок
])
def test_check_inequalities_valid_but_not_monotonic(a, b, c):
    assert check_inequalities(a, b, c) == (int(a) < int(b) < int(c) or int(a) > int(b) > int(c))


# --- Граничные случаи ---
@pytest.mark.parametrize("a, b, c", [
    (0, 0, 1),
    (-1, -1, -1),
    (-99999, 0, 99999),
    (10**12, 10**12 + 1, 10**12 + 2),
])
def test_check_inequalities_edge_cases(a, b, c):
    assert check_inequalities(a, b, c) == (int(a) < int(b) < int(c) or int(a) > int(b) > int(c))


# --- Невалидные типы ---
@pytest.mark.parametrize("a, b, c", [
    ("a", "b", "c"),
    (None, None, None),
    ([], [], []),
    ({}, {}, {}),
    ((), (), ()),
])
def test_check_inequalities_invalid_types(a, b, c):
    with pytest.raises((TypeError, ValueError)):
        check_inequalities(int(a), int(b), int(c))


# --- Очень большие числа ---
@pytest.mark.parametrize("a, b, c", [
    (10**20, 10**21, 10**22),        # возрастающая
    (-10**22, -10**21, -10**20),     # возрастающая по модулю
    (10**22, 10**21, 10**20),        # убывающая
])
def test_check_inequalities_large_numbers(a, b, c):
    assert check_inequalities(a, b, c) == (int(a) < int(b) < int(c) or int(a) > int(b) > int(c))
