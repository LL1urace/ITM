import pytest
from OOP_6.task_9 import Car
from copy import deepcopy

@pytest.fixture
def car1():
    return Car(
        make="Toyota",
        model="Camry",
        year=2020,
        color="Red",
        fuel_type="Gasoline",
        tank_capacity=50.0,
        current_fuel_level=25.0,
        number_of_doors=4,
        mileage=15000.0,
        max_speed=220.0,
        owner="Alice",
        price=20000.0
    )


@pytest.fixture
def car2():
    return Car(
        make="Honda",
        model="Civic",
        year=2018,
        color="Blue",
        fuel_type="Gasoline",
        tank_capacity=45.0,
        current_fuel_level=10.0,
        number_of_doors=4,
        mileage=30000.0,
        max_speed=210.0,
        owner="Bob",
        price=15000.0
    )


def test_getitem_setitem(car1):
    assert car1["make"] == "Toyota"
    car1["color"] = "Black"
    assert car1["color"] == "Black"

    with pytest.raises(KeyError):
        _ = car1["nonexistent"]

    with pytest.raises(KeyError):
        car1["nonexistent"] = "value"


def test_delitem(car1):
    del car1["owner"]
    with pytest.raises(AttributeError):
        _ = car1["owner"]

    with pytest.raises(KeyError):
        del car1["nonexistent"]


def test_iter(car1):
    attrs = list(iter(car1))
    expected_attrs = [
        "Toyota", "Camry", 2020, "Red", "Gasoline", 50.0, 25.0, 4,
        15000.0, 220.0, "Alice", 20000.0
    ]
    assert attrs == expected_attrs


def test_call(car1):
    car1(make="Mazda", price=18000.0)
    assert car1["make"] == "Mazda"
    assert car1["price"] == 18000.0

    with pytest.raises(KeyError):
        car1(nonexistent="value")


def test_len_bool(car1):
    assert len(car1) == 4
    assert bool(car1)

    car1(owner="")
    assert not bool(car1)


def test_arithmetic_operations(car1, car2):
    car3 = car1 + 1000.0
    assert car3["price"] == car1["price"] + 1000.0

    car3 = car1 + car2
    assert car3["price"] == car1["price"] + car2["price"]

    car1 += 500.0
    assert car1["price"] == 20500.0

    car1 += car2
    assert car1["price"] == 35500.0

    car3 = car1 - 500.0
    assert car3["price"] == car1["price"] - 500.0

    car3 = car1 - car2
    assert car3["price"] == car1["price"] - car2["price"]

    car1 -= 1000.0
    assert car1["price"] == 34500.0

    car1 -= car2
    assert car1["price"] == 19500.0

    with pytest.raises(ArithmeticError):
        _ = car1 + "wrong_type"


def test_comparisons(car1, car2):
    car_a = deepcopy(car1)
    car_b = deepcopy(car2)

    assert (car_a == car_b) is False
    assert (car_a != car_b) is True
    assert (car_a < car_b) is False
    assert (car_a > car_b) is True
    assert (car_a <= car_b) is False
    assert (car_a >= car_b) is True

    # Проверка, что сравнение с другим типом возвращает NotImplemented — в Python это значит False
    assert (car_a == 10) is False
    assert (car_a != 10) is True


def test_str_repr_format(car1):
    s = str(car1)
    assert "Toyota" in s

    r = repr(car1)
    assert "__make = Toyota" in r

    assert format(car1, "short_info") == "Toyota, Camry"
    assert format(car1, "long_info") == "Toyota, Camry, 2020, Red"
    assert format(car1, "sell_info") == "Toyota, Camry, Alice, 20000.0"


def test_context_manager(car1, capsys):
    with car1 as car:
        car._Car__mileage += 100
    captured = capsys.readouterr()
    assert "Начало работы с автомобилем" in captured.out
    assert "Автомобиль проехал 100" in captured.out
    assert "Завершение работы с автомобилем" in captured.out
