import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_1")
from task_4 import get_circle_length
from math import pi


faker: Faker = Faker()

# Тесты на устанавливаемые правильные значения
def test_get_circle_length_valid_input():
    d = faker.pyfloat(positive=True)
    assert get_circle_length(d) == (pi * d)


# Тесты на случайные неправильные значения
@pytest.mark.parametrize("d",
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
                            0
                        ])
def test_get_circle_length_invalid_input(d):
    with pytest.raises((TypeError, ValueError)):
        get_circle_length(d)