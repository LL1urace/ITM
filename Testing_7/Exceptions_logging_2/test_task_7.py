import pytest
import logging
from Exceptions_logging_2.task_7 import get_avg_of_list



def test_average_of_integers():
    assert get_avg_of_list([1, 2, 3, 4, 5]) == 3.0


def test_average_of_floats():
    assert get_avg_of_list([1.5, 2.5, 3.0]) == 2.3333333333333335


def test_average_of_mixed_types():
    assert get_avg_of_list([1, 2.0, 3]) == 2.0


def test_average_of_strings_as_numbers():
    assert get_avg_of_list(["1", "2", "3.5"]) == 2.1666666666666665


def test_with_invalid_element(caplog):
    with caplog.at_level(logging.ERROR):
        result = get_avg_of_list([1, 2, "abc"])
        assert "Ошибка-ввода" in caplog.text
        assert result is None  # Функция не возвращает результат при ValueError


def test_empty_list_raises():
    with pytest.raises(ValueError):
        get_avg_of_list([])


def test_logging_success(caplog):
    with caplog.at_level(logging.INFO):
        get_avg_of_list([10, 20, 30])
        assert "Успешно найдено среднее арифметическое" in caplog.text