import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_2")
from task_7 import get_sum_and_product_of_digits


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.fixture(params=[
    faker.pyint(min_value=10, max_value=99),
    -faker.pyint(min_value=10, max_value=99),
    faker.pyfloat(min_value=10, max_value=99),
    -faker.pyfloat(min_value=10, max_value=99),
])
def valid_inputs(request):
    return request.param


def test_get_sum_and_product_of_digits_valid_input(valid_inputs):
    num = int(valid_inputs)
    sum, prod = get_sum_and_product_of_digits(num)
    units = abs(num) % 10
    tens = abs(num) // 10
    assert sum == units + tens
    assert prod == units * tens



@pytest.fixture(params=[
    # Отрицательные числа
    -faker.pyint(min_value=1, max_value=9),
    -faker.pyint(min_value=100, max_value=99999),
    faker.pyint(min_value=1, max_value=9),
    faker.pyint(min_value=100, max_value=99999),
    faker.word(), # Строки
    None, # None
    [], # Пустые структуры
    "",
    {},
    (),
])
def invalid_inputs(request):
    return request.param


# Тест на случайные неправильные значения
def test_get_sum_and_product_of_digits_invalid_input(invalid_inputs):
    num = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        get_sum_and_product_of_digits(num)