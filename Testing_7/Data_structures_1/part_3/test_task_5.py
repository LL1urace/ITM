import pytest
from faker import Faker
from Data_structures_1.part_3.task_5 import check_inequalities


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.mark.parametrize(
                        ("num1", "num2"),
                         [
                            (faker.pyint(min_value=0, max_value=99999), faker.pyint(min_value=-99999, max_value=-3)),
                            (faker.pyint(min_value=-99999, max_value=-3), faker.pyint(min_value=0, max_value=99999)),
                            (faker.pyfloat(min_value=0, max_value=99999), faker.pyfloat(min_value=-99999, max_value=-3)),
                            (faker.pyfloat(min_value=-99999, max_value=-3), faker.pyfloat(min_value=0, max_value=99999)),
                         ]
)
def test_check_inequalities_valid_input(num1, num2):
    assert check_inequalities(num1, num2) == (int(num1) >= 0 or int(num2) < -2)



# Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        ("num1", "num2"),
                        [
                            (faker.word(), faker.word()),
                            (None, None),
                            ([], []),
                            ("", ""),
                            ({}, {}),
                            ((), ()),
                        ]

)
def test_check_inequalities_invalid_input(num1, num2):
    with pytest.raises((TypeError, ValueError)):
        check_inequalities(int(num1), int(num2))


@pytest.mark.parametrize("num1, num2", [
    (0, 1),
    (1, -1),
    (-1, 0),
])
def test_check_inequalities_edge_cases(num1, num2):
    assert check_inequalities(num1, num2) == (int(num1) >= 0 or int(num2) < -2)


@pytest.mark.parametrize("num1, num2", [
    (10**10 + 1, 3),
    (-10**10 - 2, 2),
    (10**12, -99999),
])
def test_check_inequalities_large_numbers(num1, num2):
    assert check_inequalities(num1, num2) == (int(num1) >= 0 or int(num2) < -2)