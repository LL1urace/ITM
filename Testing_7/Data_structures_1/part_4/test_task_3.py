import pytest
# from faker import Faker
from Data_structures_1.part_4.task_3 import divide_list_on_num_letters


# faker = Faker()


# Тест на случайные неправильные значения
@pytest.mark.parametrize(
    "list, expected_letters, expected_digits",
    [
        (
            ["aad", "s", "1", "a", "32", "23"],
            ['a', 'a', 'd', 's', 'a'],
            [1, 32, 23]
        ),
        (
            ["abc", "1", 2, "d", "4"],
            ['a', 'b', 'c', 'd'],
            [1, 2, 4]
        ),
        (
            ["x", "y", "z"],
            ['x', 'y', 'z'],
            []
        ),
        (
            [1, 2, "3", "004"],
            [],
            [1, 2, 3, 4]
        ),
        (
            ["hello123", "42world", "!", "@", 99],
            [],
            [99]  # потому что "hello123" и "42world" не isalpha и не isdigit
        ),
        # Не валид
        (
            [None, 1.5, "abc123", True, False, [], {}, "", "   "],
            [],  # 'abc123' и пустые строки не проходят isalpha()
            [True, False]  # 1.5 — float, True/False — bool, None — NoneType
        ),
        # Смешанные валидные и невалидные
        (
            ["a", 5, "42", None, "b1", 3.14, "z", {}, []],
            ['a', 'z'],
            [5, 42]
        ),
        # Пустой список
        (
            [],
            [],
            []
        ),
    ]
)
def test_divide_list_on_num_letters_input(list, expected_letters, expected_digits):
    letters, digits = divide_list_on_num_letters(list)
    assert letters == expected_letters
    assert digits == expected_digits