import pytest
from faker import Faker
from Data_structures_1.part_2.task_5 import get_unused_segment_length


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.fixture
def valid_inputs():
    a = faker.pyint(min_value=1, max_value=99999)
    b = faker.pyint(min_value=1, max_value=a)  # гарантируем b <= a
    return a, b


def test_get_unused_segment_length_valid_input(valid_inputs):
    a, b = valid_inputs
    segment_reminder = get_unused_segment_length(a, b)
    assert segment_reminder == a % b



@pytest.fixture(params=[
    # Отрицательные числа
    (-faker.pyint(min_value=1, max_value=99999), -faker.pyint(min_value=1, max_value=99999)),
    (faker.word(), faker.word()), # Строки
    (None, None), # None
    ([], []), # Пустые структуры
    ("", ""),
    ({}, {}),
    ((), ()),
    (faker.pyint(min_value=1, max_value=100), 0), # Деление на ноль (b == 0)
    (faker.pyint(min_value=1, max_value=50), faker.pyint(min_value=51, max_value=100))  # Невалидное условие a < b
])
def invalid_inputs(request):
    return request.param


# Тест на случайные неправильные значения
def test_get_unused_segment_length_invalid_input(invalid_inputs):
    a, b = invalid_inputs
    with pytest.raises((TypeError, ValueError)):
        get_unused_segment_length(a, b)