import pytest
import sys
from faker import Faker
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\Data_structures_1\part_2")
from task_8 import reverse_two_digits_number


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


def test_reverse_two_digits_number_valid_input(valid_inputs):
    num = int(valid_inputs)
    reverse_num = reverse_two_digits_number(num)
    sign = -1 if num < 0 else 1  # сохраняем знак
    units = abs(num) % 10
    tens = abs(num) // 10
    assert reverse_num == sign * (units * 10 + tens)



@pytest.fixture(params=[
    # Отрицательные числа
    -faker.pyint(min_value=1, max_value=9),
    -faker.pyint(min_value=100, max_value=99999),
    faker.pyint(min_value=1, max_value=9),
    faker.pyint(min_value=100, max_value=99999),
    faker.word(),  # Строки
    None,  # None
    [],  # Пустые структуры
    "",
    {},
    (),
])
def invalid_inputs(request):
    return request.param


# Тест на случайные неправильные значения
def test_reverse_two_digits_number_invalid_input(invalid_inputs):
    num = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        reverse_two_digits_number(num)