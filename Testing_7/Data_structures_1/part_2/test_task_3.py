import pytest
from faker import Faker
from Data_structures_1.part_2.task_3 import get_full_kilobytes_size


faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_full_kilobytes_size_valid_input():
    byte_size = faker.pyint(min_value=0, max_value=99999, step=1)
    full_kilobytes_size = get_full_kilobytes_size(byte_size)
    assert full_kilobytes_size == byte_size // 1024


# Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        "byte_size",
                        [
                            faker.pyint(min_value=-99999, max_value=-1, step=1),
                            faker.word(),
                            None,
                            [],
                            "",
                            {},
                            (),
                            # float(True), считает что 1 и валид проходит
                        ])
def test_get_full_kilobytes_size_invalid_input(byte_size):
    with pytest.raises((TypeError, ValueError)):
        get_full_kilobytes_size(byte_size)