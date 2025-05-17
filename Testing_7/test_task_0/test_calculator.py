import pytest
import sys
sys.path.append(r"E:\Учёба\Для проектиков по IT\ITM\test_task_0")

from calculator import parse_input, calculate_expression

### Тесты для функции `parse_input()` (разбор ввода)
def test_parse_input_valid():
    """Проверка корректного ввода"""
    assert parse_input("5 + 3") == (5, "+", 3)
    assert parse_input("10 * 2") == (10, "*", 2)
    assert parse_input("1 / 1") == (1, "/", 1)

def test_parse_input_invalid_format():
    """Проверка ошибки формата (не 3 части)"""
    assert parse_input("5 +") is None  # Слишком мало частей
    assert parse_input("5 + 3 4") is None  # Слишком много частей

def test_parse_input_non_integer():
    """Проверка ошибки, если введены не числа"""
    assert parse_input("a + b") is None
    assert parse_input("5.5 * 2") is None

def test_parse_input_out_of_range():
    """Проверка, что числа в диапазоне 1-10"""
    assert parse_input("0 + 5") is None  # a < 1
    assert parse_input("11 * 2") is None  # a > 10
    assert parse_input("5 / 0") is None   # b < 1

def test_parse_input_invalid_operator():
    """Проверка недопустимого оператора"""
    assert parse_input("5 % 3") is None  # Неверный оператор
    assert parse_input("5 ^ 2") is None

### Тесты для функции `calculate_expression()` (вычисление)
def test_calculate_addition():
    """Проверка сложения"""
    assert calculate_expression((5, "+", 3)) == 8

def test_calculate_subtraction():
    """Проверка вычитания"""
    assert calculate_expression((10, "-", 2)) == 8

def test_calculate_multiplication():
    """Проверка умножения"""
    assert calculate_expression((3, "*", 4)) == 12

def test_calculate_division():
    """Проверка целочисленного деления"""
    assert calculate_expression((10, "/", 2)) == 5
    assert calculate_expression((9, "/", 2)) == 4  # 9 // 2 = 4

def test_calculate_invalid_operator():
    """Проверка неверного оператора"""
    assert calculate_expression((5, "%", 3)) is None