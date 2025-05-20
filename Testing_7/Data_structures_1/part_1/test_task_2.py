import pytest
from faker import Faker
from Data_structures_1.part_1.task_2 import get_square_area



faker: Faker = Faker()

# Тесты на устанавливаемые правильные значения
def test_get_square_area_valid_input():
    side = 1
    assert get_square_area(side) == (side ** 2)
    side = 11
    assert get_square_area(side) == (side ** 2)
    side = "273"
    assert get_square_area(side) == (float(side) ** 2)


# Тесты на случайные правильные значения
@pytest.mark.parametrize("side",
                         [round(faker.pyfloat(min_value=0.1, max_value=100, right_digits=3), 3)
                          for _ in range(3)])
def test_get_square_perimeter_valid_input_random(side):
    assert get_square_area(side) == pytest.approx(side ** 2, rel=1e-6)


# Тесты на устанавливаемые неправильные значения
def test_get_square_perimeter_invalid_input():
    with pytest.raises(ValueError):
        get_square_area(-1)
    with pytest.raises(ValueError):
        get_square_area(0)
    with pytest.raises(TypeError):
        get_square_area([2231, "вфвфв"])
    with pytest.raises(ValueError):
        get_square_area("Антончик")


# Тесты на случайные неправильные значения
@pytest.mark.parametrize("side",
                         [-faker.pyfloat(min_value=0.1, max_value=100, right_digits=2),  # отрицательные
                            faker.word(),  # строка
                            None,  # None
                            [faker.random_int(), faker.word()] # список
                        ])
def test_get_square_area_invalid_input_parametrized(side):
    for _ in range(3):
        with pytest.raises((ValueError, TypeError)):
            get_square_area(side)