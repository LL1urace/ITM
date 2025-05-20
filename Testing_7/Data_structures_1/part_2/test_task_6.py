import pytest
from faker import Faker
from Data_structures_1.part_2.task_6 import split_two_digit_number


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.fixture
def valid_segment_inputs():
    a = faker.pyint(min_value=10, max_value=99)
    return a


def test_split_two_digit_number_valid_input(valid_segment_inputs):
    num = valid_segment_inputs
    t, u = split_two_digit_number(num)
    assert t == abs(num) // 10
    assert u == abs(num) % 10



@pytest.fixture(params=[
    -faker.pyint(min_value=1, max_value=9),  # Отрицательное число
    -faker.pyint(min_value=100, max_value=99999),  # Отрицательное число
    faker.pyint(min_value=1, max_value=9),  # Отрицательное число
    faker.pyint(min_value=100, max_value=99999),  # Отрицательное число
    faker.word(),                                # Строка
    None,                                        # None
    [],                                          # Пустой список
    "",                                          # Пустая строка
    {},                                          # Пустой словарь
    (),                                          # Пустой кортеж
])
def invalid_inputs(request):
    return request.param

# Тест на случайные неправильные значения
def test_split_two_digit_number_invalid_input(invalid_inputs):
    num = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        split_two_digit_number(num)