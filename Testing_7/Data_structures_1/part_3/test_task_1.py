import pytest
from faker import Faker
from Data_structures_1.part_3.task_1 import num_is_positive


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.fixture(params=[
    faker.pyint(min_value=1, max_value=99999),
    -faker.pyint(min_value=1, max_value=99999),
    faker.pyfloat(min_value=1, max_value=99999),
    -faker.pyfloat(min_value=1, max_value=99999),
])
def valid_inputs(request):
    return request.param


def test_num_is_positive_valid_input(valid_inputs):
    num = int(valid_inputs)
    assert num_is_positive(num) == (num > 0)



# Тест на случайные неправильные значения
@pytest.fixture(params=[
    # Отрицательные числа
    [faker.pyint(min_value=1, max_value=99)],
    faker.word(),  # Строки
    None,  # None
    [],  # Пустые структуры
    "",
    {},
    (),
])
def invalid_inputs(request):
    return request.param


def test_num_is_positive_invalid_input(invalid_inputs):
    num = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        num_is_positive(num)