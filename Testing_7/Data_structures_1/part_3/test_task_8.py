import pytest
from faker import Faker
from Data_structures_1.part_3.task_8 import each_nums_are_uneven


faker: Faker = Faker()

# --- Валидные: строго возрастающая или убывающая последовательность ---
@pytest.mark.parametrize("a, b",
                         [
    (1, 3),             # возрастающая
    (5, 9),            # убывающая
    (77, 99),          # возрастающая с отрицательными
    (999.33, -1231.3),    # убывающая с экстремумами
])
def test_each_nums_are_uneven_valid_input(a, b):
    assert each_nums_are_uneven(a, b) == (int(a) % 2 != 0 and int(b) % 2 != 0)


# --- Валидные: не монотонные или равные значения ---
@pytest.mark.parametrize("a, b",
                         [
    (77, 77),    # нестрого возрастающая
    (3, 3),    # нестрого убывающая
    (1, 1),    # все равны
    (123.2, 457.5),    # перепутанный порядок
    (95, 95),  # перепутанный порядок
])
def test_each_nums_are_uneven_equal_input(a, b):
    assert each_nums_are_uneven(a, b) == (int(a) % 2 != 0 and int(b) % 2 != 0)


# --- Граничные случаи ---
@pytest.mark.parametrize("a, b", [
    (0, 0),
    (-1, -1),
    (-99999, 99999),
    (10**12,  10**12),
])
def test_each_nums_are_uneven_edge_cases(a, b):
    assert each_nums_are_uneven(a, b) == (int(a) % 2 != 0 and int(b) % 2 != 0)


# --- Невалидные типы ---
@pytest.mark.parametrize("a, b", [
    ("a", "b"),
    (None, None, ),
    ([], []),
    ({}, {}),
    ((), ()),
])
def test_each_nums_are_uneven_invalid_types(a, b):
    with pytest.raises((TypeError, ValueError)):
        each_nums_are_uneven(int(a), int(b))