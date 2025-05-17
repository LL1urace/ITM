import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_2")
from task_1 import get_full_meters


faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_full_meters_valid_input():
    length = faker.pyint(min_value=1, max_value=99999, step=1)
    full_meters = get_full_meters(length)
    assert full_meters == length // 100


# Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        "length",
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
def test_get_full_meters_invalid_input(length):
    with pytest.raises((TypeError, ValueError)):
        get_full_meters(length)