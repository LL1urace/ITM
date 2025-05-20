import pytest
from faker import Faker
from Data_structures_1.part_1.task_1 import get_square_perimeter



faker: Faker = Faker()

# Тесты на устанавливаемые правильные значения
def test_get_square_perimeter_valid_input():
    side = 1
    assert get_square_perimeter(side) == (4 * side)
    side = 11
    assert get_square_perimeter(side) == (4 * side)
    side = "273"
    assert get_square_perimeter(side) == (4 * float(side))


@pytest.mark.parametrize("side",
                         [round(faker.pyfloat(min_value=0.1, max_value=100, right_digits=3), 3)
                          for _ in range(3)])
def test_get_square_perimeter_valid_input_random(side):
    assert get_square_perimeter(side) == pytest.approx(4 * side, rel=1e-6)

# Ещё один способ запуска тестов
# def test_get_square_perimeter_multiple():
#     for _ in range(50):
#         side = round(faker.pyfloat(min_value=0.1, max_value=100, right_digits=3), 3)
#         assert get_square_perimeter(side) == pytest.approx(4 * side, rel=1e-6)

# Тесты на устанавливаемые неправильные значения
def test_get_square_perimeter_invalid_input():
    with pytest.raises(ValueError):
        get_square_perimeter(-1)
    with pytest.raises(ValueError):
        get_square_perimeter(0)
    with pytest.raises(TypeError):
        get_square_perimeter([2231, "вфвфв"])
    with pytest.raises(ValueError):
        get_square_perimeter("Антончик")


@pytest.mark.parametrize("side",
                         [-faker.pyfloat(min_value=0.1, max_value=100, right_digits=2),  # отрицательные
                            faker.word(),  # строка
                            None,  # None
                            [faker.random_int(), faker.word()] # список
                        ])
def test_get_square_perimeter_invalid_input_parametrized(side):
    for _ in range(3):
        with pytest.raises((ValueError, TypeError)):
            get_square_perimeter(side)