import pytest
from OOP_6.task_7 import Car



def test_car_initialization():
    car = Car("Maserati", "White", 4, 2025, "gasoline")
    assert car.brand == "Maserati"
    assert car.color == "White"
    assert car.wheel_count == 4
    assert car._year == 2025  # Допустимо, но нежелательно
    assert car._Car__fuel_type == "gasoline"  # Name mangling: приватное поле


def test_show_wheel_count(capsys):
    car = Car("Maserati", "White", 4, 2025, "gasoline")
    car.show_wheel_count()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Количество колёс автомобиля: 4"


def test_private_fuel_type_access_raises():
    car = Car("Maserati", "White", 4, 2025, "gasoline")
    with pytest.raises(AttributeError):
        _ = car.__fuel_type  # Нельзя напрямую получить приватное поле