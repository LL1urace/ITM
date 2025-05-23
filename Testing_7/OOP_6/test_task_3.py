import pytest
from OOP_6.task_3 import MeansOfTransport


@pytest.fixture
def reset_car():
    return MeansOfTransport("Макларен", "серобуромалиновый")


def test_show_color(reset_car):
    car = reset_car
    assert car.show_color() == "Цвет ТС: серобуромалиновый"
    car.color = "теперь черный"
    assert car.show_color() == "Цвет ТС: теперь черный"


def test_show_brand(reset_car):
    car = reset_car
    assert car.show_brand() == "Марка ТС: Макларен"
    car.brand = "Гелик"
    assert car.show_brand() == "Марка ТС: Гелик"