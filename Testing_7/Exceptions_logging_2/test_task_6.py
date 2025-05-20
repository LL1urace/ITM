import pytest
import logging
from Exceptions_logging_2.task_6 import input_range



def test_valid_range():
    assert input_range("1", "5") == (1.0, 5.0)

def test_exit_input():
    assert input_range("exit", "5") is None
    assert input_range("1", "exit") is None

def test_non_numeric_input(caplog):
    with caplog.at_level(logging.ERROR):
        result = input_range("abc", "5")
        assert result is None
        assert "Ошибка-ввода" in caplog.text

def test_negative_input(caplog):
    with caplog.at_level(logging.ERROR):
        result = input_range("-1", "5")
        assert result is None
        assert "отрицательные значения" in caplog.text

def test_invalid_range(caplog):
    with caplog.at_level(logging.ERROR):
        result = input_range("10", "5")
        assert result is None
        assert "start = 10.0, что больше чем end = 5.0" in caplog.text