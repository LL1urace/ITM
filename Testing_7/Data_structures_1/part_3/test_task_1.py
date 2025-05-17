import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_2")
from task_10 import extract_units_and_tens


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.fixture(params=[
    faker.pyint(min_value=100, max_value=999),
    -faker.pyint(min_value=100, max_value=999),
    faker.pyfloat(min_value=100, max_value=999),
    -faker.pyfloat(min_value=100, max_value=999),
])
def valid_inputs(request):
    return request.param


def test_extract_units_and_tens_valid_input(valid_inputs):
    num = int(valid_inputs)
    units, tens = extract_units_and_tens(num)
    assert units == abs(num) % 10
    assert tens == (abs(num) // 10) % 10



# Тест на случайные неправильные значения
@pytest.fixture(params=[
    # Отрицательные числа
    -faker.pyint(min_value=1, max_value=99),
    -faker.pyint(min_value=1000, max_value=99999),
    faker.pyint(min_value=1, max_value=99),
    faker.pyint(min_value=1000, max_value=99999),
    faker.word(),  # Строки
    None,  # None
    [],  # Пустые структуры
    "",
    {},
    (),
])
def invalid_inputs(request):
    return request.param


def test_extract_units_and_tens_invalid_input(invalid_inputs):
    num = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        extract_units_and_tens(num)