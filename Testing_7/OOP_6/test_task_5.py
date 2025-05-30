import pytest
from OOP_6.task_5 import Car, Moped, MeansOfTransport




@pytest.fixture
def init_classes() -> tuple['Car', 'Moped']:
    car = Car("Maserati", "White", 4)
    moped = Moped("ALPHA RX 11", "Red", 2)
    return car, moped


def test_show_wheel_count(init_classes):
    car, moped = init_classes
    wc_car = car.show_wheel_count()
    wc_moped = moped.show_wheel_count()
    assert wc_car == "Количество колёс автомобиля: 4"
    assert wc_moped == "Количество колёс мопеда: 2"
    car.wheel_count = 8
    moped.wheel_count = 4
    wc_car = car.show_wheel_count()
    wc_moped = moped.show_wheel_count()
    assert wc_car == "Количество колёс автомобиля: 8"
    assert wc_moped == "Количество колёс мопеда: 4"