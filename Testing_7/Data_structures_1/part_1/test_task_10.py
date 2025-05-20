import pytest
from faker import Faker
from Data_structures_1.part_1.task_10 import (get_squares_operations,
                                              calc_sum_sq,
                                              calc_difference_sq,
                                              calc_product_sq,
                                              calc_quotient_sq)


faker: Faker = Faker()

# Тест на коррректный возврат значений основной функции
def test_get_squares_operations_union_output():
    """Проверяет что основная функция корректно объединяет вычисляющие."""
    num1 = faker.pyfloat(positive=True)
    num2 = faker.pyfloat(positive=True)
    sum_sq, diff_sq, prod_sq, quot_sq = get_squares_operations(num1, num2)
    assert sum_sq == calc_sum_sq(num1, num2)
    assert diff_sq == calc_difference_sq(num1, num2)
    assert prod_sq == calc_product_sq(num1, num2)
    assert quot_sq == calc_quotient_sq(num1, num2)


# Тест на случайные правильные значения
def test_get_squares_operations_valid_input():
    """Проверяет что основная функция корректно объединяет вычисляющие."""
    num1 = faker.pyfloat(positive=True)
    num2 = faker.pyfloat(positive=True)
    sum_sq, diff_sq, prod_sq, quot_sq = get_squares_operations(num1, num2)
    assert sum_sq == num1 ** 2 + num2 ** 2
    assert diff_sq == num1 ** 2 - num2 ** 2
    assert prod_sq == (num1 ** 2) * (num2 ** 2)
    assert quot_sq == (num1 ** 2) / (num2 ** 2)


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
                            (float(True), 0), # считает что 1 и валид проходит
                            (float(False), float(False)), # считает что 0 и валид проходит
                            (0, 0), # считает что 0 и валид проходит
                            # Разные аргументы
                            (faker.word(), faker.pyfloat(positive=False)),
                            (None, faker.pyfloat(positive=False)),
                        ])
def test_get_squares_operations_invalid_input(num1, num2):
    with pytest.raises((TypeError, ValueError)):
        get_squares_operations(num1, num2)