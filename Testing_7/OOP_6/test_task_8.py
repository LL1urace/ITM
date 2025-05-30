import pytest
from OOP_6.task_8 import Car, MeansOfTransport
from io import StringIO
import sys

@pytest.fixture
def car():
    return Car("Maserati", "White", 4)

def test_init(car):
    assert car.brand == "Maserati"
    assert car.color == "White"
    assert car.wheel_count == 4

def test_return_car_drive():
    assert Car.return_car_drive() == "Car_drive = 4"

def test_show_wheel_count(car):
    captured_output = StringIO()
    sys.stdout = captured_output
    car.show_wheel_count()
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "Количество колёс автомобиля: 4"