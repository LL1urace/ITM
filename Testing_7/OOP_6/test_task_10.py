import pytest
from OOP_6.task_10 import Calculator, StrCalculator



def test_calculator_addition():
    calc = Calculator()
    # Простые случаи
    assert calc.addition(5, 3) == 8
    assert calc.addition(-5, 0) == -5
    assert calc.addition(0, 0) == 0
    assert calc.addition(1000, -500) == 500
    # Дробные числа
    assert calc.addition(2.5, 3.5) == 6.0
    assert calc.addition(-1.1, -2.9) == -4.0
    # Большие числа
    assert calc.addition(1e10, 1e10) == 2e10
    # Смешанные типы (int + float)
    assert calc.addition(10, 2.5) == 12.5
    # Проверка ошибок (если есть проверки типов в реализации)
    assert calc.addition("5", 3) == 8
    with pytest.raises(TypeError):
        calc.addition(None, 1)


def test_str_calculator_addition():
    str_calc = StrCalculator()
    # Обычное соединение строк
    assert str_calc.addition("Hello", "World") == "HelloWorld"
    assert str_calc.addition("foo", "bar") == "foobar"
    # Пустые строки
    assert str_calc.addition("", "") == ""
    assert str_calc.addition("Hello", "") == "Hello"
    assert str_calc.addition("", "World") == "World"
    # Строки с пробелами
    assert str_calc.addition("Hello ", "World") == "Hello World"
    # Спецсимволы и юникод
    assert str_calc.addition("Привет", " мир") == "Привет мир"
    assert str_calc.addition("😊", "🚀") == "😊🚀"
    # Проверка ошибок при неправильных типах (если реализовано)
    assert str_calc.addition("test", 5) == "test5"
    assert str_calc.addition(None, "abc") == "Noneabc"