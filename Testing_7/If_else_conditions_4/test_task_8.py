import pytest
from If_else_conditions_4.task_8 import next_date



def test_next_date_valid_30_day_month():
    assert next_date(15, 4) == "Следующая дата: 16.4"
    assert next_date(30, 4) == "Следующая дата: 1.5"

def test_next_date_valid_31_day_month():
    assert next_date(15, 7) == "Следующая дата: 16.7"
    assert next_date(31, 7) == "Следующая дата: 1.8"

def test_next_date_february():
    assert next_date(27, 2) == "Следующая дата: 28.2"
    assert next_date(28, 2) == "Следующая дата: 1.3"

def test_next_date_new_year():
    assert next_date(31, 12) == "Следующая дата: 1.1\nC новым годом!"

def test_next_date_invalid():
    assert next_date(31, 4) == "Ошибка-ввода: значение даты некорректно"
    assert next_date(0, 1) == "Ошибка-ввода: значение даты некорректно"
    assert next_date(15, 13) == "Ошибка-ввода: значение даты некорректно"

def test_next_date_type_error():
    assert next_date("abc", 2) == "Ошибка-ввода: значения для дней и месяца должны быть целыми числами"
    assert next_date(15, "feb") == "Ошибка-ввода: значения для дней и месяца должны быть целыми числами"