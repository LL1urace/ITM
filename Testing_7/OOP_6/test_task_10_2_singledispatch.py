import pytest
from OOP_6.task_10_2_singledispatch import Calculator



@pytest.fixture
def calc():
    return Calculator()


def test_addition_with_ints(calc):
    assert calc.addition(2, 3) == 5
    assert calc.addition(-1, 4) == 3


def test_addition_with_floats(calc):
    assert calc.addition(2.5, 3.5) == 6.0
    assert calc.addition(-1.1, 1.1) == 0.0


def test_addition_with_mixed_numbers(calc):
    assert calc.addition(3, 2.5) == 5.5
    assert calc.addition(2.5, 3) == 5.5


def test_addition_with_strings(calc):
    assert calc.addition("hello", " world") == "hello world"
    assert calc.addition("", "test") == "test"


def test_addition_invalid_types(calc):
    with pytest.raises(TypeError):
        calc.addition(1, "a")
    with pytest.raises(TypeError):
        calc.addition("a", 1)
    with pytest.raises(TypeError):
        calc.addition([1, 2], [3, 4])
    with pytest.raises(TypeError):
        calc.addition(None, None)