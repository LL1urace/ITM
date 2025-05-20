import pytest
from faker import Faker
from Data_structures_1.part_1.task_9 import get_geomean_two_nums


faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_geomean_two_nums_valid_input():
    num1 = faker.pyfloat(positive=True)
    num2 = faker.pyfloat(positive=True)
    geomean = get_geomean_two_nums(num1, num2)
    assert geomean == pytest.approx((num1 * num2) ** (1 / 2), rel=1e-6)


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
                            # (float(False), float(False)), # считает что 0 и валид проходит
                            # (0, 0), # считает что 0 и валид проходит
                            # Разные аргументы
                            (faker.word(), faker.pyfloat(positive=False)),
                            (None, faker.pyfloat(positive=False)),
                        ])
def test_get_geomean_two_nums_invalid_input(num1, num2):
    with pytest.raises((TypeError, ValueError)):
        get_geomean_two_nums(num1, num2)