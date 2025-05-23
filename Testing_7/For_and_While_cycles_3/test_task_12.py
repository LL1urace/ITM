import pytest
from For_and_While_cycles_3.task_12 import output_func



def test_output_func():
    vals = output_func()
    assert vals[0] == "Значение функции y=x^2 при x = 1 равно: 1"
    assert vals[-1] == "Значение функции y=x^2 при x = 10.0 равно: 100.0"
    assert vals[7] == "Значение функции y=x^2 при x = 4.5 равно: 20.25"
    assert vals[3] == "Значение функции y=x^2 при x = 2.5 равно: 6.25"
    assert vals[-4] == "Значение функции y=x^2 при x = 8.5 равно: 72.25"