import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_1")
from task_7 import get_circle_length_area
from math import pi


faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_circle_length_area_valid_input():
    r = faker.pyfloat(positive=True)
    length, square = get_circle_length_area(r)
    assert length == pytest.approx(2 * pi * r, rel=1e-6)
    assert square == pytest.approx(pi * r ** 2, rel=1e-6)

# Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        "r",
                        [
                            faker.pyfloat(positive=False),
                            faker.word(),
                            None,
                            [],
                            "",
                            {},
                            (),
                            # float(True), считает что 1 и норм проходит
                            float(False),
                            0,
                        ])
def test_get_circle_length_area_invalid_input(r):
    with pytest.raises((TypeError, ValueError)):
        get_circle_length_area(r)