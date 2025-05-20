import logging
import pytest
from Exceptions_logging_2.task_4_main import log_divisions  # замените на имя вашего модуля



def test_log_divisions_logs(caplog):
    x_vals = [10, 20]
    y_vals = [2, 0]
    with caplog.at_level(logging.INFO):
        log_divisions(x_vals, y_vals)
    # Проверяем что лог содержит сообщения о значениях x и y
    assert "The values of x and y are 10 and 2." in caplog.text
    assert "The values of x and y are 20 and 0." in caplog.text
    # Проверяем, что успешное деление залогировано
    assert "x/y successful with result: 5.0." in caplog.text
    # Проверяем, что возникла ошибка деления на ноль и она залогирована
    assert "ZeroDivisionError" in caplog.text