import pytest
from faker import Faker
from Data_structures_1.part_3.task_6 import check_double_inequalities  # замените на актуальный путь

faker = Faker()


@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),
    (-999, 0, 999),
    (faker.pyint(min_value=-10000, max_value=-1),
     faker.pyint(min_value=0, max_value=999),
     faker.pyint(min_value=1000, max_value=99999)),
    (faker.pyfloat(min_value=-10000, max_value=-1),
     faker.pyfloat(min_value=0, max_value=999),
     faker.pyfloat(min_value=1000, max_value=99999)),
])
def test_check_double_inequalities_valid(a, b, c):
    assert check_double_inequalities(a, b, c) == (a < b < c)



@pytest.mark.parametrize("a, b, c", [
    ("a", "b", "c"),
    (None, None, None),
    ([], [], []),
    ({}, {}, {}),
    ((), (), ()),
])
def test_check_double_inequalities_invalid_types(a, b, c):
    with pytest.raises((TypeError, ValueError)):
        check_double_inequalities(a, b, c)



@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),      # все равны
    (-1, -1, 0),    # два равны
    (1, 1, 1),      # все равны, но положительные
    (-99999, 0, 99999),  # максимально широкий диапазон
])
def test_check_double_inequalities_edge_cases(a, b, c):
    assert check_double_inequalities(a, b, c) == (a < b < c)



@pytest.mark.parametrize("a, b, c", [
    (10**10, 10**11, 10**12),
    (-10**12, -10**11, -10**10),
])
def test_check_double_inequalities_large_numbers(a, b, c):
    assert check_double_inequalities(a, b, c) == (a < b < c)
