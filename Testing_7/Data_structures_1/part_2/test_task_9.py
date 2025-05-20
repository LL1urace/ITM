import pytest
from faker import Faker
from Data_structures_1.part_2.task_9 import get_hundreds


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


def test_get_hundreds_valid_input(valid_inputs):
    num = int(valid_inputs)
    hundreds = get_hundreds(num)
    assert hundreds == num // 100



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


def test_get_hundreds_invalid_input(invalid_inputs):
    num = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        get_hundreds(num)