import pytest
from OOP_6.task_4 import MeansOfTransport



@pytest.fixture
def init_car():
    return MeansOfTransport("БМВ", "Черный")


def test_get_attrs(init_car):
    car = init_car
    brand, color = car.get_attrs()
    assert brand == "БМВ"
    assert color == "Черный"


def test_set_attrs(init_car):
    car = init_car
    car.set_attrs("Машина какая-та", "Какой-то цвет")
    assert car.brand == "Машина какая-та"
    assert car.color == "Какой-то цвет"