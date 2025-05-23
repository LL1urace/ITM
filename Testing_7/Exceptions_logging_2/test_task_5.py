import pytest
from Exceptions_logging_2.task_5 import validate_coefficient, solve_quadratic
from faker import Faker

faker: Faker = Faker()

@pytest.fixture
def random_coefficients():
    a = faker.pyint(min_value=1, max_value=100)
    b = faker.pyint(min_value=-100, max_value=100)
    c = faker.pyint(min_value=-100, max_value=100)
    d = b**2 - 4*a*c
    if d < 0:
        pytest.skip("D < 0, комплексные корни")
    return a, b, c

def test_quadratic_random(random_coefficients):
    a, b, c = random_coefficients
    x1, x2 = solve_quadratic(a, b, c)
    d = b**2 - 4*a*c
    assert isinstance(x1, float)
    assert isinstance(x2, float)
    assert abs(a * x1**2 + b * x1 + c) < 1e-5
    assert abs(a * x2**2 + b * x2 + c) < 1e-5

def test_quadratic_two_roots():
    x1, x2 = solve_quadratic(1, -3, 2)
    assert round(x1, 5) == 2.0
    assert round(x2, 5) == 1.0

def test_quadratic_one_root():
    x1, x2 = solve_quadratic(1, 2, 1)
    assert x1 == x2 == -1.0

def test_negative_discriminant():
    try:
        solve_quadratic(1, 1, 1)
    except ValueError as e:
        assert "Дискриминант отрицательный" in str(e)

def test_invalid_a_zero():
    try:
        validate_coefficient("a", "0")
    except ValueError as e:
        assert "Некорректное значение для коэффициента a: 0" in str(e)

def test_invalid_input():
    try:
        validate_coefficient("b", "abc")
    except ValueError as e:
        assert "Некорректное значение" in str(e)