import pytest
from faker import Faker
from Data_structures_1.part_1.task_8 import get_avg_two_nums


faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_avg_two_nums_valid_input():
    num1 = faker.pyfloat()
    num2 = faker.pyfloat()
    avg = get_avg_two_nums(num1, num2)
    assert avg == pytest.approx((num1 + num2) / 2, rel=1e-6)


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
                            # float(True), считает что 1 и валид проходит
                            # (float(False), float(False)), считает что 0 и валид проходит
                            # (0, 0), считает что 0 и валид проходит
                        ])
def test_get_avg_two_nums_invalid_input(num1, num2):
    with pytest.raises((TypeError, ValueError)):
        get_avg_two_nums(num1, num2)