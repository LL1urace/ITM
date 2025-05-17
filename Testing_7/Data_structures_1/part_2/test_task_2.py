import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_2")
from task_2 import get_full_tons


faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_full_tons_valid_input():
    mass = faker.pyint(min_value=1, max_value=99999, step=1)
    full_tons = get_full_tons(mass)
    assert full_tons == mass // 1000


# Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        "mass",
                        [
                            faker.pyint(min_value=-99999, max_value=0, step=1),
                            faker.word(),
                            None,
                            [],
                            "",
                            {},
                            (),
                            # float(True), считает что 1 и валид проходит
                        ])
def test_get_full_tons_invalid_input(mass):
    with pytest.raises((TypeError, ValueError)):
        get_full_tons(mass)