import pytest
from OOP_6.task_4_2_property import MeansOfTransport



@pytest.fixture
def init_car():
    return MeansOfTransport("БМВ", "Черный")


def test_get_attrs(init_car):
    car = init_car
    brand, color = car.brand, car.color
    assert brand == "БМВ"
    assert color == "Черный"


def test_set_attrs(init_car):
    car = init_car
    car.brand = "Машина какая-та"
    car.color = "Какой-то цвет"
    assert car.brand == "Машина какая-та"
    assert car.color == "Какой-то цвет"