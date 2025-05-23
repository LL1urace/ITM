import pytest
from Exceptions_logging_2.task_8 import PrintData, ExceptionPrintSendData
from unittest.mock import patch



def test_successful_print():
    printer = PrintData()

    with patch.object(printer, "send_to_print", return_value=True):
        msg = printer.print("Тест")
        assert msg == "печать Тест"



def test_failed_print_raises_exception():
    printer = PrintData()

    with patch.object(printer, "send_to_print", return_value=False):
        with pytest.raises(ExceptionPrintSendData) as exc_info:
            printer.print("ошибка печати")

        assert "Принтер не отвечает" in str(exc_info.value)
        assert isinstance(exc_info.value, ExceptionPrintSendData)