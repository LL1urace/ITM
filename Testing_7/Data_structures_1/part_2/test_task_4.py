import pytest
from faker import Faker
from Data_structures_1.part_2.task_4 import count_segments_in_length


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.fixture
def valid_segment_inputs():
    a = faker.pyint(min_value=1, max_value=99999)
    b = faker.pyint(min_value=1, max_value=a)  # гарантируем b <= a
    return a, b


def test_count_segments_in_length_valid_input(valid_segment_inputs):
    a, b = valid_segment_inputs
    count_segments = count_segments_in_length(a, b)
    assert count_segments == a // b



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
def invalid_segment_inputs(request):
    return request.param


# Тест на случайные неправильные значения
def test_count_segments_in_length_invalid_input(invalid_segment_inputs):
    a, b = invalid_segment_inputs
    with pytest.raises((TypeError, ValueError)):
        count_segments_in_length(a, b)