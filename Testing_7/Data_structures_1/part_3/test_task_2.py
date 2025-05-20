import pytest
from faker import Faker
from Data_structures_1.part_3.task_2 import num_is_uneven


faker: Faker = Faker()

# Тест на случайные правильные значения
@pytest.mark.parametrize(
                        "num",
                         [
                             faker.pyint(min_value=1, max_value=99999),
                             -faker.pyint(min_value=1, max_value=99999),
                             faker.pyfloat(min_value=1, max_value=99999),
                             -faker.pyfloat(min_value=1, max_value=99999),
                         ]
)
def test_num_is_uneven_valid_input(num):
    assert num_is_uneven(num) == (int(num) % 2 != 0)



# Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        "num",
                        [
                            [faker.pyint(min_value=-99999, max_value=99999)],
                            [faker.pyfloat(min_value=-99999, max_value=99999)],
                            faker.word(),  # Строки
                            None,  # None
                            [],  # Пустые структуры
                            "",
                            {},
                            (),
                        ]

)
def test_num_is_positive_invalid_input(num):
    with pytest.raises((TypeError, ValueError)):
        num_is_uneven(num)



@pytest.mark.parametrize("num", [0, 1, -1])
def test_num_is_uneven_edge_cases(num):
    assert num_is_uneven(num) == (int(num) % 2 != 0)


@pytest.mark.parametrize("num", [10**10 + 1, -(10**10 + 2)])
def test_num_is_uneven_large_numbers(num):
    assert num_is_uneven(num) == (int(num) % 2 != 0)