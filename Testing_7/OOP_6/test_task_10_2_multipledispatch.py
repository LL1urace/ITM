import pytest
from OOP_6.task_10_2_multipledispatch import Calculator


@pytest.fixture
def calc():
    return Calculator()

def test_addition_int(calc):
    assert calc.addition(2, 3) == 5
    assert calc.addition(-5, 10) == 5
    assert calc.addition(0, 0) == 0

def test_addition_float(calc):
    assert calc.addition(2.5, 3.5) == 6.0
    assert calc.addition(-1.1, 1.1) == 0.0
    assert calc.addition(0.0, 0.0) == 0.0

def test_addition_str(calc):
    assert calc.addition("Hello, ", "World!") == "Hello, World!"
    assert calc.addition("", "") == ""
    assert calc.addition("123", "456") == "123456"

def test_addition_type_error(calc):
    with pytest.raises(NotImplementedError):
        calc.addition(1, "2")

    with pytest.raises(NotImplementedError):
        calc.addition("abc", 123)

    with pytest.raises(NotImplementedError):
        calc.addition(1.0, "xyz")

    with pytest.raises(NotImplementedError):
        calc.addition([], {})

    with pytest.raises(NotImplementedError):
        calc.addition(1, 2.0)  # Нет такого сочетания (int, float)
#     assert binary_search(arr, target) == expected